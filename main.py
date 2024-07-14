import pyautogui
import time
time.sleep(3)
with open("msg.txt") as f:
        pyautogui.typewrite(f.read())
        pyautogui.press("enter")



