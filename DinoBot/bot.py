from numpy import *
from PIL import ImageGrab, ImageOps
import pyautogui as py
import time

def pressSpace():
    py.keyDown('space')
    time.sleep(0.01)
    py.keyUp('space')


def IMG():
    Box = (271, 856, 399, 901)  # Use your own Coordinates here
    image = ImageGrab.grab(Box)
    image = ImageOps.grayscale(image)
    arr = array(image.getcolors())
    return (arr.sum())

def main():
    print("Starting Game.....")
    x = 0
    while(1):
       if(IMG()!=6007):
            pressSpace()
            x=x+1
            print(" Jumping "+str(x)+" times")

main()