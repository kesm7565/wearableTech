int motorPin = 3;
int phoneSwitch = 4;
int reading;

void setup() {
pinMode(motorPin, OUTPUT);
pinMode(phoneSwitch, INPUT);
}
void loop() {
  reading = digitalRead(phoneSwitch);
  Serial.print(reading);

   if (reading == HIGH)  //if phone is disconnected / out of pocket
   {
      digitalWrite(motorPin, HIGH);//motor vibrate
      delay(1000);//pause for one second
      digitalWrite(motorPin, LOW);
      delay(1000);
      digitalWrite(motorPin, HIGH);
      delay(1000);
      digitalWrite(motorPin, LOW);
      delay(1000);
      digitalWrite(motorPin, HIGH);
      delay(1000);
      digitalWrite(motorPin, LOW);
      delay(60000);//pause for one minute
   }
   if (reading == LOW)  //if phone is connected / in pocket...
   {
      digitalWrite(motorPin, LOW);//motor off
   }
   

}
