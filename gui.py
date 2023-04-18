import PySimpleGUI as sg
from main import send

sg.theme('BlueMono')
layout = [[sg.Text('Recievers', font='Arial 32')],
          [sg.Multiline(size=(400, 10), key='recievers', font='Arial 22')],
          [sg.Text('Message', font='Arial 32')],
          [sg.Multiline(size=(400, 10), key='message', font='Arial 22')],

          [sg.Button('Send', font="Arial 24"), sg.Button('Close', font="Arial 24")]]


window = sg.Window('Test', layout, size=(800, 800)).Finalize()


while True:
    event, values = window.read()
    if event in (None, 'Close Window'):
        break
    print('You entered in the textbox:')
    for x in str(values['recievers']).split():
        send(x, str(values['message']))

window.close()
