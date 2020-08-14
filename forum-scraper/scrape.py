import pyautogui
import time
import random
import string


#give you time to setup automation conditions
time.sleep(10)

#define variables
#if on first page, change counter to 1\0
#every consecutive page should start at 1
#to find what tab should be, press tab on page you are scraping until the number NEXT to the current page is selected
y = 0
counter = 1
pressTab = 21
while y < 203:
    #while on new page, loop to numbers div
    for x in range (pressTab):
        pyautogui.press('tab');
        time.sleep(0.3)
    #move to the new number
    for z in range (counter):
            pyautogui.press('tab')
            time.sleep(0.3)
    #generate random file name
    name = str(random.randint(1, 99999))
    name += random.choice(string.ascii_letters)
    #save the html
    pyautogui.hotkey('ctrl', 's')
    time.sleep(2)
    pyautogui.typewrite(name)
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(3)
    counter += 1
    y += 1
    if (counter > 10):
        counter = 1



