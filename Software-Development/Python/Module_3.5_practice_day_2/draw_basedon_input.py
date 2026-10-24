
import pyautogui
import time

n = int(input())

time.sleep(5)

for i in range(1, n + 1):
    pyautogui.write("#" * i)
    pyautogui.press("enter")
