from os import system, name
import sys
import time
from colorama import Fore, Back, Style
class screen:
    def clear():
        if name == 'nt':
            system('cls')
        else:
            system('clear')
class word:
    def write(message):
        print("")
        for word in message:
            time.sleep(0.07)
            sys.stdout.write(Back.GREEN + word)
            sys.stdout.flush()
            sys.stdout.write(Style.RESET_ALL)
            sys.stdout.flush()
        time.sleep(.1)
        return ""
    def write2(message):
        for word in message:
            time.sleep(0.07)
            sys.stdout.write(word)
            sys.stdout.flush()
        time.sleep(.1)
        return ""
class GUI:
    def setwidth(a, color):
        b = 0
        li = []
        while b < a:
            li.append(color + "_")
            b += 1
        return(li)
    def setline(a, color):
        for i in range(len(a)):
            sys.stdout.write(color + a[i])
    def end():
        sys.stdout.write(Style.RESET_ALL)
x = GUI.setwidth(10, Fore.GREEN)
GUI.setline(x, Back.GREEN)
GUI.end()
