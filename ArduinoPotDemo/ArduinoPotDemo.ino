#define pot A5
int reading = 0;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

void loop() {
  reading = analogRead(pot);
  Serial.println(reading);
  delay(50);  
}
