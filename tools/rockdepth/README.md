# RockDepth 板端部署与验收

本目录维护ROCK 5C Lite / RK3582的板端工具和服务模板。软件服务、官方模型参考和整体进度由[软件唯一计划](https://github.com/qiaoqiao2521/uw-yolo-code-assets/tree/main/plans/rock5-network-depth)维护。视频、权重、二进制运行库和原始运行证据不进入Git。

2026-10-12当前状态：首期验收通过后，已按用户要求临时停止NPU、publisher和MediaMTX，CPU此前已停用；四个unit无运行进程，18087和18554端口关闭。配置和原自启策略保留，整板冷启动未验收。本轮不执行以下安装或启动命令，恢复按用户后续指令进行。

## 已验证环境与模型接口

2026-10-12现场：Debian12、Python3.11.2、六核，驱动0.9.6。系统Runtime保持2.0.0b0；实验进程使用私有Runtime2.3.2与Lite2 2.3.2。芯片实际为RK3582，转换目标仍用 `rk3588`。

- 模型：Depth Anything V2 Small / vits，相对逆深度。
- 输入：float32 NCHW `(1,3,252,448)`。软件后端将uint8 RGB按Pillow bicubic缩放，再除以255并执行一次ImageNet mean/std归一化。
- 转换：ONNX opset17不内置归一化；Toolkit2配置不再次设置mean/std。非INT8构建内部使用FP16，不等同于全模型FP32。
- 输出：原始二维浮点 `(252,448)`。不将颜色图或尺度对齐结果作为后端数值一致性证据。
- 编译器保留五个原始 `align_corners` Resize的CPU实现；后端为NPU与CPU混合算子，不能标为全NPU。

比较过RCDL现成深度封装，其示例采用308/518方形输入、INT8与图内归一化，不匹配本轮冻结的参考契约。这里仅封装官方Toolkit2转换和软件侧现有后端的读回调用；不重写推理框架、RTSP服务器或生命周期管理。[RCDL模型说明](https://github.com/ruisv/rcdl/blob/main/docs/MODELS.md)

## 转换机隔离环境

在已有Python3.11环境中创建独立venv。使用CPU版Torch，避免为转换安装CUDA依赖：

```bash
uv venv --python 3.11 /home/muqiao/.cache/rockdepth-board/convert-venv
uv pip install --python /home/muqiao/.cache/rockdepth-board/convert-venv/bin/python \
  --torch-backend cpu -r tools/rockdepth/requirements-convert.txt
```

Toolkit2 2.3.2实际调用 `onnx.mapping` 和 `pkg_resources`。本轮固定ONNX1.16.2与setuptools80.9.0，分别解决ONNX1.22移除mapping、venv没有pkg_resources的环境错误；未修改模型图或monkeypatch SDK。

使用软件侧已经固定哈希的ONNX，输出必须为新路径：

```bash
/home/muqiao/.cache/rockdepth-board/convert-venv/bin/python \
  tools/rockdepth/convert_da2.py /absolute/model.onnx /absolute/new-model.rknn \
  --expected-sha256 ONNX_SHA256
```

转换退出成功只证明产物已导出。继续完成板端原始输出和参考数值对照。

## 板端目录与依赖

板端运行目录为 `/home/muqiao/rockdepth`：`app/`保存软件侧服务文件，`models/`和`media/`保存私有运行输入，`lib/`保存实验Runtime，`evidence/`和`logs/`保存本机证据。

Radxa镜像缺少ensurepip时，可以使用 `venv --without-pip --system-site-packages`，通过已校验的pip wheel引导pip，再将[板端依赖](requirements-board.txt)安装到该venv。继承的系统包与实验安装包分别记录；不在系统Python里执行pip升级。当前FFmpeg来自imageio-ffmpeg 0.6.0，版本为7.0.2-static。

将MediaMTX官方v1.21.2 ARM64包按发布摘要校验后，仅解压可执行文件至 `bin/mediamtx`。当前压缩包SHA256为 `180a235374a548d9133cdd5e20f5dbd8b01317be1c86e0d7e66df585dc42ed6f`。将imageio-ffmpeg报告的可执行路径链接为 `bin/ffmpeg`。[官方发布](https://github.com/bluenviron/mediamtx/releases/tag/v1.21.2)

模型和四个服务文件按软件侧本轮冻结版本复制。媒体回放使用授权的Sintel视频，许可证及来源由软件侧维护。模板假定这些文件已经存在，不代替模型准备和版本校验。

## CPU回放与视频服务

将[MediaMTX配置](systemd/mediamtx.yml)复制到 `config/mediamtx.yml`。RTSP只监听127.0.0.1:18554、使用TCP；MoQ、RTMP、HLS、WebRTC、SRT及管理接口关闭，避免默认额外监听器和自动证书。

将三个用户unit复制到 `/home/muqiao/.config/systemd/user/`。CPU网页绑定既有Tailscale地址100.67.14.84:18086。路径与地址变化时先修订模板，不能盲目沿用。

```bash
systemd-analyze --user verify ~/.config/systemd/user/rockdepth*.service
systemctl --user daemon-reload
sudo loginctl enable-linger muqiao
systemctl --user enable --now rockdepth-mediamtx rockdepth-publisher rockdepth
```

三个unit均 `Restart=on-failure`、间隔2秒。已启用user linger以支持退出SSH后继续运行；本轮未做部署后的整板重启验收。回放只在板本机循环发布，不依赖笔记本持续喂流。

publisher采用SIGINT和5秒停止上限。实际FFmpeg退出测试仍需要systemd的SIGKILL兜底，约5.32秒后旧进程消失；这属于有界强制停止，不是优雅退出通过。

```bash
systemctl --user stop rockdepth-publisher
systemctl --user start rockdepth-publisher
journalctl --user -u rockdepth -n 30 --no-pager
```

由软件侧根Codex串行执行断流和进程重启注入，不能与另一Agent同时操作同名unit。

## 私有Runtime与NPU服务

Lite2在本轮实际选择系统绝对路径，`LD_LIBRARY_PATH`没有覆盖加载行为。使用systemd原生 `BindReadOnlyPaths`，只在该实验进程的mount namespace内将私有库映射到SDK查找的旧库位置；系统库文件不被替换。

私有库来自官方Toolkit2提交 `59a913d172e7f5ff03c9076e2ec7b1b1288ffd08` 的 `rknpu2/runtime/Linux/librknn_api/aarch64/librknnrt.so`，SHA256为 `d31fc19c85b85f6091b2bd0f6af9d962d5264a4e410bfb536402ec92bac738e8`。实际SDK查询API2.3.2、driver0.9.6。进程映射路径仍可能显示2.0.0b0文件名，须核验namespace内文件哈希与SDK查询，不能从文件名判断版本。

先核对模板绑定目标与 `readlink -f /usr/lib/librknnrt.so` 的结果一致。安装[系统NPU unit](systemd/rockdepth-npu.service)后，先做原始输出对照，再启动独立18087端口；CPU基线长测期间不启动、不改18086。

```bash
sudo install -m 0644 tools/rockdepth/systemd/rockdepth-npu.service \
  /etc/systemd/system/rockdepth-npu.service
sudo systemctl daemon-reload
sudo systemd-analyze verify /etc/systemd/system/rockdepth-npu.service
systemctl --user disable --now rockdepth.service
sudo systemctl enable --now rockdepth-npu
```

该unit以muqiao运行，补充video/render组；失败重启间隔2秒、停止上限10秒。它使用已运行的localhost回放源，不复制另一套视频服务。NPU为当前默认后端；CPU unit保留而停用自启，避免重启后双重推理。切回CPU前先停止NPU，服务管理需要各自正确的system/user上下文，不能假定不同SSH会话共享sudo缓存。

## 原始输出验收与证据

[probe_da2.py](probe_da2.py)复用软件侧 `RKNNDepthBackend`，不重复归一化。输入哈希按冻结的 `.npy` 文件核对，另记录数组字节哈希；两种表示不能混用。每帧保存原始浮点输出、SDK版本、实际库映射/哈希和DRM设备句柄。

运行probe时使用与NPU系统unit相同的私有库绑定。AUTO及core0/core1/core2分别验收，不因一次成功宣称全部核或组合核可用。将输出交给软件侧冻结的30帧数值Oracle；`nRMSE<=0.02`且Spearman>=0.98，不先做尺度对齐。

AUTO、core0、core1、core2各自的30帧原始输出通过；各核输出存在数值差异，不承诺逐元素相同或三核并行已验收。软件侧另完成1800.54秒NPU连续窗口和300.15秒故障复验，均PASS；这些证据与短对照分别记录。停服前完整验收由[固定版本最终报告](https://github.com/qiaoqiao2521/uw-yolo-code-assets/blob/794fed65e19ec9b18154c54f21c718855214fa55/plans/rock5-network-depth/REPORT.md)持有，当前演示已按用户要求暂停。VPU和RGA未验收，已验收路径的解码与预处理使用CPU；部署后整板冷启动另验。

Lite2导入会改写Python日志等级名。本轮曾导致uvicorn的INFO日志配置失败；软件侧在导入边界通过公开logging API恢复既有名称，成功及失败加载路径都有回归。本目录不复制该软件修复，重新部署时须使用软件侧验收后的后端文件。

软件侧唯一计划、验收判据和完整运行状态回源软件仓库。本库的实际板卡结论见[设备档案](../../docs/boards/rock-5c-lite.md)。
