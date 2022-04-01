# Arduino Gamepad
Creating gamepad for beginners using Arduino and Arduino's shield 

This tutorial is designed for people having issues with programming software and connecting hardware together, highly recommended for beginners. I am a person who met some issues during this little project and wanted to share it with other people.

Remember that you have to program it by your own. The pieces I use work perfectly with each other, but other parts probably need to be configurated differently.

I am using Windows 10.

SETUP (HARDWARE):
Arduino UNO R3
My shield has 4 buttons and joystick buttons (photo).

SOFTWARE:
- Arduino IDE
- UnoJoy library and whole file with Atmel's FLIP that you can download from: https://github.com/AlanChatham/UnoJoy
Remember to add library to your Arduino IDE.
- Updated JRE (Java Runtime Environment) -> it is needed for turning into Joystick and vice versa (from: UnoJoy folder). Without this we will meet jvm.dll error. Note: If you can not update you need to reinstall. 
https://www.java.com/en/download/help/error_mainclass.html
Reinstallation makes your jre updated.
Some of java installers does not work properly or they are not needed for this project (they are some kind of "exceptions" I can say). You need to find the good one, name of my file that works: jre-8u321-windows-i586, try to google it or find on java's official site.

You can also try to check if you have your java already installed by:
1) Open the command prompt. Follow the menu path Start > Programs > Accessories > Command Prompt
2) Type command: java -version and press Enter on your keyboard.




EXPLANATION:
.ino file that is designed for Xbox 360 controller (originally it is designed for PS3 controllers - I will not paste the code for PS3 because it is already in Example Sketches):
1) Include our UnoJoy library that is created for Arduino Uno. Link to the library: https://github.com/AlanChatham/UnoJoy
2) Create variables. I use uint8_t for lower memory usage. Check what kind of digital pins your shield uses and assign correct variables if you use another setup.
3) x and y are analog of course.
4) setupPins: we check the inputs of our digital pins and set them HIGH - the button is pressed when it's LOW (logic).
5) in loop we use another function that is:
6) dataForController_t getControllerData - and we configure our inputs to do some kind of operations as Joystick.
BTW. we need BlankDataForController - we might get some trash data so this built-in UnoJoy function converts it properly.
7) We can see whole configuration for my shield - I want to have triangle, circle, square and cross buttons for using items etc. in game. Start for going to the menu (otherwise that would not be possible). Then ofc X axis and Y axis. 
However we need to use some conversion with abs value with Y axis.




NOTES:
1) Gamepad works with PC. Using it with PS3 or X360 or any other console will probably not work because of some kind of security chip.
2) You can switch between PS3 and X360 configurations (or create your own) by using if statements in setup. So if the D3 button is pressed when turning on the Gamepad from USB port, we get first configuration, when D4 - second etc. however you will be happy with one setup probably so I do not share the code.
