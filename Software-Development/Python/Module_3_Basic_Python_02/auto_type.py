import pyautogui
from time import sleep

sleep(3)

# it will write it 2 two time with 3 sec pause
for i in range(0, 3):
    pyautogui.write('Hello world!', interval=0.25) 
    pyautogui.press('enter')

