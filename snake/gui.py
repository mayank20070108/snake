import PySimpleGUI as sg
import os
from .language import *

icon = "snake/snake.png"

def eventHandling(window):
    QT_ENTER_KEY1 = 'special 16777220'
    QT_ENTER_KEY2 = 'special 16777221'

    while(True):
        event, _ = window.read()
        if event in (sg.WIN_CLOSED, '-EXIT-'):
            return 'exit'

        if event in ('\r', QT_ENTER_KEY1, QT_ENTER_KEY2):
            elem = window.find_element_with_focus()
            if elem is not None and elem.Type == sg.ELEM_TYPE_BUTTON:       # if it's a button element, click it
                elem.Click()

        if event in ("-PLAY-"):
            window.Close()
            return 'play'

        elif event == "-SETTINGS-":
            window.Close()
            return 'settings'

        elif event == "-INFO-":
            window.Close()
            return 'info'

def info(lang):
    layout = [[sg.Text(lang['h1_controls'], font = 40, justification = 'center')],
              [sg.Text(lang['controls'])],
              [sg.Text(lang['h1_rules'], font = 40, justification = 'center')],
              [sg.Text(lang['rules'])],
              [sg.Text("___________________________", font = 40, justification = 'center')],
              [sg.Text(lang['credits'])],
              [sg.Button(lang['back'], key="-MENU-")]]

    window = sg.Window(lang['info_window'], layout, finalize=True, size=(480,350), return_keyboard_events=True, icon=icon)

    while(True):
        event, _ = window.read()
        if event == sg.WIN_CLOSED:
            break
        if event in ('\r', 'special 16777220', 'special 16777221'):
            elem = window.find_element_with_focus()
            if elem is not None and elem.Type == sg.ELEM_TYPE_BUTTON:
                elem.Click()

        if event in ("-MENU-"):
            window.Close()
            break

def exitMenu(score, personalize):
    lang = languages[personalize['lang']]

    layout = [[sg.Text(lang['game_over'], font = 40, justification = 'center')],
              [sg.Text(lang['your_score'].format(score)+'\n', font = 30, justification = 'center')],
              [sg.Button(lang['play_again'], key="-PLAY-")],
              [sg.Button(lang['settings'], key="-SETTINGS-"), sg.Button(lang['info'], key='-INFO-'), sg.Button(lang['exit'], key='-EXIT-')]]

    window = sg.Window(lang['exit_window'], layout, finalize=True, icon=icon,
                        element_justification='center', size=(480,210), return_keyboard_events=True)

    return eventHandling(window)

def settings(personalize):
    lang = languages[personalize['lang']]

    layout = [[sg.Text(lang['language']), sg.OptionMenu(languages.keys(), default_value=personalize['lang'], key='lang')],
              [sg.Text(lang['board_size']), sg.Slider(range=(200, 800), default_value=personalize['board_size'],
                resolution = 40, orientation='horizontal', key="board_size")],
              [sg.Text(lang['food_quantity']), sg.Slider(range=(1, 10), default_value=personalize['food'],
                resolution = 1, orientation='horizontal', key="food")],
              [sg.Text(lang['speed']), sg.OptionMenu(lang['speeds'], default_value=lang['speeds'][personalize['speed']-1], key="speed")],
              [sg.Checkbox(lang['speed_increase'], default=personalize['speed_increase'], key='speed_increase'),
                sg.Checkbox(lang['wall_die'], default=personalize['wall_die'], key='wall_die')],
              [sg.Checkbox(lang['show_score'], default=personalize['show_score'], key="show_score")],
              [sg.Button(lang['save'], key="-MENU-")]]

    window = sg.Window(lang['settings_window'], layout, finalize=True, size=(480,280), return_keyboard_events=True, icon=icon)

    while(True):
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            return(personalize)

        if event in ('\r', 'special 16777220', 'special 16777221'):
            elem = window.find_element_with_focus()
            if elem is not None and elem.Type == sg.ELEM_TYPE_BUTTON:
                elem.Click()

        if event == "-MENU-":
            window.Close()
            values['speed'] = lang['speeds'].index(values['speed'])+1
            return(values)

def mainMenu(lang):
    sg.theme('Light Blue 3')
    layout = [[sg.Text(lang['welcome'], font = 40)],
             [sg.Button(lang['start'], key="-PLAY-")],
             [sg.Button(lang['settings'], key="-SETTINGS-"), sg.Button(lang['info'], key='-INFO-'), sg.Button(lang['exit'], key='-EXIT-')]]

    window = sg.Window(lang['menu_window'], layout, finalize=True, icon=icon,
                        element_justification='center', size=(480,200), return_keyboard_events=True)

    return eventHandling(window)


if __name__ == '__main__':
    main()
