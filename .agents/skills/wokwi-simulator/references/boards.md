# Wokwi-Simulator - Boards

**Pages:** 7

---

## CircuitPython on Wokwi

**URL:** https://docs.wokwi.com/guides/circuitpython

**Contents:**
- CircuitPython on Wokwi
- Project structure​
- Using libraries​
- CircuitPython REPL
- Project examples​

You can simulate CircuitPython on Wokwi using the Raspberry Pi Pico board. To start a new simulation project, open the Raspberry Pi Pico CircuitPython project template.

CircuitPython projects must include a code.py file. The code in this file will execute when you start the simulation.

Wokwi copies all the project files into the Pico's flash file system. This means your project can include additional Python modules and you can import them from code.py or from the interactive REPL. Your project can also include custom data inside text files.

You can get a list of all the files in the flash filesystem by running:

You can use any library from the Adafruit CircuitPython Bundle. Create a "requirements.txt" file in your project, and write the names of the libraries that you use, one per line. Lines that start with "#" are comments.

For example, if you want to install both adafruit_display_text and adafruit_dht, create a "requirements.txt" file with the following content:

When you start the simulation, Wokwi downloads all the libraries and their dependencies. It copies them into the "lib" folder in the flash filesystem. You can call os.listdir('/lib') to get a list of all the libraries installed. For a complete code example, see CircuitPython Library List.

When the code in code.py terminates (or you interrupt it with Ctrl+C), you'll get into the CircuitPython REPL. The REPL is an interactive prompt where you can type python commands and see the results immediately. To paste code into the REPL type Ctrl+E and enter paste mode.

**Examples:**

Example 1 (python):
```python
import osprint(os.listdir('/'))
```

Example 2 (markdown):
```markdown
# requirements.txt exampleadafruit_display_textadafruit_dht
```

---

## ESP32 Simulation

**URL:** https://docs.wokwi.com/guides/esp32

**Contents:**
- ESP32 Simulation
- ESP32 boards​
- Getting Started​
  - Arduino Core​
  - MicroPython​
  - Custom Application Firmware​
- Simulator Examples​
  - Arduino Examples​
  - MicroPython Examples​
  - ESP-IDF Examples​

The ESP32 is a popular WiFi and Bluetooth-enabled microcontroller, widely used for IoT Projects. Wokwi simulates the ESP32, ESP32-C3, ESP32-S2, ESP32-S3, ESP32-C6, ESP32-H2, and ESP32-P4 (beta).

You can contribute additional boards by sending a pull request to wokwi-boards.

You can use the ESP32 simulator to run different kinds of applications:

Start from the Arduino-ESP32 Project Template, or from the ESP32 Blink Example.

If you want to use third-party Arduino libraries, add a libraries.txt file with the list of libraries that you use.

Start from the MicroPython ESP32 Project Template, or from the MicroPython ESP32 Blink Example.

Note: While the simulation is running, press Ctrl+C inside the Serial Terminal to get into the MicroPython REPL. Alternatively, you can edit the Blink Example code and remove the while loop. For more information, check out the MicroPython Guide.

Open the ESP32 custom application project template, and press "F1" in the code editor. Then choose "Upload Firmware and Start Simulation…". Choose any .bin, .elf or .uf2 file from your computer and the simulation will start.

When uploading a custom firmware, it's recommended to create a single .bin file that contains the bootloader, partition table, and application. You can use the esptool merge_bin command to create such file.

For ESP-IDF projects, you can also build a single UF2 file using the command: idf.py uf2. The file will be located in build/uf2.bin, and can be uploaded to the simulator.

The following examples use the ESP-IDF functions. They are compiled using Arduino ESP32 Core:

Follow this guide to simulate Sming Framework projects.

Legend: ✔️ - Simulated 🟡 - Partial implementation/work in progress ❌ - Not implemented (but if you need it, please open a feature request) — - Not available on this chip

* The amount of SRAM can be customized using the "psramSize" attribute.

See the ESP32 WiFi Guide.

You can customize the size of flash and PSRAM by adding the following attributes to the chip:

Some chips have a built-in USB CDC (Serial over USB) + JTAG peripheral. These chips include the ESP32-S3, ESP32-C3, ESP32-C6, and ESP32-H2. You can configure USB CDC support in Wokwi by adding the following attribute to the chip:

Note that you also need to remove any connections to the $serialMonitor pins from the connections section in your diagram.json file.

You can specifiy a custom partititon table by adding a "partitions.csv" file to your project. Check out the ESP32 Partition Table Guide for the exact format of this file.

When loading a custom firmware, you can specify the offset of the firmware in the flash memory. By default, Wokwi will look at the firmware binary and try to figure out the offset automatically, based on the presence of the bootloader and the type of the chip. If Wokwi can't figure out the offset, it will assume that your firmware is an application firmware and load it at offset 0x10000.

You can specify the offset manually by adding the following attribute to the chip:

You can change the MAC address of the WiFi interface by adding the following attribute to the chip:

In order to achieve a higher simulation speed, Wokwi automatically limits the maximum simulated CPU frequency. In most cases, this doesn't affect the behavior of the simulated program and allows you to run the simulation considerably faster. The CPU frequency limit does not affect the timing of the peripherals, only the speed instructions are executed.

To override the maximum CPU frequency, you can set the "cpuFrequency" attribute to a specific frequency (e.g. "16" for 16 MHz) or "max" to run the CPU at the maximum frequency (not recommended - it will make the simulation much slower). The default value is "auto", which means that Wokwi will automatically cap the CPU frequency to about 8 MHz.

**Examples:**

Example 1 (json):
```json
{   "serialInterface": "USB_SERIAL_JTAG" }
```

---

## ESP32 WiFi Networking

**URL:** https://docs.wokwi.com/guides/esp32-wifi

**Contents:**
- ESP32 WiFi Networking
- Connecting to the WiFi​
  - Connecting from Arduino​
  - Connecting from MicroPython​
  - Connecting from Rust (std)​
- Internet Access​
  - The Public Gateway​
  - The Private Gateway​
    - Installation​
    - Usage​

Wokwi simulates a WiFi network with full internet access. You can use the ESP32 together with the virtual WiFi to prototype IoT projects. Common use cases include:

The simulator provides a virtual WiFi access point called Wokwi-GUEST. It is an open access point - no password is required.

To connect from Arduino (on an ESP32) device, use the following code:

Note: We specify the WiFi channel number (6) when calling WiFi.begin(). This skips the WiFi scanning phase and saves about 4 seconds when connecting to the WiFi.

To connect from a MicroPython project, use the following code:

Once connected, you can use the urequests library to send HTTP and HTTPS requests, and the umqtt library to establish MQTT connections.

To connect from Rust with esp-idf-svc (on an ESP32) device, use the following code:

Note: We need to specify the auth_method to None in the ClientConfiguration.

Wokwi uses a special gateway to connect your simulated ESP32 to the internet. This gateway is required since web browsers do not allow direct internet access. There are two ways you can use the Wokwi IoT Gateway: the Public Gateway, and the Private Gateway.

The Public Gateway is the default internet connection method. It works out of the box and enables access to the internet, but not to your local network. All the traffic is monitored for security purposes, so do not use it for private or sensitive data. We occasionally inspect the traffic and may enforce limits if we notice excessive usage of the gateway.

The Public Gateway is a great choice for playing around and learning about WiFi and networking in the ESP32.

The Private Gateway is a small application that you download and run on your computer. It allows faster and more robust ESP32 internet access: the data goes directly from the simulator (running in your browser) to you computer's network, without having to go through the cloud. This means:

The Private Gateway is only available for paying users.

Download the latest version from the Wokwi IoT Gateway releases page. You'll see there versions for Windows, macOS, and Linux. Then extract the ZIP file and run the executable file inside. Your browser / operating system may warn you that the file may be unsafe, so you'll have to tell them to run it anyway.

The gateway does not require any administrator / root permissions. It happily runs as a standard process on your computer.

When you run the gateway, it should print a logo, its version, and say: "Listening on TCP port 9011". Hooray, you've completed the setup!

If you are worried about running the gateway executable on your computer, you are invited to take a look at the source code, and even build the executable file yourself (ask for instructions on discord).

After running the gateway, open any project in Wokwi, go to the code editor, press "F1" and select "Enable Private Wokwi IoT Gateway". You'll be prompted if you want to enable the gateway. Answer "OK" to enable the Private Gateway, or "Cancel" to disable it and switch back to the Public Gateway.

Then run any ESP32 project that uses the WiFi. Look at the gateway output, it should say "Client connected". This means you are using the Private Gateway.

If your ESP32 project is an HTTP server, you can connect to it from your browser at http://localhost:9080/. The connection will be forwarded by the gateway to the default HTTP port (80) on the simulated ESP32.

You can forward a different port by running the IoT gateway with the --forward option, e.g. --forward 1234:10.13.37.2:8080. This will forward all TCP connections to port 1234 on your computer to port 8080 on the simulated ESP32.

Note: The Private IoT Gateway is not currently supported in Safari due to a technical limitation. Please use a different browser (e.g. Chrome, Firefox, Edge).

To connect to your local machine ("localhost") from the code running in the simulator, use the hostname host.wokwi.internal. For example, if you are running an HTTP server on port 1234 on your computer, you can connect to it from within the simulator using the URL http://host.wokwi.internal:1234/.

The ESP32 gets an IP address from a DHCP server running inside the Wokwi IoT gateway. The IP address depends on the type of the gateway that you use:

The MAC address of the simulated ESP32 is 24:0a:c4:00:01:10. You can specify a different MAC address using the macAddress attribute. The BSSID of the virtual access point ("Wokwi-GUEST") is 42:13:37:55:aa:01, and it is listening on WiFi channel 6.

Wokwi simulates a complete network stack: starting at the lowest 802.11 MAC Layer, through the IP and TCP/UDP layers, all the way up to protocols such as DNS, HTTP, MQTT, CoAP, etc. You can view the raw WiFi traffic using a network protocol analyzer such as Wireshark.

First, run an ESP32 project that uses the WiFi in the simulator. Then, click on the WiFi icon, and choose Download PCAP file. Your browser will download a file called wokwi.pcap. Use Wireshark to open this file.

The following screen shot shows an example of an HTTP request packet capture:

As you can see, the PCAP file contains all sort of packets: 802.11 beacon frames, DNS query response (the first entry in the list), and HTTP request/response packets (No. 107 and 113).

In most cases, you'll only want to focus on a specific protocol. You can achieve this by pressing Ctrl+/ in wireshark, and typing a protocol name (http, tcp, ip, dns, dhcp, etc.). The will filter the list and display only the relevant packets.

The Time field in the packet capture uses the simulation clock time. It may advance slower than wall clock time if the simulation is running slower than full speed (100%).

The Wokwi IoT Gateway supports both TCP and UDP. It does not support the ICMP protocol, so the Ping functionality is not available.

**Examples:**

Example 1 (cpp):
```cpp
#include <WiFi.h>void setup() {  Serial.begin(9600);  Serial.print("Connecting to WiFi");  WiFi.begin("Wokwi-GUEST", "", 6);  while (WiFi.status() != WL_CONNECTED) {    delay(100);    Serial.print(".");  }  Serial.println(" Connected!");}void loop() {  delay(100); // TODO: Build something amazing!}
```

Example 2 (python):
```python
import networkimport timeprint("Connecting to WiFi", end="")sta_if = network.WLAN(network.STA_IF)sta_if.active(True)sta_if.connect('Wokwi-GUEST', '')while not sta_if.isconnected():  print(".", end="")  time.sleep(0.1)print(" Connected!")
```

Example 3 (rust):
```rust
use embedded_svc::wifi::{AuthMethod, ClientConfiguration, Configuration};use esp_idf_hal::peripherals::Peripherals;use esp_idf_svc::eventloop::EspSystemEventLoop;use esp_idf_svc::nvs::EspDefaultNvsPartition;use esp_idf_svc::wifi::EspWifi;use esp_idf_sys::EspError;fn main() -> Result<(), EspError> {    esp_idf_sys::link_patches();    let peripherals = Peripherals::take().unwrap();    let sysloop = EspSystemEventLoop::take()?;    let nvs_default_partition = EspDefaultNvsPartition::take()?;    let mut wifi = EspWifi::new(        peripherals.modem,        sysloop.clone(),        Some(nvs_default_partition.clone()),    )?;    wifi.set_configuration(&Configuration::Client(ClientConfiguration {        ssid: "Wokwi-GUEST".into(),        password: "".into(),        auth_method: AuthMethod::None,        ..Default::default()    }))?;    wifi.start()?;    wifi.connect()?;    Ok(())}
```

---

## Interactive debugger

**URL:** https://docs.wokwi.com/guides/debugger

**Contents:**
- Interactive debugger
- Using the debugger​
- Debugging panes​
  - Call stack​
  - Variables​

Wokwi has a built-in debugger that allows you to step through your code, inspect variables, and set breakpoints. The debugger is currently in beta, and is available for AVR microcontrollers: Arduino Uno, Arduino Nano, Arduino Mega, and the ATtiny85.

If you wish to debug other microcontrollers, such as the ESP32 or the Raspberry Pi Pico, you can use Wokwi for VSCode, which has integrated debugger support.

To start debugging your code, click the menu button in the simulator toolbar, and select Debug:

You can set breakpoints by clicking on the left margin of the code editor. The debugger will pause the execution when the program reaches the breakpoint.

When running in debug mode, you will see the debug toolbar above the code editor. The toolbar contains the following buttons:

Continue - Continue running the program. If the program is paused at a breakpoint, the debugger will continue running until the next breakpoint.

Step over - Step over the current line of code. If the current line is a function call, the debugger will step over the function call and stop at the next line of code.

Step into - Step into the current line of code. If the current line is a function call, the debugger will step into the function and stop at the first line of the function.

Step out - Step out of the current function.

The debugging panes appear when you pause the program (either manually, or at a breakpoint). You'll find the panes below the diagram, next to the Serial Monitor pane.

The call stack shows the current function call stack. The top of the stack is the currently executing function. The bottom of the stack is the main function.

The variables pane shows the current values of the variables in the current scope. The variables are grouped by scope: local variables and global variables (which also include register values).

---

## Welcome to Wokwi!

**URL:** https://docs.wokwi.com/

**Contents:**
- Welcome to Wokwi!
- Why Wokwi?​
  - Start right now.
  - Mistakes are okay.
  - Easy to get help and feedback.
  - Gain confidence in your code.
  - Unlimited hardware.
  - Maker-friendly community.
- Unique Features​
- How much does it cost?​

Wokwi is an online Electronics simulator. You can use it to simulate Arduino, ESP32, STM32, and many other popular boards, parts and sensors.

Here are some quick examples of things you can make with Wokwi:

Start right now. No waiting for components, or downloading large software. Your browser has everything you need to start coding your next IoT project in seconds.

No waiting for components, or downloading large software. Your browser has everything you need to start coding your next IoT project in seconds.

Mistakes are okay. You can't destroy the virtual hardware. Trust us, we tried. So don't worry about frying your precious components. And unlike real hardware, you can always undo.

You can't destroy the virtual hardware. Trust us, we tried. So don't worry about frying your precious components. And unlike real hardware, you can always undo.

Easy to get help and feedback. Sharing a link to your Wokwi project is all you need.

Sharing a link to your Wokwi project is all you need.

Gain confidence in your code. Separate hardware and software issues.

Separate hardware and software issues.

Unlimited hardware. No need to scavenge parts from old projects. Use as many parts as you need, without worrying about project price and stock.

No need to scavenge parts from old projects. Use as many parts as you need, without worrying about project price and stock.

Maker-friendly community. A place for you to share your projects, ask for help, and get inspiration. Wokwi Discord Community

A place for you to share your projects, ask for help, and get inspiration. Wokwi Discord Community

Wokwi is free for personal use. For commercial users and professionals, please check out our paid plans in the pricing page.

---

## GDB Debugging (Advanced)

**URL:** https://docs.wokwi.com/gdb-debugging

**Contents:**
- GDB Debugging (Advanced)
- Running GDB in Wokwi​
- Debugging Session Example​
- Learn more​

GDB is a powerful source code debugger. You can use it to debug your Arduino and Raspberry Pi Pico code in Wokwi.

To start a GDB session, go into the code editor and press F1. In the prompt that opens, type "GDB", and select "Start Web GDB Session (debug build)".

This will open a new browser tab with the GDB prompt. If this is the first time you are using this feature, it may take up to 30 seconds for GDB to fully load.

When GDB is ready, you'll get the following prompt:

At this point you can type GDB commands. For instance, suppose you want to run your program line-by-line, starting from setup(). First, type tbreak setup and c to start the program and run it until the beginning of setup():

At this point, type layout src to show the source code of your program, and type next to execute the next line of source code. You can then type next repeatedly to go over the code line by line.

If you want to print the value of some variable, use the print command. For example, if you have a variable called ledIndex, type print ledIndex to print the value of that variable.

Take a look at the AVR GDB Cheatsheet to see many more examples of useful GDB commands. It takes time to learn about all the different GDB features and to use them efficiently, but it can get very powerful even with just a few basic commands.

If you want to learn how we got GDB to work in the browser, take a look at Running GDB in the Browser. You don't need to know this in order to use GDB - it's just the gory details that let you take a look under the hood.

**Examples:**

Example 1 (unknown):
```unknown
0x00000000 in __vectors ()(gdb)
```

Example 2 (vue):
```vue
(gdb) tbreak setupTemporary breakpoint 1 at 0x2ca: file sketch.ino, line 28.(gdb) cContinuing.Temporary breakpoint 1, setup () at sketch.ino:2828        pinMode(LED_BUILTIN, OUTPUT);(gdb)
```

---

## MicroPython on Wokwi

**URL:** https://docs.wokwi.com/guides/micropython

**Contents:**
- MicroPython on Wokwi
- Project structure​
- MicroPython REPL
- Project examples​

You can create and run MicroPython projects on Wokwi. Start from the Raspberry Pi Pico MicroPython project template.

All MicroPython projects must include a main.py file. MicroPython will automatically load and execute the code from main.py when you start the simulation.

Wokwi copies all the project files into the Pico's flash filesystem. This means your project can include additional Python modules and you can import them from main.py or from the interactive REPL. Your project can also include custom data inside text files.

You can get a list of all the files in the flash filesystem by running:

When the code in main.py terminates (or you interrupt it with Ctrl+C), you'll get into the MicroPython REPL. The REPL is an interactive prompt where you can type python commands and see the results immediately. Type help() for MicroPython API cheat sheet. To paste code into the REPL type Ctrl+E and enter paste mode.

**Examples:**

Example 1 (python):
```python
import osprint(os.listdir('/'))
```

---
