from pynput.mouse import Listener as mouseListener
from pynput.mouse import Controller, Button
from time import sleep, time

import winsound

import pyautogui

from pickle import dump

mouse = Controller()
clickbuff = [0]
clickpos = []


def pos(var):
    values = list(map(int, var))
    return (values[0], values[1])


def getclick(x, y, button, pressed, clickbuff=clickbuff):
    if pressed:
        if button == Button.left:
            clickbuff.append(time())
            if clickbuff[-1] - clickbuff[-2] < 0.3:
                print('double clicked. SHIT ALL AGAIN')
                winsound.Beep(1000, 500)
                exit()
            print('l|', x, y)
        else:
            print('r|', x, y)
        winsound.Beep(440, 500)
        clickpos.append((x, y))
        if len(clickpos) >= 6:
            winsound.Beep(200, 500)
            return False


def main():
    pyautogui.FAILSAFE = False
    filename = input("Name of paint program: ")
    seconds = int(input("Seconds to open paint: "))
    print(f"{seconds} seconds to open paint.\n")
    sleep(seconds)
    winsound.Beep(440, 1000)
    print("Start\n")

    with mouseListener(on_click=getclick) as listener:
        listener.join()
    print(clickpos)
    with open(f'coords/{filename}.pkl', 'wb') as f:
        COLORS, FIELD = {'C': clickpos[0], 'M': clickpos[1], 'Y': clickpos[2], 'K': clickpos[3]}, {'START': clickpos[4],
                                                                                                   'END': clickpos[5]}
        dump(COLORS, f)
        dump(FIELD, f)

    print("\nDone\n")


if __name__ == "__main__":
    main()
