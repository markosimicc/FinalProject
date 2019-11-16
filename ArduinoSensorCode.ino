#include <Servo.h>
Servo servo;
int trigPin = 0;  //Trigger pin for HC-SR04 sensor
int echoPin = 1;  //Echo pin for HC-SR04 sensor
int backPlateButton = A0;  //Button on shelf back plate
int buttonState = 0;  //Button initial value (Active high)
long duration;  //Duration time for return signal on sensor
int distance, range;

void setup() {
  //Serial port communication begin
  Serial.begin(9600);
  //Setting the pin directions
  pinMode(backPlateButton, INPUT);
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  //Attach servo
  servo.attach(9);
}

void loop() {
  // put your main code here, to run repeatedly:

}

void checkShelfGap(){
  buttonState = digitalRead(backPlateButton);
  if(buttonState == LOW){
    if(!servo.attach(9)){
      servo.attach(9);
      Serial.print("attached");
    }
    Serial.print(distance);
    Serial.println("pressed");
    servo.write(180);;
    delay(20);
    //distance = distance +1;  //Used for testing
  }
  else{
    Serial.print("not pressed");
    servo.detach();
    Serial.println("detached");  
  }
  delay(500);
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

boolean insideRange(int _range){
  if(sensorOn() < _range){
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
