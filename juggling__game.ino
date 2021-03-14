const int buttonPin = 2;     // the number of the pushbutton pin
const int LEDPin = 4; // number of pin for LED
int score = 0;      // initial score 
unsigned long gameTime; // current time
bool timerSwitch = false; //allows for current time value to be captured
int currentTime = 0;//time when balls are caught 
int previousButtonState = 0;//tracks the previous state of my button
int buttonState = 0;   // variable for reading the current buttonState status

void setup() {

  Serial.begin(9600);
  // initialize the LEDPin as an output:
  // initialize the buttonPin pin as an input:
  pinMode(buttonPin, INPUT);
  pinMode(LEDPin, OUTPUT);
  
}

void loop() {
  
  gameTime = millis();//keep track of time since sketch started
  // read the state of the pushbutton value:
  buttonState = digitalRead(buttonPin); //reads current state of button either HIGH or LOW
 
 if(buttonState != previousButtonState){
  score++;//if there is a change in states from the button, add to the score(this will be checked twice so we have to divide the final score by 2 to get the actual score)
  Serial.println(score);
 }
 
  // check if the pushbutton is pressed. If it is, the buttonState is HIGH:
  if (buttonState == HIGH ) {
    timerSwitch = true;
    if(timerSwitch == true){//starts counting the current time
      currentTime = gameTime;
      timerSwitch = false; //when switch is release, the time at which is was released is saved
    }
  }
  else if ((buttonState == LOW) && ((currentTime + 3000) <= gameTime) && (score > 0)){ //if there is no circuit connection, it has been 3 seconds since the user has made a complete circuit, and the user has scored at least one point, do the following:
    
    for(int i = 0 ; i < (score/2) ; i++){//flash the LED for how many points the user has scored, wait 10 seconds, and then do it again
      Serial.println(score);
      digitalWrite(LEDPin, HIGH);
      delay(500);
      digitalWrite(LEDPin, LOW);
      delay(500);
    }
    delay(10000);
  }
  


previousButtonState = buttonState;//updating the previous button state
}
 
