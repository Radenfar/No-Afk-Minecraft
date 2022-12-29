import pyautogui as pag
import time
import keyboard

print("Enter anything to begin.")
time_input = input("-: ")
print("-"*20)
print("You have 5 seconds to prepare")
time.sleep(5)
while True:
    pag.press('w')
    pag.press('space')
    time.sleep(1)
    pag.press('s')
    pag.press('space')
    if keyboard.is_pressed('q'):
        break
print('Done.')
