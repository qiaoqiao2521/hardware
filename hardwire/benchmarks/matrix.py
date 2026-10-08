from typing import Dict, List, Any

# 典型嵌入式板卡与小主机硬件事实基线
HARDWARE_DATABASE = [
    {
        "id": "rpi5",
        "name": "Raspberry Pi 5（已售出，历史参考）",
        "soc": "Broadcom BCM2712",
        "arch": "ARM64 (v8.2-A)",
        "cores": "4 × Cortex-A76 @ 2.4GHz",
        "ram": "4GB / 8GB LPDDR4X-4267",
        "npu": "无 (可选 PCIe 外接微型算力卡)",
        "pcie": "PCIe 2.0 / 3.0 x1",
        "storage": "MicroSD + M.2 NVMe HAT",
        "idle_power": "~2.8W",
        "load_power": "~10.5W",
        "best_for": {
            "service": "⭐⭐⭐⭐☆ (社区生态最强，树莓派 OS 极其稳定)",
            "compile": "⭐⭐⭐☆☆ (4核 A76 够用，但大型 C++ 编译慢于 8核)",
            "inference": "⭐⭐☆☆☆ (纯 CPU 推理，跑轻量视觉尚可，大模型吃力)",
            "power_save": "⭐⭐⭐⭐☆ (低负载功耗控制出色，但无待机开关机制)"
        },
        "verdict": "用户已确认售出；规格与评分仅保留为历史参考，不参与当前节点分工。"
    },
    {
        "id": "rock5c",
        "name": "Radxa ROCK 5C Lite (RK3582)",
        "soc": "Rockchip RK3582",
        "arch": "ARM64 (v8.2-A)",
        "cores": "2 × A76 (最高2.4GHz) + 4 × A55 (最高1.8GHz)；无GPU",
        "ram": "用户确认8GB LPDDR4X；Linux实测7.7 GiB",
        "npu": "标称5 TOPS @ INT8；MobileNet三核分别通过",
        "pcie": "FPC PCIe 2.1 x1；扩展需转接板",
        "storage": "MicroSD / eMMC；FPC扩展需转接板",
        "idle_power": "待实测",
        "load_power": "待实测",
        "best_for": {
            "service": "无线/SSH已验收；持续运行待验",
            "compile": "待实测 (官方Debian 12当前6核在线)",
            "inference": "MobileNet通过；目标YOLO/VPU与持续负载待验",
            "power_save": "待实测 (功耗与温升)"
        },
        "verdict": "OTP确认RK3582；官方系统当前6核。旧Armbian的8核为历史差异；矩阵API数值差异与Frigate另验。"
    },
    {
        "id": "gm800",
        "name": "国美云 GM800 (RK3566)",
        "soc": "Rockchip RK3566",
        "arch": "ARM64",
        "cores": "实机4核",
        "ram": "Linux实测约3.8 GiB；标称容量另核",
        "npu": "固定CNN模型30次输出比较通过；非TOPS基准",
        "pcie": "接口与扩展待实机核对",
        "storage": "内部userdata运行Ubuntu；保留Android双系统",
        "idle_power": "待实测",
        "load_power": "待实测",
        "best_for": {
            "service": "拔网线重启后无线/SSH恢复；持续运行待验",
            "compile": "待实测 (4核；Ubuntu 22.04.3)",
            "inference": "固定小模型通过；大型模型与目标YOLO待验",
            "power_save": "待实测 (功耗与温升)"
        },
        "verdict": "RK3566；Runtime2.3.2/driver0.4.2。开机须选Ubuntu；独立冷启动、持续负载与其他外设另验。"
    },
    {
        "id": "j1900",
        "name": "Intel J1900 工控小主机",
        "soc": "Intel Celeron J1900",
        "arch": "x86_64 (Silvermont)",
        "cores": "4 × 4线程 @ 2.0~2.4GHz",
        "ram": "DDR3L 1333 (常见 4G/8G)",
        "npu": "无",
        "pcie": "PCIe 2.0 (多网口板卡扩展)",
        "storage": "SATA / mSATA 盘",
        "idle_power": "~7.0W",
        "load_power": "~15.0W",
        "best_for": {
            "service": "⭐⭐⭐⭐☆ (经典 x86 软路由、OpenWrt/PVE 双软路由老将)",
            "compile": "⭐⭐☆☆☆ (单核性能老旧，缺失 AVX 指令集，现代编译慢)",
            "inference": "⭐☆☆☆☆ (不支持现代神经网络指令，推理慢)",
            "power_save": "⭐⭐⭐☆☆ (低发热无风扇，但功耗相比 ARM 架构偏高)"
        },
        "verdict": "适合作为全千兆物理软路由、旁路网关或简单 Samba 本地存储机。"
    },
    {
        "id": "laptop_linux",
        "name": "x86 笔记本 (如东芝/蛟龙)",
        "soc": "标压/低压 x86 处理器",
        "arch": "x86_64 (带 AVX2 / AVX-512)",
        "cores": "8~16 线程",
        "ram": "16G ~ 32G 高速内存",
        "npu": "可选独立显卡 CUDA",
        "pcie": "PCIe 3.0 / 4.0 高速通道",
        "storage": "高速 NVMe SSD",
        "idle_power": "~10W ~ 20W",
        "load_power": "~45W ~ 100W",
        "best_for": {
            "service": "⭐⭐⭐☆☆ (自带电池相当于自带 UPS，不怕偶发断电)",
            "compile": "⭐⭐⭐⭐⭐ (x86 高主频 + 大内存，编译速度呈压倒性优势)",
            "inference": "⭐⭐⭐⭐⭐ (搭配独显 CUDA，可跑大模型与深度学习微调)",
            "power_save": "⭐⭐☆☆☆ (不适合 24 小时低成本无看管挂机)"
        },
        "verdict": "重型研发工作站：负责编译出包、模型蒸馏调试，不适合当常开小网关。"
    }
]

class BoardMatrix:
    """多板卡选型与硬件横向定位对比看板"""

    @classmethod
    def render_markdown(cls) -> str:
        md = []
        md.append("# 嵌入式板卡与小主机横向对比矩阵 (Board Matrix)\n")
        md.append("重点解决：**在手头这几块板子中，到底哪个做服务、哪个做编译、哪个做推理、哪个最省电？**\n")
        md.append("2026-10-08同步实机验收：ROCK已由OTP确认RK3582，官方Debian 12当前6核在线；旧Armbian的8核与旧基准保留为历史。GM800无线重启SSH与固定NPU小模型通过。Pi 5已售出。规格依据[Radxa官方Product Brief](https://dl.radxa.com/rock5/5c/docs/hw/v1100/radxa_rock5c_product_brief_Revision_1.2_g02f49da.pdf)，验收范围见[ROCK档案](docs/boards/rock-5c-lite.md)、[GM800档案](docs/boards/gm800.md)；当前资产状态见[资产总表](docs/HARDWARE_ASSETS.md)。\n")
        
        # 表格一：核心硬件规格
        md.append("### 1. 硬件参数与芯片底色")
        md.append("| 板卡名称 | SoC 架构 | 核心规格 | 内存配置 | NPU 算力 | 存储接口 | 待机/满载功耗 |")
        md.append("|---|---|---|---|---|---|---|")
        for b in HARDWARE_DATABASE:
            md.append(f"| **{b['name']}** | {b['arch']} | {b['cores']} | {b['ram']} | {b['npu']} | {b['storage']} | {b['idle_power']} / {b['load_power']} |")

        md.append("\n### 2. 真实场景适用性评分 (满分五星)")
        md.append("| 板卡名称 | 长期低功耗服务机 | 软硬件代码编译 | 边缘模型推理 | 节能省电/温控 | 核心定性总结 |")
        md.append("|---|---|---|---|---|---|")
        for b in HARDWARE_DATABASE:
            md.append(f"| **{b['name']}** | {b['best_for']['service']} | {b['best_for']['compile']} | {b['best_for']['inference']} | {b['best_for']['power_save']} | {b['verdict']} |")

        md.append("\n### 3. 选型决策指南 (Answer to Practical Questions)\n")
        md.append("1. **哪个适合作为长期服务机？**")
        md.append("   - **在手ARM候选：ROCK 5C Lite与GM800**。网络与SSH已验收；长期服务、断电恢复和目标应用仍需验证。Pi 5已售出，不分配当前职责。")
        md.append("   - **次选：东芝/老款笔记本**。如果部署必须保证断电不崩，老笔记本自带的锂电池天然就是免维护 UPS。\n")

        md.append("2. **哪个适合作为编译机？**")
        md.append("   - **ARM候选：Radxa ROCK 5C Lite**。标称2大核 + 4小核；实际编译速度须用相同工程比较。")
        md.append("   - **全平台性能首选：x86 主力笔记本**。主频高，NVMe 写入快，内存大，适合重型大包构建。\n")

        md.append("3. **哪个适合模型推理？**")
        md.append("   - **ROCK 5C Lite**：官方MobileNet V1在AUTO及core0/core1/core2输出一致，单次约3.08–3.21ms；目标YOLO、解码与持续负载另验。")
        md.append("   - **GM800**：固定CNN模型30次输出比较通过，最大误差0.000141769648、平均0.215ms；模型不同，不能据此与ROCK比较速度或TOPS。")
        md.append("   - **通用大模型推理：带 CUDA 独显的笔记本**。\n")

        md.append("4. **哪个最省电？**")
        md.append("   - **ROCK 5C Lite与GM800功耗待测**。用同一供电测量待机与目标负载功耗，再比较长期运行成本。\n")

        md.append("### 4. 个人全量设备实测天梯榜与 N100 当量矩阵")
        md.append("| 设备资产 | 核心配置与架构 | 单核性能 | 全核多进程 | 内存拷贝带宽 | N100 综合当量 | 最适合的角色与定位 |")
        md.append("|---|---|---|---|---|---|---|")
        md.append("| **蛟龙 15K 笔记本** | Ryzen 7 7435H (16T, 45W+) | 0.172s | 0.454s | 1863 MB/s | **~3.8 个 N100** | 桌面性能怪物：本地大模型蒸馏、重型大工程构建 |")
        md.append("| **legacy-ai-server** | Xeon Platinum 8336C (2T) | 0.371s | 0.460s | 1303 MB/s | **~1.2 个 N100** | 单核 IPC 极高：适合跑高主频计算或轻量 API |")
        md.append("| **树莓派 5 (Pi 5，已售出)** | BCM2712 A76 (4T @ 2.4G) | 0.427s（历史） | 0.484s（历史） | 3611 MB/s（历史） | **~1.0 个 N100（历史）** | 历史性能参考，不计入当前可用资产 |")
        md.append("| **qiaobird (EPYC)** | AMD EPYC-Rome (4T) | 0.490s | 0.632s | 1206 MB/s | **~1.1 个 N100** | 稳健云端主力：多任务数据库、常驻应用、云端开发 |")
        md.append("| **东芝 R73 笔记本** | i5-7200U (4T @ 2.5G) | 0.392s | 0.905s | 1492 MB/s | **~0.85 个 N100** | 自带 UPS 免维护：不怕断电，离线工控与数据库冷备 |")
        md.append("| **ROCK 5C历史记录（型号未实证）** | 旧记录称8线程；不能代表Lite标称6核 | 0.426s（历史） | 1.004s（历史） | 7509 MB/s（历史） | 待核实 | 原始测试、时间与型号绑定缺失；不据此评价Lite |")
        md.append("| **racknerd-436b0c0** | Xeon E5-2680 v2 (6T @ 2.8G) | 0.519s | 0.809s | 330 MB/s | **~1.3 个 N100** | 闷声发大财：母机 0 抢占，适合内网 CI/CD 构建与批处理 |")
        md.append("| **racknerd-bf2025** | Xeon Gold 6152 (6T @ 2.1G) | 0.681s | 0.886s | 558 MB/s | **~1.1 个 N100** | 指令集最全 (支持 AVX-512)：建议走 Tailscale 避免丢包 |")
        md.append("| **greenrise (Contabo)** | Intel Broadwell (2T @ 2.0G) | 0.735s | 0.921s | 355 MB/s | **~0.6 个 N100** | 性价比存储机：空间充足，适合长效数据备份与同步 |")
        md.append("| **meiren (LAX BGP)** | Xeon E5-2690 v3 (2T) | 0.980s | 0.955s | 668 MB/s | **~0.5 个 N100** | 线路机：美西优质 BGP，专职外网反向代理与流量转发 |")
        md.append("| **moonrise** | Xeon E5-2683 v4 (3T) | 1.215s | 1.227s | 767 MB/s | **~0.5 个 N100** | 异地容灾备用机 |")
        md.append("| **colocrossing-ny** | Xeon E5-2683 v4 (3T) | 1.029s | 1.438s | 786 MB/s | **~0.5 个 N100** | 美东节点，轻量 Worker 备用 |")

        return "\n".join(md)
