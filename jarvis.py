import speech_recognition as sr
import subprocess
import os

# r = sr.Recognizer()
# mic = sr.Microphone()
# with mic as source:
#     print(source.list_microphone_names())
#     r.adjust_for_ambient_noise(source)
#     audio = r.listen(source)
#     transcript = r.recognize_google(audio)
#     print(transcript)

def say(text):
    subprocess.call(['say', text])

def open_app(app):
    os.system('open ' +d+'/%s.app' %app.replace(' ','\ '))


d = '/Applications'
apps = list(map(lambda x: x.split('.app')[0], os.listdir(d)))

app = 'Discord'
open_app(app)
