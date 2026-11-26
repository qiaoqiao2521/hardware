# MCS-51 / STC89C52

[返回实验台](../README.md) · [返回硬件学习入口](../../../docs/START_HERE.md)

这里维护 STC89C52 的 SDCC 最小构建链、串口发送和按键去抖示例，平台代码与 STM32 分开。

## 实际入口

| 目录 | 内容 |
| --- | --- |
| [examples/01_blink](examples/01_blink/README.md) | 点灯最小工程 |
| [examples/03_uart_tx](examples/03_uart_tx/README.md) | 串口发送示例 |
| [examples/04_key_debounce](examples/04_key_debounce/README.md) | 按键去抖示例 |
| [boards/stc89c52rc](boards/stc89c52rc/README.md) | 板卡配置与引脚说明 |
| [common](common/) | 共用代码 |
| [scripts](scripts/) | 工具链探测、构建与检查脚本 |
| [tests](tests/) | 主机侧测试 |

旧 `mcs51/Learn_STC89C52/` 第三方课程快照已在迁入时移除，本目录不再包含该路径。原课程来自 jjejdhhd 的 [Learn_STC89C52](https://github.com/jjejdhhd/Learn_STC89C52)，[UPSTREAM.md](UPSTREAM.md) 保留当年的导入日期与提交号；其中关于快照仍在本地的描述属于历史记录，以本页目录和实验台迁入说明为准。

## 工作目录与软件检查

从 `hardware` 仓库根目录进入：

```bash
cd lab/embedded-lab-monorepo/mcs51
```

本主线使用 `SDCC + packihx` 构建；`stcgal` 用于后续匹配板卡的串口下载。依赖准备见[实验台环境依赖](../README.md#环境依赖)。在本目录运行既有入口：

```bash
scripts/probe-toolchain.sh
scripts/build.sh 01_blink
scripts/check.sh
```

`check.sh` 包含工具链检查、三个示例的构建、主机侧测试与产物检查，不执行真板烧录。产物位于本目录的 `build/<example>/`。

## 验证边界

历史记录保留了 `01_blink` 在树莓派上由 `.c → .ihx → .hex` 的软件构建结果；本次资料整理未重复该验证，也未连接真实板卡。

真板烧录、串口输出、按键脚位和现象观察仍按 [HARDWARE_PENDING.md](HARDWARE_PENDING.md) 验收。构建成功与主机测试通过不能替代这些板级结果。
