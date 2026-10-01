# Wokwi-Simulator - Diagram Format

**Pages:** 12

---

## wokwi-pi-pico Reference

**URL:** https://docs.wokwi.com/parts/wokwi-pi-pico

**Contents:**
- wokwi-pi-pico Reference
- Pin names​
  - Onboard LED​
- Simulation features​
  - Arduino core​
  - Serial Monitor​
  - Serial Monitor over UART​
- Exporting UF2 binary​
- MicroPython Support​
- Simulator examples​

Raspberry Pi Pico, an RP2040 microcontroller board with dual-core ARM Cortex-M0+ processor, 264k of internal RAM, and flexible Programmable I/O (PIO) feature.

Pins GP0 to GP22 are digital GPIO pins. Pins GP26, GP27, and GP28 are digital GPIO pins with analog input function.

* The physical pin numbers of the ground pins are 3, 8, 13, 18, 23, 28, 33, and 38. † These pins do not appear in the visual diagram editor, but you can use them in your diagram.json file.

Pins 3V3_EN / RUN / ADC_VREF are not available in the simulation and are therefore omitted from the table.

The Raspberry Pi Pico has an onboard LED, attached to GPIO PIN 25. The LED is lit when the pin is driven high.

You can also use the LED_BUILTIN constant to reference the LED in your Arduino code:

See Blink for a complete code example.

The Raspberry Pi Pico is simulated using the RP2040js Library. This table summarizes the status of the simulation features:

Legend: ✔️ Simulated 🟡 Partial implementation/work in progress ❌ Not implemented

The Arduino core provides the built-in Arduino functions, such as pinMode() and digitalRead(), as well as a set of standard Arduino libraries, such as Servo, Wire and SPI.

When compiling your code for the Raspberry Pi Pico and for the Raspberry Pi Pico W, Wokwi uses the Arduino-Pico core, built on top of the Pi Pico SDK.

In the past, Wokwi also supported the RP2040-mbed Arduino core, but it has been deprecated in favor of the Arduino-Pico core.

You can use the Serial Monitor to receive information from the code running on the Pi Pico, such as debug prints. By default, the Serial Monitor communicates with the Pi Pico over USB.

Setting up the USB connection can take some time, and any messages printed during the USB setup time will be lost. Therefore, it's recommended to tell setup() to wait for the Serial Monitor connection before printing anything:

The Serial Monitor can also communicate with the Pi Pico over the physical UART interface. To configure the UART communication between the Raspberry Pi Pico and the Serial Monitor, add the following connections to your diagram.json file:

The example assumes that the Pi Pico was defined with an id of "pico", e.g.

The use the Serial1 object in your code: initialize the port using Serial1.begin(115200), and then print messages with Serial1.println(). For example:

For a complete example, check out the Pi Pico Serial Monitor over UART Example.

You can upload the program from the emulator directly into a physical Raspberry Pi Pico board. The steps are:

The Raspberry Pi Pico supports MicroPython, and you can use it for running MicroPython projects in Wokwi. For more information, check out the MicroPython Guide.

**Examples:**

Example 1 (cpp):
```cpp
pinMode(LED_BUILTIN, OUTPUT);digitalWrite(LED_BUILTIN, HIGH);
```

Example 2 (cpp):
```cpp
void setup() {  Serial.begin(115200);  while (!Serial) {    delay(10); // wait for serial port to connect. Needed for native USB  }  // Now you can safely print message:  Serial.println("Hello, Serial Monitor!");}
```

Example 3 (json):
```json
"connections": [    [ "$serialMonitor:RX", "pico:GP0", "", [] ],    [ "$serialMonitor:TX", "pico:GP1", "", [] ],    …  ]
```

Example 4 (json):
```json
"parts": [    {      "type": "wokwi-pi-pico",      "id": "pico",      …    },    …  ]
```

---

## board-ssd1306 Reference

**URL:** https://docs.wokwi.com/parts/board-ssd1306

**Contents:**
- board-ssd1306 Reference
- Pin names​
- Attributes​
- Using in Arduino​
- Simulator examples​

Monochrome 128x64 OLED display with I2C interface

The default I2C address of the SSD1306 module is 0x3c (60). Some modules have a different address (0x3d), you can change the address by editing diagram.json and setting the i2cAddress attribute to "0x3d".

You can choose between several SSD1306 Arduino libraries:

All the above libraries are available on Wokwi.

---

## Wokwi CLI Usage

**URL:** https://docs.wokwi.com/wokwi-ci/cli-usage

**Contents:**
- Wokwi CLI Usage
- CLI Options​
  - Configuration​
  - Automation​
  - General​

Create an API token on the Wokwi CI Dashboard. Set the WOKWI_CLI_TOKEN environment variable to the token value.

If you haven't set up your project for Wokwi yet, you can use the init command to configure your project for Wokwi. Run the following command in your project's root directory:

This command will ask you a few questions and will automatically generate wokwi.toml and diagram.json files for your project.

To run the simulation, use the following command:

The CLI will start the simulation and display the serial output. It will automatically exit after 30 seconds.

You can use the following options to customize the CLI behavior:

**Examples:**

Example 1 (bash):
```bash
wokwi-cli init
```

Example 2 (bash):
```bash
wokwi-cli <your-project-directory>
```

---

## Interactive Diagram Editor

**URL:** https://docs.wokwi.com/guides/diagram-editor

**Contents:**
- Interactive Diagram Editor
- Editing parts​
  - Adding a part​
  - Moving a part​
  - Rotating a part​
  - Duplicating a part​
  - Deleting a part​
  - Selecting multiple parts​
  - Copying and pasting parts​
- Editing wires​

The diagram editor provides an interactive way to edit your circuit diagram: add components to the simulation and define the connections between them. It's a convenient alternative for editing the diagram.json file directly.

To add a new part, click on the blue "+" button at the top of the diagram editor (or press "A" while the diagram is in focus).

You'll see a menu with a list of parts you can add. Choose a part to add it. The part will be added at position (0, 0), and then you can drag it to the desired position.

Not all parts are currently available through the menu. For example, MCU boards and micro-controllers such as the Arduino Nano or the ATtiny85 are missing. You can still add these parts by editing diagram.json directly.

Move a part by clicking on it and then dragging it with your mouse.

Rotate a part by clicking on it (to select it) and then pressing "R". The part will rotate 90 degrees clockwise. If you need to rotate a part by a different amount (e.g. 45 degrees), you can achieve that by editing diagram.json.

Create a new copy of a part by clicking on it (to select it) and the pressing "D". You can press "D" several times to create multiple copies of the part.

Delete a part by clicking on it (to select it) and then pressing the Delete button.

Select multiple parts by clicking on the parts with the Shift key pressed. You can then move all the parts together, duplicate them (using the "D" key), or delete them using the Delete key.

You can copy the selects part(s) by using the standard Copy keyboard shortcut (Ctrl+C or ⌘+C). If you selected multiple parts, all the wires that connect the selected parts are also copied. The parts you copied are stored in your system clipboard in a JSON format, similar to the diagram.json format.

To paste the parts you copied, click on the diagram and press the standard Paste keyboard (Ctrl+V or ⌘+V). In some cases, the parts will be pasted outside of the currently visible diagram area, so you may have to zoom out in order to find them. This will be fixed in the future.

You can use the copy-paste feature between different project, and quickly copy several parts (including all the internal connections) at once.

To create a new wire between two parts, click on one of the pins that you'd like to connect. Then click on the second (target) pin. This will create the wire.

If you want the wire to go in a specific way, you can guide it by clicking where you want it to go after selecting the first pin.

To cancel a new wire (delete it without selecting a target pin) click the right mouse button or press Escape.

The color of new wires is automatically determined by the function of the pin: wires starting from ground pins are black, 5 V pins are red, and other wires are green.

You can change the color of a wire by clicking on it, and then selecting a new color for the wire. You can also use the following keyboard shortcuts to set wire colors:

These keyboard shortcuts also work while drawing a new wire. You can also change wire colors by editing diagram.json

Select a wire by clicking on it, and then click the trash icon on the wire (or press the Delete key). You can also delete a wire by double-clicking on it.

The following table summarizes the keyboard shortcuts:

* On Mac, use ⌘ instead of Ctrl

Firefox users: if the keyboard shortcuts don't work for you, please make sure that the "Search for text when you start typing" setting is disabled.

Parts and wires automatically snap to a 2.54 mm (0.1 inches) grid. The grid is invisible by default.

The Shift key temporarily disables the grid snapping and allows free movement of parts and wires.

The Alt key or the Ctrl key temporarily toggle to fine grid snapping. The fine grid is 1.27 mm (0.05 inches) wide.

Press "G" to toggle the display of the grid and rulers. Tick labels on the rulers show measurements in millimetres (the default), but you can switch to inches by clicking on the units in the top right corner.

When you start the simulation, Wokwi hides the grid. Stopping the simulation restores the grid.

---

## Attributes

**URL:** https://docs.wokwi.com/chips-api/attributes

**Contents:**
- Attributes
  - Naming​
  - uint32_t attr_init(const char *name, uint32_t default_value)​
  - uint32_t attr_init_float(const char *name, float default_value)​
  - uint32_t attr_read(uint32_t attr)​
  - float attr_read_float(uint32_t attr)​
  - Simulator Examples​

Attributes are input parameters that the user can set in diagram.json. You can also define a controls section in the .chip.json file to let the user edit these parameters interactively during the simulation. This is particularly useful for sensor inputs (e.g. temperature, humidity, etc.).

When naming your attributes, please follow the following conventions:

Defines a new integer attribute with the given name. The default_value will be used when the user does not define a value for the attribute in diagram.json (under the attrs section of the custom chip part).

The function returns a handle to the attribute, which can be accessed using attr_read().

Note: attr_init can only be called from chip_init(). Do not call it at a later time.

Defines a new floating point attribute with the given name. See attr_init() for more info.

Note: attr_init_float can only be called from chip_init(). Do not call it at a later time.

Returns the current value of the attribute. attr should be a valid attribute handle, previously returned by attr_init().

Returns the current value of the attribute. attr should be a valid attribute handle, previously returned by attr_init_float().

---

## Custom Chip Definition (JSON)

**URL:** https://docs.wokwi.com/chips-api/chip-json

**Contents:**
- Custom Chip Definition (JSON)
- Pins​
- Controls​
- Display​

The pinout and properties of custom chips are defined in a Chip Definition JSON file. The file name should be <chip-name>.chip.json. For example, if your chip is called i2c-light-sensor, the file name should be i2c-light-sensor.chip.json.

The JSON file should contain a single object with the following properties:

The pins array should contain the names of the pins for your chip, starting from pin number 1. If you wish to skip some pins (e.g. you want the breakout board to only have pins on its left side), use an empty string ("") for the pin name.

The example above defines a chip with 5 pins, ordered as follows:

Controls provide a way for users to interact with your chip while the simulation is running. For example, a temperature sensor chip can have a control that lets the user set the current temperature.

The controls property should contain an array of control objects. Each control object should have the following properties:

To read the value of the control from your chip code, use the Attributes API.

The display property allows you to attach a display to your chip. Use the display to implement a custom LCD, OLED, or e-paper display, or to show the state of your chip (e.g. draw a graph of the temperature over time, or visually indicate the state of a blinds controller).

The display property should contain an object with the following properties:

To draw on the display from your chip code, use the Framebuffer API.

**Examples:**

Example 1 (json):
```json
"pins": ["VCC", "GND", "RST", "", "SCL", "SDA"],
```

Example 2 (unknown):
```unknown
___ VCC -|⚬  |- SDA GND -|   |- SCL RST -|___|-
```

Example 3 (json):
```json
"controls": [    {      "id": "relativeHumidity",      "label": "Relative Humidity",      "type": "range",      "min": 0,      "max": 100,      "step": 1    }  ],
```

Example 4 (json):
```json
"display": {    "width": 128,    "height": 64  },
```

---

## wokwi-slide-switch Reference

**URL:** https://docs.wokwi.com/parts/wokwi-slide-switch

**Contents:**
- wokwi-slide-switch Reference
- Pin names​
- Attributes​
  - Bouncing​
- Simulator examples​

Standard Single Pole Double Throw (SPDT) slide switch.

The slide switch has three pins. Pin 2 (in the middle) is the common pin. Depending on the position of the switch's handle, it's connected to either pin 1 or 3:

The following diagram illustrates the connections inside the slide switch. You can see the gray sliding contact that moves together with the handle and creates a connection between pin 2 and either pin 1 or 3:

When you move a physical slide switch, the circuit opens and closes tens or hundreds of times. This phenomenon is called Bouncing.

Wokwi simulates switch bouncing by default. You can disable the bouncing simulation for individual switches by setting their "bounce" attr to "0":

---

## Diagram Editor in VS Code

**URL:** https://docs.wokwi.com/vscode/diagram-editor

**Contents:**
- Diagram Editor in VS Code
- Opening the diagram editor​
- Editing the diagram as text​
- Running the simulation​

The visual diagram editor in Wokwi for VS Code allows you to edit the diagram of your simulation project. It is available in the Hobby+ and Pro plans.

To open the diagram editor, click on a diagram.json file in the Explorer view. The diagram will open in a new tab. The diagram editor also works for files matching the diagram.*.json pattern, such as diagram.esp32.json. This is useful if you have multiple target boards in your project, and want to maintain a diagram for each target board.

If you are using the Community or the Hobby plan, you will be able to view the diagram, but not edit it in the diagram editor. You can still edit the diagram.json file in the text editor.

Some advanced features are only available if you modify the diagram in the text editor. You can open the text editor by right clicking on the diagram.json tab, selecting "Reopen Editor With..." and then selecting "Text Editor".

You can run the simulation by pressing the green play button in the top left corner of the editor. Wokwi will open a new tab and start the simulation.

---

## Framebuffer API

**URL:** https://docs.wokwi.com/chips-api/framebuffer

**Contents:**
- Framebuffer API
  - buffer_t framebuffer_init(uint32_t *pixel_width, uint32_t *pixel_height)​
  - void buffer_write(buffer_t buffer, uint32_t offset, void *data, uint32_t data_len)​
  - void buffer_read(buffer_t buffer, uint32_t offset, void *data, uint32_t data_len)​
- Simulator examples​

Use the framebuffer API to implement displays (LCD, OLED, e-paper, etc.). The display size is defined in the .chip.json file. The framebuffer uses 32 bits per pixel. The pixels are stored in the RGBA format. The total size of the buffer is pixel_width * pixel_height * 4 bytes.

Returns the framebuffer for the current chip, and the pixel dimensions (width/height) of the frame buffer.

Note: framebuffer_init can only be called from chip_init(). Do not call it at a later time.

Copies data_len bytes from data into the frame buffer, at the given offset.

Copies data_len bytes at the given offset of the frame buffer into data.

---

## diagram.json File Format

**URL:** https://docs.wokwi.com/diagram-format

**Contents:**
- diagram.json File Format
- File structure​
- Parts​
- Connections​
  - Wire placement mini-language​
  - Wire placement animation​

Each simulation project contains a diagram.json file. This file defines the components that will be used for the simulation, their properties, and the connections between the components.

The diagram file is a JSON file with several sections. The basic file structure is as follows:

"version" is always 1, "author" is the name of the person who created the file, and "editor" is the name of the application that was used to edit the file ("wokwi").

In addition, you can add a "serialMonitor" section to configure the Serial Monitor.

The "parts" section defines the list of components in the simulation. It's an array of objects with the following properties:

id and type are required, the other fields are optional.

For example, here's how you define a red LED called "led1" at position (x=100, y=50):

Each part must have a unique "id" property. If two parts have the same "id", the simulation may not function correctly.

A partial list of part types (e.g. wokwi-led) can be found under the "Diagram Reference" section of this guide. We're currently working to expand this list. Meanwhile, some of the parts are also documented at Wokwi Elements.

If your simulation project contains code, the diagram should include a microcontroller part that will execute your code. The following microcontrollers are currently supported:

Instead of manually specifying the left/top coordinates for each item, you can drag them with the mouse to the desired position.

The "connections" section defines how the parts are connected. Each connection is an array with four items:

For example, the following definition will connect the A (anode) pin of led1 to pin 13 of the uno part:

You can find the name of a component pin by moving the mouse over it.

Each item in the "connections" section can specify a list of instructions how to draw the lines for the wire. Wires always go in straight lines, either horizontally or vertically, and never diagonally.

There are three instructions:

The "v10" will move 10 pixels down from the source pin, then "h5" will move five pixels the right.

The instructions that appear after the "*" are applied in reverse order: "h10" will move 10 pixels right of the target pin, then "v-15" will move 15 pixels up.

Finally, the simulator will connect the two ends of the wire with a combination of horizontal and a vertical wire that cover the remaining distance, as necessary.

If you are a visual learner, you may find the following GIF animation useful. The animation was created by Steve Sigma.

**Examples:**

Example 1 (json):
```json
{  "version": 1,  "author": "Uri Shaked",  "editor": "wokwi",  "parts": [],  "connections": []}
```

Example 2 (json):
```json
{  "id": "led1",  "type": "wokwi-led",  "left": 100,  "top": 50,  "attrs": {    "color": "red"  }}
```

Example 3 (json):
```json
["led1:A", "uno:13", "green", []],
```

Example 4 (json):
```json
["v10", "h5", "*", "v-15", "h10"]
```

---

## Translating Wokwi

**URL:** https://docs.wokwi.com/contributing/translating

**Contents:**
- Translating Wokwi
- Translating the user interface​
  - Existing translations​

This page explains how you can contribute translations to Wokwi.

To translate the user interface into a new language, download the current version of the English strings file. The translation file is a text file in the standard JSON format. It can be edited by any text editor, as well as many translation tools.

If you wish to contribute translations to one of the existing language, you can download the translation file for the specific language from the list on this issue, and work your way from there.

When you are ready to submit your translations, please open an issue and attach the file. GitHub doesn't support directly attaching JSON files, so you can either copy the content of the file into your new issue, or zip it and attach the Zip file.

Not all the texts are currently available for translation, but we're adding new texts all the time. You can subscribe to this issue to get a notification whenever new texts are available for translation.

---

## Wokwi CLI Installation

**URL:** https://docs.wokwi.com/wokwi-ci/cli-installation

**Contents:**
- Wokwi CLI Installation

The CLI allows you to run Wokwi simulations from your terminal, and integrate them with your CI system. We recommend using the Wokwi for VS Code extension for local development, and the CLI for running your tests on CI.

Both the CLI and the VS Code extension use the same project configuration files (wokwi.toml and diagram.json), so you can use the VS Code extension to create and test your project, and then use the CLI to run it on CI.

To install the Wokwi CLI, run the following command:

On Windows, you can use the following command in PowerShell:

Alternatively, you can download the CLI directly from the GitHub Releases page. Rename the file to wokwi-cli (or wokwi-cli.exe on Windows), make it executable (chmod +x wokwi-cli on Linux/Mac), and move it to a directory in your PATH (e.g. /usr/local/bin on Linux/Mac).

**Examples:**

Example 1 (bash):
```bash
curl -L https://wokwi.com/ci/install.sh | sh
```

Example 2 (powershell):
```powershell
iwr https://wokwi.com/ci/install.ps1 -useb | iex
```

---
