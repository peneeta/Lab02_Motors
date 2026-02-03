#include <Wire.h>
#include <Adafruit_MotorShield.h>
#include <Servo.h>

const int trigPin = 9;
const int echoPin = 10;
const int lightPin = A0;
const int potPin = A1;

const float light_threashold = 500;

float duration, distance;

Servo servo;
Adafruit_MotorShield AFMS = Adafruit_MotorShield();
Adafruit_DCMotor *motor = AFMS.getMotor(2);

void setup() {
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  pinMode(lightPin, INPUT);
  pinMode(potPin, INPUT);
  servo.attach(9);
  Serial.begin(9600);
  Serial.setTimeout(10);
  AFMS.begin();
}

float getDistance() {
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  float duration = pulseIn(echoPin, HIGH);
  float distance = (duration * .0343) / 2;
  return distance;
}

float getLight() {
  float val = analogRead(lightPin);
  float R = (50000/val) + 10;
  return R;
}

int getPot() {
  return analogRead(potPin);
}

void setMotors() {
  if (Serial.available() == 0) {
    return;
  }

  int angle = Serial.parseInt();
  servo.write(angle);

  int speed = Serial.parseInt();
  motor->setSpeed(speed);
  motor->run(FORWARD);
}

void loop() {

  int pot = getPot();
  float light = getLight();
  float distance = getDistance();

  Serial.print(pot);
  Serial.print(",");
  Serial.print(light);
  Serial.print(",");
  Serial.print(distance);
  Serial.print("\n");
  setMotors();

  delay(100);
}




