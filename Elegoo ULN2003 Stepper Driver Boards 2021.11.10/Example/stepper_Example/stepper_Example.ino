#include <Adafruit_MotorShield.h>

#include <Stepper.h>
#include <Servo.h>

const int stepsPerRevolution = 2048;  // change this to fit the number of steps per revolution
const int RevolutionsPerMinute = 10;  // Adjustable range of 28BYJ-48 stepper is 0~17 rpm

const int servo_pin = 10;

Servo servo;
Adafruit_MotorShield AFMS = Adafruit_MotorShield();
Adafruit_DCMotor *motor = AFMS.getMotor(1);

// initialize the stepper library on pins 8 through 11:
// Stepper stepper(stepsPerRevolution, 8, 10, 9, 11);

void setup() {
  // stepper.setSpeed(RevolutionsPerMinute);
  AFMS.begin();
  motor->setSpeed(150);
  motor->run(FORWARD);

  servo.attach(servo_pin);
}

void loop() {  
  // stepper.step(stepsPerRevolution);
  servo.write(0);
  delay(10);

  // stepper.step(-stepsPerRevolution);
  servo.write(180);
  delay(10);
}