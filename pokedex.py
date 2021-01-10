import os
import sys
import PySimpleGUI as sg
from ability import damageFrom, pokeType, doubleDamageTypesPokemon, ability

# Define the window's contents
layout = [[sg.Text("Enter pokemon's name")],
          [sg.Input(size=(60, None), key='-INPUT-')],
          [sg.Text(size=(60, 1), key='-OUTPUT-')],
          [sg.Button('Get Info'), sg.Button('Quit')]]

# Create the window
window = sg.Window('Pokedex', layout)
window.read()

# Display and interact with the Window using an Event Loop
while True:
    event, values = window.read()
    # See if user wants to quit or window was closed
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break

    # See if user pressed 'Get Info' button
    if event == 'Get Info':
        os.remove('temp_output.txt')
        file = open('temp_output.txt', 'w')
        sys.stdout = file
        try:
            types = pokeType(values['-INPUT-'])
        except:
            window['-OUTPUT-'].set_size(size=(None, 1))
            window['-OUTPUT-'].update(values['-INPUT-'] + " is not a valid pokemon")
            continue

        print()
        double_damage_types = damageFrom(types)
        print()
        doubleDamageTypesPokemon(double_damage_types)
        print()
        abilities = ability(values['-INPUT-'])
        print(f'Abilities: {abilities}')
        file.close()
        sys.stdout = sys.__stdout__

        content = open('temp_output.txt').readlines()
        window['-OUTPUT-'].set_size(size=(None, len(content)))
        window['-OUTPUT-'].update(''.join(content))

# Finish up by removing from the screen
window.close()
