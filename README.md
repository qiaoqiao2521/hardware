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
└── docs/         # 硬件接线、引脚定义、芯片手册与调优案例 (docs/cases/)
```

---

## 🩺 板载大夫 (Hardwire) 快速上手

```bash
# 1. 本地整机体检
python3 -m hardwire collect --local

# 2. 远程无侵入探测在手目标（替换为实际用户与主机）
python3 -m hardwire collect --ssh user@device-host

# 3. 远程无侵入探测 Radxa ROCK 5C Lite
python3 -m hardwire collect --ssh rock-5c

# 4. 采集 GM800 标准 Hardwire 快照
python3 -m hardwire collect --ssh gm800 --save snapshots/gm800-hardwire.json

# 5. 对比两次硬件快照
python3 -m hardwire diff snapshots/rock-5c-before.json snapshots/rock-5c-after.json

# 6. 查看嵌入式多板卡选型对比横评
python3 -m hardwire matrix
```

---

## 板卡记录

- [ROCK 5C Lite / RK3582 / 8GB：官方系统、无线 SSH 与 MobileNet NPU 验收](docs/boards/rock-5c-lite.md)
- [国美云 GM800 / RK3566：无线重启恢复、双系统与固定 NPU 小模型验收](docs/boards/gm800.md)
  - `snapshots/gm800-522.json` 保存网络与 NPU 验收字段；`gm800-hardwire.json` 保存标准探针事实，两者用途不同。

- [康士达 K-B68TK-J1900 触摸工控机：硬件枚举、双 I211、6 路 COM 与无线扩展](docs/boards/j1900-b68tk.md)
  - 2026-10-04 实测，含产品目录链接、原始采集证据与尚未完成的实物测试。

---

## 📚 真实体检与调优案例 (Case Studies)

- [案例 001：Linux 宿主机端到端网络诊断、低风险可逆优化与前后复测](docs/cases/case-001-network-optimization.md)
  - 核心场景：Wi-Fi 节能抖动排查、真实链路 vs 本地 TUN/代理识别、上游 DNS 与 BBR 拥塞控制无缝优化。

## 硬件资产与项目规划

- [我的硬件资产与实验平台](docs/HARDWARE_ASSETS.md)：完整设备清单、历史规格、接口验收边界与待核实项。
- [淘机选型与升级限制附录](docs/HARDWARE_SELECTION_CONTEXT.md)：历史商品、HP主板/电源线索、CAN与旧NPU限制及官方规格差异。
- [Frigate与HAOS监控计划](docs/FRIGATE_HAOS_PLAN.md)：候选设备、兼容性条件与分阶段验收。
- [B68TK触摸J1900历史档案](docs/boards/j1900-b68tk.md)：2026-10-04检查结果与未验收接口。
