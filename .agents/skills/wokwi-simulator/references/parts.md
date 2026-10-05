# Wokwi-Simulator - Parts

**Pages:** 55

---

## wokwi-max7219-matrix Dot Matrix Reference

**URL:** https://docs.wokwi.com/parts/wokwi-max7219-matrix

**Contents:**
- wokwi-max7219-matrix Dot Matrix Reference
- Pin names​
- Attributes​
  - Chaining​
  - Matrix layout​
  - Examples​
- Simulator examples​

8x8 LED Dot Matrix with MAX7219 Controller

Each dot matrix units is an 8x8 LED matrix. All the LEDs in the matrix have the same color. You can make the display wider by setting the "chain" attribute. For example, setting "chain" to 4 will chain four dot matrix units horizontally, resulting in 32x8 matrix (four times 8x8 matrix).

If you want to chain units in a custom way (e.g. select a different pixel color for each unit, chain them vertically, etc), connect the DOUT pin of one unit to the DIN pin of the next unit. You also need to connect the CLK / CS pins of the units together. See 32x32 LED Matrix Tunnel for an example.

There are several type of matrix layout, based on the commonly available modules. You can set the "layout" property to choose the desired pixel layout:

Choosing the wrong layout will cause your text / drawing to be rotated and / or mirrored.

---

## board-franzininho-wifi Reference

**URL:** https://docs.wokwi.com/parts/board-franzininho-wifi

**Contents:**
- board-franzininho-wifi Reference
- Board hardware​
- Simulator examples​

Open source ESP32-S2 development board created in Brazil. See the ESP32 Guide for more information.

The board includes three built-in LEDs:

---

## wokwi-potentiometer Reference

**URL:** https://docs.wokwi.com/parts/wokwi-potentiometer

**Contents:**
- wokwi-potentiometer Reference
- Pin names​
- Attributes​
- Using the Potentiometer in Arduino​
- Keyboard control​
- Automation controls​
- Simulator examples​

Knob-controlled variable resistor (linear potentiometer)

The information below also applies to the slide potentiometer.

Note: Wokwi does not support full analog simulation, so you will get the same results even if you don't connect the GND/VCC pins.

This may change in the future, so it's a good idea to connect GND/VCC anyway.

Connect the SIG pin to one of Arduino's analog input pins (A0, A1, …). Then use the analogRead() function to read the current value of the potentiometer.

The following code example assumes that the potentiometer is connected to A0. It will read and print the current value of the potentiometer every 100 milliseconds:

You can run the example on Wokwi. Observe how the plotter graph changes as you move the potentiometer's knob.

You can control the potentiometer with the keyboard:

You'll need to click on the potentiometer before using these keyboard shortcuts.

The potentiometer can be controlled using Automation Scenarios. It exposes the following controls:

The following example set the potentiometer to the middle position:

**Examples:**

Example 1 (cpp):
```cpp
void setup() {  Serial.begin(115200);  pinMode(A0, INPUT);}void loop() {  int value = analogRead(A0);  Serial.println(value);  delay(100);}
```

Example 2 (yaml):
```yaml
- set-control:      part-id: pot1      control: position      value: 0.5
```

---

## wokwi-servo Reference

**URL:** https://docs.wokwi.com/parts/wokwi-servo

**Contents:**
- wokwi-servo Reference
- Range of motion​
- Pin names​
- Attributes​
  - Examples​
- Simulator examples​
- Tutorials​

A standard Micro Servo Motor.

The servo is able to sweep from 0 degrees to 180 degrees, with hard stops at both ends.

---

## wokwi-led Reference

**URL:** https://docs.wokwi.com/parts/wokwi-led

**Contents:**
- wokwi-led Reference
- Pin names​
- Attributes​
  - Examples​
  - Gamma correction​
  - FPS​
- Simulator examples​

Note: To rotate LEDs, click on them and press "R", or set the "rotate" property.

The LED automatically applies gamma correction. This means that even a very short burst of current will result in some visible light, similar to how physical LEDs work, so you get more accurate simulation in the following cases:

You can disable the gamma correction by setting the "gamma" attribute to "1.0". You can also choose a different gamma factor by setting this attribute to the desired value. The default gamma correction factor is 2.8.

The Gamma Correction Demo project shows the behavior of different gamma values: the LED on the left has the default gamma factor of 2.8, while the LED on the right has a gamma factor of 1.0. You can see how lower values of analogWrite() look much brighter on the left LED.

For more information about gamma correction, including some code examples, check out this great guide from Adafruit.

The fps attribute controls the framerate of the LED, that is how often the LED brightness is updated. The default value is 80.

If you are using PWM (analogWrite()) and noticing flickering, try setting a smaller the fps value.

In case you are experiencing LED light ghosting, you can try increasing the fps value. For example, this rotating cube uses an fps value of 10000 to update the LEDs at a higher rate and avoid ghosting of the rotating cube.

---

## wokwi-74hc165 Reference

**URL:** https://docs.wokwi.com/parts/wokwi-74hc165

**Contents:**
- wokwi-74hc165 Reference
- Pin names​
- Operation​
  - Sampling (PL low)​
  - Shifting (PL high)​
  - Using the shift register​
  - Chaining multiple shift registers​
- Arduino code example​
- Simulator examples​

8-bit Parallel-In Serial-Out (PISO) Shift Register (Input)

Use the 74HC165 shift register to expand the number of input pins on your microcontroller. For output shift register (e.g. controlling multiple LEDs with just a few pins), please see the wokwi-74hc595.

* Use the DS to daisy-chain multiple 74HC165 units together. Connect DS to the Q7 pin of the previous 74HC165 chip in the chain. You can leave DS disconnected if you don't chain or for the first chip in the chain.

The 74HC165 is a shift register with eight parallel inputs: it enables you to simultaneously sample eight input pins, and then read the result one bit at a time. In other words, it is an easy way to expand the number of input pins for your microcontroller.

The shift register has two states: sampling and shifting. The PL pin selects the active state.

When PL is low, the shift register is in the sampling state: it reads the inputs from pins D0…D7 and stores them. It also outputs the value of D7 in the Q7 pin (so Q7 == D7).

When PL is high, the shift register is in the shifting state. It retains the value it reads from the input, and let you read this value one bit at a time through the Q7 pin. You can read the next bit by pulsing CP (the serial clock) high. Initially, Q7 contains the value read from D7. When you pulse the clock high, you get the value from D6. When you pulse it again, you get the value from D5, etc.

Changing the input pins while PL is high has no effect.

To use the shift register, connect pins D0…D7 to your inputs (e.g. slide switches or pushbuttons). You may need to add external pull-up or pull-down resistors, especially if you go with the buttons.

You also need to connect PL, CP, and Q7 to your microcontroller. Configure PL and CP as digital outputs, and Q7 as a digital input.

Finally, connect to CE pin to ground. You can use this pin to disable shifting (by driving it high), but it's usually not required. Don't leave the CE pin floating!

Sample the inputs by setting PL to low.

Read the value by setting PL to high. Read the first (most-significant) bit from Q7, then pulse the CP high to get the next bit. Repeat this eight times, until you read all the bits from the shift register.

You can chain several shift registers and still use a single microcontroller input pin. This configuration is also called a cascade. The connections are as follows:

The operation is same as above: sampling and then shifting. There is one difference: you read more than 8 bits when shifting. For a chain of n shift registers, you'll shift 8*n bits by repeatedly reading Q7 and then pulsing CP high. So for two 74hc165 units you'd shift 16 bits, for three units you'd shift 24 bits, etc.

If you don't need all the bits (e.g. you have two shift register units, by only use 10 inputs), then you can shift a smaller number of bits, as many as you are interested in.

This example assumes that you connected the shift register to Arduino as follows:

* If you chain multiple shift registers, connect only the Q7 pin of the last register in the chain to Arduino.

Run this example on Wokwi.

**Examples:**

Example 1 (cpp):
```cpp
const int dataPin = 2;   /* Q7 */const int clockPin = 3;  /* CP */const int latchPin = 4;  /* PL */const int numBits = 8;   /* Set to 8 * number of shift registers */void setup() {  Serial.begin(115200);  pinMode(dataPin, INPUT);  pinMode(clockPin, OUTPUT);  pinMode(latchPin, OUTPUT);}void loop() {  // Step 1: Sample  digitalWrite(latchPin, LOW);  digitalWrite(latchPin, HIGH);  // Step 2: Shift  Serial.print("Bits: ");  for (int i = 0; i < numBits; i++) {    int bit = digitalRead(dataPin);    if (bit == HIGH) {      Serial.print("1");    } else {      Serial.print("0");    }    digitalWrite(clockPin, HIGH); // Shift out the next bit    digitalWrite(clockPin, LOW);  }  Serial.println();  delay(1000);}
```

---

## board-grove-oled-sh1107 Reference

**URL:** https://docs.wokwi.com/parts/board-grove-oled-sh1107

**Contents:**
- board-grove-oled-sh1107 Reference
- Pin names​
- Simulator examples​

Monochrome display with 128*128 resolution

* Only the I2C interface is supported. The SPI interface is not simulated.

---

## wokwi-gas-sensor Reference

**URL:** https://docs.wokwi.com/parts/wokwi-gas-sensor

**Contents:**
- wokwi-gas-sensor Reference
- Pin names​
- Attributes​
- Operation​
  - Digital output​
- Simulator examples​

MQ2 Gas Sensor module

The MQ2 Gas Sensor is a semiconductor sensor that can detect the presence of various combustible gases including LPG, Propane, Hydrogen, Methane, and Carbon Monoxide. The sensor has both analog and digital outputs:

To use the MQ2 sensor:

Note: In real hardware, the sensor needs a pre-heating time of about 20-30 seconds before taking readings. The simulator provides readings immediately.

The digital output (DO) pin will read LOW when gas concentration exceeds the threshold. The threshold is set by the threshold attribute. The default threshold is 4.4V.

---

## Arduino Libraries

**URL:** https://docs.wokwi.com/guides/libraries

**Contents:**
- Arduino Libraries
- Adding third party libraries​
  - Uploading custom libraries​
- The libraries.txt file​

To include a library, go to the code editor and type # on an empty line. You'll see a autocomplete dropdown with #include suggestions for popular libraries.

By default, Wokwi compiles your code with the standard built-in Arduino libraries, such as Wire.h and SPI.h.

To add third-party libraries to your project, go to the "Library Manager" tab in the code editor, and press the blue "+" button. Type some text in the search box to search for a library (e.g. "FastLED"), and then click on one of the library names in the list to add it.

You can use this method to install any Arduino library from the Arduino Library Manager.

Paying users can upload any Arduino library by selecting a folder from their computer. To upload a custom library, click on the blue "+" button in the Arduino library manager and then click on "Upload a Library".

The selected folder should contain the source code for the library (.h and .c/.cpp files). After selecting a folder, Wokwi will zip its contents and upload it to the Wokwi build server. You will be able to see the library in the Library Mananger as a .zip file.

Anyone who opens the project will be able to download the library from the Library manager. Any user who creates a copy of the project will be able to use the library in the copied project.

When you add libraries through the built-in "Library Manager", it will create a "libraries.txt" file in your project. It is a simple text file that lists all of libraries installed in your project, one library per line. Lines that start with "#" are comments.

Normally, you don't need to edit this file yourself - the "Library Manager" does this for you. But you can find this file useful if you want to install a specific version of a library. To select a specific version, add "@" after the library name, followed by the version that you want to install.

For example, the following file will install the latest versions of Servo and FastLED, as well as version 2.3.0 of MySensors:

Custom libraries have the following format: the library name, followed by a the text "@wokwi:", and a unique identifier of the library's zip file on Wokwi's servers. You can copy custom libraries to a different project by copying the relevant lines from libraries.txt into the other project.

**Examples:**

Example 1 (markdown):
```markdown
# Sample libraries.txt file:ServoFastLED# Install a specific version of a library:MySensors@2.3.0
```

---

## wokwi-franzininho Reference

**URL:** https://docs.wokwi.com/parts/wokwi-franzininho

**Contents:**
- wokwi-franzininho Reference
- About the Franzininho​
- Pin names​
  - On board LEDs​
- Simulator examples​

A small ATtiny85-based development board, popular in Brazil.

The Franzininho DIY in an open-source, Arduino-compatible board designed in Brazil. It's based on the ATtiny85 chip, so please consult the ATtiny85 documentation for technical information.

The yellow LED (LED1) is connected to pin PB1 of the ATtiny85 chip. You can learn more about the board and the people behind it in the Franzininho homepage (Portuguese).

The board includes two 3mm LEDs:

---

## wokwi-hc-sr04 Reference

**URL:** https://docs.wokwi.com/parts/wokwi-hc-sr04

**Contents:**
- wokwi-hc-sr04 Reference
- Pin names​
- Attributes​
- Operation​
  - Setting the distance​
- Arduino code example​
- Simulator examples​

HC-SR04 Ultrasonic Distance Sensor

To start a new distance measurement set the TRIG pin to high for 10uS or more. Then wait until the ECHO pin goes high, and count the time it stays high (pulse length). The length of the ECHO high pulse is proportional to the distance. Use the following table to convert the ECHO pulse length in microseconds into centimeters / inches:

To change the distance while the simulation is running, click on the HC-SR04 drawing in the diagram and use the slider to set the distance value. You can choose any value between 2cm and 400cm.

Try this example on Wokwi

**Examples:**

Example 1 (cpp):
```cpp
#define PIN_TRIG 3#define PIN_ECHO 2void setup() {  Serial.begin(115200);  pinMode(PIN_TRIG, OUTPUT);  pinMode(PIN_ECHO, INPUT);}void loop() {  // Start a new measurement:  digitalWrite(PIN_TRIG, HIGH);  delayMicroseconds(10);  digitalWrite(PIN_TRIG, LOW);  // Read the result:  int duration = pulseIn(PIN_ECHO, HIGH);  Serial.print("Distance in CM: ");  Serial.println(duration / 58);  Serial.print("Distance in inches: ");  Serial.println(duration / 148);  delay(1000);}
```

---

## wokwi-pushbutton Reference

**URL:** https://docs.wokwi.com/parts/wokwi-pushbutton

**Contents:**
- wokwi-pushbutton Reference
- Pin names​
- Attributes​
  - Defining a keyboard shortcut​
  - Bouncing​
  - Stickiness​
  - Examples​
- Automation controls​
- Simulator examples​

12mm Tactile Switch Button (momentary push button).

The push button has two set of pins (contacts), 1 and 2. When the push button is pressed, it connects these two contacts, thus closing an electrical circuit.

Each contact has a pin of the left side of the push button, and another pin on the right side of the push button. So pin 1.l is the left pin for first contact, and 1.r is the right pin for the first contact. Since both belong to the same contact, they are always connected, even when the button is not pressed.

The following diagram illustrates the connections inside the pushbutton:

When working with Arduino, you'd usually connect one contact (e.g. 1.r or 1.l) to a digital pin and configure that pin as INPUT_PULLUP, and the other contact (e.g. 2.r or 2.l) to the ground. The digital pin will read LOW when you press the button, and HIGH when the button is not pressed.

You can use the "key" attribute to define a keyboard key that will control the button. The key is only active when the simulation is running and the diagram has focus.

For example, suppose you defined "key" to "Q". Then, when you run the simulation, pressing Q in the keyboard will press the push button. The button will be kept in pressed state as long as you keep pressing Q, and once you release the key, the button will also be released.

You can define any alphanumerical keyboard shortcut (so English letters and numbers), and for letters, the value of "key" is case insensitive (so "q" and "Q" mean the same).

You can also target some special keys, such as "Escape", "ArrowUp", "F8", " " (space), or "PageDown", but some keys could be blocked by the browser (e.g. "F5" that refreshes the page). The full list of key names can be found here. Note the the special key names are case sensitive - so "Escape" will work, "escape" won't.

Firefox users: if the keyboard shortcuts don't work for you, please make sure that the "Search for text when you start typing" setting is disabled.

When you press physical pushbutton, the circuit opens and closes tens or hundreds of times. This phenomenon is called Bouncing. This happens because of the mechanical nature of pushbuttons: when the metal contacts come together, there's a brief period when the contact isn't perfect, which causes a series of rapid open/close transitions.

Wokwi simulates button bouncing by default. You can disable bouncing simulation by setting the "bounce" attr to "0":

The bouncing simulation follows the behaviour described in "The Art of electronics" by Horowitz & Hill:

When the switch is closed, the two contacts actually separate and reconnect, typically 10 to 100 times over a period of about 1ms.

For example, this project shows the difference between bouncing and non bouncing button. It has two buttons connected to the same Arduino input pin:

If you want the button to stay pressed, Ctrl-click it (Cmd-click on Mac). It will cause the button to stay pressed until the next click. This is useful when you need multiple buttons pressed at the same time.

The pushbutton can be controlled using Automation Scenarios. It exposes the following controls:

The following example simulates a button press on "btn1" for 200ms:

**Examples:**

Example 1 (yaml):
```yaml
- set-control:    part-id: btn1    control: pressed    value: 1- delay: 200ms- set-control:    part-id: btn1    control: pressed    value: 0
```

---

## wokwi-tm1637-7segment Reference

**URL:** https://docs.wokwi.com/parts/wokwi-tm1637-7segment

**Contents:**
- wokwi-tm1637-7segment Reference
- Pin names​
- Attributes​
- Using the 7-segment display​
- Simulator examples​

Seven segment LED display module with TM1637 4-wire interface

* The DIO pin is also used for acknowledging the data received from the microcontroller, by pulling it down at a specific clock cycle.

This variant of the seven segment display uses the TM1637 chip. You'll only need 2 microcontroller pins to communicate with it.

The TM1637 communication protocol is non-standard. It resembles the I2C protocol, but it is simpler and incompatible with I2C. Luckily, you can use a library and not worry about the implementation of the protocol. Here are some TM1637 libraries you can use on Arduino: RT1637_RT(https://github.com/RobTillaart/TM1637_RT), Grove 4-Digit Display.

---

## wokwi-a4988 Reference

**URL:** https://docs.wokwi.com/parts/wokwi-a4988

**Contents:**
- wokwi-a4988 Reference
- Pin names​
  - Microstepping configuration​
- Using the A4988 Stepper Driver​
- Simulator Examples​

A4988 Stepper Motor driver, for use with wokwi-stepper-motor

* Digital pins with a default value of Low (0) are pulled-down, and pins with a default value of High (1) are pulled up. Pins without a default value are floating.

Standard stepper motors have 200 steps per revolution (the steps are spaces 1.8 degrees apart). The stepper driver supports microstepping: turning the motor less than one step for every pulse. Microstepping allows finer control of the motor movement.

Use the MS1/MS2/MS3 pins to select the microstepping configuration for the stepper driver:

* These mode are not fully supported by wokwi-stepper-motor. When using these modes, the number of steps per revolution will still be correct, but the motor angle will only update every half step. For instance, if you use 1/8 step mode, the motor will move half a step (0.9 degrees) every four STEP pin pulses.

Connect the stepper motor pins to the 1B/1A/2A/2B pins of the driver. The RESET pin has to be HIGH, so you can connect it to the adjacent SLEEP pin (which is pulled HIGH by default). Alternatively, you can enable/disable the stepper motor driver from your code by connecting the RESET/SLEEP pins to your microcontroller.

Use the STEP pin to move the stepper motor. Every HIGH pulse on this pin will move the motor one step (or microstep, depending on the MS1/MS2/MS3 pins). When the DIR pin is HIGH, the stepper motor will move clockwise. When the DIR pin is LOW, the motor will move counterclockwise.

For example, if DIR, MS1 and MS3 are LOW, and MS2 is HIGH (1/4 step mode), then pulsing the STEP pin will move the motor 1/4 step (0.45 degrees) counterclockwise.

---

## wokwi-ky-040 Rotary Encoder Reference

**URL:** https://docs.wokwi.com/parts/wokwi-ky-040

**Contents:**
- wokwi-ky-040 Rotary Encoder Reference
- Pin names​
- Operation​
  - Schematics​
- Using the Rotary Encoder in Arduino​
  - Reading the rotation​
  - Using the button​
- Keyboard control​
- Simulator examples  ​

KY-040 Rotary Encoder module with 20 steps per revolution.

The rotary encoder offers two ways of interaction:

Every time the user rotates the knob, it produces a LOW signal on the DT and CLK pins:

Both pins will go back high within a few milliseconds. The following diagram illustrates this:

You can experiment with the DT/CLK pin timings by connecting them to the Wokwi Logic Analyzer. Check out the Logic Analyzer Guide to learn how to use the logic analyzer.

The KY-040 module includes two internal pull-up resistors that pull-up pins CLK and DT to VCC. The simulation always pulls these pins up, even if you left the VCC pin floating.

You can read the rotation by checking the status of the CLK pin. Whenever it goes LOW, read the value of the DT pin to determine the direction: HIGH means clockwise rotation, LOW means counterclockwise rotation. Code example:

You can also run this example on Wokwi.

Note: your code will need to read the state of the pins frequently in order to detect the rotations correctly. If your loop() takes too long (e.g. you use delay() in your code), we recommend using attachInterrupt() to listen for changes in the CLK pin. Assuming CLK is connected to pin 2, and DT to pin 3 (as before):

To read the state of the encoder's button, connect to to any Arduino IO pin and initialize this pin as INPUT_PULLUP. Then read the state of the button using digitalRead(). It'll read LOW as long the the button is pressed.

The following code example will turn on Arduino's built-in LED (13) as long as the button is pressed. It assumes you connected the SW to Arduino pin 4. You also need to connect the GND pin to one of the Arduino's GND pins.

To control the rotary encoder with the keyboard, first click on it, then use the following keys:

* Hold down the arrow keys to continuously rotate the encoder, generating a series of pulses on the CLK/DT pins.

**Examples:**

Example 1 (cpp):
```cpp
#define ENCODER_CLK 2#define ENCODER_DT  3void setup() {  Serial.begin(115200);  pinMode(ENCODER_CLK, INPUT);  pinMode(ENCODER_DT, INPUT);}int lastClk = HIGH;void loop() {  int newClk = digitalRead(ENCODER_CLK);  if (newClk != lastClk) {    // There was a change on the CLK pin    lastClk = newClk;    int dtValue = digitalRead(ENCODER_DT);    if (newClk == LOW && dtValue == HIGH) {      Serial.println("Rotated clockwise ⏩");    }    if (newClk == LOW && dtValue == LOW) {      Serial.println("Rotated counterclockwise ⏪");    }  }}
```

Example 2 (cpp):
```cpp
#define ENCODER_CLK 2#define ENCODER_DT  3void setup() {  pinMode(ENCODER_CLK, INPUT);  pinMode(ENCODER_DT, INPUT);  attachInterrupt(digitalPinToInterrupt(ENCODER_CLK), readEncoder, FALLING);}void readEncoder() {  int dtValue = digitalRead(ENCODER_DT);  if (dtValue == HIGH) {    Serial.println("Rotated clockwise ⏩");  }  if (dtValue == LOW) {    Serial.println("Rotated counterclockwise ⏪");  }}void loop() {  // Do whatever}
```

Example 3 (cpp):
```cpp
#define ENCODER_BTN 4void setup() {  pinMode(ENCODER_BTN, INPUT_PULLUP);  pinMode(LED_BUILTIN, OUTPUT);}void loop() {  if (digitalRead(ENCODER_BTN) == LOW) {    digitalWrite(LED_BUILTIN, HIGH);  } else {    digitalWrite(LED_BUILTIN, LOW);  }}
```

---

## wokwi-dip-switch-8 Reference

**URL:** https://docs.wokwi.com/parts/wokwi-dip-switch-8

**Contents:**
- wokwi-dip-switch-8 Reference
- Pin names​
- Keyboard operation​
- Simulator examples​

Set of 8 electrical switches in a single package

You can use the keyboard to toggle the swithches while the simulation is running. Click on the DIP switch to select it, then toggle the switches by pressing the keys "1" to "8".

Firefox users: if the keyboard shortcuts don't work for you, please make sure that the "Search for text when you start typing" setting is disabled.

---

## Relay Module Reference

**URL:** https://docs.wokwi.com/parts/wokwi-relay-module

**Contents:**
- Relay Module Reference
- Pin names​
- Attributes​
- Operation​
- Simulator Examples​

Electrically operated switch

The relay is an electronic switch.

When the IN pin is high / disconnected, COM is connected to NC (NC means normally closed).

When the IN pin is low, COM is connected to NO (NO means normally open).

Setting the "transistor" attribute to "pnp" inverts the logic: when IN is high, COM is connected to NO, and when IN is low / disconnected, COM is connected to NC.

---

## wokwi-hx711 Reference

**URL:** https://docs.wokwi.com/parts/wokwi-hx711

**Contents:**
- wokwi-hx711 Reference
- Pin names​
- Attributes​
  - Examples​
- Operation​
- Arduino code example​
- Automation controls​
- Simulator examples​

HX711 Load Cell Amplifier

note that E+/E-/A+/A-/B+/B- pins are non-interactive and rendered based on attributes

The HX711 amplifier allows you to easily read load cells and evaluate changes in resistance. A Wheatstone bridge is used to connect load cells to the IC, which is in turn connected to the microcontroller via VCC, DT, SCK, and GND. Use begin() to initialize the scale and set_scale() and tare() to calibrate it. power_down() and power_up() can be used to bring the ADC into and out of low power mode. get_value() and get_units() are used to read the ADC minus tare and divided, passing an optional integer value to obtain that number of values, averaged. Refer to the HX711 Arduino library for more details on features and calibration.

Note that this chip does not implement channel B or gain settings of 32/64/128. The raw readings are from 0-2100 for the "type":"5kg" type, and 0-21000 for the "type":"50kg".

Try this example on Wokwi

The HX711 can be controlled using Automation Scenarios. It exposes the following controls:

**Examples:**

Example 1 (cpp):
```cpp
#include "HX711.h"HX711 scale;void setup() {  Serial.begin(9600);  Serial.println("Initializing the scale");  scale.begin(A1, A0);}void loop() {  Serial.println(scale.get_units(), 1);  delay(1000);}
```

---

## STM32 Nucleo32 L031K6

**URL:** https://docs.wokwi.com/parts/board-st-nucleo-l031k6

**Contents:**
- STM32 Nucleo32 L031K6
  - Onboard LED​
- Simulation features​
- Simulator examples​

A Nucleo-32 development board with STM32L031K6 MCU: ARM Cortex-M0+ processor, 32 KB Flash, 8 KB RAM, 1 KB EEPROM running at 32 MHz.

The Nucleo-L031K6 has an onboard user LED (LD3), attached to GPIO pin PB3 (D13). The LED is lit when the pin is driven high.

You can also use the LED_BUILTIN constant to reference the LED in your Arduino code:

See Blink for a complete code example.

This table summarizes the current status of the STM32L031K6 MCU simulation features:

Legend: ✔️ Simulated 🟡 Partial implementation/work in progress ❌ Not implemented

**Examples:**

Example 1 (cpp):
```cpp
pinMode(LED_BUILTIN, OUTPUT);digitalWrite(LED_BUILTIN, HIGH);
```

---

## wokwi-nokia-5110-screen Reference

**URL:** https://docs.wokwi.com/parts/wokwi-nokia-5110-screen

**Contents:**
- wokwi-nokia-5110-screen Reference
- Pin names​
- Simulator examples​

The Nokia 5110 is a basic graphic LCD screen for lots of applications.

The monochrome display has an 84 x 48 pixel resolution.

The example below uses the Adafruit PCD8544 library to control the display. The library provides a simple interface for drawing text, shapes and bitmaps on the screen:

---

## wokwi-slide-potentiometer Reference

**URL:** https://docs.wokwi.com/parts/wokwi-slide-potentiometer

**Contents:**
- wokwi-slide-potentiometer Reference
- Attributes​
  - Examples​
- Simulator examples​

Sliding variable resistor (linear potentiometer)

The function and pin-out of the slide potentiometer are same as wokwi-potentiometer. Check out the wokwi-potentiometer docs for more information.

---

## wokwi-analog-joystick Reference

**URL:** https://docs.wokwi.com/parts/wokwi-analog-joystick

**Contents:**
- wokwi-analog-joystick Reference
- Pin names​
- Attributes​
- Operating the Joystick​
- Using the Joystick in Arduino​
  - Joystick Position Table​
  - Using map()​
- Automation controls​
- Simulator examples​

Analog Joystick with two axes (horizontal/vertical) and an integrated push button.

The idle position voltage is VCC/2. Moving the joystick along the vertical axis changes the voltage of the VERT pin from 0 volts (bottom) to VCC (top). Moving the joystick along the horizontal axis changes the voltages of the HORZ pin from 0 volts (right) to VCC (left).

The SEL pin is normally open (floating). Clicking on the center of the joystick shorts the SEL pin to ground. The joystick's button simulates bouncing by default. You can disable bouncing by setting the "bounce" attribute to "0".

You can operate the joystick with your mouse by moving cursor over the joystick. You'll see four arrows, corresponding to the four movement directions, and a circle in the middle. Click on one of the arrows to move the joystick shaft in that direction, and on the circle in the middle to press the joystick's push button (connected to the SEL pin).

To operate the joystick with the keyboard, first focus on it (using the tab key or by clicking on it with the mouse), then use the arrow keys to move the shaft of the joystick, and the space key to press the joystick's push button (connected to the SEL pin). It's possible to combine multiple keys at once, e.g. left arrow and top arrow, to move the shaft in a diagonal direction. You can also press on the space key while holding down the arrows to press the joystick while moving the shaft.

Partial movement and touch control are not currently supported. We'd love to see them supported though - so if you are up to the task, there's an open issue waiting for your love.

To use the Joystick in Arduino, connect the VERT and the HORZ pins to analog pins (A0...A6), and configure these pins as input. Read the joystick position using analogRead().

The following table shows the different joystick position and the corresponding HORZ / VERT values, as returned by analogRead():

You can use the map() function to re-map the values to a different range. For instance, map(analogRead(HORZ_PIN), 0, 1023, -100, 100) will return -100 when the joystick is all the way to the right, 0 when the joystick in centered, and 100 when the joystick is all the way to the left.

The joystick can be controlled using Automation Scenarios. It exposes the following controls:

**Examples:**

Example 1 (cpp):
```cpp
#define VERT_PIN A0#define HORZ_PIN A1#define SEL_PIN  2void setup() {  pinMode(VERT_PIN, INPUT);  pinMode(HORZ_PIN, INPUT);  pinMode(SEL_PIN, INPUT_PULLUP);}void loop() {  int vert = analogRead(VERT_PIN);  int horz = analogRead(HORZ_PIN);  bool selPressed = digitalRead(SEL_PIN) == LOW;  // horz goes from 0 (right) to 1023 (left)  // vert goes from 0 (bottom) to 1023 (top)  // selPressed is true is the joystick is pressed}
```

---

## STM32 Nucleo64 C031C6

**URL:** https://docs.wokwi.com/parts/board-st-nucleo-c031c6

**Contents:**
- STM32 Nucleo64 C031C6
  - Onboard LED​
- Simulation features​
- Simulator examples​

A Nucleo-64 development board with STM32C031C6 MCU: ARM Cortex-M0+ processor, 32 KB Flash, 12 KB RAM running at 48 MHz.

The Nucleo-C031C6 has an onboard user LED (LD4), attached to GPIO pin PA5 (D13). The LED is lit when the pin is driven high.

You can also use the LED_BUILTIN constant to reference the LED in your Arduino code:

See Blink for a complete code example.

This table summarizes the current status of the STM32C031C6 MCU simulation features:

Legend: ✔️ Simulated 🟡 Partial implementation/work in progress ❌ Not implemented

**Examples:**

Example 1 (cpp):
```cpp
pinMode(LED_BUILTIN, OUTPUT);digitalWrite(LED_BUILTIN, HIGH);
```

---

## wokwi-74hc595 Reference

**URL:** https://docs.wokwi.com/parts/wokwi-74hc595

**Contents:**
- wokwi-74hc595 Reference
- Pin names​
- Connecting to Arduino​
- Simulator examples​

8-bit Serial-In Parallel-Out (SIPO) Shift Register

Use the 74HC595 shift register to expand the number of output pins on your microcontroller. For input shift register (e.g. reading multiple buttons with a single input pin), please see the wokwi-74hc165.

* Use the Q7S to chain multiple 74HC595 units together. Connect Q7S to the DS pin of the next 74HC595 chip in chain.

You will need to connect at least 3 pins to your microcontroller: DS, SHCP, and STCP.

The OE pin can be used to disable the output of the shift register. If you need that functionality, connect it to your microcontroller. Otherwise, connect it to the ground to permanently enable the output.

The output pins of the shift register, Q0 through Q7, are usually connected to LEDs or a 7-segment display.

The following code example assumes that you connected DS to Arduino pin 2, SHCP to Arduino pin 3, and STCP to Arduino pin 4. It outputs an 8-bit pattern that inverts two times a second:

You can also run this example on Wokwi.

**Examples:**

Example 1 (cpp):
```cpp
const int dataPin = 2;   /* DS */const int clockPin = 3;  /* SHCP */const int latchPin = 4;  /* STCP */void setup() {  pinMode(dataPin, OUTPUT);  pinMode(clockPin, OUTPUT);  pinMode(latchPin, OUTPUT);}int pattern = 0b10101010;void loop() {  digitalWrite(latchPin, LOW);  shiftOut(dataPin, clockPin, LSBFIRST, pattern);  digitalWrite(latchPin, HIGH);  delay(500);  pattern = ~pattern; // Invert the pattern}
```

---

## wokwi-tv Reference

**URL:** https://docs.wokwi.com/parts/wokwi-tv

**Contents:**
- wokwi-tv Reference
- Pin names​
- Operation​
  - Signal timing​
- Physical TV Connection​
- Arduino code example​
- Simulator examples​

Black and White analog PAL TV screen.

The resolution of the simulated PAL TV is 768x576 pixels, and the aspect ratio is 4:3.

PAL video uses analog signal. The signal is carried over the air or using a cable. One of the common cabling standard is Composite video, which combines the pixel data together with the synchronization signals and the color data on a single wire.

Wokwi TV does not support color information, and separates the pixel data from the synchronization signals. The separation of the signals makes it easier to generate the image using a digital microcontroller.

Use the IN pin for the pixel data, and the SYNC pin for the synchronization pulses. The Arduino TVout library can drive these signals for you.

The simulator mimics the standard PAL timings for the signals at 25 frames per second. The frame are interlaced: each frame is divided into two parts, called "fields". The first field contains the odd lines, and the second field contains the even lines. Each frame takes 40ms, and each field takes 20ms (half the duration of a frame).

Each frame is divided into 625 time slots of 64uS. Each time slot contains the pixel data for a single line, but some of these lines are empty - their only use is for synchronization.

The simulator expects every field (half-frame) to start with at least one ~30uS synchronization pulse. This means you have to hold the SYNC line low for about 30uS. The PAL standard dictates a specific series of synchronization pulses, but the simulator is pretty lax: it's happy even with a single ~30uS pulse.

Each line should also start with a short, 4uS synchronization pulse. Keep the DATA signal low during these synchronization pulses.

The Logic Analyzer is very helpful in debugging the PAL TV signals.

The PAL standard uses an analog signal. When running in the simulator, you don't have to worry about this, but if you want to run your game on a physical TV, then you'd need to generate the following voltage levels:

The good news is: you only need a few resistors to convert the digital signal (that works in the simulator) to an analog one.

Composite video usually uses RCA connectors. You'd need the make the following connections to the central pin of the RCA connector:

* if you use a 3.3V board (such as the Raspberry Pi Pico), use 470Ω for SYNC and 270Ω for DATA.

Also make sure you also connect the ground to the ring of the RCA connector.

How does this work? We implement a simple voltage divider to generate the required voltages, based on the two digital pin levels:

As you can see, driving both SYNC/DATA high results in a about 1V, the white pixel level, driving SYNC high and DATA low results in about 0.3V, the black pixel level, and driving both pins low results in 0 volts, that's the sync level.

In theory, using this setup and driving DATA high while SYNC is low, you can also generate a gray pixel level (~0.65V), but this is not currently supported by the simulator.

A simple example that draws a circle using the TVout library:

**Examples:**

Example 1 (cpp):
```cpp
// Connect SYNC to Arduino pin 9, IN to Arduino pin 7#include <TVout.h>TVout TV;void setup() {  TV.begin(PAL, 120, 96);  TV.clear_screen();  TV.draw_circle(60, 48, 32, WHITE);}void loop() {}
```

---

## wokwi-ir-receiver Reference

**URL:** https://docs.wokwi.com/parts/wokwi-ir-receiver

**Contents:**
- wokwi-ir-receiver Reference
- Pin names​
- Using the receiver​
- Simulator examples​

38KHz infrared receiver

The receiver can be used in two ways:

To read the commands from your Arduino Code, you can use the IRRemote or IRMP libraries.

---

## wokwi-membrane-keypad Reference

**URL:** https://docs.wokwi.com/parts/wokwi-membrane-keypad

**Contents:**
- wokwi-membrane-keypad Reference
- Pin names​
- Attributes​
    - Arduino code example​
  - Examples​
- Simulator examples​

A standard 4x4 keypad. Great for numeric input, e.g. security pin code.

* These are just the Arduino Uno pin numbers used in the code example below. You can use any input digital input pin.

You can change the key labels as you like. The first four items in the array set the labels for the first row of keys, the next four items set the labels for the second row of keys, etc. Unicode characters are supported, so you can use special characters, accented letters, superscript/subscript (e.g. Xⁿ or A₁), and even emojis.

The example below uses the Keypad library for Arduino. The key names set in the keys array define the values that keypad.getKey() returns. They don't have to match the actual key labels (but it can be confusing if they don't), and they must contain exactly one ASCII character.

You can also try this example on Wokwi.

Tip: You can use keyboard shortcuts to activate the buttons on the keypad. Click on the keypad once (now the keypad is in focus), and you can press 0...9/A/B/C/D/#/* in the keyboard to activate the corresponding key.

**Examples:**

Example 1 (cpp):
```cpp
#include <Keypad.h>const uint8_t ROWS = 4;const uint8_t COLS = 4;char keys[ROWS][COLS] = {  { '1', '2', '3', 'A' },  { '4', '5', '6', 'B' },  { '7', '8', '9', 'C' },  { '*', '0', '#', 'D' }};uint8_t colPins[COLS] = { 5, 4, 3, 2 }; // Pins connected to C1, C2, C3, C4uint8_t rowPins[ROWS] = { 9, 8, 7, 6 }; // Pins connected to R1, R2, R3, R4Keypad keypad = Keypad(makeKeymap(keys), rowPins, colPins, ROWS, COLS);void setup() {  Serial.begin(9600);}void loop() {  char key = keypad.getKey();  if (key != NO_KEY) {    Serial.println(key);  }}
```

---

## wokwi-ir-remote Reference

**URL:** https://docs.wokwi.com/parts/wokwi-ir-remote

**Contents:**
- wokwi-ir-remote Reference
- Function keys​
- Simulator examples​

38KHz infrared remote with 20 function keys. Use together with the IR Receiver module.

The keys send infrared messages encoded using the NEC frame format. Each key sends a different command value (see the table below), and the address field is always 0.

Each key has a keyboard shortcut that actives the key while the remote is in focus.

The following table lists the NEC command, NEC encoded value and keyboard shortcut for each of the keys:

---

## wokwi-photoresistor-sensor Reference

**URL:** https://docs.wokwi.com/parts/wokwi-photoresistor-sensor

**Contents:**
- wokwi-photoresistor-sensor Reference
- Pin names​
- Attributes​
- Operation​
  - Digital output​
  - Schematics​
- Automation controls​
- Simulator examples​

Photoresistor (LDR) sensor module

The photoresistor sensor module includes a LDR (light-dependant resistor) in series with a 10K resistor. The AO pin is connected between the LDR and the 10K resistor.

The voltage on the AO pin depends on the illumination - that is the amount of light that falls on the sensor. You can read this voltage by connecting the AO pin of the photoresistor sensor to an analog input pin and then using the analogRead() function.

There are two parameters that control the sensitivity of the LDR: rl10 and gamma. rl10 is the resistance of the LDR at illumination level of 10 lux. The gamma value determines the slope of the log(R) / log(lux) graph. You can usually find these two values in the datasheet of the LDR.

The following table shows the relationship between the illumination level (lux), resistance (R), and the voltage level on the AO pin when gamma = 0.7 and rl10 = 50 (the default values):

* When VCC = 5V ** Measured one meter away from the monitor

The following code to convert the return value of analogRead() into a illumination value (in lux):

The lux variable will contain the illumination level in lux. The value of lux may be infinite (inf) when the sensor is in a very bright environment. You can use isfinite(lux) to check if the value is finite before using it, like in this example.

The digital output ("DO") pin goes high when it's dark, and low when there's light. On the physical sensor, you tweak the small on-board potentiometer to set the threshold. In the simulator, use the "threshold" attribute to set the threshold voltage. The default threshold is 2.5 volts, or about 100 lux.

The bottom LED ("DO LED") is connected to the digital output, and lights whenever the DO pin goes low. In other words, it lights when the sensor is illuminated.

The photoresistor sensor can be controlled using Automation Scenarios. The names of the controls match the names of the attributes defined above:

The following example sets the illumination to 100 lux:

**Examples:**

Example 1 (cpp):
```cpp
// These constants should match the photoresistor's "gamma" and "rl10" attributesconst float GAMMA = 0.7;const float RL10 = 50;// Convert the analog value into lux value:int analogValue = analogRead(A0);float voltage = analogValue / 1024. * 5;float resistance = 2000 * voltage / (1 - voltage / 5);float lux = pow(RL10 * 1e3 * pow(10, GAMMA) / resistance, (1 / GAMMA));
```

Example 2 (yaml):
```yaml
- set-control:      part-id: photoresistor1      control: lux      value: 100
```

---

## wokwi-led-bar-graph Reference

**URL:** https://docs.wokwi.com/parts/wokwi-led-bar-graph

**Contents:**
- wokwi-led-bar-graph Reference
- Pin names​
- Attributes​
  - Examples​
- Simulator examples​

10-segment LED Bar Graph.

e.g. A1 is the anode of the top LED, and C1 is the cathode of the top LED.

* GYR means Green-Yellow-Red. BCYR means Cyan-Blue-Yellow-Red

---

## wokwi-biaxial-stepper Reference

**URL:** https://docs.wokwi.com/parts/wokwi-biaxial-stepper

**Contents:**
- wokwi-biaxial-stepper Reference
- Pin names​
- Attributes​
  - Examples​
- Using the biaxial stepper motor​
- Simulator examples​

A concentric biaxial stepper motor, containing two stepper motors packaged in a single enclosure.

The biaxial stepper motor is made of two individual stepper motors. Check out the wokwi-stepper-motor and wokwi-a4988 documentation for more information about using stepper motors and their simulation behavior.

---

## wokwi-lcd1602 Reference

**URL:** https://docs.wokwi.com/parts/wokwi-lcd1602

**Contents:**
- wokwi-lcd1602 Reference
- Pin names​
  - I2C configuration​
  - Standard configuration​
    - Arduino code example​
- Attributes​
  - Examples​
- Font​
  - A00 variant​
  - A02 variant​

An LCD with 2 lines, 16 characters per line.

The LCD1602 comes in 2 possible configurations: I2C configuration and standard configuration. The I2C configuration is usually simpler to use.

The following table summarizes the key differences:

* Controlling the backlight requires another I/O pin.

You can select the desired configuration by setting the pins attribute. Set it to "i2c" for the I2C configuration, or "full" for the standard configuration (the default).

The default I2C address of the LCD1602 module is 0x27. You can change the address by setting the i2cAddress attribute.

Note: The I2C configuration simulates a PCF8574T chip that controls the LCD module. Normally, you wouldn't have to worry about this as the LiquidCrystal_I2C library takes care of the communication with the chip.

* These are just example pin numbers, they are not mandatory. You need can use any digital/analog pin, but make sure to update the code accordingly! † Normally, you'd configure the chip in 4-bit parallel mode, which means you only need to connect RS, E, D4, D5, D6, and D7 pins to Arduino. ‡ If you need to control the backlight, connect the anode to an I/O pin. Otherwise, connect it to the supply voltage. For a real circuit, you'd also need a current-limiting resistor, but you may skip it in the simulation environment.

When you initialize the LiquidCrystal library in your code, you need to pass the pin numbers to the constructor.

The following example uses pin numbers that match the table above:

You can also try this example on Wokwi.

The LCD1602 uses the Hitachi HD44780 LCD Controller chip. The chip comes with a built-in font, as well as the ability to define up to 8 custom characters.

There are two versions of the chip's ROM with two different fonts: HD44780UA00, which includes Japanese katakana characters, and HD44780UA02, which includes Western European characters.

Wokwi simulates the HD44780UA00 variant by default, but you can switch to the HD44780UA02 variant by setting the variant attribute to "A02".

The HD44780UA00 font has 256 characters, with the following ranges:

ASCII character glyphs:

High characters glyphs:

The HD44780UA02 font has 256 characters, with the following ranges:

ASCII character glyphs:

High characters glyphs:

You can define custom characters using the createChar method of the LiquidCrystal (or LiquidCrystal_I2C) library. The custom characters are the first 8 characters in the font, with indexes from 0 to 7. You can print them to the LCD display using the write() method, or using C string escape sequence, such as "\x07".

The following code example defines a heart shaped character, stores it at index 3, and then uses it to display the text "I (heart) Arduino":

You can also run this example on Wokwi.

You can modify any custom character while the program is running. This method is useful for creating simple animations. For example, change loop() in the code sample above to slowly reveal the heart icon, line-by-line:

**Examples:**

Example 1 (cpp):
```cpp
#include <LiquidCrystal.h>LiquidCrystal lcd(12, 11, 10, 9, 8, 7);void setup() {  lcd.begin(16, 2);  // you can now interact with the LCD, e.g.:  lcd.print("Hello World!");}void loop() {  // ...}
```

Example 2 (cpp):
```cpp
#include <LiquidCrystal.h>LiquidCrystal lcd(12, 11, 10, 9, 8, 7);uint8_t heart[8] = {  0b00000,  0b01010,  0b11111,  0b11111,  0b11111,  0b01110,  0b00100,  0b00000,};void setup() {  lcd.createChar(3, heart);  lcd.begin(16, 2);  lcd.print("  I \x03 Arduino");}void loop() { }
```

Example 3 (cpp):
```cpp
void loop() {  uint8_t heart2[8] = {0};  for (int i = 0; i < 8; i++) {    heart2[i] = heart[i];    lcd.createChar(3, heart2);    delay(100);  }  delay(500);}
```

---

## wokwi-pushbutton-6mm Reference

**URL:** https://docs.wokwi.com/parts/wokwi-pushbutton-6mm

**Contents:**
- wokwi-pushbutton-6mm Reference

6mm Tactile Switch Button (momentary push button).

The function and pin-out of the 6mm pushbutton are same as wokwi-pushbutton. Check out the wokwi-pushbutton docs for more information.

---

## wokwi-ssd1306 Reference

**URL:** https://docs.wokwi.com/parts/wokwi-ssd1306

**Contents:**
- wokwi-ssd1306 Reference
- Pin names​
- Attributes​
- Simulator examples​

Monochrome 128x64 OLED display with I2C interface

Note: this part has been deprecated. Please use board-ssd1306 instead.

* DC, RST and CS are for SPI mode. The SSD1306 simulation only supports I2C mode, so these pins are not functional.

The default I2C address of the SSD1306 module is 0x3c (60).

---

## wokwi-logic-analyzer Reference

**URL:** https://docs.wokwi.com/parts/wokwi-logic-analyzer

**Contents:**
- wokwi-logic-analyzer Reference
- Pin names​
- Attributes​
  - Sample buffer​
  - Trigger​
- Viewing the data​
- Simulator examples​

8-Channel Digital Logic Analyzer

Pins D0 to D7 are connected to the input channels of the logic analyzer. There's also a GND pin, which should be connected to the digital ground.

The logic analyzer uses a buffer to store the recorded pin data. Each pin level change (e.g. low to high) occupies one slot in the buffer. The simulator allocates the memory for the buffer in advance, to ensure fast simulation.

You can choose the size of the buffer by setting the bufferSize attribute. Each slot in the buffer uses 9 bytes of RAM. Thus, the default buffer size of 1 million samples will use about 9 MB of RAM. Allocating a large buffer may strain your browser.

The logic analyzer displays the number of samples captured while the simulation is running. You can use this number to estimate the required buffer size.

The trigger controls when the logic analyzer starts recording data. By default, the trigger is off, so the logic analyzer captures all the data. You can configure the trigger using three attributes triggerMode, triggerPin and triggerEdge.

The following table summarizes the available trigger modes:

The "edge" mode starts recording when the triggerPin changes to triggerLevel, and continues recording until the simulation terminates. For example, if you set triggerPin to "D7" and triggerLevel to "high" (their default values), the logic analyzer will start recording when pin D7 goes high.

The "level" mode is more versatile: just like the "edge" mode, it starts recording when the triggerPin changes to triggerLevel, but it will pause the recording as soon as triggerPin changes again.

For usage examples, check out the Using the Trigger section in the Logic Analyzer Guide.

When you stop the simulation, the logic analyzer downloads a file with the recorded samples to your computer. The recording file uses the standard Value Change Dump (VCD) format. The file is called "wokwi-logic.vcd" by default, but you can configure the name using the filename attribute.

To learn how to view the data, please visit our Logic Analyzer Guide.

---

## wokwi-nlsf595 Reference

**URL:** https://docs.wokwi.com/parts/wokwi-nlsf595

**Contents:**
- wokwi-nlsf595 Reference
- Pin names​
- Using the NLSF595​
- Simulator examples​

Serial (SPI) Tri-Color LED Driver

Use the NLSF595 shift register to connect power-hungry RGB LEDs to your microcontroller. A single unit can control two RGB LEDs, and a chain of two units can control up to five RGB LEDs.

* Use the Q7S to chain multiple NLSF595 units together. Connect SQH to the SI pin of the next NLSF595 chip in chain.

You will need to connect at least 3 pins to your microcontroller: SI, SCK, and RCK.

The OE pin can be used to disable the output of the shift register. If you need that functionality, connect it to your microcontroller. Otherwise, connect it to the ground to permanently enable the output.

The output pins of the shift register, QA through QH, are usually connected to the input pins of common-anode RGB LEDs.

---

## wokwi-ntc-temperature-sensor Reference

**URL:** https://docs.wokwi.com/parts/wokwi-ntc-temperature-sensor

**Contents:**
- wokwi-ntc-temperature-sensor Reference
- Pin names​
- Attributes​
- Reading the temperature​
- Simulator examples​

Analog temperature sensor: NTC (negative temperature coefficient) thermistor.

The temperature sensor module includes a 10K NTC thermistor in series with a 10K resistor.

This setup produces a voltage that depends on the temperature. You can read this voltage by connecting the OUT pin of the thermistor to an analog input pin and then using the analogRead() function.

Use the following code to convert the return value of analogRead() into a temperature value (in celsius):

**Examples:**

Example 1 (cpp):
```cpp
const float BETA = 3950; // should match the Beta Coefficient of the thermistorint analogValue = analogRead(A0);float celsius = 1 / (log(1 / (1023. / analogValue - 1)) / BETA + 1.0 / 298.15) - 273.15;
```

---

## wokwi-arduino-nano Reference

**URL:** https://docs.wokwi.com/parts/wokwi-arduino-nano

**Contents:**
- wokwi-arduino-nano Reference
- Differences from the Arduino Uno​

The Arduino Nano is very similar to the Arduino Uno, but in a smaller form factor. It carries the same ATmega328p chip, which has 32K bytes of Flash program memory, 2k bytes of SRAM and 1K bytes of EEPROM.

For more information, see the wokwi-arduino-uno reference.

The Arduino Nano includes two extra analog pins: A6 and A7. These pins can only be used for Analog input. They can't be used as digital GPIO pins.

---

## wokwi-attiny85 Reference

**URL:** https://docs.wokwi.com/parts/wokwi-attiny85

**Contents:**
- wokwi-attiny85 Reference
- Pin names​
- Attributes​
  - Debug prints with TinyDebug​
  - Serial Output​
  - I2C​
- Simulation features​
- Simulator examples​

The ATtiny85 is a small 8-bit AVR microcontroller. It has 8KB of Flash program memory, 512 bytes of SRAM, and 512 bytes of EEPROM.

You can use the TinyDebug library to print debug messages from your code. These messages appear in Wokwi's Serial Monitor. To use the library, include "TinyDebug.h" in your project and create a libraries.txt file with the text "TinyDebug" in it.

Call Debug.begin() and then print your debug messages using Debug.println():

Similarly, you can use the Debug object to read input from the Simulator's serial monitor:

For more information about the available methods, check out the Stream class documentation.

The Debug interface consumes ~30 bytes of SRAM and 150 bytes of Flash memory, depending on which methods you use in your code. This can sometimes be an issue, since the ATtiny85 only has 512 bytes of SRAM.

That's why TinyDebug also provides an alternative, lightweight logging interface that doesn't use any SRAM. It provides two functions, tdPrint() and tdPrintln(). The downside is that you can only print c-style (char*) strings:

The TinyDebug library works out of the box in Wokwi, without any changes to your diagram. It uses an internal debug interface that is part of the Wokwi simulation engine, and does not use any MCU pins.

You can safely run code that uses TinyDebug on a physical ATtiny85 chip. The physical chip doesn't have the debug interface, so you obviously won't see the debugging messages, but other than that it shouldn't interfere with your code.

For a complete code example, check out the TinyDebug demo project on Wokwi.

The ATtiny85 doesn't have a dedicated UART peripheral, but it it still possible to get Serial Output using the Software Serial library. For more information and demo code, please see the Serial Monitor Guide.

For I2C communication use the TinyWireM library.

The ATtiny85 is simulated using the AVR8js Library. The table below summarizes the status of features:

Legend: ✔️ Simulated 🟡 Partial support ❌ Not implemented

If you need any of the missing features, please open an issue on the AVR8js repo or reach out on Discord.

**Examples:**

Example 1 (cpp):
```cpp
#include <TinyDebug.h>void setup() {  Debug.begin();  Debug.println(F("Hello, TinyDebug!"));}void loop() {  /* Sprinkle some magic code here */}
```

Example 2 (cpp):
```cpp
if (Debug.read() == 'c') {  // Do something, e.g. toggle an LED}
```

Example 3 (cpp):
```cpp
#include <TinyDebug.h>void setup() {  tdPrintln(F("I do not use any SRAM!"));}void loop() {  /* ... */}
```

---

## wokwi-resistor Reference

**URL:** https://docs.wokwi.com/parts/wokwi-resistor

**Contents:**
- wokwi-resistor Reference
- Pin names​
- Attributes​
  - Examples​
- Simulator examples​

Wokwi only has a very basic analog circuit simulation. You won't be able to use resistors together with analog components (e.g. potentiometer or NTC temperature sensor). You can still use the resistors as external pull-up/pull-down resistors.

Check out the resistor showcase by Koepel for more examples.

---

## wokwi-stepper-motor Reference

**URL:** https://docs.wokwi.com/parts/wokwi-stepper-motor

**Contents:**
- wokwi-stepper-motor Reference
- Pin names​
- Attributes​
  - Examples​
- Using the stepper motor​
  - Simulation Behavior​
- Simulator examples​

A bipolar stepper motor

When using a stepper motor you need a driver chip that can supply large amounts of current to the motor's coils. Wokwi supports the common A4988 driver board. You can also wire the stepper motor directly to your microcontroller. Wokwi uses a digital simulation engine, so the coil current is not taken into account.

You can use a variety of Arduino libraries to control the stepper motor: Stepper, AccelStepper, etc.

The stepper motor moves 1.8 degrees per step (200 steps per revolution). The motor also supports half-stepping (0.9 degrees per step / 400 steps per revolution). You can even use smaller microsteps (e.g. 1/4 or 1/8 step), but the simulated motor only displays the angle in half-step resolution. For more information, check out the A4988 microstepping configuration table.

---

## wokwi-dht22 Reference

**URL:** https://docs.wokwi.com/parts/wokwi-dht22

**Contents:**
- wokwi-dht22 Reference
- Pin names​
- Attributes​
- Controlling the temperature​
- Simulator examples​

Digital Humidity and Temperature sensor.

You can change the temperature and humidity values while the simulation is running. Click on the DHT22 sensor and a small popup window will open. Use the temperature and humidity sliders to change the values. Click "Hide" to close the popup window.

If you are trying to read this sensor from the ESP32, use the "DHT sensor library for ESPx" library. Other DHT22 libraries may not work reliably on the ESP32. You can use this example project as a starting point.

---

## wokwi-ds1307 Reference

**URL:** https://docs.wokwi.com/parts/wokwi-ds1307

**Contents:**
- wokwi-ds1307 Reference
- Pin names​
- Attributes​
- Simulation Behavior​
- Simulator examples​

RTC (Real Time Clock) module with I2C interface and 56 bytes of NV SRAM.

The I2C address of the DS1307 is 0x68.

The simulated DS1307 is automatically initialized to the current system time when starting the simulation. It then keeps counting the time. You can override the initial time by setting the initTime attribute to a different value. The value can be either a valid ISO 8601 date string (e.g. "2019-11-19T11:41:56Z"), or one of the following special values:

Note that "Z" at the end of the date string indicates that the time is in UTC, and not in the local time zone. If you omit the "Z", the time will be interpreted as local time.

The code running in the simulation can update the date/time of the DS1307, and the DS1307 will keep track of the updated time.

---

## wokwi-buzzer Reference

**URL:** https://docs.wokwi.com/parts/wokwi-buzzer

**Contents:**
- wokwi-buzzer Reference
- Pin names​
- Attributes​
  - Operation modes​
- Arduino example​
- Simulator examples​

A piezoelectric buzzer

The buzzer can operate in two modes: "smooth" (the default) and "accurate".

"smooth" sounds better and is suitable for simple, single-frequency tones. Use it when playing a melody or playing tones with Arduino's tone() function. Complex and polyphonic sounds may not play correctly (or not play at all) in "smooth mode"

Use the "accurate" mode when you need to play complex sounds. It will accurately play the sound you feed in. However, it'll add audible click noises to your sound. These noises are due to fluctuations in the simulation speed - it's not always able to provide the complete sound buffer in real time.

Connect pin 1 of the buzzer to Arduino GND pin, and pin 2 of the buzzer to Arduino pin 8. Then use the tone() function to play a sound:

**Examples:**

Example 1 (cpp):
```cpp
tone(8, 262, 250); // Plays 262Hz tone for 0.250 seconds
```

---

## wokwi-arduino-uno Reference

**URL:** https://docs.wokwi.com/parts/wokwi-arduino-uno

**Contents:**
- wokwi-arduino-uno Reference
- Pin names​
  - On board LEDs​
- Attributes​
- Simulation features​
  - Serial Monitor​
  - Libraries​
- Simulator examples​

Arduino Uno is the most popular board in the Arduino family. It is powered by the ATmega328p chip, which has 32K bytes of Flash program memory, 2k bytes of SRAM and 1K bytes of EEPROM.

Pins 0 to 13 are digital GPIO pins. Pins A0 to A5 double as analog input pins, in addition to being digital GPIO pins.

There are three ground pins: GND.1, which is on top of the board, next to pin 13, and GND.2/GND.3, which are on the bottom.

Pins VIN / 5V are connected to the positive power supply.

Pins 3.3V / IOREF / AREF / RESET are not available in the simulation.

Digital pins 3, 5, 6, 9, 10, and 11 have hardware PWM support.

Some of the digital pins also have additional functions:

The board includes four LEDs:

In general, only the "L" LED can be controlled by the user's code. You can use the LED_BUILTIN constant to reference it from your code:

See Blink for a complete code example.

* Many Arduino libraries assume 16 MHz clock frequency. Changing the clock frequency will void your warranty!

The Arduino Uno is simulated using the AVR8js Library. The table below summarizes the status of features:

Legend: ✔️ Simulated 🟡 Simulated, but see notes ❌ Not implemented

If you need any of the missing features, please open an issue on the AVR8js repo or reach out on Discord.

You can use the Serial Monitor to receive information from your Arduino code, such as debug print. You can also use it to send information to your code, such as textual commands.

For more information and code samples, check out the Serial Monitor guide. It also explains how to configure the Serial monitor, e.g. set the line ending characters.

The simulator supports many popular Arduino libraries. For a complete list, see the Libraries guides.

**Examples:**

Example 1 (cpp):
```cpp
pinMode(LED_BUILTIN, OUTPUT);digitalWrite(LED_BUILTIN, HIGH);
```

---

## wokwi-ili9341 Reference

**URL:** https://docs.wokwi.com/parts/wokwi-ili9341

**Contents:**
- wokwi-ili9341 Reference
- Pin names​
- Attributes​
- Using in Arduino​
- Simulator examples​

Full color 240x320 2.8" LCD-TFT display with SPI interface

* The RST and backlight (LED) pins are not available in the simulation. † You connect CS and D/C to any digital Arduino pin. The pin numbers here are just an example. ‡ You can leave MISO disconnected, unless you need to read data back from the LCD.

You can use the Adafruit_ILI9341 library or the lcdgfx library to interface with the LCD display. The following code example shows basic usage with Adafruit_ILI9341. It works with the pin connections from the table above:

Run this example on Wokwi

**Examples:**

Example 1 (cpp):
```cpp
#include "SPI.h"#include "Adafruit_GFX.h"#include "Adafruit_ILI9341.h"#define TFT_DC 9#define TFT_CS 10Adafruit_ILI9341 tft = Adafruit_ILI9341(TFT_CS, TFT_DC);void setup() {  tft.begin();  tft.setCursor(26, 120);  tft.setTextColor(ILI9341_RED);  tft.setTextSize(3);  tft.println("Hello, TFT!");  tft.setCursor(20, 160);  tft.setTextColor(ILI9341_GREEN);  tft.setTextSize(2);  tft.println("I can has colors?");}void loop() { }
```

---

## wokwi-microsd-card Reference

**URL:** https://docs.wokwi.com/parts/wokwi-microsd-card

**Contents:**
- wokwi-microsd-card Reference
- Pin names​
- Filesystem​
  - Uploading binary files​
- Arduino code example​
- Simulator examples​

microSD card with SPI interface

* The CD pin is connected to ground when there's no card in the socket. In the simulator, there's always a card in the socket, so this pin is always disconnected.

When you start the simulation, Wokwi creates a FAT16 file system and attaches it to the microSD card. By default, Wokwi copies all your project files into the microSD card.

Paying users can upload custom binary files (e.g. bitmaps, sounds, etc.) to the microSD card's filesystem. After adding a microSD card to your project, you'll see a new "SD Card" tab next to the other tabs in the code editor. Click on the "Upload Files" buttons and select any files you wish to upload.

You can also upload a complete folder tree (useful if you have a physical SD card attached to your computer and you want to upload all the data from it, as-as). Click on the small arrow next to the "Upload Files" button and select "Upload complete folder". Then select the folder with the files you want to upload.

Wokwi stores the uploaded files for you, alongside with your project. Anyone who opens your project and starts the simulation will have to wait for all the micro SD card files to download before the simulation starts.

Example: microSD Card project with a custom bitmap file

The example below uses the popular SdFat Arduino library. It prints a list of all the files in the card. The code assumes the following connections:

Run this example on Wokwi

**Examples:**

Example 1 (cpp):
```cpp
#include "SdFat.h"#define SPI_SPEED SD_SCK_MHZ(4)#define CS_PIN 10SdFat sd;void setup() {  Serial.begin(115200);  if (!sd.begin(CS_PIN, SPI_SPEED)) {    if (sd.card()->errorCode()) {      Serial.println("SD initialization failed.");    } else if (sd.vol()->fatType() == 0) {      Serial.println("Can't find a valid FAT16/FAT32 partition.");    } else {      Serial.println("Can't determine error type");    }    return;  }  Serial.println("Files on card:");  Serial.println("   Size    Name");  sd.ls(LS_R | LS_SIZE);}void loop() {}
```

---

## wokwi-mpu6050 6-Axis Accel & Gyro Sensor

**URL:** https://docs.wokwi.com/parts/wokwi-mpu6050

**Contents:**
- wokwi-mpu6050 6-Axis Accel & Gyro Sensor
- Pin names​
- Attributes​
  - Units​
    - Arduino code example​
- Automation controls​
- Simulator examples​

Integrated sensor with 3-axis accelerometer, 3-axis gyroscope and a temperature sensor with I2C interface.

* These pins are not currently implemented in the simulator. If you need them, please open a request.

You normally only need to connect the VCC, GND, SCL, and SDA pins. The I2C address of the device is 0x68. You can change the address of 0x69 by connecting the AD0 pin to VCC.

All the acceleration values (x/y/z) use g-force units, where 1g = 9.80665 m/s². The gyroscope measures angular rotation and returns the number of degrees per second.

The example below uses the Adafruit MPU6050 library to read and display the acceleration values from the sensor. On Arduino Uno, connect the SDA pin to A4, and the SCL pin to A5.

Run this example on Wokwi

The mpu6050 sensor can be controlled using Automation Scenarios. The names of the controls match the names of the attributes defined above:

The following example set the temperature to 25°C:

**Examples:**

Example 1 (cpp):
```cpp
#include <Adafruit_MPU6050.h>#include <Adafruit_Sensor.h>#include <Wire.h>Adafruit_MPU6050 mpu;void setup(void) {  Serial.begin(115200);  while (!mpu.begin()) {    Serial.println("MPU6050 not connected!");    delay(1000);  }  Serial.println("MPU6050 ready!");}sensors_event_t event;void loop() {  mpu.getAccelerometerSensor()->getEvent(&event);  Serial.print("[");  Serial.print(millis());  Serial.print("] X: ");  Serial.print(event.acceleration.x);  Serial.print(", Y: ");  Serial.print(event.acceleration.y);  Serial.print(", Z: ");  Serial.print(event.acceleration.z);  Serial.println(" m/s^2");  delay(500);}
```

Example 2 (yaml):
```yaml
- set-control:      part-id: imu1      control: temperature      value: 25
```

---

## wokwi-pir-motion-sensor Reference

**URL:** https://docs.wokwi.com/parts/wokwi-pir-motion-sensor

**Contents:**
- wokwi-pir-motion-sensor Reference
- Pin names​
- Attributes​
- Using the sensor​
- Simulator examples​

Passive Infrared (PIR) motion sensor.

To trigger the PIR motion sensor:

Triggering the sensor will drive the OUT pin high for 5 seconds (delay time), and then go low again. The sensor will ignore any further input for the next 1.2 seconds (inhibit time), and then start sensing for motion again.

You can adjust the high duration of the OUT pin by setting the delayTime attribute (on a physical sensor you use a potentiometer to set the delay).

The default setting of the sensor is to retrigger: the sensor keeps checking for motion while the OUT pin is high. It will extend the delay time every time another motion event is detected. You can disable this behavior by setting the "retrigger" attribute to "0".

---

## wokwi-text Reference

**URL:** https://docs.wokwi.com/parts/wokwi-text

**Contents:**
- wokwi-text Reference
- Attributes​

A simple text element.

---

## wokwi-rgb-led Reference

**URL:** https://docs.wokwi.com/parts/wokwi-rgb-led

**Contents:**
- wokwi-rgb-led Reference
- Pin names​
- Attributes​
- Simulator examples​

5mm Red, Green and Blue (RGB) LED.

* By default, the common pin is the anode (positive). You can change it by setting the "common" attribute to "cathode".

---

## wokwi-7segment Reference

**URL:** https://docs.wokwi.com/parts/wokwi-7segment

**Contents:**
- wokwi-7segment Reference
- Pin names​
- Attributes​
  - Examples​
- Using the 7-segment display​
- Simulator examples​

Seven segment LED display

* COM is the common pin for a single digit 7-segment display. For multi digit displays, use DIG1…DIG4.

With the default common attribute setting of anode, the segment pins (A…G, DP, CLN) are connected to the cathode (negative side) of the LEDS, and the common pins (COM, DIG1…DIG4) are connected to the anode (positive side) of the LEDs. Segments are lit by driving their pins low. Setting common to cathode reverses this behavior, with the segment pins turning on when high.

The segment mapping is as follows:

And the digit mapping:

For a single digit, you'll need 8 microcontroller GPIO pins. Each pin should be connected to a single segment through a resistor, and the common pin should be connected to 5V (or GND if you are using the common cathode variant). You can spare one pin (DP) if you don't use the dot LED. Turn a segment on by driving the corresponding segment on (or HIGH for the common cathode variant).

For multiple digits, you'll need 8 microcontroller pins for the segments and the dot plus one extra microcontroller pin for each digit. So if you have 4 digits, you'll need 12 microcontroller pins in total. Controlling the display in this mode is a bit tricky, as you'll need to continuously alternate between the different digits.

Luckily, there are libraries that can help:

If you are out of microcontroller pins, consider using a 74HC595 Shift Register to drive the display.

---

## wokwi-lcd2004 Reference

**URL:** https://docs.wokwi.com/parts/wokwi-lcd2004

**Contents:**
- wokwi-lcd2004 Reference
  - Examples​
- Simulator examples​

An LCD display with 4 lines, 20 characters per line.

This part has the same pins and attributes as the wokwi-lcd1602.

For complete information and code examples, please see the wokwi-lcd1602 reference.

---

## ks2e-m-dc5 Relay Reference

**URL:** https://docs.wokwi.com/parts/wokwi-ks2e-m-dc5

**Contents:**
- ks2e-m-dc5 Relay Reference
- Pin names​
- Operation​
- Simulator Examples​

Double Pole Double Throw (DPDT) Relay

The relay is an electronic switch with two states: coil unpowered, and coil powered. By default, the coil is unpowered. You can power the coil by applying voltage between the pins COIL1 and COIL2.

When the coil is unpowered, P1 is connected to NC1, and P2 is connected to NC2 (NC means normally closed/connected).

When the coil is powered, P1 is connected to NO1, and P2 is connected to NO2 (NO means normally open/disconnected).

The following diagram summarizes the states of the relay:

---

## wokwi-arduino-mega Reference

**URL:** https://docs.wokwi.com/parts/wokwi-arduino-mega

**Contents:**
- wokwi-arduino-mega Reference
- Pin names​
  - On board LEDs​
- Simulation features​
  - Serial Monitor​
  - Libraries​
- Simulator examples​

Arduino Mega 2560. Powered by the ATmega2560 chip, which has 256K bytes of Flash program memory, 8k bytes of SRAM and 4K bytes of EEPROM. The board features 54 digital pins, 16 analog input pins, and 4 serial ports. It runs at 16MHz.

Pins 0 to 53 are digital GPIO pins. Pins A0 to A15 double as analog input pins, in addition to being digital GPIO pins.

There are five ground pins: GND.1 (next to pin 13), GND.2/GND.3 (next to the Vin pin), and GND.4/GND.5 (at the bottom of the dual-row female header connector)

Pins VIN / 5V are connected to the positive power supply. There are also two additional power supply pins, 5V.1/5V.2, at the top of the dual-row female header connector.

Pins 3.3V / IOREF / AREF / RESET are not available in the simulation.

Digital pins 2 … 13, 44, 45, and 46 have hardware PWM support (total of 15 PWM channels).

Some of the digital pins also have additional functions:

The board includes four LEDs:

In general, only the "L" LED can be controlled by the user's code. You can use the LED_BUILTIN constant to reference it from your code:

See Blink for a complete code example.

The Arduino Mega 2560 is simulated using the AVR8js Library. The table below summarizes the status of features:

Legend: ✔️ Simulated 🟡 Simulated, but see notes ❌ Not implemented

* Input Capture is not implemented in the 16-bit timers.

If you need any of the missing features, please open an issue on the AVR8js repo or reach out on Discord.

You can use the Serial Monitor to receive information from your Arduino code, such as debug print. You can also use it to send information to your code, such as textual commands.

For more information and code samples, check out the Serial Monitor guide. It also explains how to connect the serial monitor to a different pin (e.g. to Serial2 instead of Serial), and how to configure the line ending characters.

The simulator supports many popular Arduino libraries. For a complete list, see the Libraries guides.

**Examples:**

Example 1 (cpp):
```cpp
pinMode(LED_BUILTIN, OUTPUT);digitalWrite(LED_BUILTIN, HIGH);
```

---
