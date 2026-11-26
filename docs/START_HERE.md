# 硬件与嵌入式学习入口

硬件资产、单片机课程、嵌入式实验和诊断工具统一在 `hardware` 维护。`embedded-learning` 是旧归档仓库，日常学习和新增记录都从这里进入。

[返回仓库首页](../README.md) · [查看硬件资产](HARDWARE_ASSETS.md) · [接线与烧录记录](BOARD_WIRING_AND_FLASHING.md)

## 先找你要做的事

| 目的 | 入口 | 内容与边界 |
| --- | --- | --- |
| 看现有设备、规格和用途 | [硬件资产总表](HARDWARE_ASSETS.md)、[板卡档案](boards/) | 在手、已售、待核实分别记录；旧快照不代表当前状态 |
| 从头学习 51 单片机 | [整理后的 51 课程](../mcu/51/51_mcu/README.md) | 按课编号整理的源码；原工程以 Keil C51 为基础，SDCC 迁移仍需逐项核查 |
| 查 51 原始课件、开发板资料和配套软件 | [51 单片机入门教程资料](../mcu/51/51单片机入门教程资料/) | 保留原资料包结构，用于对照课程来源 |
| 给 AT89S52 做最小点灯实验 | [AT89S52 + SDCC](../mcu/51/at89s52_blink_sdcc/README.md) | 独立最小工程，包含 LED、数码管和烧录说明；下载方式须匹配实际芯片和下载器 |
| 按章节学习 STM32 | [STM32 学习指引](../mcu/stm32/learning/学习指引.md)、[逐课工程](../mcu/stm32/learning/) | GPIO、OLED、中断、定时器、ADC、DMA、串口及 I2C/SPI 等现有课程 |
| 把 STM32 外设组合成项目 | [课程综合项目](../mcu/stm32/projects/course_capstone/README.md) | 用 `APP` 选择机械臂、网关、小车、记录器等已有工程入口 |
| 查 ESP32 机械臂控制固件 | [ESP32 双模控制器](../mcu/esp32/esp32_arm_controller/README.md) | Wi-Fi / BLE、舵机命令和 PlatformIO 工程 |
| 学习共用驱动、软件测试和多板卡实验 | [嵌入式实验台](../lab/embedded-lab-monorepo/README.md) | STM32、STC89C52、HPAD 和 WM8960 各自保留构建方式与验证边界 |
| 查看硬件体检和故障记录 | [Hardwire 上手](../README.md)、[实战案例](cases/) | 只读采集、历史快照与诊断；不等同于固件烧录或设备运维 |

## 第一次从哪一份开始

### 学 STM32：先读一课，再扩展到实验台

从 [lesson_2-1](../mcu/stm32/learning/lesson_2-1/) 进入，结合[课程指引](../mcu/stm32/learning/学习指引.md)找 `src/` 中的程序入口和 `boards/` 中的板卡配置；遇到概念问题，查 [STM32 概念索引](../mcu/stm32/docs/concepts/README.md)。

课程工程的工作目录现在是 `hardware/mcu/stm32/learning/lesson_*`。旧文档中的 `stm32/...` 和 `E:\web\embedded\...` 是迁入前路径，应按本页链接定位。

需要研究共用驱动、统一构建与主机测试时，再看实验台的 [GPIO 点灯示例](../lab/embedded-lab-monorepo/examples/01_gpio_led/README.md)和[平台层](../lab/embedded-lab-monorepo/common/)。课程目录与实验台是两种已有组织方式，不必先把它们改成同一套工程。

### 学 51：先分清课程源码与芯片目标

| 手头目标 | 建议先打开 |
| --- | --- |
| 按原课程学习点灯、按键、数码管 | [整理后的课程目录](../mcu/51/51_mcu/learning/)、[第一课点灯](../mcu/51/51_mcu/learning/lesson_02_01_led_on/) |
| STC89C52，想看 SDCC 最小构建链 | [实验台 MCS-51 说明](../lab/embedded-lab-monorepo/mcs51/README.md)、[点灯示例](../lab/embedded-lab-monorepo/mcs51/examples/01_blink/README.md) |
| AT89S52，想做独立最小工程 | [AT89S52 点灯工程](../mcu/51/at89s52_blink_sdcc/README.md) |

原始资料包和整理后的课程同时保留，前者用于查资料，后者用于按课阅读；STC89C52 与 AT89S52 的烧录流程分别看各自说明。

### 暂时没有板子：从 HPAD 的模拟数据闭环开始

打开 [HPAD 快速上手](../lab/embedded-lab-monorepo/rpi_hpad/QUICKSTART.md)，按 `mock → log → replay` 了解采样、记录和回放。入口位于 `hardware/lab/embedded-lab-monorepo/rpi_hpad`，不会通过这条模拟流程采集真实 ADC 数据。

HPAD 的 `real` backend 尚未实现实际硬件接入；已有协议、模拟和回放示例不能作为 ADS1256/DAC8532 真板验收证据。

## 嵌入式实验台的四个入口

| 主线 | 代码与说明 | 验证说明 |
| --- | --- | --- |
| STM32F103 | [9 个示例](../lab/embedded-lab-monorepo/examples/)、[实验台总说明](../lab/embedded-lab-monorepo/README.md) | [真板待验事项](../lab/embedded-lab-monorepo/HARDWARE_PENDING.md)；软件构建与真板烧录分别记录 |
| STC89C52 / MCS-51 | [说明](../lab/embedded-lab-monorepo/mcs51/README.md)、[3 个示例](../lab/embedded-lab-monorepo/mcs51/examples/) | [串口、按键与烧录待验](../lab/embedded-lab-monorepo/mcs51/HARDWARE_PENDING.md) |
| Raspberry Pi HPAD | [快速上手](../lab/embedded-lab-monorepo/rpi_hpad/QUICKSTART.md)、[事件协议](../lab/embedded-lab-monorepo/rpi_hpad/PROTOCOL.md) | 先使用 `mock` / `replay`；真实 SPI/GPIO 与精度另验 |
| WM8960 Audio HAT | [驱动来源与安装说明](../lab/embedded-lab-monorepo/WM8960-Audio-HAT/README.md) | 保留 vendor 驱动、overlay 和 ALSA 配置；不在三条软件检查链内 |

准备好各子项目的依赖后，可从 `hardware` 仓库根目录进入实验台，运行既有软件检查：

```bash
cd lab/embedded-lab-monorepo
bash scripts/check-all.sh
```

脚本依次检查 STM32、MCS-51 与 HPAD，会生成构建产物和测试环境；不包含 WM8960 安装，也不代表真实板卡验证完成。各脚本依赖见[实验台环境依赖](../lab/embedded-lab-monorepo/README.md#环境依赖)。本次资料整理仅核对入口与文件，不新增硬件验收结论。

## 接线、工具链和旧记录

| 要查的资料 | 入口 |
| --- | --- |
| 板卡接线、端口和固件操作记录 | [接线与烧录](BOARD_WIRING_AND_FLASHING.md) |
| 编译器、调试器和 Windows / WSL 工具路径 | [工具链历史报告](TOOLCHAIN_SUMMARY.md)；其中版本和路径是历史环境记录 |
| 现有烧录和跨端脚本 | [tools/flashing](../tools/flashing/) |
| 硬件调优与排查案例 | [docs/cases](cases/) |
| 后续资料的归档位置和项目边界 | [PROJECT.md](../PROJECT.md) |

今后课程与固件继续归 `mcu/`，综合实验归 `lab/`，接线和设备记录归 `docs/`，工具脚本归 `tools/`；在同一仓库内按用途查找和更新。
