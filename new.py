import pyautogui
import time as tm 


tm.sleep(1)



bar= pyautogui.locateOnScreen('SCWI.png',confidence=0.7)
print(bar)
x,y=pyautogui.center(bar)
print(x,y)
pyautogui.moveTo(int(x),int(y))
pyautogui.moveTo(int(x),int(y)-50)
