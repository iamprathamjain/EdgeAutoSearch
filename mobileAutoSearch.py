import pyautogui,random
import time as tm

words = ["Mine", "Tenent", "Disapper", "Inquisitive", "Ambivalent", "Eccentric", "Euphemism", "Nostalgia", "Melancholy", "Serendipity", "Surreal", "Whimsical", "Zealot", "Quixotic", "Lethargic", "Insidious", "Inevitable", "Inscrutable", "Inexorable", "Ineffable", "Idiosyncratic", "Hubris", "Gregarious", "Furtive", "Esoteric", "Enigmatic", "Disparate", "Cryptic ", "Cap"]

confidence=0.9
searches=25
sleep=1.5



def mobileSearches(c,n):
    
    tm.sleep(1)
    # pyautogui.hotkey('ctrl','shift','i')
    # tm.sleep(2)
    try:
        
        
        x=pyautogui.locateOnScreen('aa.png',confidence=c)
        if x:
            x,y=(pyautogui.center(x))
            print(type(x),type(y),x,y)
            pyautogui.moveTo(x,y)
            pix = pyautogui.pixel(int(x),int(y))
            print(pix[0],pix[1],pix[2])
            if pix[0]==99 and pix[1]==129 and pix[2]==153:
                print("blue")

                dimentions=pyautogui.locateOnScreen('dimentions.png',confidence=c)
                dim_x,dim_y=(pyautogui.center(dimentions))
                print(dimentions,"dimentions",dim_x,dim_y)

                pyautogui.click(dim_x,dim_y)

                for i in range(6):
                    pyautogui.press("down")
                pyautogui.press("Enter")
                pyautogui.press("F5")

                for i in range(n):
                    print(f"mob blue search{i+1} out of {n}")
                    pyautogui.click(588,69)
                    pyautogui.hotkey('ctrl',"a")
                    tm.sleep(.3)
                    pyautogui.press('backspace')
                    pyautogui.press('backspace')
                    word=random.choice(words)
                    pyautogui.write(f"Blue{word}", interval=0.01)
                    tm.sleep(1)
                    pyautogui.press("Enter")
                pyautogui.press("Enter")
                
                
            if pix[0]==152 and pix[1]==153 and pix[2]==155:
                print("white")
                tm.sleep(2)
                pyautogui.moveTo(x,y)
                tm.sleep(.2)
                pyautogui.click(x,y)
                # pyautogui.press('ctrl','shift','m')
                tm.sleep(1)

                dimentions=pyautogui.locateOnScreen('dimentions.png',confidence=c)
                dim_x,dim_y=(pyautogui.center(dimentions))
                print(dim_x,dim_y)
                pyautogui.moveTo(dim_x,dim_y)
                print(dimentions,"dimentions",dim_x,dim_y)

                pyautogui.click(dim_x,dim_y)

                for i in range(6):
                    pyautogui.press("down")
                pyautogui.press("Enter")
                pyautogui.press("F5")

                # pyautogui.click(588,69)
                # pyautogui.hotkey('ctrl'+"a")
                # pyautogui.press('backspace')
                
                for i in range(n):
                    print(f"mob white search{i+1} out of {n}")
                    pyautogui.click(588,69)
                    pyautogui.hotkey('ctrl',"a")
                    tm.sleep(.3)
                    pyautogui.press('backspace')
                    pyautogui.press('backspace')
                    word=random.choice(words)
                    pyautogui.write(f"white {word}", interval=0.01)
                    tm.sleep(2)
                    pyautogui.press("Enter")
                pyautogui.press("Enter")

                    
                # pyautogui.hotkey('ctrl',"shift","i")
                # pyautogui.press("F5")


                
                # mic_mag=pyautogui.locateOnScreen('micnsearch.png',confidence=0.7)
                # mic_mag_x,mic_mag_y=(pyautogui.center(mic_mag))
                # tm.sleep(1)
                # print(mic_mag_x,mic_mag_y,"mic_mag_x,mic_mag_y")
                # pyautogui.moveTo(mic_mag_x,mic_mag_y)
                # print(mic_mag_x,mic_mag_y,"mic_mag_x,mic_mag_y")

           
                

            
        else:
            print("not found, Mobile Search Failed")

        

    except:
        pass




mobileSearches(confidence,searches)