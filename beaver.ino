const int pir = 2;
// const int led = 6; 
const int spk = 8; 

unsigned long lastMotionTime = 0;
const unsigned long timeoutDuration = 8000;
bool motionActive = false;

void setup() {
  Serial.begin(9600);
  pinMode(pir, INPUT);
  pinMode(LED_BUILTIN, OUTPUT);
  pinMode(spk, OUTPUT);  
  Serial.println("System state: IDLE.");
}
 digitalWrite(spk, LOW);
  digitalWrite(BUILTIN_LED, LOW);


void loop() {
  int motionState = digitalRead(pir);
  if (motionState == HIGH) {
    Serial.println("BEING DETECTED!");
    digitalWrite(BUILTIN_LED, HIGH);
    digitalWrite(spk, HIGH);
    lastMotionTime = millis();
    motionDetected = true;
  }
  if (motionDetected && (millis() - lastMotionTime >= timeoutDuration)) {
    Serial.println("NO BEINGS DETECTED.");
    digitalWrite(BUILTIN_LED, LOW);
    // digitalWrite(led, LOW);
    digitalWrite(spk, LOW);
    motionDetected = false;
  }
}
