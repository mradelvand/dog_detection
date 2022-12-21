import RPi.GPIO as GPIO
import telepot
import time
import requests
from picamera import PiCamera
from datetime import datetime

bot=telepot.Bot('401505656:AAEv-VB9tWZMTWesMWb3f35VsFP_ua88U9k')
chat=138722685
GPIO.setmode(GPIO.BCM)#GPIO numbering type
PIR_PIN= 21 #pin number of PIR sensor
Imagepath = '/home/pi/'
GPIO.setup(PIR_PIN,GPIO.IN)
camera = PiCamera()
print('________raspberry pi motion sensitive camera________')
print('')
print(' CLRL+C to exit ')
print('')
print(' waiting for motion')
print('_____________________________________________________')
def snap_photo():
    print('snapping...')
    print(data)
    camera.resolution =(1280,720)
    time.sleep(1)
    camera.capture(Tstamp)
    print('photo taken')
def motion_detected(PIR_PIN):
    if GPIO.input(PIR_PIN)== GPIO.HIGH:
        print('motion detected')
def sendingphoto():
    bot.sendPhoto(chat_id=chat,photo=open(Tstamp,'rb'),caption=datetime.now().strftime('%Y-%m-%d_%H-%M-%S'))

#Main code
try:
    GPIO.add_event_detect(PIR_PIN ,GPIO.RISING, callback= motion_detected)
    while 1:
        if GPIO.input(PIR_PIN)== GPIO.HIGH:
            data = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            Tstamp = Imagepath+ datetime.now().strftime('%Y-%m-%d_%H-%M-%S')+'.jpg'
            snap_photo()
            #camera.stop_preview()
            #sending photo to server
            
            files= {'image':('file',open(Tstamp, 'rb'),'application.octet-stream') }
            url= "https://cvsdep.canadaeast.inference.ml.azure.com/score"
            headers={'Authorization':"Bearer jNXNzdaHSRSVYvucugJlMKxLpDTLvvsy"}
            start = time.process_time()
            response=requests.request("POST",url,headers=headers,files=files)
            print(time.process_time() - start)
            result=response.json()['Result']
            print(result)
            if result == "It's a dog!":    
                sendingphoto()
            time.sleep(1)
        #else:
            #print('no motion')
except KeyboardInterrupt:
    print('Quit')
    camera.stop_preview()
    camera.close()
    GPIO.cleanup()
