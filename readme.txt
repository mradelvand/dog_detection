In this projects, Raspeberry Pi 3 model B has been used as main part of hardware components. we can easily program this board with python 3.7.3 and we can make interface with off-board devices easily with using GPIO.Here, We explain more about the Main code we used on raspberry pi.
List of files:
mrpiot.py: the client-side code
dependencies.yaml: defining the required modules on the Azure environment to run the server-side code
Dockerfile: defining the environment on the Azure platform
Scoring.py: the server-side code

//////////////////////////////////////////////////////////////////////////

First we import several libraries let's introduce them:
-RPi.GPIO 0.7.0 (https://pypi.org/project/RPi.GPIO/) required to set up GPIO of Rasp.
-telepot 12.7 (https://pypi.org/project/telepot/) required to set up Python framework for Telegram Bot API on Rasp.
-time (https://docs.python.org/3/library/datetime.html) required to time access
-requests 2.21.0 (https://pypi.org/project/requests/) required to provide python HTTP.
-datetime (https://docs.python.org/3/library/datetime.html) The datetime module supplies classes for manipulating dates and times
-picamera 1.13 (https://picamera.readthedocs.io/en/release-1.13/) required to setup pi camera

\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

We provide interactive API(Telegram bot) for users to receive dog images in case of detection.
 