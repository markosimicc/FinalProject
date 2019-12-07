#include <Servo.h>
#include <LiquidCrystal.h>

//Setup the distance sensor
int trigPin = 10;
int echoPin = 13;
long duration;
float indexCount = 600.0;

//Setup the backplate sensors
int backPlateButtonPin = A2;
int stockButtonPin = A1;

//Create states for the button
int stockButtonState = 0;
int backPlateButtonState = 0;

//Create flags for stocking the shelf
bool stockMode = false;
bool skipLoop = false;


String itemName = "Empty";
String itemPrice = "Empty";

//Create a max and min range
float maxRange = 20.0;
float minRange = 10.0;

//Create a variable which will hold the distance
float itemDistance;

//Create a condition for the backplate
bool stopCondition;

//Create a servo variable to control the two servos
Servo servoControl;

LiquidCrystal lcd(12, 11, 5, 4, 3, 6);

//shelfClass shelf;

void setup() {
  //Setting the pin directrions
  pinMode(backPlateButtonPin, INPUT);
  pinMode(stockButtonPin, INPUT);
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);

  servoControl.attach(9);
  lcd.begin(16, 2);

  Serial.begin(9600);
  Serial.println(1001);
  if (Serial.available() == 0) {
    while(Serial.available() == 0){
    } 
    itemName = Serial.readString();
  }
  Serial.println(1002);
  if (Serial.available() == 0) {
    while(Serial.available() == 0){
    }
    itemPrice = Serial.readString();
  }

  lcd.print(itemName);
  lcd.setCursor(0, 1);
  lcd.print(itemPrice);

}

float pollDistance() {
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);

  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  duration = pulseIn(echoPin, HIGH);
  return (duration * 0.034 / 2);
}

void loop() {
  stockButtonState = digitalRead(stockButtonPin); //Poll for the button being pressed

  //Detect that the button is pressed
  if (stockButtonState == HIGH) {

    //Enter a state of stocking mode being on
    stockMode = true;
    skipLoop = false;

    while (stockMode) {
      //Serial.println("Stocking");
      //Initial poll of backplate postition
      float itemDistance = pollDistance();
      //Move the back plate to the back of the range
      if (!skipLoop) {
        while ((indexCount < 600) && (itemDistance <= maxRange)) {
          //Serial.println((int)itemDistance);
          servoControl.write(0);
          indexCount++;
          delay(100);
          //check if the backplate is still in range before moving looping again
          itemDistance = pollDistance();
          }
          if (itemDistance >= maxRange) {
            servoControl.write(94); //In theory this is the midpoint so it should stop the servo
            skipLoop = true;
            indexCount = 600.0;
        }
      }
      //poll the stocking button again
      stockButtonState = digitalRead(stockButtonPin);

      //Create a structure that will exit the while loop
      if (stockButtonState == HIGH) {
        stockMode = false;
        delay(2000);
      }
    }
  } else {
    if (!stockMode) {
      //Poll for the item distance and if the backplate button is pressed
      //The above conditions are the tests to see if the items are pushed all the way to the front
      itemDistance = pollDistance();
      backPlateButtonState = digitalRead(backPlateButtonPin);
      stockButtonState = digitalRead(stockButtonPin);
      if (stockButtonState) {
        stockMode = true;
      }
      if (((itemDistance > minRange) || (backPlateButtonState == LOW)) && !stockMode) {
        //Push to the front
        stopCondition = (((itemDistance < minRange) && (backPlateButtonState == HIGH)) || (indexCount < 0));
        while (!stopCondition) {
          //move forward
          servoControl.write(180);
          indexCount--;
          delay(100);
          //update stop conditions
          itemDistance = pollDistance();
          backPlateButtonState = digitalRead(backPlateButtonPin);
          stockButtonState = digitalRead(stockButtonPin);
          stopCondition = (((itemDistance < minRange) && (backPlateButtonState == HIGH)) || (indexCount < 0));
          if (stopCondition) {
            servoControl.write(94); //In theory this is the midpoint so it should stop the servo
          }
          if (stockButtonState) {
            servoControl.write(94);
            stockMode = true;
            break;
          }
        }
      }

    }
    Serial.println((int)(indexCount / 6));
  }
}
