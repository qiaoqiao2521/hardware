---
name: hardware-realboard-proteus-debug-workflow
description: Diagnose an unfamiliar physical circuit or reconstruct it in Proteus using observed wiring, datasheets,
  and bounded hardware probes.
---

# Physical Board Diagnosis

Separate observed board facts from hypotheses. Identify chip markings, supply
voltage, interfaces, and relevant connections before choosing firmware or tests.
Resolve pinouts and electrical limits from the matching datasheet revision.

Start with the evidence already available. Ask for a specific photo, measurement,
or continuity check only when it resolves a concrete missing connection. Do not
make the user repeat facts the tools or existing documentation can establish.

Inspect power and ground before driving outputs. Never short outputs, drive an
unknown voltage domain, or use broad writes to discover what a board does.
For flashing or other destructive probes, identify the exact device and preserve
the existing firmware or data where possible; follow the task's authorization.

Use a minimal probe to answer one bounded question, such as polarity, bit order,
or input level. Keep the known-good image, pin map, command, and observed result.
Do not infer correctness from a successful upload or a simulation alone.

When Proteus reconstruction is requested, model verified wiring and clearly label
unverified sections. Simulation can test a hypothesis but does not establish the
physical board's connections. Skip simulation when the task does not need it.

For display and driver circuits, consult
[probe-notes.md](references/probe-notes.md) when planning the actual probe.

Finish with the evidence, unresolved connections, and the next discriminating
test. Preserve previous maps and working probes.
