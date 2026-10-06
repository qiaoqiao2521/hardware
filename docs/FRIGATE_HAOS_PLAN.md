# Frigate与HAOS监控项目计划

更新日期：2026-10-06（Asia/Shanghai）。

目标是用已有硬件建立可维护的本地监控与家庭自动化方案，并量化当前YOLO识别不足的问题。当前完成资料核实和候选规划，部署与现场验收尚未开始。硬件身份和已有状态见[资产总表](HARDWARE_ASSETS.md)。

## 系统分工与候选设备

| 组件 | 作用 | 候选设备与条件 |
|---|---|---|
| 海康NVR与摄像头 | 提供RTSP视频；现有录像职责保留到验证迁移必要性 | 型号与通道关系待核实；三路RTSP只有旧助手总结，原始检查记录待补 |
| Frigate | 目标检测、跟踪、事件录像与快照 | ROCK 5C沿用此前试验候选，当前可用性待确认；监控J1900保留现有职责，RK3566/RK3568需板级与驱动检查 |
| Home Assistant与HAOS | 自动化规则、仪表盘、通知；HAOS是其系统安装方式 | 树莓派已售出；从在手x86中核实用途、空闲状态与UEFI后再安排，暂无指定空闲宿主机 |
| 现有YOLO | 准确率比较基线与问题定位 | 用同一录像比较，保留现有模型、输入分辨率与参数记录 |

Frigate先用运动检测找到感兴趣区域，再送入目标检测，并持续跟踪目标。区域处理可能改善小目标输入的有效像素，但实际收益取决于画面、模型、参数与样本；不能承诺必然提高准确率。[官方视频管线](https://docs.frigate.video/frigate/video_pipeline/)

## 已核实的兼容性条件

| 项目 | 官方资料结论 | 用户设备的待核实项 |
|---|---|---|
| ROCK 5C型号 | 标准版RK3588S2，Lite版RK3582 | 历史快照只写RK3588/S，仍需确认实机具体版本。[Radxa](https://docs.radxa.com/en/rock5/rock5c/getting-started/introduction) |
| Frigate Rockchip检测 | RKNN为社区支持路线；文档列RK3562、RK3566、RK3568、RK3576、RK3588 | 型号之外，还需模型、驱动与系统兼容。[检测器文档](https://docs.frigate.video/configuration/object_detectors/) |
| Rockchip系统与镜像 | 官方安装说明要求适用的BSP 5.10/6.1与NPU/VPU驱动，采用Rockchip镜像 | ROCK 5C历史内核为6.18.45-current-rockchip64，不能直接判为满足这一路线。[安装文档](https://docs.frigate.video/frigate/installation/) |
| 视频解码 | RKMPP路线提供 `preset-rkmpp` | 摄像头编码、分辨率与实际VPU工作状态单独验证；解码成功不等于NPU推理通过。[硬件解码](https://docs.frigate.video/configuration/hardware_acceleration_video/) |
| HAOS on Pi 5（平台参考） | 官方安装页面提供Pi 5镜像 | 用户确认已售出，已从当前候选移除；仅保留官方能力背景。[Pi安装](https://www.home-assistant.io/installation/raspberrypi/) |
| HAOS on Generic x86-64 | 要求64位、UEFI、关闭Secure Boot，使用512n/512e启动介质 | B68TK在2026-10-04以Legacy BIOS启动，UEFI能力与可用性待核实；不直接安装覆盖。[x86安装](https://www.home-assistant.io/installation/generic-x86-64/) |
| HAOS on ROCK 5C | 官方板级支持名单没有ROCK 5C | 不将社区方式写成官方板级镜像支持。[支持名单](https://developers.home-assistant.io/docs/operating-system/boards/overview/) |

### ROCK 5C的设备树识别条件

试验候选版本固定为Frigate v0.18.0及对应 `0.18.0-rk` 镜像；执行时再核对镜像摘要，避免浮动标签改变比较条件。[发布说明](https://github.com/blakeblackshear/frigate/releases/tag/v0.18.0)

这一版本的RKNN检测器读取 `/proc/device-tree/compatible` 的最后一个字段，再与支持SoC列表严格比较；列表包含 `rk3588`，没有 `rk3588s` 或 `rk3588s2`。如果用户所选系统返回后两者，会在型号识别阶段被拒绝。若返回 `rk3588`，仍须检验驱动、模型与持续推理，不能仅凭通过型号匹配判定全部可用。[RKNN源码](https://github.com/blakeblackshear/frigate/blob/v0.18.0/frigate/detectors/plugins/rknn.py#L80)、[支持常量](https://github.com/blakeblackshear/frigate/blob/v0.18.0/frigate/const.py#L96)

## 新补会话中的候选限制

新增设备与历史商品配置见[选型及升级附录](HARDWARE_SELECTION_CONTEXT.md)。2026-10-06用户明确V15B、Wyse5070、CM01和黑豹X2为后续购买目标；它们在购入并核实后才参与现场规划，具体购买顺序未定。其他历史商品沿用讨论参考，不改变单路试验与准确率比较的验收顺序。

| 候选 | 可评估角色 | 必须先核实的条件 |
|---|---|---|
| 天波TELPO V15B（待购买） | ARM检测/工控节点 | 用户看重8GB成品盒装与性价比；商品实装、可用Linux、管理权限、恢复固件、设备树匹配及NPU/VPU分别核实，不能将宣传接入路数当检测FPS |
| Firefly RK3399Pro板线索 | 旧NPU/CAN研究 | 商品板型待确认；官方Toolkit2将RK3399Pro指向旧Toolkit，两者不兼容，不能直接套用当前Frigate Rockchip镜像与模型。系统截图已占满存储，但没有推理或故障定位证据。[Rockchip官方说明](https://github.com/airockchip/rknn-toolkit2) |
| Wyse5070 J5005（待购买） | x86解码/服务方向 | 用户看重综合性价比；商品实装、供电、存储协议、UEFI和目标负载待核实，核显EU数量与跑分不能代替实际解码或检测能力 |
| 阿里CM01（待购买） | 屏幕/交互扩展方向 | 用户按RK3399考虑；具体版本、屏幕、触摸、摄像头与可维护系统分别确认，尚无本轮官方型号确认 |
| 黑豹X2（待购买） | 监控配套小节点 | 用户看重接口齐全和小体积；商品接口、系统与配套职责待核实，不预设多路检测已可用 |
| 国美云（在手） | 显示/触摸交互候选 | 当前用途待补，屏幕、触摸、摄像头、音频和可维护系统分别确认 |
| J4125触摸机、HP t630/t740 | 历史讨论参考 | 尚非本次确认购买目标，保留原商品与官方能力资料 |
| 旧惠普商用板与航嘉电源 | 旧平台实验讨论项 | 先确认主板型号；若为4000 Pro SFF，官方最大8GB，换CPU不解决32GB目标。电源健康未验收，不能凭能开机分配长期供电职责 |

## 分阶段执行与验收

| 阶段 | 工作 | 验收依据 | 当前状态 |
|---|---|---|---|
| 1 设备身份与角色 | J1900数量与监控/软路由角色已确认，触摸机为第三台；补逐台板号与配置，ROCK 5C核对可用性、版本、系统和驱动 | 板号/系统信息与台账对应；保留现有职责，指定宿主前确认空闲状态 | 用户角色已确认；身份/配置待补 |
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

本轮完成清单与计划。下一次从“阶段1的设备可用性/配置核实”和“一条摄像头的录像基线”接续；ROCK 5C需先确认当前可用性再验证兼容性，其余尚未指定角色的设备保留候选安排。硬件仓库负责资产与验收记录，运行凭据、摄像头录像和服务运维资料按已有项目边界保存。

当前职责以用户确认的三台J1900记录为准：一台监控、一台软路由、一台B68TK触摸工控机（用途待补）。设备在手不代表空闲，不默认重装监控机或软路由；Pi 5已售出，不安排HAOS。其余在手x86和未来Wyse5070是否承担HAOS，待用途与安装条件确认后决定。
