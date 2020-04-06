# --------------------------------------------------------------------------------- #
# Name: Johnathan Chivington - (github|twitter|facebook > chivingtoninc)            #
# Project: MicroPython IoT RTOS.                                                    #
# Description: Networked real-time device control system with web app UI.           #
# File: "ioUtils.py" - Unix-like utility functions for file, user, socket, i/o      #
# License: DO_WHATEVER_YOU_WANT - use/modify/redistribute as you like.              #
# --------------------------------------------------------------------------------- #

# ------------------------------------ Includes ----------------------------------- #
import uos


# "clear" terminal
def clr():
    [print('\n' if i < 99 else '\033[H') for i in range(100)]


# list directory contents
def ls(path):
    abs = '.' if len(path) == 0 else (path if path[0] == '/' else ('/%s' % path))
    contents = uos.listdir(abs)
    print('\n Directory of: %s\n' % abs)

    for i,f in enumerate(contents):
        print(('  - %s' % f) + ('\n' if i == len(contents)-1 else ''))


# print bar under title/msg/header/etc
def bar(str):
    return ''.join(['-' for letter in str]);


# progress bar during load events
def progress(duration, dots):
    for i in range(duration*15000):
        print(' .' if (i % int(duration*15000/dots) == 0) else '', end='')


# print file contents
def cat(fname):
    f = open(fname, 'r')

    while True:
        line = f.readline()
        if line != '':
            print(line, end='')
        else:
            break

    f.close()


# greet user
def greet():
    title = 'MicroPython IoT RTOS'
    description = 'A networked, real-time hardware monitoring & control system with a web app UI.'

    clr()
    print('\n %s\n %s\n %s\n\n * type "help" (without quotes) for more...' % (title, bar(title), description))

# display help menu
def help():
    opts = [
        ['help', 'Display this menu.'],
        ['connectToWifi', 'Pass (name, password) of a wireless network to connect to.'],
        ['setAPinfo', 'Pass (name, password) to create a wireless network others can connect to.'],
    ]

    print('\n Options\n %s' % bar('Options'))
    for i,opt in enumerate(opts):
        print(" %s%s- %s" % (opt[0], ('\t\t' if len(opt[0]) < 9 else '\t'), opt[1]), end=('\n\n' if i == len(opts)-1 else '\n'))
