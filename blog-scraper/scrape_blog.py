import pyautogui
import time
import random
import string


#give you time to setup automation conditions
time.sleep(20)

#define variables
#if on first page, change counter to 1\0
#every consecutive page should start at 1
#to find what tab should be, press tab on page you are scraping until the number NEXT to the current page is selected
y = 0
counter = 187
#pressTab = 76
while y < 18:
    #switch to another tab
    pyautogui.hotkey('ctrl','tab')
    time.sleep(15)
    
    #while on new page, loop to numbers div
    #for x in range (pressTab):
    #    pyautogui.press('tab');
    #    time.sleep(0.5)
    #move to the new number
    #for z in range (counter):
    #        pyautogui.press('tab')
    #        time.sleep(0.3)
    #generate random file name ending in counter
    name = str(random.randint(1, 99999))
    name += random.choice(string.ascii_letters)
    name += "_" + str(counter)
    #save the html
    #pyautogui.press('enter')
    #time.sleep(10)
    pyautogui.hotkey('ctrl', 's')
    time.sleep(5)
    pyautogui.typewrite(name)
    pyautogui.press('enter')
    time.sleep(5)
    pyautogui.press('enter')
    time.sleep(5)
    counter += 1
    y += 1
    #return to previous page
    #pyautogui.hotkey('ctrl','r')
    #time.sleep(10)
    #for x in range(4):
    #    pyautogui.press('tab')
    #    time.sleep(5)
    #pyautogui.press('enter')
    time.sleep(10)



