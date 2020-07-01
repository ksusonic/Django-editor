import subprocess
import os
import time

process = subprocess.Popen(['python', 'manage.py', 'runserver'])
print('Запуск проекта...')
time.sleep(3)
os.system("start \"\" http://127.0.0.1:8000")
process.wait()
