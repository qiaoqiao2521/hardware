# Frigate与HAOS监控项目计划

更新日期：2026-10-06（Asia/Shanghai）。

目标是用已有硬件建立可维护的本地监控与家庭自动化方案，并量化当前YOLO识别不足的问题。当前完成资料核实和候选规划，部署与现场验收尚未开始。硬件身份和已有状态见[资产总表](HARDWARE_ASSETS.md)。

## 系统分工与候选设备

| 组件 | 作用 | 候选设备与条件 |
|---|---|---|
| 海康NVR与摄像头 | 提供RTSP视频；现有录像职责保留到验证迁移必要性 | 型号与通道关系待核实；三路RTSP只有旧助手总结，原始检查记录待补 |
| Frigate | 目标检测、跟踪、事件录像与快照 | 优先评估ROCK 5C；RK3566/RK3568是其他试验候选，需板级与驱动检查 |
| Home Assistant与HAOS | 自动化规则、仪表盘、通知；HAOS是其系统安装方式 | Pi 5有官方镜像；合格空闲x86设备可评估Generic x86-64，J1900逐台判断 |
| 现有YOLO | 准确率比较基线与问题定位 | 用同一录像比较，保留现有模型、输入分辨率与参数记录 |

Frigate先用运动检测找到感兴趣区域，再送入目标检测，并持续跟踪目标。区域处理可能改善小目标输入的有效像素，但实际收益取决于画面、模型、参数与样本；不能承诺必然提高准确率。[官方视频管线](https://docs.frigate.video/frigate/video_pipeline/)

## 已核实的兼容性条件

| 项目 | 官方资料结论 | 用户设备的待核实项 |
|---|---|---|
| ROCK 5C型号 | 标准版RK3588S2，Lite版RK3582 | 历史快照只写RK3588/S，仍需确认实机具体版本。[Radxa](https://docs.radxa.com/en/rock5/rock5c/getting-started/introduction) |
| Frigate Rockchip检测 | RKNN为社区支持路线；文档列RK3562、RK3566、RK3568、RK3576、RK3588 | 型号之外，还需模型、驱动与系统兼容。[检测器文档](https://docs.frigate.video/configuration/object_detectors/) |
| Rockchip系统与镜像 | 官方安装说明要求适用的BSP 5.10/6.1与NPU/VPU驱动，采用Rockchip镜像 | ROCK 5C历史内核为6.18.45-current-rockchip64，不能直接判为满足这一路线。[安装文档](https://docs.frigate.video/frigate/installation/) |
| 视频解码 | RKMPP路线提供 `preset-rkmpp` | 摄像头编码、分辨率与实际VPU工作状态单独验证；解码成功不等于NPU推理通过。[硬件解码](https://docs.frigate.video/configuration/hardware_acceleration_video/) |
| HAOS on Pi 5 | 官方安装页面提供Pi 5镜像 | 确认可用启动介质与现有用途。[Pi安装](https://www.home-assistant.io/installation/raspberrypi/) |
| HAOS on Generic x86-64 | 要求64位、UEFI、关闭Secure Boot，使用512n/512e启动介质 | B68TK在2026-10-04以Legacy BIOS启动，UEFI能力与可用性待核实；不直接安装覆盖。[x86安装](https://www.home-assistant.io/installation/generic-x86-64/) |
| HAOS on ROCK 5C | 官方板级支持名单没有ROCK 5C | 不将社区方式写成官方板级镜像支持。[支持名单](https://developers.home-assistant.io/docs/operating-system/boards/overview/) |

### ROCK 5C的设备树识别条件

试验候选版本固定为Frigate v0.18.0及对应 `0.18.0-rk` 镜像；执行时再核对镜像摘要，避免浮动标签改变比较条件。[发布说明](https://github.com/blakeblackshear/frigate/releases/tag/v0.18.0)

这一版本的RKNN检测器读取 `/proc/device-tree/compatible` 的最后一个字段，再与支持SoC列表严格比较；列表包含 `rk3588`，没有 `rk3588s` 或 `rk3588s2`。如果用户所选系统返回后两者，会在型号识别阶段被拒绝。若返回 `rk3588`，仍须检验驱动、模型与持续推理，不能仅凭通过型号匹配判定全部可用。[RKNN源码](https://github.com/blakeblackshear/frigate/blob/v0.18.0/frigate/detectors/plugins/rknn.py#L80)、[支持常量](https://github.com/blakeblackshear/frigate/blob/v0.18.0/frigate/const.py#L96)

## 分阶段执行与验收

| 阶段 | 工作 | 验收依据 | 当前状态 |
|---|---|---|---|
| 1 设备身份与角色 | 给J1900逐台确认身份；ROCK 5C核对版本、系统、设备树和驱动；记录现有用途与可用介质 | 板号/照片或系统信息与台账对应，明确每台设备的已有职责 | 待现场核实 |
| 2 单路视频基线 | 从一条已知摄像头记录主副码流编码、分辨率、FPS、画面与稳定性；保存可用于比较的录像 | 同一片段可重复播放；时间与人工标注可靠；凭据单独保管 | 待执行 |
| 3 单路Frigate试验 | 验证解码、模型推理、跟踪、事件录像与快照；记录资源、温度和连续运行状态 | 输出与实际目标对应，事件录像可回放；VPU/NPU分别有运行证据；试运行时长记录在结果中 | 待执行 |
| 4 准确率比较 | 现有YOLO与Frigate使用同一录像，覆盖白天、夜间、远处小人、遮挡；记录各自模型与参数 | 同一人工标注下比较漏报、误报、事件延迟；改善与退化均保留 | 待执行 |
| 5 扩至三路 | 单路通过后扩展，检查解码、推理排队、磁盘写入、网络负载与持续运行 | 三路真实同时运行，稳定性与质量符合现场目标；不能由单路外推 | 待执行 |
| 6 HA联动 | Frigate与HA连接同一MQTT broker并配置集成；先验证事件与通知，再增加规则 | 真实事件传到HA、通知实际到达；重复、延迟和误报行为有记录 | 待执行 |

MQTT与集成前提见[Frigate安装文档](https://docs.frigate.video/frigate/installation/)。v0.18.0提供Debug Replay，可在后续试验中复用录像调参；不需要为了准备文档先运行摄像头或重新部署。[发布说明](https://github.com/blakeblackshear/frigate/releases/tag/v0.18.0)

## 检测质量记录

对每段测试录像保留场景、时长、人工标注数量、模型版本、输入尺寸、检测FPS、置信度门槛与区域配置。漏报记录为未被识别的真实目标或事件，误报记录为没有真实目标却触发的事件；分母与事件归并规则写明，避免以不同计数口径比较。

目标尺寸、曝光、遮挡、主副码流分辨率和缩放裁剪都可能影响识别。先用相同录像比较结果，再决定调整模型、码流或区域参数。当前没有准确率数字，不能称Frigate已经胜过现有YOLO。

## 接续入口

本轮完成清单与计划。下一次从“阶段1的ROCK 5C兼容性核实”和“一条摄像头的录像基线”接续；在设备角色尚未确认时保留候选安排。硬件仓库负责资产与验收记录，运行凭据、摄像头录像和服务运维资料按已有项目边界保存。
