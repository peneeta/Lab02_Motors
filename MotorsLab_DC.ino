#include <Wire.h>
#include <Adafruit_MotorShield.h>
#include "utility/Adafruit_MS_PWMServoDriver.h"
#include <Servo.h>

Adafruit_MotorShield AFMS = Adafruit_MotorShield(); 
Adafruit_DCMotor *myMotor = AFMS.getMotor(2);
Servo myservo;


void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  myservo.attach(9);
  AFMS.begin();
  myMotor->setSpeed(100);
  myMotor->run(FORWARD);
}

void loop() {
  // put your main code here, to run repeatedly:
  delay(2000);
  myMotor->run(BACKWARD); // Reverse direction
  myservo.write(180);
  delay(1000);
  myservo.write(0);
  delay(1000);
  myservo.write(180);
}
