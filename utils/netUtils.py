# --------------------------------------------------------------------------------- #
# Name: Johnathan Chivington - (github|twitter|facebook > chivingtoninc)            #
# Project: MicroPython IoT RTOS.                                                    #
# Description: Networked real-time device control system with web app UI.           #
# File: "netUtils.py" - Utility functions for working with BSD-like sockets.        #
# License: DO_WHATEVER_YOU_WANT - use/modify/redistribute as you like.              #
# --------------------------------------------------------------------------------- #

# ------------------------------------ Includes ----------------------------------- #
import uos
import network
import socket
from utils.ioUtils import *

# connect to network
def connectToWifi(sta_ssid, sta_pass):
    sta_if = network.WLAN(network.STA_IF)

    if sta_ssid != 0:
        clr()
        print(' Connecting to "%s"' % sta_ssid)
        sta_if.connect(sta_ssid, sta_pass)

    progress(1,3)
    print(' Connected!\n' if sta_if.isconnected() else ' Not Connected... Try again.\n')

# set up local network
def setupAP(ap_ssid, ap_pass):
    ap_if = network.WLAN(network.AP_IF)
    print(ap_ssid)
