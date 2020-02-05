import speech_recognition as sr
import playsound
import pyaudio
import webbrowser
import time
import os
import random
from gtts import gTTS
from time import ctime
import pyttsx3


class TTS:
    engine = None

    def __init__(self):
        self.engine = pyttsx3.init()

    def start(self, text):
        self.engine.say(text)
        self.engine.runAndWait()


r = sr.Recognizer()


def record_audio(ask=False):
    with sr.Microphone() as source:
        if ask:
            violet_speak(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            violet_speak('Sorry, I did not get that')
        except sr.RequestError as e:
            violet_speak('Sphinx error; {0}'.format(e))
        print(voice_data)
        return voice_data


def violet_speak(audio_string):
    '''
    tts = gTTS(text=audio_string, lang='en')
    r = random.randint(1, 10000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)
    '''
    engine = pyttsx3.init()
    engine.say(audio_string)
    engine.runAndWait()


def respond(voice_data):
    if 'what is your name' in voice_data:
        violet_speak('My name is Violet')
    if 'what time is it' in voice_data:
        violet_speak(ctime())
    if 'what is the time' in voice_data:
        violet_speak(ctime())
    if 'search' in voice_data:
        search = record_audio('what do you want to search for')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        violet_speak('Here is what I found for' + search)
    if 'find location' in voice_data:
        location = record_audio('what is the location')
        url = 'https://google.nl/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        violet_speak('Here\'s the location of' + location)
    if 'exit' in voice_data:
        exit()
    if 'quit' in voice_data:
        exit()


time.sleep(1)
violet_speak('Hi, I\'m Violet. How can I help you?')
while 1:
    voice_data = record_audio()
    respond(voice_data)
