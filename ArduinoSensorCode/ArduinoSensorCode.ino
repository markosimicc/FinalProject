#include <Servo.h>
Servo servo;
const int trigPin = 9;  //Trigger pin for HC-SR04 sensor
const int echoPin = 10;  //Echo pin for HC-SR04 sensor
int backPlateButton = A0;  //Button on shelf back plate
int stockButton = A1;
int stockButtonState = 0;
int backButtonState = 0;  //Button initial value (Active high)
long duration;  //Duration time for return signal on sensor
int distance;
float range, minRange;
boolean stocking = false;

void setup() {
  //Setting the pin directions
  pinMode(backPlateButton, INPUT);
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  //Serial port communication begin
  Serial.begin(9600);
  //Attach servo
  servo.attach(9);
  range = 15.0;
  minRange = 4.0;
  distance = sensorOn();
  stockButtonState = digitalRead(stockButton);
}

//void loop() {
//  // put your main code here, to run repeatedly:
//  if(stocking = false){  //Not in restocking mode
//    if(distance > minRange){  //Move items to the front of the shelf
//      moveForward();
//    }
//    checkShelfGap();  //Always checking if there is a gap in the items on the shelf
//    Serial.println(distance);
//  }
//  if(stockButtonState == LOW){  //Shelf is being restocked
//    moveBack();
//  }
//  if(outsideRange(range)){
//    abort;
//  }
//}

void loop(){
  float temp = distanceAfterDelay(200);
  Serial.println(temp);
  outsideRange(range);
  insideRange(range);
  Serial.println("Completed");
  delay(3000);
}

/*
 * Function to move the shelf to the back when it needs to be restocked when the restock button has been pressed
 */
void moveBack(){
  stocking = true;
  servo.attach(9);
  Serial.print("attached");  //Flag
  while(distance < range){
    Serial.print(distance);
    Serial.println("stocking");  //Flag
    servo.write(20);;
    delay(200);
    distance = distance - 1;  //Used for testing
  }
  if(distance == range){
    delay(2000);
    stocking = false;
  }
}

/*
 * Function to move the shelf forward when required
 */
void moveForward(){
  if(!servo.attach(9)){
    servo.attach(9);
  }
  servo.write(180);
}

void checkShelfGap(){
  backButtonState = digitalRead(backPlateButton);
  if(backButtonState == LOW){
    if(!servo.attach(9)){
      servo.attach(9);
      Serial.print("attached");  //Flag
    }
    Serial.print(distance);
    Serial.println("pressed");  //Flag
    servo.write(180);;
    delay(20);
    distance = distance +1;  //Used for testing
  }
  else{
    Serial.print("not pressed");  //Flag
    servo.detach();
    Serial.println("detached");  //Flag
  }
  //delay(500);
}

float convertToDistance(long _duration){
   return (float)_duration*0.0343/2;  //Convert duration to distance(cm)
}

float sensorOn(){
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  
  float temp = pulseIn(echoPin, HIGH);
  return convertToDistance(temp);
}

boolean outsideRange(float _range){
  if(sensorOn() > _range || sensorOn() < minRange){
    Serial.println("outsideRange: Y");
    return true;
  }
  else{
    Serial.println("outsideRange: N");
    return false;
  }
}

boolean insideRange(float _range){
  if(sensorOn() < _range && sensorOn() > minRange){
    Serial.println("insideRange: Y");
    return true;
  }
  else{
    Serial.println("insideRange: N");
    return false;
  }
}

float distanceAfterDelay(int _delay){
  delay(_delay);
  return convertToDistance(sensorOn());
}
