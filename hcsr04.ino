// Right Motor >>> L298N
const int enA = 9; 
const int in1 = 7; 
const int in2 = 6;  

// Left Motor >>> L298N
const int enB = 10;
const int in3 = 5; 
const int in4 = 4;

// HC-SR04
const int trigPin = A4;
const int echoPin = A5;

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
    
    if (rightDistance > leftDistance) {
      // Turn right
      turnRight();
      delay(400);
    } else {
      // Turn left
      turnLeft();
      delay(400);
    }
    
    moveForward();
  }
}

// L298N Control Functions
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

// HC-SR04 Functions
int getDistance() {
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  
  duration = pulseIn(echoPin, HIGH);
  return duration * 0.034 / 2; // convert ms to cm
}

int lookRight() {
  // right forward, left reverse
  digitalWrite(in1, HIGH);
  digitalWrite(in2, LOW);
  analogWrite(enA, speed);
  
  digitalWrite(in3, LOW);
  digitalWrite(in4, HIGH);
  analogWrite(enB, speed);
  
  delay(300);
  stopRobot();
  return getDistance();
}

int lookLeft() {
  // left forward, right reverse
  digitalWrite(in1, LOW);
  digitalWrite(in2, HIGH);
  analogWrite(enA, speed);
  
  digitalWrite(in3, HIGH);
  digitalWrite(in4, LOW);
  analogWrite(enB, speed);
  
  delay(300);
  stopRobot();
  return getDistance();
}
