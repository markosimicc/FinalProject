#include <Servo.h>
Servo servo;
int trigPin = 0;  //Trigger pin for HC-SR04 sensor
int echoPin = 1;  //Echo pin for HC-SR04 sensor
int backPlateButton = A0;  //Button on shelf back plate
int stockButton = A1;
int stockButtonState = 0;
int backButtonState = 0;  //Button initial value (Active high)
long duration;  //Duration time for return signal on sensor
int distance, range, minRange;
boolean stocking = false;

void setup() {
  //Serial port communication begin
  Serial.begin(9600);
  //Setting the pin directions
  pinMode(backPlateButton, INPUT);
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  //Attach servo
  servo.attach(9);
  range = 25;
  minRange = 4;
  distance = sensorOn();
  stockButtonState = digitalRead(stockButton);
}

void loop() {
  // put your main code here, to run repeatedly:
  if(stocking = false){  //Not in restocking mode
    if(distance > minRange){  //Move items to the front of the shelf
      moveForward();
    }
    checkShelfGap();  //Always checking if there is a gap in the items on the shelf
    Serial.println(distance);
  }
  if(stockButtonState == LOW){  //Shelf is being restocked
    moveBack();
  }
  if(outsideRange(range)){
    abort;
  }
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

int convertToDistance(long _duration){
   return (int)_duration*0.0343/2;  //Convert duration to distance(cm)
}

int sensorOn(){
  digitalWrite(trigPin, LOW);
  delayMicroseconds(5);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  
  int temp = pulseIn(echoPin, HIGH);
  return convertToDistance(temp);
}

boolean outsideRange(int _range){
  if(sensorOn() > _range){
    return true;
  }
  else{
    return false;
  }
}

int distanceAfterDelay(int _delay){
  delay(_delay);
  return convertToDistance(sensorOn());
}
