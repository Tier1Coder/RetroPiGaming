#include "UnoJoy.h"

const uint8_t d3 = 3;
const uint8_t d4 = 4; 
const uint8_t d5 = 5;
const uint8_t d6 = 6;
const uint8_t js = 2;

uint16_t x_pin = A0;
uint16_t y_pin = A1;

void setup()
{
  setupPins();
  setupUnoJoy();
}

void loop()
{
  dataForController_t controllerData = getControllerData();
  setControllerData(controllerData);
}

void setupPins(void)
{
  pinMode(d3, INPUT);
  digitalWrite(d3, HIGH);
  pinMode(d4, INPUT);
  digitalWrite(d4, HIGH);
  pinMode(d5, INPUT);
  digitalWrite(d5, HIGH);
  pinMode(d6, INPUT);
  digitalWrite(d6, HIGH);
  pinMode(js, INPUT);
  digitalWrite(js, HIGH);
}

dataForController_t getControllerData(void)
{
  dataForController_t controllerData = getBlankDataForController();

  controllerData.triangleOn = !digitalRead(d6);
  controllerData.circleOn = !digitalRead(d5); 
  controllerData.squareOn = !digitalRead(d4);
  controllerData.crossOn = !digitalRead(d3);
  controllerData.startOn = !digitalRead(js);
 
  
  controllerData.leftStickX = analogRead(A0) >> 2;
  controllerData.leftStickY = abs((analogRead(A1) >> 2) - 255);


  return controllerData;
}
