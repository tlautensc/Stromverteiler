import sys
import time
import pymodbus
import serial
import signal
from pymodbus.pdu import ModbusRequest
from pymodbus.client.sync import ModbusSerialClient as ModbusClient
from pymodbus.transaction import ModbusRtuFramer
from pymodbus.payload import BinaryPayloadDecoder
from pymodbus.constants import Endian
from prometheus_client import start_http_server, Gauge



def signal_handler(signal, frame):
    print('Exit')
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)


modbusClient = ModbusClient(method = "rtu", port="/dev/serial0", stopbits = 1, bytesize = 8, parity = 'N', baudrate = 38400, timeout = 2)

connection = modbusClient.connect()

U1 = Gauge('U1', '')
I1 = Gauge('I1', '')
P1 = Gauge('P1', 'Wirkleistung')
PB1 = Gauge('PB1', 'Blindleistung')
PS1 = Gauge('PS1', 'Scheinleistung')
PF1 = Gauge('WF1', 'Wirkungsfaktor')
FTG1 = Gauge('FTG1', 'FaktorTg')
THDU1 = Gauge('THDU1', '')
THDI1 = Gauge('THDI1', '')

U2 = Gauge('U2', '')
I2 = Gauge('I2', '')
P2 = Gauge('P2', 'Wirkleistung')
PB2 = Gauge('PB2', 'Blindleistung')
PS2 = Gauge('PS2', 'Scheinleistung')
PF2 = Gauge('WF2', 'Wirkungsfaktor')
FTG2 = Gauge('FTG2', 'FaktorTg')
THDU2 = Gauge('THDU2', '')
THDI2 = Gauge('THDI2', '')

U3 = Gauge('U3', '')
I3 = Gauge('I3', '')
P3 = Gauge('P3', 'Wirkleistung')
PB3 = Gauge('PB3', 'Blindleistung')
PS3 = Gauge('PS3', 'Scheinleistung')
PF3 = Gauge('WF3', 'Wirkungsfaktor')
FTG3 = Gauge('FTG3', 'FaktorTg')
THDU3 = Gauge('THDU3', '')
THDI3 = Gauge('THDI3', '')

def updateRegisters():
    result = modbusClient.read_holding_registers(7000,54,unit=0x1)
    decoder1 = BinaryPayloadDecoder.fromRegisters(result.registers, byteorder=Endian.Big, wordorder=Endian.Big)

    U1.set(decoder1.decode_32bit_float())
    I1.set(decoder1.decode_32bit_float())
    P1.set(decoder1.decode_32bit_float())
    PB1.set(decoder1.decode_32bit_float())
    PS1.set(decoder1.decode_32bit_float())
    PF1.set(decoder1.decode_32bit_float())
    FTG1.set(decoder1.decode_32bit_float())
    THDU1.set(decoder1.decode_32bit_float())
    THDI1.set(decoder1.decode_32bit_float())

    U2.set(decoder1.decode_32bit_float())
    I2.set(decoder1.decode_32bit_float())
    P2.set(decoder1.decode_32bit_float())
    PB2.set(decoder1.decode_32bit_float())
    PS2.set(decoder1.decode_32bit_float())
    PF2.set(decoder1.decode_32bit_float())
    FTG2.set(decoder1.decode_32bit_float())
    THDU2.set(decoder1.decode_32bit_float())
    THDI2.set(decoder1.decode_32bit_float())

    U3.set(decoder1.decode_32bit_float())
    I3.set(decoder1.decode_32bit_float())
    P3.set(decoder1.decode_32bit_float())
    PB3.set(decoder1.decode_32bit_float())
    PS3.set(decoder1.decode_32bit_float())
    PF3.set(decoder1.decode_32bit_float())
    FTG3.set(decoder1.decode_32bit_float())
    THDU3.set(decoder1.decode_32bit_float())
    THDI3.set(decoder1.decode_32bit_float())

if __name__ == '__main__':
    start_http_server(8000)
    while True:
        updateRegisters()
        time.sleep(0.5)
