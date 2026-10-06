# ROCK 5C Lite / RK3582 / 8GB

更新日期：2026-10-06（Asia/Shanghai）。资产编号沿用 `HW-ROCK5C`，SSH别名沿用 `rock-5c`。

## 当前结论与证据

| 项目 | 结论 | 依据与边界 |
|---|---|---|
| 购买版本 | ROCK 5C Lite / RK3582 / 8GB | 购买版本与8GB为用户纠正；本次OTP的 `cpu-code=35 82` 确认实际SoC为RK3582 |
| 标称CPU | 2×Cortex-A76 + 4×Cortex-A55，6核 | Radxa官方Lite规格；不能仅由 `nproc` 确认型号 |
| GPU / NPU | Lite官方无GPU；5 TOPS @ INT8 NPU | 本次OTP的GPU掩码位有标记，设备树无GPU节点；未验证本机NPU驱动或推理 |
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

设备树可见三个NPU节点；DRM只有card0及HDMI，没有render节点。这些只属于枚举结果，不证明NPU推理、TOPS或图形功能通过。OTP的上述三字节映射不含NPU状态位。

先前本机 `eno1` 未连通、Tailscale别名超时；本次重查时有线链路与DHCP已建立，随后Tailscale恢复在线。恢复过程未修改网络配置、SSH别名、固件或设备树，也未重启服务；不能据此断言永久恢复或唯一故障原因。

## 最短接续入口

接续owner：根Codex。当前 `ssh rock-5c` 已通过；若Tailscale暂不可达，先核对电脑共享租约，再用 `ssh -o HostName=10.42.0.220 rock-5c` 连接本次局域网地址。DHCP地址可能变化，不能固定猜测旧地址。只读复核命令：

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
