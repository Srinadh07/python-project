import speech_recognition as sr 
import pyttsx3
import datetime as dt
import pywhatkit as pk
import wikipedia as wiki



#for listening 
listner = sr.Recognizer()

#for speaking
speaker = pyttsx3.init()

#for voice speed and slow rate purpose
""" RATE"""
rate = speaker.getProperty('rate')   # getting details of current speaking rate
print (rate)                        #printing current voice rate
speaker.setProperty('rate', 150)     # setting up new voice rate



def speak(text):
    speaker.say('Yes Boss,' +text)
    speaker.runAndWait()
    
def speak_ex(text):
    speaker.say(text)
    speaker.runAndWait()    

va_name = 'jarvis'

speak_ex( ' , i am your' +va_name+ ', tell me boss.')

def take_command():
  try:

     with sr.Microphone()as source:
         print('listening...')
         voice = listner.listen(source)
         command = listner.recognize_google(voice)
         command = command.lower()
         if va_name in command:
            command = command.replace(va_name + '','')
            #print(command)
            #speak(command)
        
        
  except:
        print('Check Your Microphone')       
  return command

while True:
    user_command = take_command()
   
   
    if 'close' in user_command:
        print('see you again boss. i will be there when ever you call me.')
        speak('see you agian boss. i will be there when ever you call me.')
        break
   
   
    # this is for date and time conveying
    elif 'time' in user_command:
        cur_time = dt.datetime.now().strftime("%I:%M %p") #Adding datetime command
        print(cur_time)
        speak(cur_time)
  
    # this is for playing youtube videos
    elif 'play' in user_command:
        user_command= user_command.replace('play','')
        print('playing' + user_command) 
        speak('playing' + user_command + ', enjoy boss.') 
        pk.playonyt(user_command) #Adding youtube command
        break
    
    # this is for searching or googling data
    elif 'search for' in user_command or 'google' in user_command:
        user_command= user_command.replace('search for', '') # this command helps to recognize only subject removeing other words
        user_command= user_command.replace('google', '')
        speak('searching for' +user_command)
        pk.search(user_command) 
    
    # this is for collecting and knowing data
    elif 'who is' in user_command:  
        user_command= user_command.replace('who is', '')
        info = wiki.summary(user_command,2)  
        print(info)
        speak(info)
        
    elif 'who are you'  in user_command:
        speak_ex('iam your friend' +va_name+ ',tell me boss.')   
        
    else:
        speak_ex('please say it agian boss.')    
