# Hardware：硬件与嵌入式学习

硬件资产、51 / STM32 / ESP32 学习工程、嵌入式实验台和 Hardwire 诊断工具，统一在这个仓库维护。

`embedded-learning` 原是旧的学习仓库。主要工程已于 2026-09-15 迁入本仓库，2026-11-26 进一步核对旧文件、补齐遗漏资料并整理入口，随后删除该旧仓库（文件与历史留存见[归集核对记录](docs/REPOSITORY_CONSOLIDATION.md)）。以后从这里查资料、做实验、更新记录即可；`hardwire/` 是本仓库里的诊断模块。

## 从这里开始

| 你要做什么 | 入口 |
| --- | --- |
| 看全部嵌入式学习路线、选第一个实验 | [学习与实验导航](docs/START_HERE.md) |
| 查已有设备、配件和用途 | [硬件资产总表](docs/HARDWARE_ASSETS.md) |
| 学 51 单片机，找整理版、原课程和 AT89S52 工程 | [51 工程目录](mcu/51/) |
| 学 STM32，找课程、模板和综合项目 | [STM32 工程目录](mcu/stm32/) |
| 找 ESP32 机械臂控制器 | [ESP32 工程](mcu/esp32/esp32_arm_controller/README.md) |
| 做 STM32 / 51 / HPAD / WM8960 综合实验 | [嵌入式实验台](lab/embedded-lab-monorepo/README.md) |
| 查接线和烧录 | [接线与烧录记录](docs/BOARD_WIRING_AND_FLASHING.md) |
| 找旧开发笔记、接线图和迁移对应关系 | [旧资料索引](docs/legacy/embedded-learning/INDEX.md) · [归集核对记录](docs/REPOSITORY_CONSOLIDATION.md) |

设备当前归属以资产总表为准；旧学习记录里的工具版本、串口号和历史验收结果不代表本次已复测。

---

## 内容范围

- **本仓库职责（100% 聚焦实物硬件与微控制器）**：
  - **微控制器工程（MCU）**：51 单片机、STM32、ESP32 机械臂控制器及嵌入式外设代码（`mcu/`）。
  - **嵌入式实验工作区**：嵌入式综合工程 Monorepo（`lab/embedded-lab-monorepo`）。
  - **硬件大夫诊断探针（Hardwire）**：零侵入、证据驱动的单板计算机（树莓派 5、ROCK 5C、J1900、东芝笔记本）硬件体检、状态快照与版本 Diff（`hardwire/`）。
  - **硬件烧录工具链**：烧录脚本、跨端工具与引脚图（`tools/`、`docs/`）。
- **非本仓库职责（严格物理隔离）**：
  - 云端 VPS 舰队运维、公网域名解析、监控中心（该职责 100% 归属于 `Ops-Vault`）。
  - 实物板卡作为边缘服务器的角色监控，已集成在全局 `fleet-status` 中统一管理。

---

## 仓库结构速览

| 目录 | 内容 |
| --- | --- |
| [mcu/](mcu/) | 51、STM32、ESP32 单片机与控制器工程 |
| [lab/](lab/) | 嵌入式综合实验台，保留各子项目的构建与验证入口 |
| [hardwire/](hardwire/) | 硬件探针、只读诊断与基线测试 |
| [tools/](tools/) | 烧录、环境与跨端工具 |
| [snapshots/](snapshots/) | 历史硬件体检快照 |
| [tests/](tests/) | 诊断工具的自动检查 |
| [docs/](docs/) | 资产、学习导航、接线、板卡档案、案例与旧资料 |

---

## Hardwire 诊断工具快速上手

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

- [NSY-G16-Plus：完整 Armbian、200 GiB 根文件、NPU 当前不可用与温度差异记录](docs/boards/nsy-g16-plus.md)

- [ROCK 5C Lite / RK3582 / 8GB：官方系统、无线 SSH 与 MobileNet NPU 验收](docs/boards/rock-5c-lite.md)
- [国美云 GM800 / RK3566：无线重启恢复、双系统与固定 NPU 小模型验收](docs/boards/gm800.md)
  - `snapshots/gm800-522.json` 保存网络与 NPU 验收字段；`gm800-hardwire.json` 保存标准探针事实，两者用途不同。
- [国美云 GM800 第二台 GM260200534：安卓11双系统、10秒默认Ubuntu与NPU验收](docs/boards/gm800-534.md)

- [康士达 K-B68TK-J1900 触摸工控机：硬件枚举、双 I211、6 路 COM 与无线扩展](docs/boards/j1900-b68tk.md)
  - 2026-10-04 实测，含产品目录链接、原始采集证据与尚未完成的实物测试。

---

## 真实体检与调优案例

- [案例 001：Linux 宿主机端到端网络诊断、低风险可逆优化与前后复测](docs/cases/case-001-network-optimization.md)
  - 核心场景：Wi-Fi 节能抖动排查、真实链路 vs 本地 TUN/代理识别、上游 DNS 与 BBR 拥塞控制无缝优化。

## 硬件资产与项目规划

- [我的硬件资产与实验平台](docs/HARDWARE_ASSETS.md)：2026-11-15回顾更新；包含主机/板卡、显卡电源、机器人、监控、光通信、车载与存储附件，以及已售出、待归并和未购买边界。
- [淘机选型与升级限制附录](docs/HARDWARE_SELECTION_CONTEXT.md)：历史商品、HP主板/电源线索、CAN与旧NPU限制及官方规格差异。
- [Frigate与HAOS监控计划](docs/FRIGATE_HAOS_PLAN.md)：候选设备、兼容性条件与分阶段验收。
- [B68TK触摸J1900历史档案](docs/boards/j1900-b68tk.md)：2026-10-04检查结果与未验收接口。
