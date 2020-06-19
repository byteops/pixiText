import pyautogui
from PIL import Image, ImageGrab
import time
import keyboard

def display():
    image = ImageGrab.grab().convert('L')  
    data = image.load()
    for i in range(95, 115):
        for j in range(145, 180):
            data[i, j] = 0;
    image.show()   
                  
character = [['1'],['2'],['3']]
time.sleep(1)
for i in character:
    pyautogui.press(i)
    pyautogui.press(i)
    image = ImageGrab.grab().convert('L')  
    data = image.load()
    black_count=0
    for j in range(95, 115):
        for k in range(135, 180):
            if data[j,k] == 0:
                black_count=black_count+1
    print(i,"=",black_count)
    pyautogui.press("backspace")
    pyautogui.press("backspace")
