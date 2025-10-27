const int pir = 7;
//const int led = 6; 
const int spk = 8; 

unsigned long lastMotionTime = 0;
const unsigned long TIMEOUT_DURATION = 8000;
bool motionActive = false;

void setup() {
  Serial.begin(9600);
  pinMode(pir, INPUT);
  pinMode(LED_BUILTIN, OUTPUT);
  pinMode(spk, OUTPUT);  
  Serial.println("System state: IDLE.");
}

void loop() {
  int motionState = digitalRead(pir);
  if (motionState == HIGH) {
    if (!motionActive) {
      Serial.println("BEING DETECTED!");
      digitalWrite(led, HIGH);
      digitalWrite(spk, HIGH);
      motionActive = true;
    }
    lastMotionTime = millis();
  } 
  else {
    if (motionActive && (millis() - lastMotionTime >= TIMEOUT_DURATION)) {
      Serial.println("NO BEINGS DETECTED.");
      digitalWrite(led, LOW);
      digitalWrite(spk, LOW);
      motionActive = false;
    }
  }
}
