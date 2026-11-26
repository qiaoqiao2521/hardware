# 嵌入式学习历史资料索引

这里补齐原 `embedded-learning` 中未迁入 `hardware` 的文档、配置参考、七段数码管图和 Proteus 备份。学习代码统一在本仓库的 [MCU 工程](../../../mcu/) 与 [嵌入式实验台](../../../lab/embedded-lab-monorepo/)；当前硬件资料从 [hardware 首页](../../../README.md) 进入。

来源固定为 `qiaoqiao2521/embedded-learning@ad4e5f15732bade382888a7711dd5685b73b409a`。整理日期为 2026-11-26，该远端仓库已于同日删除；其全部文件已在本仓库留存，提交历史另存于本地 `~/projects/embedded-learning-archive.bundle`。旧目录结构、安装路径、板卡连接与运行记录均属于历史上下文，实际使用前按当前环境核对，本次整理没有连接设备、烧录固件或重新验证硬件。

## 找资料

| 资料 | 本仓库入口 | 保留方式 |
| --- | --- | --- |
| 开发环境、构建、烧录与调试总览 | [开发工作区历史说明](README.historical.md) | 保留技术内容；移除明文凭据，sudo 改为交互式 |
| WSL2、ST-Link 与串口转发 | [WSL2 指南](WSL2_STLink_USBIPD_OpenOCD.md) | 历史 BUSID 与设备记录仅作案例 |
| Windows 工具链与常见故障 | [Windows 实战手册](Windows_Survival_Guide.md) | 保留原有范例与踩坑记录 |
| STM32 综合项目方向 | [项目创意](PROJECT_IDEAS.md) | 历史学习记录与候选项目 |
| 七段数码管示意 | [七段数码管图](seven_segment_diagram.png) | 原图按 Git blob SHA 验证 |
| Proteus 工程备份 | [2026-01-16 备份](../../proteus/backups/exam-20260116-135059.pdsprj) | 原始工程字节保留，文件名规范化 |
| ARM 工具链环境配置 | [历史环境脚本](../../../tools/env/embedded_env.historical.sh) | 保留配置参考，不自动加载 |
| 旧 Git 忽略规则 | [历史规则文本](gitignore.historical.txt) | 当前有效规则仍由根目录 `.gitignore` 管理 |

## 历史 Agent 说明

[AGENTS](AGENTS.historical.md)、[CLAUDE](CLAUDE.historical.md)、[IFLOW](IFLOW.historical.md) 和 [GEMINI 解释](GEMINI_AGENTS_Explained.historical.md) 保留用于追溯旧工作区；文件已经改为历史文件名，均不作为当前 Agent 指令。涉及系统密码的原文已经清理，构建与调试知识保留。

当前仓库的规则以根目录 [AGENTS.md](../../../AGENTS.md) 与 [PROJECT.md](../../../PROJECT.md) 为入口。本组没有重新导入实验台迁移记录中明确排除的第三方章节。

## 旧路径与新路径

| 原 `embedded-learning` 路径 | 新 `hardware` 路径 |
| --- | --- |
| `.embedded_env` | `tools/env/embedded_env.historical.sh` |
| `.gitignore` | `docs/legacy/embedded-learning/gitignore.historical.txt` |
| `GEMINI_AGENTS_Explained.md` | `docs/legacy/embedded-learning/GEMINI_AGENTS_Explained.historical.md` |
| `docs_backup/AGENTS.md` | `docs/legacy/embedded-learning/AGENTS.historical.md` |
| `docs_backup/CLAUDE.md` | `docs/legacy/embedded-learning/CLAUDE.historical.md` |
| `docs_backup/IFLOW.MD` | `docs/legacy/embedded-learning/IFLOW.historical.md` |
| `docs_backup/PROJECT_IDEAS.md` | `docs/legacy/embedded-learning/PROJECT_IDEAS.md` |
| `docs_backup/README.md` | `docs/legacy/embedded-learning/README.historical.md` |
| `docs_backup/WSL2_STLink_USBIPD_OpenOCD.md` | `docs/legacy/embedded-learning/WSL2_STLink_USBIPD_OpenOCD.md` |
| `docs_backup/Windows_Survival_Guide.md` | `docs/legacy/embedded-learning/Windows_Survival_Guide.md` |
| `docs_backup/seven_segment_diagram.png` | `docs/legacy/embedded-learning/seven_segment_diagram.png` |
| `Project Backups/考试 [20260116, 13-50-59].pdsprj` | `docs/proteus/backups/exam-20260116-135059.pdsprj` |

本次对照以 Git 跟踪的文件为范围，不把课程说明中提到、但旧仓库实际未包含的安装包或课件视为已经迁入。
