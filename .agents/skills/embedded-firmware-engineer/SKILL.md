---
name: embedded-firmware-engineer
description: "Implement and debug bare-metal/RTOS firmware against a known board, SDK, memory map, timing budget and measured peripheral behavior."
---

# Embedded Firmware Engineering

Start from the actual MCU/board, schematic or pin map, SDK/build configuration, linker/map output and failing logs. Preserve board-specific HAL/LL, boot and peripheral choices unless the requested change requires otherwise. Arduino CLI setup/upload belongs to [Arduino hardware development](../arduino-cli-hardware-dev/SKILL.md); Wokwi simulation belongs to [Wokwi](../wokwi-simulator/SKILL.md).

## Engineering invariants

- Identify RAM/flash, stack/heap, interrupt, timing, power and electrical limits relevant to this change. Use datasheets/reference manuals and measured traces; do not transfer devkit assumptions to another board.
- Give peripheral operations bounded waits/timeouts and defined error behavior. Busy-wait loops are blocking, even if an old example called them non-blocking. Never wait indefinitely or call task-blocking APIs from ISR context.
- Keep ISR work minimal; use appropriate ISR-safe APIs and deferred work. Review interrupt priorities, shared-state synchronization, queue pressure, priority inversion and watchdog interactions.
- Prefer static allocation/pools in time-critical paths when bounded timing and fragmentation matter; justify any dynamic allocation from the actual runtime requirements instead of imposing a universal ban.
- Estimate stack needs and measure high-water marks under representative load. Check allocation/task-creation and driver return values; do not copy a pattern that silently ignores failure.
- Keep SDK/toolchain/library versions reproducible. Use devicetree/Kconfig on targets that require them, and follow the existing platform's supported interrupt/DMA/peripheral APIs.

## Match validation to the result

For bring-up, establish the build/flash/boot path and the exact device before changing application logic. For timing faults, use logic-analyzer/oscilloscope, trace or bounded timestamp evidence as appropriate. For OTA/boot changes, preserve the recovery image/path and verify rollback/cold-start behavior in the authorized test environment.

Read [platform patterns](references/platform-patterns.md) only for the relevant RTOS, platform or diagnostic mode. Treat example sizes, frequencies, duration targets and framework versions as examples to derive from the project, not universal acceptance thresholds.

Report source/build results, simulator evidence, flashed firmware identity and physical observations separately. Compilation, a serial banner or a working simulator does not prove electrical timing or safe actuator behavior.
