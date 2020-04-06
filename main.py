# --------------------------------------------------------------------------------- #
# Name: Johnathan Chivington - (github|twitter|facebook > chivingtoninc)            #
# Project: MicroPython IoT RTOS.                                                    #
# Description: Networked real-time device control system with web app UI.           #
# File: "main.py" - Executed after every sequence.                                  #
# License: DO_WHATEVER_YOU_WANT - use/modify/redistribute as you like.              #
# --------------------------------------------------------------------------------- #

# ------------------------------------ Includes ----------------------------------- #
import uos
import socket
import network
from utils.ioUtils import *
from utils.netUtils import *

# -------------------------------------- Main ------------------------------------- #
def main(args):
    sta_ssid, sta_pass = args[0], args[1]

    # greet user
    greet()

    # connect to network
    if sta_ssid:
        print('\n\n Connecting to specified wireless network', end='')
        progress(4,3)
        connectToWifi(sta_ssid, sta_pass)

    # create AP
    setupAP('Stepper Control', 'stepper1')

    # # create socket &
    # s = socket.socket()
    #
    # ai = socket.getaddrinfo("0.0.0.0", 8080)
    # print("\n Socket info: ", ai)
    # addr = ai[0][-1]
    #
    # s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # s.bind(addr)
    # s.listen(5)
    # print("Listening, connect your browser to http://%s:8080/" % addr[0])

    # counter = 0
    # while True:
    #     res = s.accept()
    #
    #     client_sock = res[0]
    #     client_addr = res[1]
    #     print("\n Client\n - address: %d | socket: %d", client_addr, client_sock)
    #
    #     print("\n Request:")
    #     req = client_sock.readline()
    #     print(req)
    #
    #     while True:
    #         h = client_sock.readline()
    #         if h == b"" or h == b"\r\n":
    #             break
    #         print(h)
    #
    #     client_sock.write(CONTENT % counter)
    #     client_sock.close()
    #
    #     counter += 1
    #     print()


# main()
