# Wokwi-Simulator - Getting Started

**Pages:** 4

---

## Wokwi for VS Code

**URL:** https://docs.wokwi.com/vscode/getting-started

**Contents:**
- Wokwi for VS Code
- Installation​
- Example Projects​
  - Platform IO Examples​
  - ESP-IDF Examples​
  - STM32 Examples​
  - ESP32 + Rust​
  - MicroPython​
  - Sming Framework​
  - Arduino Extension Examples​

Wokwi for Visual Studio Code provides a simulation solution for embedded and IoT system engineers. The extension integrates with your existing development environment, allowing you to simulate your projects directly from your code editor.

You can use Wokwi for VS Code with Zephyr Project, PlatformIO, ESP-IDF, Pi Pico SDK, NuttX, Rust, Arduino CLI, MicroPython, and other embedded development frameworks and toolchains.

First, install the Wokwi for VS Code extension. Then, press F1 and select "Wokwi: Request a new License". VS Code will ask you confirm opening the Wokwi website in your browser. Confirm by clicking "Open".

Then click on the button that says "GET YOUR LICENSE". You may be asked to sign in to your Wokwi account. If you don't have an account, you can create one for free.

The browser will ask for a confirmation to send the license to VS Code. Confirm (you may have to confirm twice, once in the browser, and once in VS Code). You'll see a message in VS Code that says "License activated for [your name]". Congratulations!

To configure Wokwi for your own project, see the Project Configuration page.

If you just want to get started quickly and play around with Wokwi for VS Code, here are some example projects, preconfigured with diagram.json and wokwi.toml files.

Before simulating any of the following projects, you need to compile the code and generate the firmware / ELF file. Consult the project's README file for instructions on how to compile the code.

Check out the MicroPython on Wokwi for VS Code repo for examples and instructions.

---

## Getting Started with the Wokwi Custom Chips C API

**URL:** https://docs.wokwi.com/chips-api/getting-started

**Contents:**
- Getting Started with the Wokwi Custom Chips C API
- Introduction​
- Tutorials​
- Getting started​
  - Debugging your custom chip​
- Chips API reference 📖​
- Chip examples​
  - Basics​
  - Communication​
  - Displays​

The Chips API is currently in beta. Please share your experiments and provide feedback in the #custom-chips channel on the Discord chat.

The Custom Chips API allows you to create new simulation models and extend the functionality of Wokwi. You can create new sensors, displays, memories, testing instruments, and even simulate your own custom hardware.

Custom Chips are usually written in C, but you can use any language that compiles to WebAssembly (e.g. Rust, AssemblyScript, etc.). There is also an experimental support for writing custom chips in Verilog.

Open any Wokwi project (or create a new one) and click on the blue "+" button in the diagram editor. Select "Custom Chip" from the list of options.

You'll see a dialog where you can enter the chip name, as well as the language you wish to use. We recommend using C for now. After typing a name for your chip, click on the "Create Chip" button.

This will add a copy of the chip to your diagram and create two files in your project:

The JSON file file defines a minimal set of pins ("VCC", "GND", "IN", "OUT"). Change the pin names and add more pins as needed.

The C file contains a minimal chip implementation. Add your code to the chip_init() function. This function is called for every instance of the chip in the diagram. You can use it to initialize the chip state, configure timers, and set up pin watches.

The example code also includes a chip_state_t struct, where you can store any state that your chip needs. You can use the user_data field of the i2c_config_t, timer_config_t, etc. to store a pointer to this struct.

You can print debugging messages using the standard C printf() function. Make sure to also #include <stdio.h> in your program. The debug messages will appear in a new "Chips Console" tab below the diagram view:

In addition, you can use the Wokwi Logic Analyzer to debug the communication with your custom chip.

Make sure to include a newline ("\n") at the end of your printf() messages. The simulator shows the messages only when it reaches a newline character.

---

## Supported Hardware

**URL:** https://docs.wokwi.com/getting-started/supported-hardware

**Contents:**
- Supported Hardware
- Microcontrollers​
- Sensors​
- Input devices​
- LEDs​
- Display​
- Motors​
- Communications​
- Logic​
- Other parts​

Wokwi simulates a wide variety of hardware components, including microcontrollers, sensors, displays, and more. It supports the following architectures: ARM, AVR, RISC-V, and Xtensa.

The following microcontrollers are currently supported:

* ESP32-H2 support is in beta, ESP32-P4 support is in alpha.

---

## Wokwi for CI and GitHub Actions

**URL:** https://docs.wokwi.com/wokwi-ci/getting-started

**Contents:**
- Wokwi for CI and GitHub Actions
- Wokwi in the Loop (WITL)​
- CI Architecture​
- Simulation Time and Limits​
  - Limiting Individual Test Time​
- AI Agent Integration​
- Next Steps​

Wokwi provides a robust simulation solution for automated testing of your embedded firmware on CI systems like GitHub Actions, GitLab CI, and others. You can use Wokwi to run your tests on every commit, and get instant feedback on your code changes.

Behind the scenes, Wokwi CI uses the same simulation engine that powers the Wokwi Simulator. The simulation runs in the cloud, and you can stream the serial output back to your CI system to verify that your firmware behaves as expected.

Wokwi in the Loop (WITL) is a testing methodology that combines the best of both worlds: the speed and convenience of unit testing with the realism of hardware testing. With WITL, you can run your firmware on a simulated hardware platform, interact with the firmware using virtual buttons and sensors, and verify the firmware's behavior by checking the serial output.

For basic testing scenarios, you can use the Wokwi CLI to run your firmware on your local machine or CI system. The CLI allows you to start the simulation, check the serial output, and fail the test if the output does not match the expected value.

For more advanced testing scenarios, you can write automation scenarios that automate the simulation, push buttons, change the state of the sensors, and check the serial output.

Wokwi CI is powered by a simulation server that runs in the cloud. The server receives your firmware binary, simulates it, and streams the serial output back to your CI system. The server is stateless and can run multiple simulations in parallel.

Wokwi does not store your firmware, and it is deleted from the cloud server after the simulation is finished. If you do not want to upload your firmware to the cloud, please contact us to discuss options for on-premise deployment of Wokwi CI.

The simulation time is calculated as the sum of the simulation time of all the tests in your CI workflow.

Each user has a limit of simulation time per month, according to their Wokwi plan:

For more information about the paid plans, please see the Pricing page.

If you need more simulation time, please contact us to discuss options for a custom plan.

You can limit the simulation time for each test in your CI workflow using the --timeout option of the CLI. For example, to limit the simulation time to 10 seconds, use:

The Wokwi CLI includes experimental support for the Model Context Protocol (MCP), enabling AI agents to interact with Wokwi's simulation capabilities. This allows AI assistants to run automated tests, simulate hardware behavior, and integrate Wokwi into AI-powered development workflows.

**Examples:**

Example 1 (bash):
```bash
wokwi-cli --timeout 10000
```

---
