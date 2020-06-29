#!/usr/bin/env python

import sys
import time
import pymodbus
import serial
import json
import SimpleHTTPServer
import SocketServer
import threading
import signal
from collections import deque
from threading import Timer
from pymodbus.pdu import ModbusRequest
from pymodbus.client.sync import ModbusSerialClient as ModbusClient
from pymodbus.transaction import ModbusRtuFramer
from pymodbus.payload import BinaryPayloadDecoder
from pymodbus.constants import Endian
from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket

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

verlauf = []

for x in range(40):
    verlauf.append(decoded)




SocketServer.TCPServer.allow_reuse_address = True
class ThreadedHTTPServer(object):
    handler = SimpleHTTPServer.SimpleHTTPRequestHandler
    def __init__(self, host, port):
        self.server = SocketServer.TCPServer((host,port), self.handler)
        self.server_thread = threading.Thread(target=self.server.serve_forever)
        self.server_thread.daemon = True

    def start(self):
        self.server_thread.start()
        print('HTTP Server started')

    def stop(self):
        self.server.shutdown()
        self.server.server_close()

HTTPServer = ThreadedHTTPServer("",8080)
HTTPServer.start()


clients = []

class WebsocketServer(WebSocket):

    def handleConnected(self):
        print(self.address, 'connected')
        clients.append(self)
        self.sendMessage(unicode(json.dumps(verlauf)))

    def handleClose(self):
        clients.remove(self)
        print(self.address, 'closed')

    def handleMessage(self):
        self.sendMessage(unicode(json.dumps(verlauf)))



class ThreadedWebsocketServer(object):
    def __init__(self, host, port, handler):
        self.server = SimpleWebSocketServer(host, port, handler)
        self.server_thread = threading.Thread(target=self.server.serveforever)
        self.server_thread.daemon = True

    def start(self):
        self.server_thread.start()
        print('Websocket Server started')


MyWebsocketServer = ThreadedWebsocketServer('',8081, WebsocketServer)
MyWebsocketServer.start()




class ClientUpdater(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        while True:
            verlauf.remove(verlauf[0])
            verlauf.append(decoded)
            for x in clients:
                x.sendMessage(unicode(json.dumps(decoded)))
            time.sleep(0.5)

clientUpdater = ClientUpdater()
clientUpdater.daemon = True
clientUpdater.start()




class perpetualTimer():

    def __init__(self, t, hFunction):
        self.t=t
        self.hFunction = hFunction
        self.thread = Timer(self.t ,self.handle_function)

    def handle_function(self):
        self.hFunction()
        self.thread = Timer(self.t,self.handle_function)
        self.thread.start()

    def start(self):
        self.thread.start()

    def cancel(self):
        self.thread.cancel()


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
            time.sleep(0.2)

registerUpdater = RegisterUpdater()
registerUpdater.daemon = True
registerUpdater.start()

keepAlive = threading.Event()
keepAlive.wait()

#time.sleep(40)
#t = perpetualTimer(0.5,updateRegisters)
#t.start()
