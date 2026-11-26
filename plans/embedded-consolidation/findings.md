# 归集核对发现

## 基线

- 日期：2026-11-26。
- `hardware`：`master`，基线 `fb6f788750dec98ddf8da193d0364a423db7575c`。
- `embedded-learning`：`main`，源提交 `ad4e5f15732bade382888a7711dd5685b73b409a`，已归档。
- 首次工程迁移：`211c6abc7cdd539181413d7c0339dfb67796503e`，2026-09-15。

## 证据

旧仓库完整 Git tree 未截断，共 5,631 个 blob 文件；其中 5,619 个在 `hardware` 中存在相同 blob。缺少的 12 项是旧环境配置、旧忽略规则、Agent 说明、Proteus 备份及 `docs_backup/` 下 8 份资料。

STM32、51 整理版、51 原课程、AT89S52、ESP32 和嵌入式实验台主体均已有相同内容。不能把“用户仍看见两个仓库”解释成工程完全没有迁移。

旧仓根没有 README 迁移说明，hardware 首页偏重 Hardwire，学习内容缺乏可点击的统一导航。实验台 README 还列出实际已经移除的上游章节路径；这些失效指引需纠正。

旧文档内发现历史明文凭据，补迁应保留技术资料并移除凭据及密码管道。原始含凭据文档不写入公开提交；历史说明不成为当前 Agent 指令。

## 结果入口

完整处理对应关系见 [归集记录](../../docs/REPOSITORY_CONSOLIDATION.md)，使用入口见 [学习导航](../../docs/START_HERE.md)。
