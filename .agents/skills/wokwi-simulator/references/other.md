# Wokwi-Simulator - Other

**Pages:** 17

---

## Wokwi Automation Scenarios

**URL:** https://docs.wokwi.com/wokwi-ci/automation-scenarios

**Contents:**
- Wokwi Automation Scenarios
- Scenario File Structure​
- Available Steps​
  - Wait (delay)​
    - Parameters​
    - Example Usage​
  - Assert Pin Value (expect-pin)​
    - Parameters​
    - Example Usage​
  - Control a Part (set-control)​

Automation scenarios allow you to automate the simulation, push buttons, change the state of the sensors, and check the serial output. You can use automation scenarios to test your firmware in a realistic environment, and verify that it behaves as expected.

Each automation scenario is a YAML file that describes a sequence of actions that the simulator should take. You can use the --scenario CLI option to load an automation scenario file.

The basic structure of an automation scenario file is as follows:

Automation scenarios are currently in alpha. The API is not fully documented yet, and may change in the future. You can use the example projects as a reference.

These can be used as a sequence of actions to perform when running the scenario. Use these to build a list of steps for testing your project.

Wait for an amount of time.

Check if a pin is set to an expected value.

Set a controllable part of a compontent to a specified value. View part documentation for available controls or see a list of supported parts below.

Wait for serial console output which matches a given string.

Write text or an array of numbers to the serial console.

Take a screenshot of a specific component and compare it with an existing capture.

This step requires part-id and save-to and/or compare-with.

To build the test projects and run the tests, you need to install PlatformIO Core and the Wokwi CLI, get a Wokwi CI token and set the WOKWI_CLI_TOKEN environment variable with the token.

You can then use pio run to compile the project and wokwi-cli . --scenario <scenraio_file>.yaml to run the tests. You can also use Wokwi for VS Code to interactively simulate the test projects.

Example parts with test scenarios are available at the wokwi-part-tests GitHub repository. We will try to compile and run tests for the wokwi-dht22 part on the ESP32.

Begin with cloning the repository:

Navigate to the part in question:

Build the required microcontroller firmware:

This can also be done via the PlatformIO VS Code extension - just click the build button.

Finally, run the test!

If successful, the output of the test looks as follows:

Several Wokwi parts support automation controls that can be controlled using automation scenarios. These controls allow you to programmatically change the state of sensors, press buttons, and modify component values during simulation.

Each part's documentation page contains detailed information about the specific automation controls available, including control names, types, and example usage.

**Examples:**

Example 1 (yaml):
```yaml
name: 'Your scenario name'version: 1author: 'Your name'steps:  # List of steps:  - set-control:      part-id: btn1      control: pressed      value: 1  - delay: 500ms  - wait-serial: 'Button 1 pressed'
```

Example 2 (yaml):
```yaml
delay: 30ms
```

Example 3 (yaml):
```yaml
expect-pin:  part-id: esp  pin: 2  expected: 1
```

Example 4 (yaml):
```yaml
set-control:  part-id: dht  control: humidity  value: 39
```

---

## Migrating Wokwi projects to VS Code

**URL:** https://docs.wokwi.com/vscode/migrating

**Contents:**
- Migrating Wokwi projects to VS Code
- Download the project source​
- Create an empty project in VS Code​
- Add the source​
- Verify/add libraries​
- Test the build tools​
- Add configuration​
- Test the simulator​

The web-based Wokwi simulator is a powerful and well-integrated way to try out your project designs: there are many capabilities which "just work" in the online simulator which will require some additional steps or workarounds to build and run locally.

This checklist of steps should help you overcome the most common issues. It is assumed that you have already installed the VS Code extension for Wokwi (see the Getting started guide).

Using MicroPython? The setup for MicroPython projects is quite different - please see the VS Code for MicroPython page.

To start, the first step is to save your online project. From the same menu, under the save button, you can then select to download a .zip archive of the project. This will contain useful files such as any source code and the diagram.json file used by Wokwi. Once downloaded you can extract the files from the archive and use them in your local project.

If you are using an extension such as ESP-IDF or PlatformIO in VS Code, it is far easier to create an empty template project first before adding your Wokwi code. Use the provided templates for your chosen platform to create a new empty project. This will include specifying the hardware to be targeted and will create the required source structure and build files.

This step will create a boilerplate project in a working state, ready to add your own code.

Depending on the complexity of your project, adding the source should be quite straightforward.

For a new PlatformIO Arduino project, the directory tree should look like this:

In this case you would delete the /src/main.cpp and replace it with the '.ino' file from the project you downloaded.

PlatformIO encourages the use of standard C++ files (.cpp). To convert your .ino file, you can rename it and change the extension to '.cpp', but you will also need to add a line to include the standard Arduino headers at the beginning of the file:

Any user functions should also be declared before they are called. There is a more detailed example of this in the PlatformIO documentation FAQ.

For ESP-IDF the default project directory tree looks like this:

This is not the entire tree, as it is very large!

The build directory is where the built artifacts will be created, which you will need to refer to in a later step.

All of the source files should go in main. If you have multiple source files, you should also update the CMakelists.txt file in the same directory to include any other files which need to be built.

For Zephyr, the default workspace tree looks like this:

This is not the entire tree, as it is very large!

You are encouraged to follow the Zephyr getting started guide, and to prepare your project following the application development documentation for Zephyr (in particular, see the different application types).

If your project has used any additional libraries you may need to resolve them for your local build environment. The Wokwi online simulator includes access to a whole range of built-in and third party libraries which you may have added to your project - now your local build environment will also need them. It is usually better to use the library manager included with your build tools to ensure that you get an up to date and known working version of the library.

If you are using PlatformIO in VS Code, many libraries are available in the Library Manager. Use the libraries.txt file downloaded with your project as a guide to the names of the libraries you need.

The PlatformIO Library Manager has a search facility which will make this easier - just copy in the name of the library and hit search. Clicking on the 'Add' button will add the library to the platformio.ini file for each of the build targets you have configured.

Note that many libraries have similar or sometimes even the same name.

If you are using the ESP-IDF extension for VS Code, libraries are managed as 'components'. A component is any modular code object compiled as a static library. The component library for ESP-IDF, much like the Library Manager in PlatformIO, contains many useful libraries maintained by Espressif, and tested third-party contributions.

If the library you wish to use isn't available in the supported available libraries, you can add it manually.

For PlatformIO, the library documentation will give further guidance.

For ESP-IDF projects, custom libraries can be added as a component. Check out the ESP-IDF project structure documentation for more details.

The Wokwi simulator requires a built firmware file to run, so the next step should be to check that you can generate one. Use the relevant build command from your chosen framework to build the files.

Check the terminal window output for any errors or warnings which you may want or need to correct.

The online simulator controls its own build environment. To work locally in VS Code, you will need to provide an extra configuration file, wokwi.toml. This will not be part of the downloaded archive because Wokwi doesn't know what build tools or framework you will use for local VS Code development.

The structure and contents of the wokwi.toml file are covered in the VS Code project configuration page. In the previous step you already built the firmware files needed.

You can also generate the wokwi.toml file using the Wokwi CLI if it is installed (see install instructions here), by running the command:

At this point you should also add the diagram.json file from your downloaded project. This must be in the same directory as the wokwi.toml file.

When you select the diagram.json file in the VS Code editor, it will automatically open an embedded window with a graphical display showing the Wokwi circuit layout.

Use the start button in this window to start the simulation. The simulation should run exactly as it did in the online Wokwi simulator.

Note: You will need a license to edit the diagram in this view (see the Wokwi pricing page).

**Examples:**

Example 1 (unknown):
```unknown
├── .gitignore├── include│   └── README├── lib│   └── README├── platformio.ini├── src│   └── main.cpp└── test    └── README
```

Example 2 (cpp):
```cpp
#include <Arduino.h>
```

Example 3 (unknown):
```unknown
├── build│   ├── app-flash_args│   ├── bootloader│   ├── bootloader-flash_args│   ├── bootloader-prefix|   ...│   ├── cmake_install.cmake  │   ├── compile_commands.json│   ├── config│   │   ├── kconfig_menus.json│   │   ├── sdkconfig.cmake│   │   ├── sdkconfig.h│   │   └── sdkconfig.json│   ├── config.env│   ├── esp-idf│   ...├── CMakeLists.txt├── main│   ├── CMakeLists.txt│   └── main.c├── README.md└── sdkconfig
```

Example 4 (unknown):
```unknown
├── bootloader│   └── mcuboot├── modules│   ├── bsim_hw_models│   ├── crypto│   ├── debug│   ├── fs│   ├── hal│   ├── lib│   └── tee├── tools│   ├── edtt│   └── net-tools├── .west│   └── config└── zephyr    ├── arch    ├── boards    ...    ├── zephyr-env.cmd    └── zephyr-env.sh
```

---

## Frequently Asked Questions

**URL:** https://docs.wokwi.com/faq

**Contents:**
- Frequently Asked Questions
- What does Wokwi mean?​
- How do I find a project I saved previously?​
- How do I change or cancel my subscription?​
- The simulation is slow, how can I make it faster?​
- How can I use Wokwi offline?​
- How does Wokwi work?​
- How can I update the payment method for my subscription?​

When choosing the name for Wokwi, we were looking for a short word that would be easy to pronounce and didn't have any meaning yet. We came up with a list of possible names, and picked the one we liked the most, Wokwi. Here are some of the names that didn't make it: Duvav, Hajuu, Chipine, Zeprr.

If you haven't signed in to Wokwi, use the same device & browser that saved the project and visit https://wokwi.com/dashboard/projects. If you sign in to Wokwi before saving projects, that same URL will show all projects that you have saved on any device/browser. You can also navigate to your saved projects by clicking on your profile picture and selecting "My Projects" from the menu.

You can manage your subscription, including updating or canceling it, by visiting the Subscriptions page.

There are many factors that can affect the simulation speed. Here are some tips that can help you get better performance:

Wokwi offers an offline mode through the Wokwi for VS Code extension. To set it up and learn more, visit the official guide here: Wokwi Offline Mode Documentation.

Wokwi compiles your code into a binary firmware, and then executes the binary firmware one instruction at a time, as a real microcontroller would. If you want to learn about the internals, check out the following resources:

Go to https://wokwi.com/dashboard/subscriptions and click on "Change" next to the payment method.

---

## Editor Keyboard Shortcuts

**URL:** https://docs.wokwi.com/keyboard-shortcuts

**Contents:**
- Editor Keyboard Shortcuts
- General shortcuts​
- Basic editing keys​
- Power editing keys​

* if you have selected some text, this will operate on the selection instead of the current line

These keyboard shortcuts enable powerful editing operations, such as managing multiple cursors / selections.

* if you selected some text, this will operate on the selection instead of the current line

---

## GPIO pins API

**URL:** https://docs.wokwi.com/chips-api/gpio

**Contents:**
- GPIO pins API
  - pin_t pin_init(const char *name, uint32_t mode)​
  - void pin_mode(pin_t pin, uint32_t mode)​
  - void pin_write(pin_t pin, uint32_t value)​
  - uint32_t pin_read(pin_t pin)​
  - bool pin_watch(pin_t pin, pin_watch_config_t *config)​
  - void pin_watch_stop(pin_t pin)​

Chips interact with the simulator using digital pins. The pins are defined in a JSON file, called {chip-name}.chip.json (replace {chip-name} with the actual name of the chip). For instance, the following JSON file defines a chip with 4 pins (IN, OUT, VCC, GND):

The GPIO pins API allows your chip implementation code to interact with the GPIO pins:

Initializes the given pin, and returns a pin identifier for use with the other pin methods. The mode parameters configure the initial state of the pin. The following values are available:

Note: pin_init() can only be called from chip_init(). Do not call it at a later time. You can use pin_mode() to change the mode of a pin at any time.

Configures the given pin as digital input or output. The valid values for mode are the same as pin_init(): INPUT, INPUT_PULLUP, INPUT_PULLDOWN, OUTPUT, OUTPUT_LOW, OUTPUT_HIGH, and ANALOG.

Set the output value for a digital pin. Use the LOW and HIGH constants for value.

Reads the current digital value of the pin, returns either LOW or HIGH.

Listens for changes in the digital value of the given pin. The config structure contains the following fields:

The valid values for edge are:

You can only have one watch for a pin at any given time. The function returns true if the watch was successfully set, or false in case there is already a watch defined for this pin (and thus the new watch was not set).

The pin_change callback signature is as follows:

Stops watching for changes on the given pin.

**Examples:**

Example 1 (json):
```json
{  "name": "Inverter",  "author": "Uri Shaked",  "pins": ["OUT", "IN", "VCC", "GND"]}
```

Example 2 (cpp):
```cpp
void chip_pin_change(void *user_data, pin_t pin, uint32_t value) {  // value will either be HIGH or LOW}
```

Example 3 (cpp):
```cpp
const pin_watch_config_t watch_config = {  .edge = FALLING,  .pin_change = chip_pin_change,  .user_data = chip,};pin_watch(pin, &watch_config);
```

---

## Debugging your code

**URL:** https://docs.wokwi.com/vscode/debugging

**Contents:**
- Debugging your code
- Configure Wokwi​
- Configure VS Code​
  - ESP-IDF projects​
  - PlatformIO projects​
  - Arduino (AVR) projects​
- Start the debugger​
- Troubleshooting​

You can debug your code while it is running in the simulation using the VS Code debugger. To set up the debugger, follow these steps:

Add the following line to the [wokwi] section of your wokwi.toml configuration file:

Create a launch configuration file for VS Code at .vscode/launch.json. Here's a template you can use:

The type describes the VS Code extension used here. In this case cppdbg. Therefore the following extension must be installed: https://marketplace.visualstudio.com/items?itemName=ms-vscode.cpptools

Replace the program path with the path to your firmware's ELF file, and the miDebuggerPath with the path to a GDB executable that supports your project's architecture (e.g. for AVR projects, use avr-gdb).

For ESP-IDF projects, you can set the miDebuggerPath to "${command:espIdf.getToolchainGdb}", and the debugger will automatically use the correct GDB executable (this requires the ESP-IDF extension to be installed). For a complete example, check out the ESP32 Hello WiFi debug configuration.

PlatformIO provides a precompiled version of GDB that you can use. For example, the debug an ESP32 project, you can set the miDebuggerPath to "${userHome}/.platformio/packages/toolchain-xtensa-esp32/bin/xtensa-esp32-elf-gdb.exe" on Windows, or "${userHome}/.platformio/packages/toolchain-xtensa-esp32/bin/xtensa-esp32-elf-gdb" on macOS and Linux.

For Arduino projects, you need to use a recent version of GDB. The version that comes with the Arduino IDE (7.8) is too old, and will fail with an error: "ERROR: Unable to start debugging. Failed to find thread 1 for break event".

You can download a recent version of avr-gdb from here (Windows/Linux) or here (macOS, using Homebrew).

Before starting the simulator, build your software for the target to simulate.

Building the "debug" configuration can simplify the analysis of the program execution while debugging.

Start the Wokwi simulator by pressing F1 and then selecting "Wokwi: Start Simulator and Wait for Debugger". The simulator will load, but the program will be paused, waiting for the debugger to connect. Then press F5 to start the debugger.

You need to start Wokwi before starting the debugger. If you start the debugger first, it will fail to connect to the simulator.

If you get an error message saying "Remote 'g' packet reply is too long", you are probably using a GDB version that is incompatible with the microcontroller architecture (e.g. using avr-gdb with an ESP32 project). Make sure you are using the correct GDB version for your project's microcontroller.

**Examples:**

Example 1 (unknown):
```unknown
gdbServerPort=3333
```

Example 2 (json):
```json
{  "version": "0.2.0",  "configurations": [    {      "name": "Wokwi GDB",      "type": "cppdbg",      "request": "launch",      "program": "${workspaceFolder}/build/your-firmware.elf",      "cwd": "${workspaceFolder}",      "MIMode": "gdb",      "miDebuggerPath": "/usr/local/bin/xtensa-esp32-elf-gdb",      "miDebuggerServerAddress": "localhost:3333"    }  ]}
```

---

## MCP Support

**URL:** https://docs.wokwi.com/wokwi-ci/mcp-support

**Contents:**
- MCP Support
- Wokwi MCP Server​
- Configuration​
  - Authentication​

The Model Context Protocol (MCP) is an open standard that allows AI agents—such as Copilot, Claude Code, Cursor, Gemini, ChatGPT and others to securely interact with external tools and services. For Wokwi users, MCP enables seamless integration between AI assistants and embedded simulation.

The Wokwi CLI includes an experimental MCP server that allows AI agents to interact with Wokwi's simulation and testing capabilities. This enables AI agents to:

To configure your AI agent to use the Wokwi MCP server, add the following to your agent's MCP configuration:

You will need a valid Wokwi CLI token to use the MCP server. You can generate a token in the Wokwi CI Dashboard.

**Examples:**

Example 1 (json):
```json
{  "servers": {    "Wokwi": {      "type": "stdio",      "command": "wokwi-cli",      "args": ["mcp"],      "env": {        "WOKWI_CLI_TOKEN": "${input:wokwi-cli-token}"      }    }  }}
```

---

## Analog API

**URL:** https://docs.wokwi.com/chips-api/analog

**Contents:**
- Analog API
  - float pin_adc_read(pin_t pin)​
  - void pin_dac_write(pin_t pin, float voltage)​
- Simulator examples​

Measures the current voltage on the given pin, and returns it. The pin must be set to ANALOG mode, otherwise the return value of this function is undefined. Note that Wokwi is a digital simulator with basic analog support, so there is currently very limited analog simulation. Some parts which support analog output include the potentiometer, NTC temperature sensor, photoresistor, and analog joystick.

Sets the analog voltage on the given pin. Currently, the reference voltage for all the virtual ADCs is 5 volts (regardless of the MCU), so setting the voltage to 0 will return the minimum value, and setting the voltage to 5 will return the maximum value (that is 1023 on Arduino). This may change in the future.

This method can be called before setting the pin to ANALOG mode, but the voltage will only update once the pin mode is set to ANALOG.

---

## Running Wokwi Offline

**URL:** https://docs.wokwi.com/vscode/offline-mode

**Contents:**
- Running Wokwi Offline
- Offline installation​

Wokwi for VS Code requires an internet connection to run. If you need to use Wokwi for VS Code in an environment without internet access, you can subscribe to the Pro plan.

When running in offline mode, the title of the simulator tab will be "Wokwi Simulator (Offline)", and the simulator will display the date when the simulation engine was last updated:

To update the simulator engine, go online and start the simulator. The simulator will automatically update the engine to the latest version, and will use it the next time you run the simulator in offline mode.

If you need to install Wokwi for VS Code on a machine that does not have internet access, we can prepare a custom installation package for you. Please contact us to get a quote.

---

## UART API

**URL:** https://docs.wokwi.com/chips-api/uart

**Contents:**
- UART API
  - uart_dev_t uart_init (const uart_config_t *config)​
  - bool uart_write (uart_dev_t uart, uint8_t *buffer, uint32_t count)​
- Simulator examples​

To create an UART device, first call uart_init, passing in an uart_config_t struct. This struct defines the RX/TX pins, the baud rate, and the rx/write_done callbacks.

Initializes UART device. The config argument defines the pins, configuration, and callbacks for the UART device. It contains the following fields:

Both of the callbacks (rx_data, write_done) are optional. They all use the user_data pointer as their first argument.

Write count bytes from the memory pointed to by buffer to the given uart device. Returns true on success, or false if the UART device is already busy transmitting data from a previous uart_write call (and the new data won't be transmitted).

The data starts transmitting after uart_write returns. Once Wokwi finishes transmitting the data, the write_done callback is called (from the uart_config_t structure that you passed to uart_init).

**Examples:**

Example 1 (cpp):
```cpp
static void on_uart_rx_data(void *user_data, uint8_t byte) {  // `byte` is the byte received on the "RX" pin}static uint8_t on_uart_write_done(void *user_data) {  // You can write the chunk of data to transmit here (by calling uart_write).}// ...const uart_config_t uart1 = {  .tx = pin_init("TX", INPUT_PULLUP),  .rx = pin_init("RX", INPUT),  .baud_rate = 115200,  .rx_data = on_uart_rx_data,  .write_done = on_uart_write_done,  .user_data = chip,};
```

---

## MicroPython projects in VS Code

**URL:** https://docs.wokwi.com/vscode/vscode-micropython

**Contents:**
- MicroPython projects in VS Code
- Before you start​
- Open the repository in Visual Studio Code​
- (Optional) Add your own files​
- Uploading files to the Wokwi simulator​

MicroPython projects differ from those in most of the other frameworks, because in this case the majority of the firmware to be installed on your hardware device (or Wokwi simulator) is MicroPython itself. This firmware, the main.py you create and any additional libraries are the components which need to be uploaded. When the device or simulator is initialized or rebooted, it will first load MicroPython, then run the main.py code, and then (assuming the main code exits) respond to further interaction using the REPL prompt. In the case of the Wokwi simulator, this means, in addition to the code you have created, it also requires a version of the firmware to run the simulation on.

There are three things you should install before migrating your project to VS Code (or starting a new one).

Make sure you have the VS Code extension for Wokwi (See the getting started guide).

Install the mpremote software (see the MicroPython documentation for this step). This software uses a serial connection to your MicroPython-enabled hardware (or the Wokwi simulator) to manage the filesystem and perform tasks such as rebooting or entering the REPL interactive mode.

To avoid compatibility issues, it is strongly advised to install a version of mpremote of the same version as your firmware. The default firmware in the project repository is currently 1.23. To install the matching mpremote with pip for example:

...or adjust for whatever method you are using for installing mpremote.

Clone the example project from GitHub. This project has been set up with the relevant files that the Wokwi simulator requires for different types of hardware. You can visit the link to clone or download the repository, or download it via this link as a zip file. Remember to uncompress the file somewhere you want to work with it!

Run Visual Studio Code and then use 'File>Open folder' to open the directory containing the example project. You'll find the project contains a useful README, a main.py file and some hardware specific directories (esp32, rp2040, and so on, for different microcontrollers).

Each of the hardware directories contains the relevant firmware file for MicroPython, a Wokwi diagram.json file and the wokwi.toml file used to configure the simulator.

Select the diagram.json file, and a new view should open showing a board and the familiar Wokwi simulation display. Click on the play button to run the simulation and test that it works.

Once the simulator starts, it will also open a terminal window which will show the startup messages and then start the interactive REPL. You can enter MicroPython commands here to further test the simulation.

What you may have noticed is that it didn't execute the code in main.py. That's because the local version of main.py hasn't been uploaded to the filesystem of MicroPython in the simulator - it's just running the bare MicroPython firmware.

If you have downloaded a MicroPython project from the Wokwi online simulator, you should add these files to the project, replacing the default files. The download will contain at a minimum the main.py file and a diagram.json file.

Replace main.py in the main directory of the project with your own. If you used any additional files (for example, extra python modules or data files), these should also be added here.

The diagram.json file needs to be in the hardware specific directories. Copy it into each of the hardware directories (or just the ones you intend to use).

You can select the diagram.json file again to open the simulator and confirm that your circuit is displayed.

Before we can upload anything, we need to start the simulation. When it's running, Wokwi also opens a serial connection through a server on a local port. We can then use this connection to upload the files.

The serial port configuration for the simulator can be found in the wokwi.toml file in eache hardware specific directory:

This designates port '4000' for the connection. You may wish to change this if you have other services already using this port.

To upload the main.py file, open a new terminal (you can add an additional terminal within VS Code and switch between it and the Wokwi REPL) and enter the command to upload the main.py file:

Sometimes the command will return an error which ends with TransportError("could not enter raw repl"). If you get this error you can force the REPL into 'Raw' mode by activating the Wokwi REPL window and pressing Ctrl + A, then go back to your terminal and run the command again.

On Unix based systems (e.g. Mac or Linux), you can create a shortcut for connecting to the simulator by running the following command:

After running this command, you can connect to the simulator by running mpremote wokwi.

You can also use mpremote to install libraries which are part of the MicroPython mip package library. For example, to install the ssd1306 library:

For your own additional files, simply upload with the syntax:

You can confirm what files have been uploaded with the ls command:

Once the required files are uploaded, you can either perform a hard reset of the device by accessing the REPL and entering:

Or issue Ctrl + D in the REPL, which will perform a soft reset.

In both instances, main.py will begin running automatically after the device finishes booting.

If using the soft-reboot command provided by mpremote, main.py will not begin running automatically - you will have to connect to the device and specify for it to run the file.

The filesystem stored in the simulator is not persistent. If you stop the simulation or close the simulation window in VS Code, you will need to repeat the steps to upload any files or libraries again.

**Examples:**

Example 1 (bash):
```bash
pip install mpremote==1.23
```

Example 2 (unknown):
```unknown
rfc2217ServerPort = 4000
```

Example 3 (json):
```json
mpremote connect port:rfc2217://localhost:4000 fs cp main.py :main.py
```

Example 4 (json):
```json
mkdir -p ~/.config/mpremoteecho 'config={"wokwi": "connect port:rfc2217://localhost:4000"}' > ~/.config/mpremote/config.py
```

---

## I2C Device API

**URL:** https://docs.wokwi.com/chips-api/i2c

**Contents:**
- I2C Device API
  - i2c_dev_t i2c_init(i2c_config_t *config)​

To create an I2C device, first call i2c_init, passing in an i2c_config_t struct. This struct defines the SCL/SDA pins, the I2C device address, and the connect/read/write/disconnect callbacks.

Initializes an I2C device. The config argument defines the pins, address, and callbacks for the I2C device. It contains the following fields:

All the callbacks (connect, read, write, disconnect) are optional. They all use the user_data pointer as their first argument.

Note: i2c_init can only be called from chip_init(). Do not call it at a later time.

**Examples:**

Example 1 (cpp):
```cpp
bool on_i2c_connect(void *user_data, uint32_t address, bool read) {  // `address` parameter contains the 7-bit address that was received on the I2C bus.  // `read` indicates whether this is a read request (true) or write request (false).  return true; // true means ACK, false NACK}uint8_t on_i2c_read(void *user_data) {  return 0; // The byte to be returned to the microcontroller}bool on_i2c_write(void *user_data, uint8_t data) {  // `data` is the byte received from the microcontroller  return true; // true means ACK, false NACK}void on_i2c_disconnect(void *user_data) {  // This method is optional. Useful if you need to know when the I2C transaction has concluded.}static const i2c_config_t i2c1 {  .address = 0x22,  .scl = pin_init("SCL", INPUT_PULLUP),  .sda = pin_init("SDA", INPUT_PULLUP),  .connect = on_i2c_connect,  .read = on_i2c_read,  .write = on_i2c_write,  .disconnect = on_i2c_disconnect,  .user_data = chip,};
```

---

## Contributing to Wokwi

**URL:** https://docs.wokwi.com/contributing/docs

**Contents:**
- Contributing to Wokwi
- Reporting errors​
- Making quick fixes​
- Larger submissions​
- Style guide​
- Translations​

We warmly welcome community contributions, suggestions, examples, fixes and constructive feedback for our documentation. Every piece of feedback we get helps to make the documentation better, easier to understand and more suited to the needs of our users - so don't hold back! We have tried to make it as easy and painless as possible to contribute - check out the following sections for more details.

If you spot an error (please try and verify first), a broken link or missing word, you can simply file an issue on the GitHub repository where the docs are generated. Please try to include as much detail as possible, definitely including a link to the page(s) affected.

If you know your way around a Markdown file, or the fix you want to make is pretty straightforward, you will find that the bottom of every page has a link called 'Edit this page'. This redirects to GitHub's web-based editor where you can make the changes you want to see and immediately submit a pull request. The changes will get reviewed by the team as soon as possible.

To prevent wasted effort, if you have a larger submission in mind (like adding examples or complete new pages) please get in touch with someone from the team first. You can either raise an issue (as above) to discuss the new material, or better still, pop in to our discord channel and chat to the team and other users there: Join us on Discord

Consistency in documentation is important for many reasons, but mostly for ensuring clarity and usability. It just adds to the cognitive load of people reading docs if language and terms are inconsistent and information is structured in different ways on each new page. We'd like to strive for a light-touch but unambiguous style where it comes to documentation. If you want to contribute, especially larger documents, check out the style guide in the Github repository.

We want as many people as possible to be able to access Wokwi and its documentation in a language they are comfortable with. As part of this ambition, we've already implemented some localizations for the user interface and have begun work on translating the documentation too. If you want to help, check out the translations page.

We’re excited to see what you’ll contribute. Thanks for helping make Wokwi better for everyone!

---

## Using Wokwi in GitHub Actions

**URL:** https://docs.wokwi.com/wokwi-ci/github-actions

**Contents:**
- Using Wokwi in GitHub Actions
- CLI tokens​
- Examples​
- Additional resources​

You can use Wokwi CI with GitHub Actions to run your tests on every commit. You need to have a workflow that builds your project's firmware. Add the following step to your workflow:

For a complete list of options, check out the action's README.

You also need to set up the WOKWI_CLI_TOKEN secret in your repository settings. You can create an API token on the Wokwi CI Dashboard.

The following projects are set up to run on Wokwi CI. You can use them as a reference for your own projects. Check out the .github/workflows directory for the complete GitHub Action configuration in each example.

**Examples:**

Example 1 (yaml):
```yaml
- name: Test with Wokwi  uses: wokwi/wokwi-ci-action@v1  with:    token: ${{ secrets.WOKWI_CLI_TOKEN }}    path: / # directory with wokwi.toml, relative to repo's root    expect_text: 'Hello, world!' # optional
```

---

## SPI Device API

**URL:** https://docs.wokwi.com/chips-api/spi

**Contents:**
- SPI Device API
  - spi_dev_t spi_init(spi_config_t *config)​
  - void spi_start(spi_dev_t spi, uint8_t *buffer, uint32_t count)​
  - void spi_stop(spi_dev_t spi)​
  - The done callback​
- Simulator examples​

To create an SPI device, first call spi_init, passing in an spi_config_t struct. This struct defines the clock and MOSI/MISO pins, the SPI mode, and the done callback.

Initializes an SPI device interface. The config argument defines the pins, mode, and callbacks for the SPI device. It contains the following fields:

The API does not support a CS/SS pin: it is up to the user to select/deselect the SPI interface by calling spi_start() and spi_stop().

Note: spi_init can only be called from chip_init(). Do not call it at a later time.

Starts an SPI transaction, sending and receiving count bytes to/from the given buffer.

You will usually listen for the CS (chip select) pin with pin_watch. Call spi_start() when the CS pin goes low, and spi_stop() when the CS pin goes high.

When creating a device that transfers large amounts of data (e.g. an LCD display), it's recommended to use a large buffer size (few kilobytes). The simulator can use the larger buffer to optimize DMA-controlled SPI transfer and speed up the simulation.

For simple devices that transfer small amounts of data, you can use a single-byte buffer, and process each byte as it arrives in the done callback.

Stops the SPI interface. Usually, you'd call this method when the CS pin goes high.

The signature for the done callback is as follows:

The done callback runs when an SPI transaction finishes: either when the buffer provided to spi_start is full, or when spi_stop was called. The buffer contains the data received (it is the same buffer given to spi_start), and count is the number of bytes that have been transferred (or 0 if spi_stop was called before a complete byte has been transferred).

Your done callback should check the status of the CS pin, and if it is still low, it should call spi_start() again to receive the next chunk of data from the microcontroller.

**Examples:**

Example 1 (cpp):
```cpp
const spi_config_t spi1 = {  .sck = pin_init("SCK", INPUT),  .mosi = pin_init("MOSI", INPUT),  .miso = pin_init("MISO", INPUT),  .mode = 0,  .done = chip_spi_done, // See the example below  .user_data = chip,};
```

Example 2 (cpp):
```cpp
static void chip_spi_done(void *user_data, uint8_t *buffer, uint32_t count) {  // 1. process the received data (optional)  // 2. if the CS pin is still low, schedule the next SPI transaction using `spi_start`}
```

---

## Configuring Your Project (wokwi.toml)

**URL:** https://docs.wokwi.com/vscode/project-config

**Contents:**
- Configuring Your Project (wokwi.toml)
- wokwi.toml​
  - ESP-IDF support​
  - Serial port forwarding​
  - IoT Gateway (ESP32 WiFi)​
  - Custom chips​
- diagram.json​

To simulate your project on Wokwi, you need to create two files in your project's root directory:

A basic wokwi.toml file looks like this:

Replace "path-to-your-firmware" with the location of the compiled firmware, relative to the wokwi.toml file (that is your workspace's root directory).

The extension of the firmware file depends on the board you are using:

The elf field is optional, but providing it can speed up the simulation in some cases.

You check test your configuration by pressing F1 and then selecting "Wokwi: Start Simulator". Make sure you compile your program before starting the simulation.

Avoid using backslashes (\) in your paths. Use forward slash (/) instead, as it makes it possible to open your project on any platform (Windows, Mac and Linux).

For ESP-IDF apps, set firmware to 'build/flasher_args.json' field to automatically load the complete application (including the bootloader and partition table) to esp32. The flasher_args.json file is automatically generated by the idf.py build command. Example:

Wokwi for VS Code allows you to connect to the serial port of the simulated microcontroller using an RFC2217 TCP server. To enable this feature, add the following configuration to your wokwi.toml file, inside the [wokwi] section:

This will start an RFC2217 server on port 4000. You can connect to the serial port using the Serial Monitor extension (select TCP monitor mode) or PuTTY (select Telnet connection type). In addition, you can use PySerial's RFC2217 support to connect to the serial port from your Python code:

Note: make sure the simulator tab is visible in VS Code, otherwise the simulation may pause and you won't get any serial output from the microcontroller.

Wokwi for VS Code includes a bundled version of the Wokwi Private IoT Gateway, which allows you to connect the virtual WiFi of the simulated ESP32 to your local network and the Internet.

You can also connect to the simulated ESP from your computer (e.g. you are running a web server on the ESP32). To do so, set up port forwarding in wokwi.toml. For instance, to forward local port 8180 to port 80 on the ESP32, add the following configuration:

To forward multiple ports, add multiple [[net.forward]] sections.

For a complete example, see the ESP32 Web Server project.

You can load custom chips to the simulation by adding a [[chip]] sections to your wokwi.toml configuration. The following example will load a chip from "chip/inverter.chip.wasm" and make it available under the name chip-inverter in Wokwi's diagram:

Wokwi also requires a JSON file that describes the chip pins. The JSON file should have the same name as the wasm binary, but with a json extension (e.g. chips/inverter.chip.json in the above example). For a complete example, check out the inverter-chip repo.

You can add multiple chips to your project by adding multiple [[chip]] sections, each with a different name and binary.

You can copy the diagram file from an existing project on Wokwi.com. For instance, if you are working on an ESP32 project, you can copy the contents of diagram.json from https://wokwi.com/projects/new/esp32.

**Examples:**

Example 1 (json):
```json
[wokwi]version = 1firmware = 'path-to-your-firmware.hex'elf = 'path-to-your-firmware.elf'
```

Example 2 (json):
```json
[wokwi]version = 1firmware = 'build/flasher_args.json'elf = 'build/example_app.elf'
```

Example 3 (unknown):
```unknown
rfc2217ServerPort = 4000
```

Example 4 (python):
```python
import serialser = serial.serial_for_url('rfc2217://localhost:4000', baudrate=115200)ser.write(b'hello')
```

---

## Time simulation

**URL:** https://docs.wokwi.com/chips-api/time

**Contents:**
- Time simulation
  - uint64_t get_sim_nanos()​
  - timer_t timer_init(timer_config_t *config)​
  - void timer_start(timer_t timer_id, uint32_t micros, bool repeat)​
  - void timer_start_ns(timer_t timer_id, uint64_t nanos, bool repeat)​
  - void timer_stop(timer_t timer_id)​

Returns the current simulator (virtual) time in nanoseconds.

You can get the current time in microseconds by calling get_sim_nanos() / 1000, or in milliseconds by calling get_sim_nanos() / 1000000.

Initializes a new timer. Returns the identifier of the timer. Call timer_start() to start the timer, and define the chip_timer_event() callback to response to timer events.

The timer_config_t struct contains the following fields:

The signature for the callback function is as follows:

Note: timer_init() can only be called from chip_init(). Do not call it at a later time.

Schedules the timer given by timer_id. The micros argument determines how many microseconds will pass until the timer will call chip_timer_event(). If repeat is false, the timer event will be called once (one-shot timer). If repeat is true, the timer event will keep getting called every micros microseconds, until you call timer_stop() or reconfigure the timer with timer_start.

Similar to timer_start, but specifies the duration of the timer in nanoseconds instead of microseconds. Prefer timer_start() when possible, in order to improve performance.

Stops the given timer. If the timer hasn't fired yet, it won't fire until you call timer_start() again.

**Examples:**

Example 1 (cpp):
```cpp
void chip_timer_callback(void *user_data) {  /* Called when the timer fires */}
```

---
