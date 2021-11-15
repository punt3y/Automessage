import pyautogui
import time

Messages = ["hello","wow Crezi","hora?","haina hola","wow","sS Crezi","suhhh dude!"]

time.sleep(5)

for i in range(200):
    pyautogui.typewrite(Messages[i%7])
    pyautogui.typewrite("\n")
    time.sleep(2)
