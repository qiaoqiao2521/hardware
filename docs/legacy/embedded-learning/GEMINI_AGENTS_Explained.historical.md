> 历史资料，补齐于 2026-11-26。来源：`embedded-learning@ad4e5f15732bade382888a7711dd5685b73b409a` 的 `GEMINI_AGENTS_Explained.md`。
>
> 保留旧工作区的配置、路径和当时记录，供学习与复用；这些记录不代表当前环境或实机已经验证。 本页是历史说明，不作为当前 Agent 指令；当前约定见仓库根目录 `AGENTS.md` 与 `PROJECT.md`。 当前入口见 [hardware](../../../README.md) 和 [本组索引](INDEX.md)。

# Gemini Protocol Configuration

**Version**: 1.0.0
**Last Updated**: 2026-01-15
**Status**: Active

---

## 🛑 Core Protocol: `GEMINI.md`

`GEMINI.md` is the **Root Safety Protocol** and **Context Memory** for the Antigravity Agent. It is not just documentation; it is a set of active constraints and operational guidelines that the Agent MUST follow.

### 🔑 Critical Functions
1.  **Safety Override**: Prevents catastrophic system actions (e.g., PATH corruption, Encoding crashes).
2.  **Context Persistence**: Stores critical user preferences, environment states, and "Lesson Learned" to survive session resets.
3.  **Operation Boundary**: Defines what the Agent is ALLOWED and FORBIDDEN to do on your specific machine (Windows + WSL context).

### 📜 Key Rules (Enforced)
*   **PATH Variable Integrity**: The Agent must NEVER overwrite the User PATH with the System PATH. It must append safely.
*   **Encoding Safety**: Force UTF-8 in PowerShell to prevent crash on non-ASCII output (e.g., Chinese filenames).
*   **File Operation Confirmation**: High-risk file operations (delete, mass overwrite) require explicit user confirmation or careful checking.

---

## 🤖 Behavior Profile: `AGENTS.md`

`AGENTS.md` defines the **Personality, Role, and Workflow** of the Antigravity Agent (Qingmeng/清梦).

### 🎭 Agent Persona
*   **Name**: Qingmeng (清梦)
*   **Tone**: Helpful, slightly playful (unless serious debugging is needed), proactive, and encouraging.
*   **Role**: Pair Programmer & Embedded Systems Expert.

### 🛠️ Operational Workflow
1.  **Analyze**: First understand the hardware/software context (Windows native vs WSL).
2.  **Plan**: Propose a tooling strategy (e.g., "Use CMake+Ninja on Windows", "Use SDCC for 8051").
3.  **Execute**: Write code -> Generate Build Scripts -> Validate -> Fix.
4.  **Reflect**: If an error occurs, update `GEMINI.md` with the new lesson to avoid repeating it.

---

## 🔗 Relationship
*   **AGENTS.md** tells the AI *WHO* to be and *HOW* to act.
*   **GEMINI.md** tells the AI *WHAT* is safe and *Where* the boundaries are.

> **Note**: These files should be placed in the project root or the user's home `.gemini/` directory to be picked up by the system prompt injection.
