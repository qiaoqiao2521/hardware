> 历史资料，补齐于 2026-11-26。来源：`embedded-learning@ad4e5f15732bade382888a7711dd5685b73b409a` 的 `docs_backup/Windows_Survival_Guide.md`。
>
> 保留旧工作区的配置、路径和当时记录，供学习与复用；这些记录不代表当前环境或实机已经验证。 当前入口见 [hardware](../../../README.md) 和 [本组索引](INDEX.md)。

# 🦅 Windows 嵌入式开发：生存与避坑实战手册 (Battle Manual)

本文档基于真实环境搭建中遇到的 10+ 个核心故障总结而成。这里没有废话，只有**报错代码**和**绝对不能做的事**。

---

## 🛑 第一章：绝对红线 (Critical Zone)

### 1.1 环境变量毁灭事件
**场景**：试图将 `C:\OpenOCD` 添加到 PATH。
**错误操作**：
```powershell
# ❌ [自杀式指令] 这会将 System PATH 和 User PATH 混合后写入 User，导致原来的 User 变量（如 nvm, cursor）全部丢失！
[Environment]::SetEnvironmentVariable("Path", $env:Path + ";C:\OpenOCD", "User")
```
**正确操作**：
```powershell
# ✅ [安全范式] 先读 User 域，再写回 User 域
$current = [Environment]::GetEnvironmentVariable("Path", "User")
if ($current -notlike "*OpenOCD*") {
    [Environment]::SetEnvironmentVariable("Path", $current + ";C:\OpenOCD", "User")
}
```
**补救措施**：
如果已经误删，重新手动添加以下关键路径：
- `E:\nvm`
- `C:\nvm4w\nodejs`
- `C:\Users\<User>\AppData\Roaming\npm`

### 1.2 Git 中文乱码崩溃
**场景**：Clone 包含中文文件名的仓库（如 `308模拟量控制`）。
**报错**：
- IDE 弹出 `invalid UTF-8 marshal message`。
- `git status` 报错 `invalid path '...'`.
**解决方案**：
1. **强制开启 Sparse-Checkout**：只拉取纯英文代码目录。
   ```bash
   git config core.sparseCheckout true
   echo "stm32/*" > .git/info/sparse-checkout
   git checkout -f HEAD
   ```
2. **强制终端编码**：
   ```powershell
   [Console]::OutputEncoding = [System.Text.Encoding]::UTF8
   $env:PYTHONIOENCODING = "utf-8"
   ```

---

## 🛠️ 第二章：工具链配置深坑

### 2.1 Arm GCC 路径空格地狱
**报错**：`CMake Error: CMAKE_C_COMPILER not found` 或 `The system cannot find the file specified`.
**原因**：默认安装路径 `C:\Program Files (x86)\Arm GNU Toolchain...` 包含**空格**和**括号**。
**CMake 必须加引号**：
```cmake
# ❌ CMake 会把空格解析为参数分隔符
set(CMAKE_C_COMPILER ${ARM_TOOLCHAIN}/bin/arm-none-eabi-gcc)

# ✅ 必须加引号包裹
set(CMAKE_C_COMPILER "${ARM_TOOLCHAIN}/bin/arm-none-eabi-gcc")
```

### 2.2 Ninja 找不到
**场景**：Winget 安装了 Ninja 但不生效。
**原因**：Winget 安装后需要**重启终端**才能刷新 PATH。
**替代方案**：使用 `uv` 秒装（强烈推荐）：
```bash
uv pip install --system ninja
# 安装后 ninja.exe 位于 Python Scripts 目录，立即可用
```

### 2.3 OpenOCD 脚本路径迷局
**报错**：`Can't find interface/stlink.cfg`
**原因**：不同发行版（xPack/官方）的 scripts 目录结构不同。
- 有时是 `install_dir/scripts`
- 有时是 `install_dir/share/openocd/scripts`
- 甚至 `install_dir/openocd/scripts`
**脚本自适应逻辑**：
```powershell
$ScriptDir = "$OpenOCDPath\openocd\scripts"
if (-not (Test-Path $ScriptDir)) {
    $ScriptDir = "$OpenOCDPath\share\openocd\scripts" # Fallback
}
```

### 2.4 ST-Link 驱动冲突
**现象**：OpenOCD 报错 `Error: libusb_open() failed with LIBUSB_ERROR_NOT_SUPPORTED`
**原因**：
- **CubeProgrammer** 用的是官方 ST 驱动。
- **OpenOCD** 需要 `WinUSB` 或 `libusbK` 驱动。
**解法**：使用 **Zadig** 软件，Options -> List All Devices -> 选中 ST-Link -> Replace Driver (WinUSB)。

---

## 🏗️ 第三章：CMake 构建实战技巧

### 3.1 缓存污染 (Cache Poisoning)
**现象**：修改了 Toolchain 路径或环境变量，但在报错日志里看到的还是旧路径。
**原因**：CMake 会生成 `build/CMakeCache.txt`，如果不删掉，它会一直记住旧的配置。
**必杀技**：每次环境变动，**彻底删除 build 目录**。
```powershell
Remove-Item build -Recurse -Force
```

### 3.2 缺少板卡文件 (Missing Board.cmake)
**现象**：`Please specify board: -DBOARD=...` 即使加了参数也报错。
**原因**：许多 Lesson 项目是独立的，缺少公共的 `cmake/boards` 文件夹。
**解法**：从其他完整项目（如 `vscode_template`）复制 `stm32f103c8t6.cmake` 到当前项目的 `cmake/boards/` 目录。

---

## ⚡ ALL-IN-ONE 自动化脚本 (`flash.ps1`)

将此脚本复制到任何 Lesson 目录下使用。它解决了上述所有路径、空格、查找问题。

```powershell
param([string]$App = "demo", [string]$Board = "stm32f103c8t6")

# 1. 动态注入环境变量 (解决 Path 没刷新的问题)
$ArmBin = "C:\Program Files (x86)\Arm GNU Toolchain arm-none-eabi\14.2 rel1\bin"
if (Test-Path $ArmBin) { $env:Path = "$ArmBin;" + $env:Path }

# 2. 清理旧构建 (解决缓存污染)
# Remove-Item build -Recurse -Force -ErrorAction SilentlyContinue

# 3. 智能查找 OpenOCD 脚本
$OpenOCDPath = "C:\OpenOCD"
$Scripts = "$OpenOCDPath\openocd\scripts"
if (-not (Test-Path $Scripts)) { $Scripts = "$OpenOCDPath\share\openocd\scripts" }

# 4. 构建 (强制指定 Ninja)
cmake -S . -B build -G Ninja -DCMAKE_TOOLCHAIN_FILE=cmake/toolchains/arm-gcc.cmake -DBOARD=$Board -DAPP=$App
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }

cmake --build build
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }

# 5. 自动查找 ELF 并烧录
$Elf = Get-ChildItem "build/*.elf" | Select -First 1
& "$OpenOCDPath\openocd.exe" -s "$Scripts" -f "boards/$Board/openocd.cfg" -c "program '$($Elf.FullName)' verify reset exit"
```

---

## 🔍 第四章：常用排错指令

| 症状 | 检查指令 |
| :--- | :--- |
| **找不到命令** | `Get-Command arm-none-eabi-gcc` |
| **Path 乱了** | `$env:Path -split ";"` |
| **查看 OpenOCD 版本** | `openocd --version` |
| **查看 USB 设备** | `usbipd list` (如果在 WSL), 设备管理器 (Windows) |
| **中文乱码** | `[Console]::OutputEncoding.EncodingName` |

---
*Last Updated: 2026-01-14 by Antigravity*
