#include <Servo.h> 

// Right Motor >>> L298N >>> R3UNO
const int enA = 9; 
const int in1 = 7; 
const int in2 = 6;  

// Left Motor >>> L298N >>> R3UNO
const int enB = 10;
const int in3 = 5; 
const int in4 = 4;

// HC-SR04 >>> R3UNO
const int trigPin = A4;
const int echoPin = A5;

// SG90 >>> R3UNO
const int servoPin = 3;
Servo detectionServo;
const int servoCenter = 90; // center
const int servoLeft = 60;   // 90 - 30 = 60 degrees
const int servoRight = 120; // 90 + 30 = 120 degrees

const int speed = 200;              // base speed 0-255
const int obstacleDistance = 20;    // distance to trigger avoidance
long duration;
int distance;

void setup() {
  // L298N pins as outputs
  pinMode(enA, OUTPUT);
  pinMode(in1, OUTPUT);
  pinMode(in2, OUTPUT);
  pinMode(enB, OUTPUT);
  pinMode(in3, OUTPUT);
  pinMode(in4, OUTPUT);
  
  // HC-SR04 sensor pins
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);

  // SG90 pin
  detectionServo.attach(servoPin);
  detectionServo.write(servoCenter); // set center 90 degrees
  
  Serial.begin(9600); // for debugging
}

void loop() {
  distance = getDistance();
  Serial.print("Distance: ");
  Serial.print(distance);
  Serial.println(" cm");
  
  if (distance > obstacleDistance) {
    moveForward();
  } else {
       stopRobot();
    delay(500);
    
    int rightDistance = lookRight();
    delay(300);
    
    int leftDistance = lookLeft();
    delay(300);

    detectionServo.write(servoCenter);
    delay(300); // return to 90
    
    if (rightDistance > leftDistance) {
      turnRight();
      delay(400);
    } else if (leftDistance > rightDistance) {
      turnLeft();
      delay(400);
    } else {
      moveBackward();
      delay(500);
      turnRight(); // if no options, turn right
      delay(400);
    }
    
    moveForward();
  }
}

// L298N
void moveForward() {
  digitalWrite(in1, HIGH);
  digitalWrite(in2, LOW);
  analogWrite(enA, speed);
  
  digitalWrite(in3, HIGH);
  digitalWrite(in4, LOW);
  analogWrite(enB, speed);
}

void moveBackward() {
  digitalWrite(in1, LOW);
  digitalWrite(in2, HIGH);
  analogWrite(enA, speed);
  
  digitalWrite(in3, LOW);
  digitalWrite(in4, HIGH);
  analogWrite(enB, speed);
}

void turnRight() {
  digitalWrite(in1, HIGH);
  digitalWrite(in2, LOW);
  analogWrite(enA, speed);
  
  digitalWrite(in3, LOW);
  digitalWrite(in4, HIGH);
  analogWrite(enB, speed);
}

void turnLeft() {
  digitalWrite(in1, LOW);
  digitalWrite(in2, HIGH);
  analogWrite(enA, speed);
  
  digitalWrite(in3, HIGH);
  digitalWrite(in4, LOW);
  analogWrite(enB, speed);
}

void stopRobot() {
  digitalWrite(in1, LOW);
  digitalWrite(in2, LOW);
  digitalWrite(in3, LOW);
  digitalWrite(in4, LOW);
}

// HC-SR04
int getDistance() {
  digitalWrite(trigPin, LOW); // clear pin
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  duration = pulseIn(echoPin, HIGH);
  return duration * 0.034 / 2; // distance in cm
}

int lookRight() {
  detectionServo.write(servoRight);
  delay(500); // wait for servo
  int distance = getDistance();
  Serial.print("Right Distance: ");
  Serial.println(distance);
  return distance;
}

int lookLeft() {
  detectionServo.write(servoLeft);
  delay(500); // wait for servo
  int distance = getDistance();
  Serial.print("Left Distance: ");
  Serial.println(distance);
  return distance;
}
