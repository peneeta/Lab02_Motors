//Cytron DC motor 

//define pins
const int pin_A = 7; //direction pin 1 
const int pin_B = 8; //direction pin 2
const int PWM = 9; //must be a PWM compatible (Pulse Width Modulation)

const int ENC_A = 2; //interrupt pin on UNO
const int ENC_B = 4; //any digital pin

volatile long encoderCount = 0;

void InterruptSequence() {
  // Runs automatically when A goes from Low to High. 
  // If B is HIGH when A rises, one direction; else the other
  if (digitalRead(ENC_B) == HIGH) encoderCount++;
  else encoderCount--;
}

//core functions
void run_CW(int speed){   //run clockwise
  digitalWrite(pin_A, HIGH);
  digitalWrite(pin_B, LOW);
  analogWrite(PWM, speed); //0-255
}
void run_CCW(int speed){  //run counterclockwise
  digitalWrite(pin_A, LOW);
  digitalWrite(pin_B, HIGH);
  analogWrite(PWM, speed); //0-255
}

void stop_Motor(){  //brake
  digitalWrite(pin_A, LOW);
  digitalWrite(pin_B, LOW);
  analogWrite(PWM, 0); //0-255
}


void setup(){
  Serial.begin(115200);

  pinMode(pin_A, OUTPUT);
  pinMode(pin_B, OUTPUT);
  pinMode(PWM, OUTPUT);

  pinMode(ENC_A, INPUT_PULLUP);
  pinMode(ENC_B, INPUT_PULLUP);

  attachInterrupt(digitalPinToInterrupt(ENC_A), InterruptSequence, RISING);

  stop_Motor();
  delay(500);
}



void loop() {
   encoderCount = 0;
  Serial.println("Run Clockwise");
  run_CW(180);
  delay(2000);
  stop_Motor();
  Serial.println("Count After Clockwise:");
  Serial.println(encoderCount);

  delay(1000);

  encoderCount = 0;
  Serial.println("Run Counterclockwise");
  run_CCW(180);
  delay(2000);
  stop_Motor();
  Serial.println("Count After Going Counterclockwise:");
  Serial.println(encoderCount);

  Serial.println("Completed");
  while (true){ 
    delay(1000);
  }


}
