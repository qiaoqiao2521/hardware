# Firmware platform patterns

Use only the relevant platform section. These are review/implementation considerations, not a prebuilt driver library.

## FreeRTOS / ESP-IDF

Use queues, notifications, semaphores or event groups according to ownership and wakeup semantics. Check queue/task allocation and send/receive results; choose queue length, stack and priority from throughput, latency and measured headroom. Use `pdMS_TO_TICKS` where milliseconds are intended. Use ISR-safe variants inside interrupts and defer blocking work. Distinguish fatal ESP-IDF startup failures from recoverable peripheral errors; report the `esp_err_t` and meaningful context.

## STM32 HAL/LL

Prefer the existing project's abstraction. LL can help timing-critical paths but does not itself make code non-blocking. A loop polling TXE/BSY must have an appropriate bounded wait/error path and cannot be presented as a non-blocking transfer. Choose interrupt/DMA modes where that is the actual requirement. Confirm peripheral clocks, alternate functions, data width, DMA mapping/cache/alignment and board errata for the precise MCU.

## Nordic / Zephyr

Use the target's devicetree/Kconfig and SDK APIs. Verify advertising/GATT parameters and return codes instead of assuming a snippet starts a usable link. Memory retention, sleep wakeups and peripheral state depend on the specific SoC and board.

## PlatformIO and toolchains

Pin the chosen platform/libraries in the existing configuration for reproducible builds; do not copy the former ESP32 version or placeholder library as a universal template. Preserve selected framework, board, upload/monitor configuration and build flags.

## Timing, power, protocols and recovery

Choose the appropriate instrument: SWD/JTAG, SWV/ITM, SystemView/RTOS statistics, ESP-IDF core dumps or serial logging. Derive ISR latency and frame/scan budgets from requirements; a generic microsecond figure is not proof. For UART/SPI/I2C/CAN/BLE/network issues, validate wiring/electrical configuration plus timeout/error/recovery behavior.

For low power, verify the board's wake sources and retained state. For OTA/bootloaders, preserve image validation and rollback/cold-boot evidence. Record what was tested and on which hardware instead of treating a fixed stress-test duration or memory percentage as universal acceptance.
