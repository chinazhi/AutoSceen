
from ctypes import *
import pyautogui
import printscreen
import random

def click_exit():
    pyautogui.click(printscreen.right - 30, printscreen.top + 20, clicks=1, interval=0.0, button='left')

def click_start():
    randnum1 = random.randrange(200,300)
    randnum2 = random.randrange(240,380)
    pyautogui.click(printscreen.left + randnum1, printscreen.top + randnum2, clicks=1, interval=0.0, button='left')

def click_dati():
    pyautogui.click(printscreen.left + 150 , printscreen.bottom - 40, clicks=1, interval=0.0, button='left')  

def click_into():
    pyautogui.click(printscreen.left - 190 , printscreen.top + 240, clicks=1, interval=0.0, button='left')

def click_entrance():
    pyautogui.click(printscreen.left - 280 , printscreen.bottom - 105, clicks=1, interval=0.0, button='left')    