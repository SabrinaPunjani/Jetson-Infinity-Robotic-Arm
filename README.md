# Jetson-Infinity-Robotic-Arm
Code Models for the Jetson Infinity Arm ( xArm ESP32 Bus Servo Robotic Arm )


# Software Dependencies
Python
PIP
cython-hidapi
# License
MIT Open Source Initiative
# Installation (Linux, MacOS and Raspberry Pi)
$ sudo apt-get install python-dev libusb-1.0-0-dev libudev-dev
$ sudo pip install --upgrade setuptools
$ sudo pip install hidapi
$ sudo pip install xarm


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
