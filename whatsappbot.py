import pyautogui
import webbrowser as wb
import time
wb.open("web.whatsapp.com")
time.sleep(60)
for i in range(150):
    pyautogui.press('2')
    pyautogui.press('0')
    pyautogui.press('2')
    pyautogui.press('2')
    pyautogui.press('enter')

    
    