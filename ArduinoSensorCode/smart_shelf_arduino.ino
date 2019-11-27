#include <Servo.h>
//#include <LiquidCrystal.h>
//#include "shelfContainer.h"


//Setup the distance sensor
int trigPin = 2;
int echoPin = 3;
long duration;

//Setup the backplate sensors 
int backPlateButtonPin = A0;
int stockButtonPin = A1;

//Create states for the button
int stockButtonState = 0;
int backPlateButtonState = 0;

//Create mode for stocking the shelf 
bool stockMode = false;

//Create a max and min range
float maxRange = 15.0;
float minRange = 4.0;

//Create a variable which will hold the distance
float itemDistance;

//Create a condition for the backplate
bool stopCondition;

//Create a servo variable to control the two servos 
Servo servoControl;

//shelfClass shelf;

void setup(){
  //Setting the pin directrions
  pinMode(backPlateButtonPin, INPUT);
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);

  Serial.begin(9600);

  servoControl.attach(9);
  
}

float pollDistance(){
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);

  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  duration = pulseIn(echoPin, HIGH);
  return (duration * 0.034 / 2);
}

void loop(){
  stockButtonState = digitalRead(stockButtonPin); //Poll for the button being pressed

  //Detect that the button is pressed 
  if (stockButtonState == LOW) {
  
    //Enter a state of stocking mode being on
    stockMode = true;
    while(stockMode){
      //Initial poll of backplate postition 
      float tempPosition = pollDistance();
      //Move the back plate to the back of the range
      while(tempPosition < maxRange){
         servoControl.write(-180);
         //check if the backplate is still in range before moving looping again
         tempPosition = pollDistance();
         if(tempPosition < maxRange){
          servoControl.write(90); //In theory this is the midpoint so it should stop the servo
         }
      }
      //poll the stocking button again 
      stockButtonState = digitalRead(stockButtonPin); 

      //Create a structure that will exit the while loop 
      if (stockButtonState == LOW) {
        stockMode = false;
      }
    }
  } else {
    //Poll for the item distance and if the backplate button is pressed
    //The above conditions are the tests to see if the items are pushed all the way to the front
    itemDistance = pollDistance();
    backPlateButtonState = digitalRead(backPlateButtonPin);
    if((itemDistance != minRange) || (backPlateButtonState == HIGH)){
      //Push to the front
      stopCondition = ((itemDistance != minRange) && (backPlateButtonState == HIGH));
      while(!stopCondition){
        //move forward
        servoControl.write(180);
        //update stop conditions 
        stopCondition = ((itemDistance != minRange) && (backPlateButtonState == HIGH));
        if(stopCondition){
          servoControl.write(90); //In theory this is the midpoint so it should stop the servo
        }
      }
    }
  Serial.println(50); //temp holder until we find a way how to read from the servo
  }
}
 
