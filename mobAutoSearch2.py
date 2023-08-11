import pyautogui,random
import time as tm

words = ["Mine", "Tenent", "Disapper", "Inquisitive", "Ambivalent", "Eccentric", "Euphemism", "Nostalgia", "Melancholy", "Serendipity", "Surreal", "Whimsical", "Zealot", "Quixotic", "Lethargic", "Insidious", "Inevitable", "Inscrutable", "Inexorable", "Ineffable", "Idiosyncratic", "Hubris", "Gregarious", "Furtive", "Esoteric", "Enigmatic", "Disparate", "Cryptic ", "Cap"]



confidence=0.9
searches=25
sleep=1.5

def mobileSearches():
    
    tm.sleep(1)
    # pyautogui.hotkey('ctrl','shift','i')
    # tm.sleep(2)
    try:
         
        x=pyautogui.locateOnScreen('dimentions.png',confidence=confidence)
        if x:
            x,y=(pyautogui.center(x))
            print(type(x),type(y),x,y)
            pyautogui.moveTo(x,y)
            pyautogui.click(x,y)

            for i in range(6):
                pyautogui.press("down")
            pyautogui.press("Enter")
            pyautogui.press("F5")

            for i in range(searches):
                print(f"mob dimention found search{i+1} out of {searches}")
                pyautogui.click(588,69)
                pyautogui.hotkey('ctrl',"a")
                tm.sleep(.3)
                pyautogui.press('backspace')
                pyautogui.press('backspace')
                word=random.choice(words)
                pyautogui.write(f"{i}dimention found search Blue{word}", interval=0.01)
                tm.sleep(1)
                pyautogui.press("Enter")
            pyautogui.press("Enter")

        else:
            pyautogui.hotkey('ctrl','shift','m')
            tm.sleep(2)
            x=pyautogui.locateOnScreen('dimentions.png',confidence=confidence)
            x,y=(pyautogui.center(x))
            print(type(x),type(y),x,y)
            pyautogui.moveTo(x,y)
            pyautogui.click(x,y)

            for i in range(6):
                pyautogui.press("down")
            pyautogui.press("Enter")
            pyautogui.press("F5")

            for i in range(searches):
                print(f"{i}mob dimention not found search{i+1} out of {searches}")
                pyautogui.click(588,69)
                pyautogui.hotkey('ctrl',"a")
                tm.sleep(.3)
                pyautogui.press('backspace')
                pyautogui.press('backspace')
                word=random.choice(words)
                pyautogui.write(f" dimention not found Blue{word}", interval=0.01)
                tm.sleep(1)
                pyautogui.press("Enter")
            pyautogui.press("Enter")
            print("not found, Mobile Search Failed")

        

    except:
        print('error occured')




# mobileSearches()