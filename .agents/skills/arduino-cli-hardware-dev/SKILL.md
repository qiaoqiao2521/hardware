---
name: arduino-cli-hardware-dev
description: "Build, upload and monitor Arduino-compatible sketches with verified board/FQBN/port, project-local CLI configuration and Windows/WSL USB routing."
---

# Arduino CLI Hardware Development

Use the existing sketch and toolchain when present. Inspect CLI availability, board identity, FQBN, connection type and port before upload; discover facts from the workspace and `board list` before asking the user. A stale `COMx` or `/dev/ttyUSB*` name is not hardware identity after reconnect.

## Select the path

- Existing sketch: read the [compile/upload workflow](references/workflow.md); do not scaffold another Blink project.
- New Windows project: [init-project.ps1](scripts/init-project.ps1) creates a project-local `.arduino-cli` config and starter sketches. Use it only when a scaffold is needed; [config notes](references/config.md) explain local core/library/index isolation.
- WSL2 with only Windows `COMx` visible: prefer the installed Windows CLI for upload. Staying in WSL requires verified USB passthrough and a real Linux serial node; see [WSL notes](references/wsl2.md).
- Unknown board: `board listall` can help determine the FQBN; an `Unknown` label alone does not establish failure, but never flash a guessed board target.

Install only missing cores/libraries. Obtain third-party Boards Manager URLs from the selected board vendor; project-local `additional-urls` keeps builds reproducible. Git/ZIP library installs and core updates change dependencies, so preserve the intended version/source.

Compile the requested sketch/variant before uploading to the verified device. Upload requires the user's flashing/deployment scope; a compile-only request stops at its build artifact. Re-enumerate the device after reconnect before another upload. For serial monitoring, discover supported settings and use the firmware's baud rate.

Read [troubleshooting](references/troubleshooting.md) for the actual failure. Report compile output, upload result, observed serial/device behavior and unresolved wiring/timing separately. A successful upload is not proof that the physical circuit works.
