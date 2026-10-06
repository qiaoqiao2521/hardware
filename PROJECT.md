# PROJECT.md

## Why
个人硬件与单片机相关工程、历史采集资料此前散落在多个仓库。本项目将实体硬件代码、微控制器工程（MCU）、固件烧录工具与板卡诊断探针（原 hardwire + embedded-learning）统一收敛至硬件大本营——**`hardware`**，同时保留已售出设备（如树莓派5）的历史快照；当前在手状态以资产总表为准。

## User Intent
1. **纯粹面向实物硬件**：仅涵盖物理硬件与微控制器工程，与云端服务器运维（Ops-Vault）严格物理隔离。
2. **微控制器工程归集**：集中沉淀 51 单片机、STM32、ESP32 机械臂控制器及嵌入式实验台代码。
3. **硬件听诊器与只读体检**：提供快速只读体检诊断，事实与推断严格分离（Evidence-based Diagnostics）。
4. **板卡硬件基准**：建立长期可复现的板卡基线测试（CPU、内存、只读测速、温升），回答物理板卡选型定位。

## Non-goals
- 云端 VPS 舰队与在线生产服务运维（该职责 100% 归属于 `Ops-Vault`）。
- 侵入式客户端：探针绝不在目标开发板上常驻重型依赖。

## Directory Map
- `mcu/`: 单片机与控制器工程（51, STM32, ESP32）
- `lab/`: 嵌入式综合实验工作区（embedded-lab-monorepo）
- `tools/`: 烧录工具与跨端脚本（flash.ps1, migrate_51.ps1 等）
- `docs/`: 硬件接线、引脚定义、工具链指南与实战调优案例（`docs/cases/`）
- `hardwire/`: 硬件体检探针与只读诊断核心模块（core, targets, benchmarks）
- `snapshots/`: 板卡硬件体检快照数据

## 硬件资产与当前规划

- 长期资产入口：[我的硬件资产与实验平台](docs/HARDWARE_ASSETS.md)，逐台记录规格、接口、历史实测、故障、用途、性能比较与下一步；先列全，未知数量与身份保留待核实。
- 选型背景：[淘机与升级限制附录](docs/HARDWARE_SELECTION_CONTEXT.md)，保存新增历史商品和附件来源；在手状态、官方平台规格与实机验收分别记录。
- 当前状态：用户确认在手i5-3230M板U、RK3568B2路由板、国美云、HM170及三台J1900（监控、软路由、另列B68TK触摸机）。未来购买目标为V15B、Wyse5070、CM01和黑豹X2；树莓派已售出。
- 当前监控规划：[Frigate与HAOS计划](docs/FRIGATE_HAOS_PLAN.md)。保留J1900监控/软路由职责，用户已纠正ROCK为5C Lite / RK3582 / 8GB并告知上线；本次SSH已连通、OTP确认RK3582；当前系统8核与官方6核的差异及NPU/VPU兼容性仍待核实；HAOS宿主从合格且可用的在手x86中再选，已售Pi 5不参与。部署与准确率尚未现场验收。
- 本轮进度：[资产整理任务](plans/hardware-asset-records/progress.md)。本轮完成文档整理，不以历史快照证明当前设备状态。
