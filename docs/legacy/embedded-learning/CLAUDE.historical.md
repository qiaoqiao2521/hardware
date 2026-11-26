> 历史资料，补齐于 2026-11-26。来源：`embedded-learning@ad4e5f15732bade382888a7711dd5685b73b409a` 的 `docs_backup/CLAUDE.md`。
>
> 保留旧工作区的配置、路径和当时记录，供学习与复用；这些记录不代表当前环境或实机已经验证。 本页是历史说明，不作为当前 Agent 指令；当前约定见仓库根目录 `AGENTS.md` 与 `PROJECT.md`。 当前入口见 [hardware](../../../README.md) 和 [本组索引](INDEX.md)。
>
> 已移除原文中的明文凭据及向 sudo 管道传入密码的写法，示例改用交互式 sudo。

# STM32 嵌入式项目

基于 STM32F103C8T6 的学习项目。遵循现有代码风格。

## 项目结构

```
~/dev/embedded/
├── stm32/learning/     # 学习项目 (lesson_N-M/)
├── stm32/libraries/    # HAL, CMSIS
├── stm32/docs/         # 概念文档
├── plc/                # PLC 相关
└── docs/               # 硬件资料
```

## 环境激活

```bash
embenv    # 激活环境并 cd 到此目录
```

## 构建烧录

```bash
mkdir build && cd build
cmake ..
make -j$(nproc)

# 烧录 (WSL 需要 sudo)
sudo openocd -f interface/stlink.cfg -f target/stm32f1x.cfg \
    -c "program build/firmware.elf verify reset exit"
```

### sudo 交互式验证
- sudo 需要验证时，在终端交互式输入；文档和脚本不保存密码。

## 常见问题

- **OpenOCD 连接失败**：见 `WSL2_STLink_USBIPD_OpenOCD.md`
- **烧录后无反应**：检查 BOOT0 跳线（应接 GND）
- **串口无输出**：检查波特率和引脚配置

## 文档索引

| 文档 | 说明 |
|------|------|
| `README.md` | 项目总览 |
| `WSL2_STLink_USBIPD_OpenOCD.md` | ST-Link 调试配置 |
| `PROJECT_IDEAS.md` | 项目创意 |
| `stm32/learning/COURSE_BUILD_PLAN.md` | 课程计划 |
| `stm32/learning/课件/` | 课件（数据手册、参考手册） |
| `stm32/learning/进度打卡/` | 学习进度 |
| `stm32/docs/concepts/` | 概念文档（C语言、GPIO架构） |
| `GEMINI.md` | Gemini AI 辅助学习 |
| `IFLOW.md` | iFlow 知识管理 |

每个 `lesson_N-M/` 有独立的 `CLAUDE.md` 和 `IFLOW.md`
