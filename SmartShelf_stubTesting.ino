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
class stubDistanceSensor:

    //Initialize the trigger, echo, and duration  
    def __init__(self, trigger, echo, duration)
    
        self.trigger = trigger 
        self.echo = echo 
        self.duration = duration

    //create a function that will return the duration
    def detectDuration(self) 
        return self.duration

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
 
class testDistanceSensor:

    //Create a stub sensor 
    sensor = stubDistanceSensor(1,2,588)

    //Create a test which will sense if the sensor is on
    def testSensorOn(self)
      assert(sensor.detectDuration > 0)

    //Create a test which will test if the sensor is within the range of the shelf
    //By testing if it is out of the range
    def testOutsideRange(float range)
      cmReading = durationToDistance(sensor.detectDuration)
      assert(cmReading > range)

    //Create a test which will test if the sensor is within the range of the shelf
    //By testing if it is reading within the range
    def testInsideRange(float range)
      cmReading = durationToDistance(sensor.detectDuration)
      assert(cmReading < range)

/*
 * 
 * Create a function which will convert the duration that the HC Sr04 distance
 * sensor measures to centimeters
 * 
 */
float durationToDistance(float duration):

  distance = duration*0.034/2
  return distance

/*
 * 
 * Create a code that will run the test with the script is run. This will then
 * output the results to the serial port where the results will be sent to the 
 * pi
 * 
 */

 shelfTest = testDistanceSensor()
 shelfTest.testSensorOn()
 shelfTest.testOutsideRange()
 shelfTest.testInsideRange()
