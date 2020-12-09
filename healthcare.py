import time 
from plyer import notification

def notify(time_interval):
    notification.notify(title = 'I am Your Health Care Worker',message = 'Please Drink Water\n\nWater is Neccesary For Our Body So, Please Drink Almost 40 litre per day',app_icon = 'favicon-glass.ico',timeout = 2)
    time.sleep(time_interval)


while True:
    notify(6)
