# Jetson-Infinity-Robotic-Arm
Code Models for the Jetson Infinity Arm (xArm ESP32 Bus Servo)
# License
MIT Open Source Initiative

##### Table of Contents  
[Installation](#installation)  
[Code Modules](#modules)  

<a name="modules"/>
# Modules

#Module 3 - Surgeon:

## Module3.py

Commands such as "grab tool" , "clean tool" and "turn off medical robot" can be used to make the robotic arm do various tasks. This replicates the real world application of a surgeon doing surgery and having the robot help grab tools. 

## Module3_problem(easy).py

Problem/Challenge:
Can you make the Robot only respond to the voice commands with it's name at the start? ex: "name grab tool"
Bonus Task: write the code in a way where we can easily change the name for all the commands using one line of code

## Module3_problem(medium).py

Can you make the Robot do certain tasks using voice commands?
Tasks: grab the tool, clean the tool
Bonus Task: stop the surgery loop -> get to the last line of code that prints Surgery is Done! 


# Module 4 - API

## Pointing_Finger.py

A script that follows a finger across a screen using your computers webcam.

Problem/Challenge:
how would u scale the x and y movement to the position on the screen?


hint1: x and y coordinates on lines 112 and 113 correspond to position

hint2: do u need to pass more paramters through the movement function?

## music_api.py

Allows the user to type in a song name, code will pull the first search result from YouTube and play the first TIME seconds of that song while the robot dances. This requires 64bit VLC installed on the machine running the code, does not need to be opened just installed. 





# Module 5:

## ElectricVehicle.py

in progress. . .




<a name="installation"/>
# Installation (Linux, MacOS and Raspberry Pi)
$ sudo apt-get install python-dev libusb-1.0-0-dev libudev-dev
$ sudo pip install --upgrade setuptools
$ sudo pip install hidapi
$ sudo pip install xarm

# Software Dependencies
Python
PIP
cython-hidapi

To enable the xArm/LeArm USB interface it is necessary to add udev rules.
## Debian Linux:
  $ sudo nano /usr/lib/udev/rules.d/99-xarm.rules


## Raspbian (RPi) Linux:
  $ sudo nano /etc/udev/rules.d/99-xarm.rules


Copy this line into the file and then save and exit:
SUBSYSTEM=="usb", ATTR{idVendor}=="0483", ATTR{idProduct}=="5750", MODE="0660", GROUP="plugdev"


If after adding the udev rules you get an OSError using the open statement, perform one of the following:
Reload rules from terminal.
 $ sudo udevadm control --reload-rules && udevadm trigger


Restart the comuter.
Installation (Windows)
> pip install --upgrade setuptools
> pip install hidapi
> pip install xarm
