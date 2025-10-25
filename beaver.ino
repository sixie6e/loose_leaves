const int led = 6
const int pir = 7
const int spk = 8
void setup() {
  pinMode(pir, INPUT);
  pinMode(LED_BUILTIN, OUTPUT);
  pinMode(spk, OUTPUT);
  Serial.begin(9600);
  sensors.begin();
}
void loop() {
  if (digitalRead(pir)) {
	  int totalseconds = millis() / 1000;
	  int seconds = totalseconds % 60;
	  int mins = totalseconds / 60;
	  Serial.print(mins);
	  Serial.print(":");
	  if (seconds < 10) Serial.print("0");
	  Serial.print(seconds);
	  Serial.print("\tANIMAL DETECTED");
	  digitalWrite(led, HIGH);
	  digitalWrite(spk, HIGH);
	  delay(10000);}
  else {
	  continue;}
}
