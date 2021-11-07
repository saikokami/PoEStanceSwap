#Imports
import pyautogui
import keyboard
import winsound
import os

#var
pos=[["charBelt",0,0], ["invBelt",0,0],["returnCusor",0,0]]
freq = 200
dur = 150

#config
print("Open your inventory, hover with your mouse over the belt in your charakter slot and press space")
keyboard.wait("space")
winsound.Beep(freq, dur)
pos[0][1], pos[0][2] = pyautogui.position()
os.system('cls')

print("Open your inventory, hover with your mouse over the belt in your inventory slot and press space")
keyboard.wait("space")
winsound.Beep(freq, dur)
pos[1][1], pos[1][2] = pyautogui.position()
os.system('cls')


try:
    while True:
        print('Press "f" to swap')
        keyboard.wait("f")
        pos[2][1], pos[2][2] = pyautogui.position()
        keyboard.send('i')
        pyautogui.moveTo(pos[1][1], pos[1][2])
        pyautogui.click()
        pyautogui.moveTo(pos[0][1], pos[0][2])
        pyautogui.click()
        pyautogui.moveTo(pos[1][1], pos[1][2])
        pyautogui.click()
        keyboard.send('i')
        pyautogui.moveTo(pos[2][1], pos[2][2])


except KeyboardInterrupt:
    print('\n')
