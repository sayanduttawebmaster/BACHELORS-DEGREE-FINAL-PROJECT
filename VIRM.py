import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes 

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'itachi' in command:
                command = command.replace('itachi', '')
                print(command)
    except:
        pass
    return command


def run_itachi():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is ' + time)
       
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'date' in command:
        date = datetime.datetime.now().strftime('%d /%m /%Y')
        print(date)
        talk("Today’s date " + date)
       
    
    elif 'how are you' in command:
         print('I am fine, how about you')
         talk('I am fine, how about you')
        
       
        
    elif 'what is your name' in command:
        print('I am Itachi, What can I do for you?')
        talk('I am Itachi, What can I do for you?')
    
    elif 'what is your favorite food' in command:
        print('I Dont eat anything i am a bot')
        talk('I Dont eat anything i am a bot')
        
    elif 'sport' in command:
        print('football')
        talk('football')
        
    
        
        
    
        
        
    elif 'joke' in command:
        talk(pyjokes.get_joke())
        
    else:
        talk('Please say the command again.')


while True:
    run_itachi()
