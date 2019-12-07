# SYSC 3010: SmartShelf Project
Completed on: December 4th, 2019

SYSC 3010 The SmartShelf

							The SmartShelf 
								
Contributors:
--------------

Archit Bhatia\
Ross Matthew\
Marko Simic\
David Casciano

------------------------------------------------------------------------------------------------------------------------------

To operate the SmartShelf in similar fashion to the demo, you will need two Raspberry Pi 4's and an Arduino Uno R3. Additional hardware includes:

Electrical Components
- 2x Continuos Rotation Servo Motor
- Arduino 1602 LCD Display
- 2x Buttons

Mechanical Components
- 16x bolts
- 4x washers
- 2x 25 cm Threaded Rods 

------------------------------------------------------------------------------------------------------------------------------

Once assembled, the steps to start the smartshelf are:

1) Connect the Ardriod via serial to the Client Pi
2) Connect the Client Pi to the Server Pi via ethernet
3) Start the python server script by running:

			python JSONsandrfinal.py
			
4) Start the python client script by running:

			python SampleClient.py
			
5) Ensure that your andriod device is on the same network as the Server Pi and open the app
