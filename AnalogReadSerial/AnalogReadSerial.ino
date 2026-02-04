#include <Stepper.h>
#include <Wire.h>
#include <Adafruit_MotorShield.h>
#include <Servo.h>

const int trigPin = 9;
const int echoPin = 10;
const int lightPin = A0;
const int potPin = A1;

const int stepsPerRevolution = 2048;
const int rpm = 5;
const float light_threashold = 500;

float duration, distance;

Servo servo;
Adafruit_MotorShield AFMS = Adafruit_MotorShield();
Adafruit_DCMotor *motor = AFMS.getMotor(2);
Stepper stepper(stepsPerRevolution, 3, 5, 4, 6);

// selection of sensor or GUI
enum ControlMode {
  SENSOR_MODE,
  GUI_MODE
};

ControlMode currentMode = SENSOR_MODE;

void setup() {
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  pinMode(lightPin, INPUT);
  pinMode(potPin, INPUT);
  pinMode(3, OUTPUT);
  pinMode(4, OUTPUT);
  pinMode(5, OUTPUT);
  pinMode(6, OUTPUT);

  servo.attach(9);
  Serial.begin(9600);
  Serial.setTimeout(10);
  AFMS.begin();
  stepper.setSpeed(rpm);
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

void setDC(int speed) {
  motor->setSpeed(speed);
  motor->run(FORWARD);
}

void setMotors() {
  if (Serial.available() == 0) {
    return;
  }

  // use char identifiers (see motor_comm.py)
  char motorID = Serial.read();

  // set each motor individually depending on packet
  if (motorID == 'M') {
    int mode = Serial.parseInt();
    currentMode = (mode == 0)? SENSOR_MODE : GUI_MODE;
  }
  else if (motorID == 'S') {
    // Servo command
    int angle = Serial.parseInt();
    servo.write(angle);

  }
  else if (motorID == 'D') {
    // DC Motor command
    int speed = Serial.parseInt();
    setDC(speed);
  }
  else if (motorID == 'T') {
    // Stepper command
    int steps = Serial.parseInt();
    stepper.step(steps);
  }
}

void loop() {
  int pot = getPot();
  float light = getLight();
  float distance = getDistance();

  // print sensor data 
  Serial.print(pot);
  Serial.print(",");
  Serial.print(light);
  Serial.print(",");
  Serial.print(distance);
  Serial.print("\n");

  // check if GUI or Sensor mode
  setMotors();

  if (currentMode == SENSOR_MODE){
    // update servo
    servo.write(distance * 10);
    int dc = pot / (1023 / 255);
    setDC(dc);

    // update dc

    // update stepper
  }
  

  delay(100);
}




