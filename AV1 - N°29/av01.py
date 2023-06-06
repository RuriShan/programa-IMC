import PySimpleGUI as sg

sg.theme('NeutralBlue')


layout = [  
  [sg.Text('IMC')],
  [sg.Push(), sg.Text('Height '), sg.Push(), sg.Input(key='-HEIGHT-', size=(10,1)), sg.Push(), sg.Push(), sg.Push()],
  [sg.Push(), sg.Text('Mass '), sg.Push(), sg.Input(key='-MASS-', size=(10,1)), sg.Push()],
  [sg.Push(), sg.Button('Calcular'), sg.Push()]
]
window = sg.Window('IMC', layout=layout, font='Monaco 18', element_justification='center')


while True:
  event, value = window.read()
  massa = float(value['-MASS-'])
  altura = float(value['-HEIGHT-'])
  imc = massa/(altura**2)
  
  if event == 'Calcular':
    sg.popup(f'seu imc é {imc:.2f}', font='monaco 18')
  if event == sg.WIN_CLOSED or event == 'Sair':
    break
window.close()