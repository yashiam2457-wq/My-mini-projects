import pyttsx3
#for windows
engine = pyttsx3.init()
volume = engine.getProperty("volume")
engine.setProperty("volume", 1.0)  
engine.setProperty("pitch",1.4)
voices= engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
engine.say("Hello sir how may i help you sir")
engine.runAndWait()
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    engine.save_to_file(audio, "test.mp3")
    engine.runAndWait()
#import os, sys
# file_path = 'AdditionalModules/'''
# sys.path.append(os.path.dirname(file_path))