import os
import sys
import time
import subprocess
import requests

# Аргументы: новый EXE, старый EXE, версия (необязательно)
new_exe = sys.argv[1]
old_exe = sys.argv[2]

# Ссылка на version.txt в GitHub репозитории (raw)
VERSION_URL = "https://github.com/AgentZero-afk/OopLearn/releases/download/1.1.0/version.txt"

# Ждём, пока старый EXE закроется
time.sleep(2)

try:
    # Удаляем старый EXE и ставим новый
    os.remove(old_exe)
    os.rename(new_exe, old_exe)
    print("EXE обновлён!")

    # Скачиваем свежий version.txt
    r = requests.get(VERSION_URL)
    r.raise_for_status()
    with open("version.txt", "wb") as f:
        f.write(r.content)
    print("version.txt обновлён!")

    # Запускаем новый EXE
    subprocess.Popen([old_exe])
except Exception as e:
    print("Ошибка при обновлении:", e)
