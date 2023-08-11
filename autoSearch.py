import pyautogui,random
import time as tm
import mobAutoSearch2
words = ["Mine", "Tenent", "Disapper", "Inquisitive", "Ambivalent", "Eccentric", "Euphemism", "Nostalgia", "Melancholy", "Serendipity", "Surreal", "Whimsical", "Zealot", "Quixotic", "Lethargic", "Insidious", "Inevitable", "Inscrutable", "Inexorable", "Ineffable", "Idiosyncratic", "Hubris", "Gregarious", "Furtive", "Esoteric", "Enigmatic", "Disparate", "Cryptic ", "Cap"]


#https://rewards.bing.com/redeem/?ref=rewardspanel
def search(num):
    tm.sleep(3)

    for i in range(num):
        print(i)
        pyautogui.click(463 ,168)
        pyautogui.hotkey('ctrl','shift','right')
        pyautogui.hotkey('ctrl','a')
        pyautogui.press('backspace')
        pyautogui.press('backspace')
        pyautogui.hotkey('ctrl','shift','left')
        pyautogui.hotkey('ctrl','a')
        pyautogui.press('backspace')
        pyautogui.press('backspace')
        
        word=random.choice(words)
        pyautogui.write(f'{word}{i}', interval=0.01)
        pyautogui.press('enter')
        tm.sleep(2)
        currentMouseX, currentMouseY = pyautogui.position()
        if currentMouseX<100:
            break



start=8
num_of_ids=9
num=3


for ii in range(num_of_ids):
    search(num)
    ###########
    
    pyautogui.hotkey('ctrl','shift',"i")
    tm.sleep(1.5)
    mobAutoSearch2.mobileSearches()
    pyautogui.hotkey('ctrl','shift',"i")
    tm.sleep(1)
    pyautogui.press('f5')
    ############
    tm.sleep(.5)
    currentMouseX, currentMouseY = pyautogui.position()
    if currentMouseX<=100:
        break
    tm.sleep(1)
    pyautogui.hotkey('ctrl', 'shift', 'm')
    for i in range(start):
        tm.sleep(.30)
        pyautogui.press('tab', interval=.05)
        currentMouseX, currentMouseY = pyautogui.position()
        if currentMouseX<=100:
            break
    pyautogui.press('enter')
    tm.sleep(1)
    start=start+1
    print('round',ii,'completed')













