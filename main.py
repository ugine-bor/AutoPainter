from pynput.mouse import Controller, Button
from time import sleep

import pyautogui

from imgconvert import convertimage
import pickle
from tkinter.filedialog import askopenfilename

import getcoords

mouse = Controller()


def click(xy, times=1, side='left'):
    mouse.position = xy
    if side == 'right':
        mouse.click(Button.right, times)
    else:
        mouse.click(Button.left, times)


def press(xy, side='left'):
    mouse.position = xy
    if side == 'right':
        mouse.press(Button.right)
    else:
        mouse.press(Button.left)


def release(xy, side='left'):
    mouse.position = xy
    if side == 'right':
        mouse.release(Button.right)
    else:
        mouse.release(Button.left)


def __main__():
    pyautogui.FAILSAFE = False

    newfield = input("New template (y/n)? ")
    if newfield == 'y':
        getcoords.main()

    print("Choose program template")
    filepath = askopenfilename(
        initialdir='coords',
        filetypes=[('Pickle files', '*.pkl')])

    with open(filepath, 'rb') as f:
        COLORS = pickle.load(f)
        FIELD = pickle.load(f)

    print("Choose image to paint")
    imagepath = askopenfilename(initialdir=r'C:\Users\user\Pictures', filetypes=[('JPG files', '*.jpg')])
    convertimage(imagepath)
    print("Processing image...")
    sleep(5)

    seconds = int(input("Seconds to open paint: "))
    print(f"{seconds} seconds to start. open paint\n")
    sleep(seconds)
    with open(f"matrix/{imagepath.split(r'/')[-1].split('.')[0]}_matrix.pkl", 'rb') as f:
        binary_matrix = pickle.load(f)

    print("Start painting\n")

    #click((COLORS['C'][0], COLORS['C'][1]))
    #click((COLORS['M'][0], COLORS['M'][1]))
    #click((COLORS['Y'][0], COLORS['Y'][1]))
    #click((COLORS['K'][0], COLORS['K'][1]))

    pressed = False
    for y, row in enumerate(binary_matrix):
        for x, pixel in enumerate(row):
            if pixel == 0 and not pressed:
                press((FIELD['START'][0] + x, FIELD['START'][1] + y))
                pressed = True
                sleep(0.05)
            elif pixel == 1 and pressed:
                release((FIELD['START'][0] + x, FIELD['START'][1] + y))
                pressed = False
    print("Done")


__main__()
