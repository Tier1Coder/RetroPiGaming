# Arduino Uno Gamepad

This project is a simple tutorial for creating a gamepad using an Arduino Uno and a compatible shield, tailored especially for beginners. If you're new to programming or working with hardware, this guide will walk you through the necessary steps to get your gamepad up and running.

I encountered several challenges during this project, and I hope to help others avoid the same pitfalls by sharing my experiences and solutions.

## Table of Contents

- [Hardware Setup](#hardware-setup)
- [Software Setup](#software-setup)
- [Explanation](#explanation)
- [Putting It All Together](#putting-it-all-together)
- [Notes](#notes)

## Hardware Setup

You'll need the following components:

- **Arduino UNO R3**
- **Shield with 4 buttons and a joystick** (see photo)

## Software Setup

1. **Arduino IDE**
2. **UnoJoy Library**: This library, along with the necessary files for Atmel's FLIP, can be downloaded from [this GitHub repository](https://github.com/AlanChatham/UnoJoy). Make sure to add the library to your Arduino IDE.
3. **Java Runtime Environment (JRE)**: You'll need an updated JRE to use the `TurnIntoJoystick` function from the UnoJoy folder. Without it, you might encounter the `jvm.dll` error. If updating fails, try reinstalling JRE. I recommend version `jre-8u321-windows-i586`, which you can find on Java's official site or through a quick search.

   You can verify your JRE installation by:
   1. Opening the Command Prompt (`Start > Programs > Accessories > Command Prompt`).
   2. Typing `java -version` and pressing Enter.

## Explanation

The `.ino` file provided is designed to mimic an Xbox 360 controller (originally intended for PS3 controllers, which can be found in the Example Sketches).

### Key Points:
1. **Include the UnoJoy Library**: This library is specifically created for Arduino Uno. You can find it [here](https://github.com/AlanChatham/UnoJoy).
2. **Variable Creation**: Use `uint8_t` for lower memory usage. Assign the correct variables based on the digital pins your shield uses.
3. **Analog Inputs**: `x` and `y` correspond to the analog inputs.
4. **setupPins Function**: This function checks the inputs of the digital pins, setting them to HIGH. The button is pressed when the pin is LOW (logic).
5. **Loop Function**: The `dataForController_t getControllerData` function is used to configure your inputs to behave as a joystick.
   - Use `BlankDataForController` to clean up any garbage data. This built-in UnoJoy function ensures proper conversion.
6. **Shield Configuration**: The example provided configures the shield to have buttons corresponding to triangle, circle, square, and cross, which are used for in-game actions. The `Start` button accesses the menu, and the X and Y axes are configured with a conversion using the absolute value of the Y-axis.

## Putting It All Together

1. Connect the Arduino to your computer.
2. Upload the `.ino` file containing your gamepad's code to the Arduino.
3. Use a tool (e.g., a screwdriver) to connect to the pins, entering Arduino's DFU mode.
4. Launch `TurnIntoJoystick` from the UnoJoy folder.
5. Unplug the Arduino.
6. Plug it back in with your shield attached.
7. Enjoy your new gamepad!

## Notes

1. **PC Compatibility**: This gamepad works with a PC. It is unlikely to work with consoles like the PS3 or Xbox 360 due to security chips.
2. **Configurable Setup**: You can switch between PS3 and Xbox 360 configurations (or create your own) using `if` statements in the `setup` function. For example, if button D3 is pressed when the Gamepad is turned on, it will load the first configuration; if D4 is pressed, it will load the second, and so on. However, one configuration is usually sufficient, so I haven't provided additional code for this. Feel free to adjust the pin assignments as needed.
