import pandas as pd
import plyer
import playsound
import datetime
import os

def Remind(noti_title = 'no title given',noti_msg = 'no message given',noti_timeout = 10):
   playsound.playsound('./notiflication-sound.mp3')
   plyer.notification.notify(title = noti_title,message = noti_msg,timeout = noti_timeout,app_icon = './favicon-reminder.ico')

def CreateTask():
      file = open('./schedule.txt','w')
      file.write('Task Scheduled Succesfully')
      file.close()
      os.system('')
def CheckTask():
      if os.path.isfile('./schedule.txt') == False:
         CreateTask()
      else:
         pass


CheckTask()
df = pd.read_excel('./reminders.xlsx')
for index, item in df.iterrows():
   reminder_index = index
   reminder = item['Reminder']
   reminder_time = item['Time'].strftime("%I:%M %p")
   reminder_date = item['Date'].strftime("%m/%d/%Y")
   reminder_message = item['Message']
   current_time = datetime.datetime.now().strftime("%I:%M %p")
   today_date = datetime.datetime.now().strftime("%m/%d/%Y")

   if current_time == reminder_time and today_date == reminder_date:
      Remind(noti_title=reminder,noti_msg=reminder_message)
   else:
      pass
    
