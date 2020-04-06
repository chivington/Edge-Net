# --------------------------------------------------------------------------------- #
# Name: Johnathan Chivington - (github|twitter|facebook > chivingtoninc)            #
# Project: MicroPython IoT RTOS.                                                    #
# Description: Networked real-time device control system with web app UI.           #
# File: "boot.py" - Executed on every boot (including wake-boot from deepsleep)     #
# License: DO_WHATEVER_YOU_WANT - use/modify/redistribute as you like.              #
# --------------------------------------------------------------------------------- #

# ------------------------------------ Includes ----------------------------------- #
import esp
import machine
import gc

# -------------------------------- Startup Commands ------------------------------- #
esp.osdebug(None)
gc.collect()
machine.freq(160000000)
