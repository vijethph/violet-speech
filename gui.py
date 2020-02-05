import PySimpleGUI as sg
import os

sg.theme('DarkAmber')
conv = sg.Multiline("", key='conver')
string = ''

layout = [[sg.Text('Violet, a speech assistant')],
          [sg.Text('Choose the method of Speech-to text and Text-to-Speech Conversion:')],
          [sg.Radio('Online', "Radio1", default=True),
           sg.Radio('Offline', "Radio1")],
          [conv],
          [sg.Button('Start Assistant'), sg.Button('Cancel')]]

window = sg.Window('Violet Speech Assistant', layout)

while True:
    event, values = window.read()
    if event in (None, 'Cancel'):
        break
    if event in 'Start Assistant':
        os.system('python main.py')
    if values[0] is True and values[1] is False:
        string += ' Online'
        conv(string+" hello")
    if values[0] is False and values[1] is True:
        string += ' Offline'
        conv(string+" good boy")

window.close()
