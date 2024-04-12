from pynput.mouse import Controller, Button
from time import sleep

from environs import Env

import pyautogui

from imgconvert import convertimage
import pickle

# coords for my paint
env = Env()
env.read_env()

mouse = Controller()


def pos(var):
    values = list(map(int, env.list(var)))
    return (values[0], values[1])


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
    image = input('Image name or path with extension: ')
    convertimage(image)

    print("5 seconds to start. open paint\n")
    sleep(5)

    with open(f"{image.split('.')[0]}_matrix.pkl", 'rb') as f:
        binary_matrix = pickle.load(f)

    print("Start\n")

    click(pos('BRUSH'))
    sleep(0.1)
    click(pos('BLACK'))
    sleep(0.1)

    pressed = False
    for y, row in enumerate(binary_matrix):
        for x, pixel in enumerate(row):
            if pixel == 0 and not pressed:
                press((pos("STARTCOORDS")[0] + x, pos("STARTCOORDS")[1] + y))
                pressed = True
                sleep(0.05)
            elif pixel == 1 and pressed:
                release((pos("STARTCOORDS")[0] + x, pos("STARTCOORDS")[1] + y))
                pressed = False
    print("Done")


__main__()
