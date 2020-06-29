#!/usr/bin/env python

import sys
import time
import pymodbus
import serial
import json
import threading
import signal
from collections import deque
from threading import Timer
from pymodbus.pdu import ModbusRequest
from pymodbus.client.sync import ModbusSerialClient as ModbusClient
from pymodbus.transaction import ModbusRtuFramer
from pymodbus.payload import BinaryPayloadDecoder
from pymodbus.constants import Endian

decoded = {'Spannung1' : 230,
            'Strom1' : 0,
            'Wirkleistung1' : 0,
            'Blindleistung1' : 0,
            'Scheinleistung1' : 0,
            'Wirkungsfaktor1' : 0,
            'FaktorTg1' : 0,
            'THDU1' : 0,
            'THDI1' : 0,
            'Spannung2' : 230,
            'Strom2' : 0,
            'Wirkleistung2' : 0,
            'Blindleistung2' : 0,
            'Scheinleistung2' : 0,
            'Wirkungsfaktor2' : 0,
            'FaktorTg2' : 0,
            'THDU2' : 0,
            'THDI2' : 0,
            'Spannung3' : 230,
            'Strom3' : 0,
            'Wirkleistung3' : 0,
            'Blindleistung3' : 0,
            'Scheinleistung3' : 0,
            'Wirkungsfaktor3' : 0,
            'FaktorTg3' : 0,
            'THDU3' : 0,
            'THDI3' : 0
            }



def signal_handler(signal, frame):
    print('Exit')
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)




modbusClient = ModbusClient(method = "rtu", port="/dev/serial0", stopbits = 1, bytesize = 8, parity = 'N', baudrate = 38400, timeout = 2)

connection = modbusClient.connect()


def updateRegisters():
    result = modbusClient.read_holding_registers(7000,54,unit=0x1)
    decoder1 = BinaryPayloadDecoder.fromRegisters(result.registers, byteorder=Endian.Big, wordorder=Endian.Big)

    decoded['Spannung1'] = decoder1.decode_32bit_float()
    decoded['Strom1'] = decoder1.decode_32bit_float()
    decoded['Wirkleistung1'] = decoder1.decode_32bit_float()
    decoded['Blindleistung1'] = decoder1.decode_32bit_float()
    decoded['Scheinleistung1'] = decoder1.decode_32bit_float()
    decoded['Wirkungsfaktor1'] = decoder1.decode_32bit_float()
    decoded['FaktorTg1'] = decoder1.decode_32bit_float()
    decoded['THDU1'] = decoder1.decode_32bit_float()
    decoded['THDI1'] = decoder1.decode_32bit_float()
    decoded['Spannung2'] = decoder1.decode_32bit_float()
    decoded['Strom2'] = decoder1.decode_32bit_float()
    decoded['Wirkleistung2'] = decoder1.decode_32bit_float()
    decoded['Blindleistung2'] = decoder1.decode_32bit_float()
    decoded['Scheinleistung2'] = decoder1.decode_32bit_float()
    decoded['Wirkungsfaktor2'] = decoder1.decode_32bit_float()
    decoded['FaktorTg2'] = decoder1.decode_32bit_float()
    decoded['THDU2'] = decoder1.decode_32bit_float()
    decoded['THDI2'] = decoder1.decode_32bit_float()
    decoded['Spannung3'] = decoder1.decode_32bit_float()
    decoded['Strom3'] = decoder1.decode_32bit_float()
    decoded['Wirkleistung3'] = decoder1.decode_32bit_float()
    decoded['Blindleistung3'] = decoder1.decode_32bit_float()
    decoded['Scheinleistung3'] = decoder1.decode_32bit_float()
    decoded['Wirkungsfaktor3'] = decoder1.decode_32bit_float()
    decoded['FaktorTg3'] = decoder1.decode_32bit_float()
    decoded['THDU3'] = decoder1.decode_32bit_float()
    decoded['THDI3'] = decoder1.decode_32bit_float()


class RegisterUpdater(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        while True:
            updateRegisters()
            print (decoded['Spannung1'])
            time.sleep(0.2)

registerUpdater = RegisterUpdater()
registerUpdater.daemon = True
registerUpdater.start()
