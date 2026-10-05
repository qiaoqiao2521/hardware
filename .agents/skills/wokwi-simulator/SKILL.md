---
name: wokwi-simulator
description: "Create or validate Wokwi diagrams and automation scenarios, and diagnose firmware behavior within the simulator’s supported board/part model."
---

# Wokwi Simulator

Use for Wokwi `diagram.json`, `wokwi.toml`, scenario YAML, simulated boards/parts and custom chips. Preserve existing part IDs, firmware build paths and connections unless the task changes them. Simulation is not electrical or physical-hardware acceptance.

## Select the reference by task

These local references were extracted from documentation and contain source links. Search the named heading before reading a long file; flattened examples may need reconstruction and validation rather than direct pasting.

| Task | Reference / heading |
|---|---|
| New project, supported hardware, VS Code/CI setup | [Getting started](references/getting_started.md) |
| Diagram structure, connections, custom-chip definition, CLI | [Diagram format](references/diagram_format.md): `diagram.json File Format`, `Wokwi CLI Usage`, `Custom Chip Definition` |
| Exact part pins/attributes | [Parts](references/parts.md): find the selected part type |
| Board/runtime specifics (ESP32, Pico, Python) | [Boards](references/boards.md), and matching part entry |
| Scenario YAML / serial assertions / screenshot comparisons | [Other](references/other.md): `Wokwi Automation Scenarios` |
| Build artifact path and simulation settings | [Other](references/other.md): `Configuring Your Project (wokwi.toml)` |
| Logic analyzer, serial monitor or custom-chip WASM | [Guides](references/guides.md) |
| Custom-chip GPIO/I2C/SPI/UART/time APIs | [Other](references/other.md): select the required API heading |

## Validation decisions

- Resolve exact board/part names, pins and attributes from the selected reference; similar physical names do not prove a simulator part exposes the same pin IDs.
- Check diagram IDs are unique and all connection endpoints resolve. Respect internal contacts (for example, the two sides of the same pushbutton contact are already connected).
- Match firmware target/build output and the simulation configuration. Do not initialize over an existing diagram merely to use a canned example.
- For scenarios, use a meaningful observed stimulus/result: control input, expected serial output, timeout or display comparison. Keep screenshots/baselines tied to the intended part and test; rendering a blank canvas is not success.
- Use an available, authorized simulator/CLI path. A missing account/license/tool is a reported dependency, not permission to provision it or claim a run.

Report static diagram/config validation, actual simulator execution and any remaining physical-hardware work separately. Recheck official documentation for version-sensitive APIs when needed; without that check, identify the local-reference limitation.
