# Hardware 与嵌入式学习归集记录

归集日期：2026-11-26。当前维护仓库为 [qiaoqiao2521/hardware](https://github.com/qiaoqiao2521/hardware)，使用入口为[学习与实验导航](START_HERE.md)。

## 为什么会看到两个仓库

`embedded-learning` 是保留提交历史的归档仓库，根目录没有迁移 README；其主要内容已经在 [2026-09-15 的迁移提交](https://github.com/qiaoqiao2521/hardware/commit/211c6abc7cdd539181413d7c0339dfb67796503e)中放入 `hardware`。此前 hardware 首页侧重 Hardwire，嵌入式学习缺少统一入口，又遗漏了一小组旧资料，因此仅看仓库列表或首页容易以为两套仍各自维护。

现在硬件资产、课程、固件、综合实验、工具和学习记录都在 `hardware` 继续维护。旧仓保留归档历史，`hardwire/` 是这里的诊断模块。仓库保留现有默认分支 `master`，没有另外建立维护分支。

## 核对范围与结果

| 项目 | 固定基线 |
| --- | --- |
| 原始学习仓库 | [embedded-learning@ad4e5f1](https://github.com/qiaoqiao2521/embedded-learning/tree/ad4e5f15732bade382888a7711dd5685b73b409a)，`main`，已归档 |
| 本次整理前的 hardware | [hardware@fb6f788](https://github.com/qiaoqiao2521/hardware/tree/fb6f788750dec98ddf8da193d0364a423db7575c)，`master` |
| 文件范围 | 源提交完整 Git tree 中的全部 5,631 个 blob 文件，树未截断 |
| 整理前 | 5,619 个文件内容已在 hardware 存在；12 项需要补齐 |
| 整理后 | 5,631 个旧文件均有对应路径；5,617 个内容逐字节一致，14 份文本有注明的历史说明、脱敏或入口修正 |
| 本次新增旧资料 | 12 项，另增一份历史资料索引 |

核对先比较 Git blob SHA，再按下列目录映射逐文件检查目标路径。SHA 变化只允许下表列出的文本整理；两份二进制直接复核原始 blob。没有把“同内容在别处出现”作为缺失目标路径的替代证据。

5,617 个一致项的计数为：原先 5,619 项中有 4 份旧说明需要修正，加上本次补回的 2 份原始二进制。另 14 份为 10 份补迁文本和 4 份现有说明；这些变化不属于文件丢失。

## 工程和资料对应关系

| 原 embedded-learning 路径 | hardware 内当前位置 |
| --- | --- |
| `51_mcu/` | [mcu/51/51_mcu/](../mcu/51/51_mcu/) |
| `51单片机入门教程资料/` | [mcu/51/51单片机入门教程资料/](../mcu/51/51单片机入门教程资料/) |
| `at89s52_blink_sdcc/` | [mcu/51/at89s52_blink_sdcc/](../mcu/51/at89s52_blink_sdcc/) |
| `stm32/` | [mcu/stm32/](../mcu/stm32/) |
| `esp32_arm_controller/` | [mcu/esp32/esp32_arm_controller/](../mcu/esp32/esp32_arm_controller/) |
| `embedded-lab-monorepo/` | [lab/embedded-lab-monorepo/](../lab/embedded-lab-monorepo/) |
| `bin/` | [tools/bin/](../tools/bin/) |
| `flash.ps1`、`migrate_51.ps1`、`sync-to-wsl.ps1` | [tools/flashing/](../tools/flashing/) |
| `skills/` | [docs/skills/](skills/)，保留原导入位置 |
| 根目录接线、环境、源码汇总和工具链文档 | [docs/](./)，文件名保持对应关系 |
| `machinearm_search.json`、`notebook_creation.json`、`考试.pdsprj` | [docs/](./)，文件名保持对应关系 |

这里的根目录文档具体包括 `BOARD_WIRING_AND_FLASHING.md`、`Development-Environment-Report.md`、`PROJECT_SOURCE_DUMP.md`、`SOURCE_CODE_BUNDLE.md`、`TOOLCHAIN_SUMMARY.md`。

## 本次补齐的 12 项

| 原路径 | 本仓库入口 | 处理 |
| --- | --- | --- |
| `.embedded_env` | [历史环境配置](../tools/env/embedded_env.historical.sh) | 保留旧配置并增加来源说明，不自动加载 |
| `.gitignore` | [历史忽略规则](legacy/embedded-learning/gitignore.historical.txt) | 保留为普通文本，现行根规则不变 |
| `GEMINI_AGENTS_Explained.md` | [历史 Agent 说明](legacy/embedded-learning/GEMINI_AGENTS_Explained.historical.md) | 改历史文件名并标注来源 |
| `docs_backup/AGENTS.md` | [AGENTS 历史说明](legacy/embedded-learning/AGENTS.historical.md) | 改历史文件名，不作为现行指令 |
| `docs_backup/CLAUDE.md` | [CLAUDE 历史说明](legacy/embedded-learning/CLAUDE.historical.md) | 移除凭据，sudo 改交互式 |
| `docs_backup/IFLOW.MD` | [IFLOW 历史说明](legacy/embedded-learning/IFLOW.historical.md) | 移除凭据，sudo 改交互式 |
| `docs_backup/PROJECT_IDEAS.md` | [项目创意](legacy/embedded-learning/PROJECT_IDEAS.md) | 保留历史内容与来源 |
| `docs_backup/README.md` | [开发工作区历史说明](legacy/embedded-learning/README.historical.md) | 移除凭据，sudo 改交互式 |
| `docs_backup/WSL2_STLink_USBIPD_OpenOCD.md` | [WSL2 与 ST-Link 指南](legacy/embedded-learning/WSL2_STLink_USBIPD_OpenOCD.md) | 保留历史内容与来源 |
| `docs_backup/Windows_Survival_Guide.md` | [Windows 工具链手册](legacy/embedded-learning/Windows_Survival_Guide.md) | 保留历史内容与来源 |
| `docs_backup/seven_segment_diagram.png` | [七段数码管图](legacy/embedded-learning/seven_segment_diagram.png) | 原始字节和 blob SHA 一致 |
| `Project Backups/考试 [20260116, 13-50-59].pdsprj` | [Proteus 备份](proteus/backups/exam-20260116-135059.pdsprj) | 规范文件名，原始字节和 blob SHA 一致 |

[历史资料索引](legacy/embedded-learning/INDEX.md)提供这些材料的集中入口。历史资料中的机器路径、USB BUSID、串口号和版本属于当时环境，不能直接当作当前配置。

二进制复核结果：

| 文件 | 字节数 | 原始 Git blob SHA |
| --- | ---: | --- |
| 七段数码管 PNG | 370,311 | `6be7a7dcee9f72ea44eeb01118f051e887c2b2ae` |
| Proteus 备份 | 21,579 | `883de3b5050927f0194dc3bb0dc900b84b6a4bac` |

可以在仓库根目录复查：

```bash
git hash-object docs/legacy/embedded-learning/seven_segment_diagram.png
git hash-object docs/proteus/backups/exam-20260116-135059.pdsprj
```

## 同步修正的 4 份现有说明

| 文件 | 修正原因 |
| --- | --- |
| [实验台 README](../lab/embedded-lab-monorepo/README.md) | 主线统一为四条；软件检查仍为三条；已移除的第三方章节改上游来源入口；状态标为历史基线 |
| [MCS-51 README](../lab/embedded-lab-monorepo/mcs51/README.md) | 使用真实存在的三个示例、脚本和工作目录，纠正“尚待建立”与旧快照指引 |
| [HPAD 快速上手](../lab/embedded-lab-monorepo/rpi_hpad/QUICKSTART.md) | 旧独立绝对路径改为 hardware 内的相对工作目录 |
| [STM32 学习指引](../mcu/stm32/learning/学习指引.md) | 清理明文密码管道，改为交互 sudo，并修正迁入后的工程路径 |

## 验收边界

本次是资料归集与导航修复，未连接用户电脑或板卡，未运行烧录、设备探针或硬件测试。原工程和构建体系继续保留；历史通过记录没有被改称为本次通过。

没有重新导入实验台迁移说明中明确移除的第三方课程，也没有把仅在说明中提到、源仓库从未追踪的安装包或课件写成已经收集。密码不会随旧文档重新发布；现有 Git 历史未改写。
