# Project: Greenhouse Automation System (working title)
# Version: 0.01
# Description: Networked embedded mechanical & power electronics controls system for automating our home greenhouse
#   operations. This systems utilizes an inexpensive embedded SoC to monitor & control a variety of sensors & hardware.
# Authors: Ashley Stephenson & Johnathan Chivington
# License: N/A
# Keywords: embedded, power electronics, controls, automation, SoC, IoT

# ----- OS Modules ------------------------------------------------- #
import esp, machine, time, uos, sys, network, socket


# ----- Constants -------------------------------------------------- #
SYS, NODE, SYS_VER, MPY_VER, BOARD = uos.uname()
FREQ = 160000000
MODE = "DEV_MODE"
PLAT = "Greenhouse Automation System"
PLAT_VER = "0.01"


# ----- System Settings -------------------------------------------- #
if MODE == "PROD_MODE":
    esp.osdebug(None)

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

def cd(path="."):
    uos.chdir(path)

def pwd():
    uos.getcwd()

def err_msg(t="f"):
    print("\n Requires a "+"file" if t=="f" else "directory"+" name.")

def rm(file=""):
    if file == "":
        err_msg("f")
        return
    else:
        uos.remove(file)

def mkdir(path=""):
    if path == "":
        err_msg("d")
        return
    else:
        uos.mkdir(path)

def rmdir(path=""):
    if path == "":
        err_msg("d")
        return
    else:
        uos.rmdir(path)


# ----- WiFi Utilities --------------------------------------------- #
def initialize_station(ap,pwd):
    s = network.WLAN(network.STA_IF)
    if not s.isconnected():
        print(' Connecting to network...')
        s.active(True)
        s.connect(ap,pwd)
        while not s.isconnected():
            pass
    print('\n Network config: ', s.ifconfig())









pins = [machine.Pin(i, machine.Pin.IN) for i in (0, 2, 4, 5, 12, 13, 14, 15)]

html = """<!DOCTYPE html>
<html>
    <head> <title>ESP8266 Pins</title> </head>
    <body> <h1>ESP8266 Pins</h1>
        <table border="1"> <tr><th>Pin</th><th>Value</th></tr> %s </table>
    </body>
</html>
"""

import socket
addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]

s = socket.socket()
s.bind(addr)
s.listen(1)

print('listening on', addr)

while True:
    cl, addr = s.accept()
    print('client connected from', addr)
    cl_file = cl.makefile('rwb', 0)
    while True:
        line = cl_file.readline()
        if not line or line == b'\r\n':
            break
    rows = ['<tr><td>%s</td><td>%d</td></tr>' % (str(p), p.value()) for p in pins]
    response = html % '\n'.join(rows)
    cl.send('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
    cl.send(response)
    cl.close()












# ----- State Management Engine ----------------------------------- #


# ----- Boot Sequence --------------------------------------------- #
clear(" "+PLAT+" v"+PLAT_VER)
print(" Boot Sequence...\n\n")
