# 🛠️ Hardware: 实体硬件与嵌入式大本营 (MCU, Embedded Lab & Hardwire)

> 纯粹面向实物硬件、微控制器工程（51 / STM32 / ESP32）与板载大夫探针（Hardwire）的唯一收敛大本营。

---

## 🏛️ 边界与架构定位 (Architecture Boundaries)

- **本仓库职责（100% 聚焦实物硬件与微控制器）**：
  - **微控制器工程（MCU）**：51 单片机、STM32、ESP32 机械臂控制器及嵌入式外设代码（`mcu/`）。
  - **嵌入式实验工作区**：嵌入式综合工程 Monorepo（`lab/embedded-lab-monorepo`）。
  - **硬件大夫诊断探针（Hardwire）**：零侵入、证据驱动的单板计算机（树莓派 5、ROCK 5C、J1900、东芝笔记本）硬件体检、状态快照与版本 Diff（`hardwire/`）。
  - **硬件烧录工具链**：烧录脚本、跨端工具与引脚图（`tools/`、`docs/`）。
- **非本仓库职责（严格物理隔离）**：
  - 云端 VPS 舰队运维、公网域名解析、监控中心（该职责 100% 归属于 `Ops-Vault`）。
  - 实物板卡作为边缘服务器的角色监控，已集成在全局 `fleet-status` 中统一管理。

---

## 📂 仓库结构速览

```text
hardware/
├── mcu/          # 单片机与控制器工程 (51, STM32, ESP32)
├── lab/          # 嵌入式综合实验 Monorepo
├── hardwire/     # 硬件大夫核心探针与基线测试 (core, targets, benchmarks)
├── tools/        # 固件烧录、迁移与跨端工具链
├── snapshots/    # 实体板卡硬件体检快照数据
├── tests/        # 单元与集成测试
└── docs/         # 硬件接线、引脚定义与芯片手册
```

---

## 🩺 板载大夫 (Hardwire) 快速上手

```bash
# 1. 本地整机体检
python3 -m hardwire collect --local

# 2. 远程无侵入探测树莓派 5
python3 -m hardwire collect --ssh muqiaopi

# 3. 远程无侵入探测 Radxa ROCK 5C
python3 -m hardwire collect --ssh rock-5c

# 4. 对比两次硬件快照
python3 -m hardwire diff snapshots/rock-5c-before.json snapshots/rock-5c-after.json

# 5. 查看嵌入式多板卡选型对比横评
python3 -m hardwire matrix
```
