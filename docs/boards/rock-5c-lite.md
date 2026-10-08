# ROCK 5C Lite / RK3582 / 8GB

更新日期：2026-10-08（Asia/Shanghai）。资产编号沿用 `HW-ROCK5C`，SSH别名沿用 `rock-5c`。

## 刷写前结论与证据

以下运行结果来自2026-10-06刷写前的Armbian系统。用户随后明确选择重刷官方Radxa OS；新系统启动与网络验收单独记录，不沿用这些旧系统结果。

| 项目 | 结论 | 依据与边界 |
|---|---|---|
| 购买版本 | ROCK 5C Lite / RK3582 / 8GB | 购买版本与8GB为用户纠正；本次OTP的 `cpu-code=35 82` 确认实际SoC为RK3582 |
| 标称CPU | 2×Cortex-A76 + 4×Cortex-A55，6核 | Radxa官方Lite规格；不能仅由 `nproc` 确认型号 |
| GPU / NPU | Lite官方无GPU；5 TOPS @ INT8 NPU | 本次OTP的GPU掩码位有标记，设备树无GPU节点；三个NPU节点均disabled、无驱动绑定，当前NPU未启用 |
| 当前CPU | 4×A55 + 4×A76，系统报告8核在线 | `nproc`、`nproc --all` 均为8；CPU masks为0-7；与官方Lite六核规格分开记录 |
| 内存类型 | LPDDR4X | 8GB为用户确认容量；本次Linux报告总内存7.7 GiB，不能把可用容量当作标称容量 |
| 上线状态 | 电脑有线共享与SSH已现场连通 | `eno1`共享10.42.0.1/24；DHCP租约名rock-5c、地址10.42.0.220；保存的SSH主机密钥匹配，用户qiao。随后Tailscale上线，原 `ssh rock-5c` 新连接也通过 |
| 当前系统 | Armbian 26.8.3 resolute；6.18.45-current-rockchip64 | 本次SSH读取，与历史记录分别保存 |
| 历史系统 | 2026-09-15快照：Armbian 26.8.3，6.18.45-current-rockchip64，Linux内存7934.8 MB | [历史快照](../../snapshots/rock-5c.json)，不代表当前系统 |

规格依据：[Radxa产品介绍](https://docs.radxa.com/en/rock5/rock5c/getting-started/introduction)、[官方Product Brief v1.2](https://dl.radxa.com/rock5/5c/docs/hw/v1100/radxa_rock5c_product_brief_Revision_1.2_g02f49da.pdf)。

## 旧型号误判

旧探针只要在 `/proc/cpuinfo` 中同时发现 `0xd0b`（A76）和 `0xd05`（A55），就写入 `RK3588/S (4×Cortex-A76 + 4×Cortex-A55)`。六核输入已在本地复现同一错误。该值不是芯片型号的原始输出；修复后只描述核心类型并保留SoC未确认状态。

历史快照中的 `threads=8` 来自独立的 `nproc` 字段，不由上述型号分支生成。本次现场也读取到8核，因此不能将这个历史字段直接判为错误。快照没有保留原始CPU列表，仍不能还原当时的启动配置；保留旧快照，不改写历史。

设备树中的 `Radxa ROCK 5C`、`rockchip,rk3588s` 或兼容名称不足以区分Lite与标准版。Linux开发者明确讨论过两款SoC的软件兼容性以及共享描述。[Linux-rockchip原始邮件](https://lists.infradead.org/pipermail/linux-rockchip/2024-December/053364.html)

## 本次只读芯片标识与CPU检查

本次在确认nvmem provider为 `rockchip,rk3588-otp` 后，仅读取以下两个字段，没有导出唯一标识或整块OTP：

| 字段 | 原始值 | 解释边界 |
|---|---|---|
| cpu-code，逻辑偏移0x02、2字节 | `35 82` | U-Boot主线对应RK3582；不依赖rk3588兼容名称判断 |
| ip-state，逻辑偏移0x1d、3字节 | `00 08 00` | CPU位未置；GPU掩码中的bit3置位；该实现使用的vdec/venc位未置。未置位不等于完整功能或稳定性通过 |

当前系统的CPU现场值：

```text
nproc = 8
nproc --all = 8
online = present = possible = 0-7
offline = 空
/proc/cpuinfo: 0xd05 × 4，0xd0b × 4
CPU启动限制: 未检出maxcpus、nr_cpus或nosmp
DT cpu@0、100、200、300、400、500、600、700: 均未显式禁用
```

当前U-Boot主线RK3582策略会把原始 `00 08 00` 转成 `c0 9e 04`，额外禁用一组A76、GPU以及各一个vdec/venc。因此当前8核在线结果不符合这版主线的CPU裁切策略；实际启动固件版本、厂商策略或设备树处理原因仍待核实。不能称为特殊料、解锁成功或八核稳定性验收。[U-Boot实现](https://github.com/u-boot/u-boot/blob/master/arch/arm/mach-rockchip/rk3588/rk3588.c)

设备树可见三个NPU节点，但后续逐节点读取确认全部为 `disabled`；没有NPU平台驱动绑定或设备接口。DRM只有card0及HDMI，没有render节点。OTP的上述三字节映射不含NPU状态位。

先前本机 `eno1` 未连通、Tailscale别名超时；本次重查时有线链路与DHCP已建立，随后Tailscale恢复在线。恢复过程未修改网络配置、SSH别名、固件或设备树，也未重启服务；不能据此断言永久恢复或唯一故障原因。

## GPU与NPU：官方规格和当前系统

Radxa产品对比表明确写Lite的GPU为 `N/A`；官方Product Brief明确写NPU为5 TOPS @ INT8。官网通用介绍中的八核CPU与Mali-G610段落不能套到Lite，应以明确标注型号的参数表为依据。

Rockchip RK3582 Datasheet第9页§1.2.6写三个NPU core、最高5 TOPS，第10页§1.2.7另列2D图像引擎。2D缩放、旋转、显示控制与Mali 3D GPU是不同单元；有HDMI或DRM card0不证明有Mali GPU。[芯片官方资料](https://dl.radxa.com/rock5/5c/docs/hw/datasheet/Rockchip%20RK3582%20Datasheet%20V1.1-20230221.pdf)

本次只读系统检查：

| 项目 | 现场结果 | 可支持的结论 |
|---|---|---|
| NPU设备树 | npu@fdab0000、fdac0000、fdad0000均 `status=disabled`，兼容名为rockchip,rk3588-rknn-core | 三个软件节点存在，但当前系统未启用它们 |
| NPU驱动与接口 | 没有NPU平台驱动绑定；未加载rknpu/rocket；没有 `/dev/rknpu` 或 `/dev/accel`；ldconfig未列出RKNN库 | 当前未提供可用的NPU推理栈；不能称板上没有NPU或硬件损坏 |
| 内核选项与模块文件 | CONFIG_DRM_ACCEL_ROCKET=m；后续现场确认rocket.ko已安装，modinfo匹配当前内核与rockchip,rk3588-rknn-core | 模块文件存在，但未加载、绑定或启用NPU；不能等同于官方RKNN的rknpu驱动栈 |
| GPU与显示 | 无GPU设备树节点、无 `/dev/mali0` 或render节点；card0绑定rockchip-drm的display-subsystem | 当前未提供Mali图形加速；card0为显示控制器 |
| RGA / VPU | rockchip-rga平台驱动已绑定，但未见 `/dev/rga` 或 `/dev/mpp_service` | 驱动绑定与用户态接口/实际功能分别验收；未做图像或编解码验证 |

Radxa专门说明ROCK 5C Lite / RK3582在RKNN和RKLLM中使用 `target_platform=rk3588`，RK3588模型可用于RK3582。软件名称与实际芯片标识分开，不能因为模型平台叫rk3588而改判SoC。[RK3582 NPU平台指定说明](https://docs.radxa.com/e/e54c/app-development/artificial-intelligence/rk3582_npu_explanation)

此轮只核对官方资料、设备树、模块、驱动绑定和设备节点。没有修改设备树、加载模块、安装运行时、更换内核或运行推理。下一步须选择与RKNN栈匹配的系统/驱动并实际验证模型，不能仅把disabled改为okay就宣称NPU可用。

后续系统选择复核：当前系统提供主线rocket模块；Linux官方文档将其用户态定义为Mesa Gallium rocket，并仅列RK3588为支持硬件，未对本块RK3582完成验证。Rockchip官方RKNN方案使用RKNPU内核驱动与RKNN Runtime/Lite2，不能把rocket模块存在视为RKNN环境就绪。[Linux rocket文档](https://www.kernel.org/doc/html/latest/accel/rocket/index.html)、[Rockchip RKNN说明](https://github.com/airockchip/rknn-toolkit2)

不必先重装整个系统：Armbian支持切换内核，当前本机APT索引中有vendor内核与DTB候选26.8.3；但仅有候选包或vendor名称不证明已包含并启用rknpu。保留现有系统时，需核对匹配的内核、DTB、驱动和运行库，再执行模型验收。当前Python为3.14.4，而官方RKNN 2.3.2说明列Python 3.6–3.12；使用Python接口还需单独配置匹配环境。[Armbian内核管理](https://docs.armbian.com/config/)、[Rockchip版本说明](https://github.com/airockchip/rknn-toolkit2)

若选择备用TF测试官方路线，Radxa下载页明确提供ROCK 5C Lite的Debian12 CLI b1镜像。镜像启动后仍需检查rknpu驱动、用户态包与实际推理，不能承诺刷入即通过NPU验收；Radxa说明部分CLI镜像可能缺少RKNPU2用户态包。本次没有下载镜像、切换内核、安装软件或刷写介质。[Lite官方下载入口](https://docs.radxa.com/en/rock5/rock5c/download)、[Radxa板端驱动与CLI包说明](https://docs.radxa.com/rock5/rock5a/app-development/ai/rkllm-install)

## 刷写前Wi-Fi连接排查

2026-10-06再次现场读取：当前SSH由电脑有线共享网络承载，`end0=10.42.0.220/24`、默认网关为电脑的 `10.42.0.1`；SSH别名使用Tailscale地址 `100.103.100.10`。用户希望ROCK自动连接家庭Wi-Fi。直接SSH成功不证明无线已连接。

板上使用Netplan、systemd-networkd与wpa_supplicant管理网络，当前没有可用的nmcli命令。`/etc/netplan/60-rock5c-wifi.yaml` 文件存在，权限为root 0600；`netplan-wpa-wlan0.service` 为active。没有读取或导出无线密码。

只读现场字段：

```text
iw dev wlan0 link: Not connected.
networkctl status wlan0: no-carrier (configuring), Online state: offline
wlan0: 接口存在，无IPv4地址
Wi-Fi rfkill soft=0, hard=0
lsusb: AICSemi AIC 8800D80
netplan-wpa-wlan0.service: active (running)
```

接口、配置文件和服务存在不能证明关联或联网成功；历史快照的 `active_interfaces` 也只枚举非lo接口，不能证明历史Wi-Fi已连接。当前qiao账号不能免密sudo，也无权访问wpa控制接口，因此保存的SSID、网络启用标志和认证状态仍待核实，不能判定密码错误、信号问题或驱动故障。

此前接续入口为用户执行以下只读命令；后来用户改为直接重刷，不再等待旧系统sudo检查。TF插入电脑后，离线读取确认保存的家庭SSID与无线密码均匹配当前电脑配置，因此不能把旧无线故障归因于密码已失效。旧故障的唯一原因仍未确定。

```bash
ssh -t rock-5c 'sudo wpa_cli -i wlan0 list_networks && sudo wpa_cli -i wlan0 status'
```

## 官方系统重刷（2026-10-06）

用户明确选择直接刷TF，并要求配置muqiao用户、家庭Wi-Fi与SSH，另将系统镜像加入既有Ventoy盘。Wi-Fi凭据、账号密码、SSH私钥和原系统备份只保留在受限本地目录与TF卡，不进入仓库。

目标TF通过USB读卡器枚举为Mass-Storage，容量250145669120字节；原rootfs的BOARD=rock-5c、Armbian26.8.3及SSH主机公钥指纹均匹配刷写前的ROCK。Ventoy位于另一块253671505920字节U盘；内置NVMe与Ubuntu移动盘排除在写入范围外。用户的直接刷写授权覆盖此已识别目标，写前再次核对读卡器身份与原文件系统UUID。

使用Radxa官方Lite下载项所链接的 `rock-5c_bookworm_cli_b1.output.img.xz`，压缩文件757179348字节；官方SHA-512核对通过。发布仓库的latest同为rsdk-b1。目标镜像为Debian12 CLI、6.1.43-15-rk2312内核，配置明确 `CONFIG_ROCKCHIP_RKNPU=y`，manifest包含rknpu2-rk3588、NetworkManager、OpenSSH与Avahi；这只证明配套软件存在，实际NPU推理待板上验收。

原系统文件、分区表、文件系统元数据与前16 MiB启动区域已备份到受限本地目录；浏览器配置目录未复制。镜像副本离线创建muqiao用户与sudo组，保存密码哈希，写入家庭Wi-Fi自动连接及有线DHCP配置，启用SSH和Avahi，并保留此板的SSH主机密钥。官方首次启动脚本改为始终启用SSH，删除其默认账号创建与主机密钥重新生成步骤，保留rootfs扩容。

账号哈希与组、NetworkManager真实配置解析、SSH配置/主机密钥解析、首次启动脚本及ext4/FAT只读检查均通过。4860060672字节定制镜像已写入，完整读回SHA-256与镜像一致：`2f8a62c28ac3e7eb021481b1231d8f10ddcd614fee7485b2db7dbec4be5e2b24`。卡上config/efi/rootfs三个分区正确枚举，随后安全断电移除读卡器；媒体验收通过，实机启动仍待验证。

Ventoy的 `ARM/ROCK-5C-Lite` 已加入官方原始压缩镜像、校验文件与说明，复制后再次核对官方SHA-512通过。该原版镜像没有加入私人配置，也不是普通x86电脑的Ventoy启动安装项。电脑的 `ssh rock-5c` 已改为muqiao@rock-5c.local，保留维护公钥及既有主机密钥别名；新地址解析与实际登录待板子上电后验证。

## 新系统启动与SSH验收（2026-10-08）

用户确认已重启，并将ROCK网线直接连接电脑。电脑保持 `88888888` Wi-Fi，不切换其无线配置；有线共享为10.42.0.1/24。最初ARP扫描无回应，随后收到主机名rock-5c的新DHCP请求并分配10.42.0.221。不能把此前无回应直接判为启动失败，也不能沿用旧租约地址。

通过严格主机密钥检查，以muqiao成功登录；独立禁用公钥后，用户指定的密码也完成SSH登录。mDNS随后解析为10.42.0.221，原 `ssh rock-5c` 新会话通过。现场系统为Debian12 bookworm、6.1.43-15-rk2312，CPU在线范围0-5、nproc为6；rootfs已扩容至229G，剩余217G。有线接口为end1，ssh、NetworkManager、Avahi和rknpu2服务均active。

家庭无线尚未通过：home-wifi配置已加载，autoconnect=yes、凭据存在，rfkill没有阻止；wlan0可扫描到MUQIAO-2.4G。无线设备为USB AIC8800D80。wpa_supplicant反复报告 `CTRL-EVENT-ASSOC-REJECT status_code=1`，失败发生在关联阶段；不能据此判定无线密码错误。手动激活曾返回网络未找到；随后关闭省电并指定该AP重试，仍发生关联拒绝，测试结束后恢复原省电设置。关联、射频条件和驱动/AP兼容性仍待核实。此前有线DHCP多次超时，取得地址后SSH才具备网络入口；账号验证本身已通过。

NPU驱动入口已出现：平台fdab0000.npu绑定RKNPU，renderD129对应RKNPU，内核报告rknpu0.9.6；renderD128对应显示驱动rockchip-drm，不作Mali GPU证据。启动日志仍有fdac/fdad资源区域申请警告，模型推理、各核可用性和稳定性尚未验收，不将服务active或设备节点存在写成功能通过。

## NPU模型与私有远程SSH验收（2026-10-08）

采用板上rknpu2-rk3588包记录的官方源码链：Radxa打包提交 `e16dcae133a61f3564470b98119fe1006cd6ca23` 对应Rockchip SDK提交 `77b71094e08391c543d9c65fea5f7cf98cc16eee`。使用该提交的RK3588 MobileNet V1模型与224×224狗图，按RGB输入调用RKNN模型接口；模型SHA-256为 `381dae3b7038a98b10f6ec9dcdbb094a49247341856fb294e692ef518218fcfb`。[官方模型来源](https://github.com/airockchip/rknn-toolkit2/tree/77b71094e08391c543d9c65fea5f7cf98cc16eee/rknpu2/examples/rknn_mobilenet_demo)

板上查询得到API2.0.0b0、driver0.9.6；AUTO及core0/core1/core2分别推理通过，四次top1均为156、分数0.884766、概率和0.999737，跨核最大输出差异为0。单次推理及取输出调用约3.08–3.21ms；仅为此模型的短测试，不作为YOLO、5 TOPS或持续负载基准。独立INT8矩阵API探针两次出现数值不一致，原因未定位；不能将其判为接口可用，也不据此推翻已通过的模型路径。启动资源警告、其他模型、各类算子与稳定性继续保留未验收状态。

Tailscale1.104.1从官方Debian12源安装，使用既有控制端签发的单次、非ephemeral、预授权tag:server登记密钥创建 `rock5c-lite-rk3582`；未复制旧节点状态。IPv4为100.67.14.84，MagicDNS为rock5c-lite-rk3582.tail24a4cf.ts.net。配置accept-dns=false、accept-routes=false、ssh=false，不广告子网或出口节点；继续使用muqiao与既有OpenSSH主机身份。所有本轮临时登记密钥文件已删除，旧离线节点未删除。[官方安装源](https://pkgs.tailscale.com/stable/#debian-bookworm)

电脑及外部Greenrise均通过Tailscale新建OpenSSH会话，严格核对原主机密钥。tailscaled重启后仍Running，远端SSH复测通过；systemd自启为enabled，完整断电冷启动尚未复测。本机 `ssh rock-5c` 使用100.67.14.84，`ssh rock-5c-lan` 保留mDNS局域网恢复入口；当前end1=10.42.0.221/24，家庭无线仍未关联，因此当前外网通路依赖电脑有线共享。

## 最短接续入口

接续owner：根Codex。媒体、启动、有线及Tailscale SSH、官方MobileNet三核路径已验收，保持电脑原Wi-Fi与网线恢复入口。接续家庭无线关联故障、独立矩阵API差异及目标YOLO模型验收；旧100.103.100.10不作为新系统地址。DHCP地址可能变化，应读取当前租约或mDNS结果，不能固定猜测旧地址。登录后只读复核命令：

```bash
nproc
nproc --all
lscpu
cat /sys/devices/system/cpu/{online,offline,present,possible}
cat /proc/cmdline
tr '\0' '\n' < /proc/device-tree/model
tr '\0' '\n' < /proc/device-tree/compatible
free -h
```

`nproc` 报当前进程可用CPU数，可能受亲和性或运行环境限制；6或8都不能单独证明SoC SKU。交叉检查CPU masks、启动限制和设备树后，再读取可用的芯片标识。[GNU nproc手册](https://www.gnu.org/software/coreutils/manual/html_node/nproc-invocation.html)

若系统暴露OTP nvmem，先确认provider为 `rockchip,rk3588-otp`，仅以只读方式读取 `cpu-code` 的两个字节和 `ip-state` 的三个字节。不得导出整块OTP、唯一标识或执行写入。U-Boot主线使用逻辑偏移 `0x02` 和 `0x1d`；`35 82` 对应RK3582。解读时区分OTP原始标记和启动代码追加的禁用策略，不能把设备树 `fail` 自动判为物理坏块或可解锁单元。[U-Boot实现](https://github.com/u-boot/u-boot/blob/master/arch/arm/mach-rockchip/rk3588/rk3588.c)、[Linux只读OTP驱动](https://github.com/torvalds/linux/blob/master/drivers/nvmem/rockchip-otp.c)

本次已取得远端CPU和OTP原始字段，以及网络/设备树枚举。GPU、NPU、VPU功能和持续负载未验收。Frigate部署与验收继续沿用[监控计划](../FRIGATE_HAOS_PLAN.md)，不将型号纠正扩大为功能通过。
