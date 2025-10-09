const int tiltPin = 2; 
const int ledPin = 13; 
// motorpins 

void setup() {
  pinMode(tiltPin, INPUT);
  pinMode(ledPin, OUTPUT);
  // set motor pins as OUTPUT
}

void loop() {
  // read tilt state
  int tiltState = digitalRead(tiltPin);
  if (tiltState == HIGH) { 
	  // motor
    digitalWrite(ledPin, HIGH);
    // stop motors
  } else {
    // upright/stable, do nothing
    digitalWrite(ledPin, LOW); 
    // motor functions
  }
  // delay(10);
}
