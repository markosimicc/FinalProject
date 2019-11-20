/*
 * 
 * Create a function which will convert the duration that the HC Sr04 distance
 * sensor measures to centimeters
 * 
 */


float durationToDistance(float duration)
{
    float distance;
    distance = duration*0.034/2;
    return distance;
}

/* 
 *  
 *Create a stub for the HC SR04 distance sensor that is provided through 
 *the Arduino kit. The HC SR04 has four pins:
 *
 *  1. 5V in
 *  2. Ground pin 
 *  3. Echo
 *  4. Trigger 
 *
 *By creating stub a stub, we can mimic the trigger and the echo of the 
 *distance sensor. The HC SR04 senses distance by measuring how long the
 *wave takes to bounce off of an object
 *
 */
class stubDistanceSensor
{

    private:
      int trigger = 1;
      int echo = 2;
      int duration = 999999;

    public:
      //create a function that will return the duration
      int detectDuration(void)
      {
        return duration;
      }
};

/*
 * 
 * Create a class which wil test the sensor with te stub created in the
 * stubDistanceSensor class above 
 * 
 * The stub will be initialized with the values
 * 
 *  trigger = 1
 *  echo = 2
 *  duration = 588
 * 
 * We chose random numbers for the echo and trigger values as they are not 
 * being used to test the distancing. For the duration we chose 588 
 * speciically because of the formaula of converting the duration to distancing:
 * 
 *                      distance = duration*0.034/2
 *                      
 * The duration value of 588 was selected because when put into the formula, 
 * the distance value is roughly 10 centimeters
 */
 
class testDistanceSensor
{
    private:  
      //Create a stub sensor 
      stubDistanceSensor sensor; 
    public:
      //Create a test which will sense if the sensor is on
      bool testSensorOn(void)
      {
        return (sensor.detectDuration() > 0);
      }
  
      //Create a test which will test if the sensor is within the range of the shelf
      //By testing if it is out of the range
      bool testOutsideRange(float range)
      {
        float cmReading;
        cmReading = durationToDistance(sensor.detectDuration());
        return ((cmReading > range) == false);
      }
        
  
      //Create a test which will test if the sensor is within the range of the shelf
      //By testing if it is reading within the range
      bool testInsideRange(float range)
      {
        float cmReading;
        cmReading = durationToDistance(sensor.detectDuration());
        return (cmReading < range);
      }
      bool testDistanceAfterDelay(int setDelay){
        float cmReading;
        cmReading = durationToDistance(sensor.detectDuration());
        float delayReading;
        delay(setDelay);
        delayReading = durationToDistance(sensor.detectDuration());
        return (cmReading == delayReading);
      }
};
        


/*
 * 
 * Create a code that will run the test with the script is run. This will then
 * output the results to the serial port where the results will be sent to the 
 * pi
 * 
 */
void setup()
{
  Serial.begin(9600); 
} 

void loop(){
  int counter = 0;
  int countFail = 0;
    
  testDistanceSensor shelfTest;
  if (shelfTest.testSensorOn())
  {
    counter++;
  } else{
    countFail++;
  }
  if (shelfTest.testOutsideRange(20))
  {
    counter++;
  } else{
    countFail++;
  }
  if (shelfTest.testInsideRange(20))
  {
    counter++;
  } else{
    countFail++;
  }
  if (shelfTest.testDistanceAfterDelay(200))
  {
    counter++;
  } else{
    countFail++;
  }
  
  Serial.print(String(counter) + " of 4 Tests passed. ");
  Serial.println(String(countFail) + " of 4 Tests failed.");
  
  for(;;){
    
  }
}
