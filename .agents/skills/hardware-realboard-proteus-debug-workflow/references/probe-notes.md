# Display and driver probe notes

Distinguish shift registers, decoders, latches, transistor arrays, and direct GPIO
before selecting pin behavior. A visually similar package can have a different
function and pinout.

For multiplexed displays, verify common-anode/common-cathode wiring, segment and
digit select polarity, inversion stages, current limiting, and refresh timing.
Establish safe current and duty cycle before a sustained all-on pattern.

Useful bounded probes include one segment or output channel at a time, a short
known digit sequence, and an input-only read to establish pull-up or pull-down
behavior. Do not substitute a firmware probe for an unknown electrical connection.

Record MCU pins, active levels, supply voltage, exact firmware artifact, flashing
tool version, and observed physical behavior. Retain a known-good binary when a
particular programmer is sensitive to file format; do not generalize a past HEX
workaround to unrelated programmers.
