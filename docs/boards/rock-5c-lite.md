# ROCK 5C Lite / RK3582 / 8GB

更新日期：2026-10-06（Asia/Shanghai）。资产编号沿用 `HW-ROCK5C`，SSH别名沿用 `rock-5c`。

## 当前结论与证据

| 项目 | 结论 | 依据与边界 |
|---|---|---|
| 购买版本 | ROCK 5C Lite / RK3582 / 8GB | 用户本次纠正；尚未取得本次实机芯片标识 |
| 标称CPU | 2×Cortex-A76 + 4×Cortex-A55，6核 | Radxa官方Lite规格；不能仅由 `nproc` 确认型号 |
| GPU / NPU | 无GPU；5 TOPS @ INT8 NPU | 官方平台能力；未验证本机NPU驱动或推理 |
| 内存类型 | LPDDR4X | 官方平台能力；8GB为用户确认容量，Linux可用容量待复核 |
| 上线状态 | 用户告知“rock已经上线” | 本机对现有SSH别名连接超时；两条同名Tailscale记录显示离线，当前连接地址待补。不能据此判断板子未开机 |
| 历史系统 | 2026-09-15快照：Armbian 26.8.3，6.18.45-current-rockchip64，Linux内存7934.8 MB | [历史快照](../../snapshots/rock-5c.json)，不代表当前系统 |

规格依据：[Radxa产品介绍](https://docs.radxa.com/en/rock5/rock5c/getting-started/introduction)、[官方Product Brief v1.2](https://dl.radxa.com/rock5/5c/docs/hw/v1100/radxa_rock5c_product_brief_Revision_1.2_g02f49da.pdf)。

## 旧型号误判

旧探针只要在 `/proc/cpuinfo` 中同时发现 `0xd0b`（A76）和 `0xd05`（A55），就写入 `RK3588/S (4×Cortex-A76 + 4×Cortex-A55)`。六核输入已在本地复现同一错误。该值不是芯片型号的原始输出；修复后只描述核心类型并保留SoC未确认状态。

历史快照中的 `threads=8` 来自独立的 `nproc` 字段，不由上述型号分支生成。快照没有保留原始CPU列表，暂不能还原当时的启动配置。保留快照，不将它改写成RK3582现场证据。

设备树中的 `Radxa ROCK 5C`、`rockchip,rk3588s` 或兼容名称不足以区分Lite与标准版。Linux开发者明确讨论过两款SoC的软件兼容性以及共享描述。[Linux-rockchip原始邮件](https://lists.infradead.org/pipermail/linux-rockchip/2024-December/053364.html)

## 最短接续入口

接续owner：根Codex。先取得当前SSH地址和用户名，再只读采集：

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

本次未取得远端CPU、OTP、GPU、NPU或VPU实测。Frigate部署与验收继续沿用[监控计划](../FRIGATE_HAOS_PLAN.md)，不将型号纠正扩大为功能通过。
