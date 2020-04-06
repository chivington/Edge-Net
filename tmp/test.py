# Project: ESP MicroPython Test Environment
# Version: 0.01
# Description: MicroPython test environment for rapid prototyping on the ESP8266.
# Authors: Johnathan Chivington
# License: N/A
# Keywords: test, dev, devtools, embedded, controls, automation, SoC, IoT

# ----- OS Modules ------------------------------------------------- #
import esp, machine, time, uos, sys, network, socket


# ----- Constants -------------------------------------------------- #
SYS, NODE, SYS_VER, MPY_VER, BOARD = uos.uname()
FREQ = 160000000
PLAT = "Test Environment"
PLAT_VER = "0.01"


# ----- System Settings -------------------------------------------- #
machine.freq(FREQ)


# ----- CLI Utilities ---------------------------------------------- #
def underline(msg):
    if msg == "":
        print("\n No message passed.")
        return
    else:
        print(msg)
        for i in range(len(msg)):
            sys.stdout.write((" " if msg[i] == " " else "-") if i == 0 else "-")
        print("")

def clear(msg=""):
    print("\x1B\x5B2J", end="")
    print("\x1B\x5BH", end="")
    if msg != "":
        print("")
        underline(msg)

def ls(dir="."):
    uos.listdir(dir)

def cd(dir="."):
    uos.chdir(dir)

def pwd():
    uos.getcwd()

def help():
    print("")
    underline(" Help Menu")
    print("  - ls(dir): list the contents of the current directory (or of an optional specified directory).")
    print("  - cd(dir): navigate to the specified directory.")
    print("  - pwd():   display the full path of the current working directory.")
    print("")


# ----- Test Program ----------------------------------------------- #
clear(" Welcome to the ESP8266 MicroPython Development Environment")
print("\n\n")
