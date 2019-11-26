#include <Servo.h>
Servo servo;
int trigPin = 2;  //Trigger pin for HC-SR04 sensor
int echoPin = 3;  //Echo pin for HC-SR04 sensor
int backPlateButton = A0;  //Button on shelf back plate
int stockButton = A1;
int stockButtonState = 0;
int backButtonState = 0;  //Button initial value (Active high)
long duration;  //Duration time for return signal on sensor
double distance, distanceOld, range, minRange;

void setup() {
  //Serial port communication begin
  Serial.begin(9600);
  //Setting the pin directions
  pinMode(backPlateButton, INPUT);
  pinMode(stockButton, INPUT);
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  //Attach servo
  servo.attach(9);
  range = 35.0;
  minRange = 4;
  distance = sensorOn();
  stockButtonState = digitalRead(stockButton);
}

void loop() {
  while(outsideRange(range)){   //Sensor is giving a bad reading
    servo.detach();
    delay(20);
    //Serial.println("rechecking");
  }
  //Save previous and current distance so it can be seen if there is a change which the client PI needs to know about
  distanceOld = distance;
  distance = sensorOn();

  while(stockButtonState == HIGH){  //If restocking button is being pressed
    moveBack();
  }
  
  while(distance > 15.0){  //Using 15.0 as the desired distance for testing purposes
    Serial.println("moving forward");
    moveForward();
    distance = sensorOn();
  }
  if(distance > minRange && distance < 15.0){  //Check if the backing plate has entered the "sweet spot" where we want it to be (for testing)
    Serial.println("hit");
    servo.detach();
  }
  if(distance != distanceOld){  //If the distance has changed
    Serial.println(distance); //Update the client PI
  }
  delay(500);
}

/*
 * Function to move the shelf to the back when it needs to be restocked when the restock button has been pressed
 */
void moveBack(){
  servo.attach(9);
  Serial.print("attached");  //Flag
  while(distance < range){
    Serial.print(distance);
    Serial.println("stocking");  //Flag
    servo.write(-180);
    distance = sensorOn();
  }
  if(distance >= range){
    servo.detach();
    delay(2000);
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
  //servo.writeMicroseconds(2000);
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
/*
 * Convert time response measurement from sensor to a unit
 */

int convertToDistance(long _duration){
   return (double)_duration*0.0343/2;  //Convert duration to distance(cm)
}

/*
 * Get a distance reading
 */
double sensorOn(){
  digitalWrite(trigPin, LOW);
  delayMicroseconds(5);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  
  double temp = pulseIn(echoPin, HIGH);
  return convertToDistance(temp);
}

/*
 * Check if outside of range
 */
boolean outsideRange(double _range){
  if(sensorOn() > _range){
    return true;
  }
  else{
    return false;
  }
}

//boolean insideRange(double _range){
//  if(sensorOn() < _range){
//    return true;
//  }
//  else{
//    return false;
//  }
//}

double distanceAfterDelay(double _delay){
  delay(_delay);
  return convertToDistance(sensorOn());
}
