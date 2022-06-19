from pyModbusTCP.client import ModbusClient
from pymodbus.payload import BinaryPayloadDecoder
from pymodbus.constants import Endian
from collections import OrderedDict
from pymodbus.compat import iteritems
from time import sleep

client = ModbusClient('challenges.france-cybersecurity-challenge.fr', port = 502, timeout=2)
client.open()
result = client.read_holding_registers(0,32)
res = ''
for i in result:
    res += chr(i)

print("[*] Token : " + res)

def checkstate(coil):
    state = client.read_coils(coil, 1)
    if state:
        print("[*] Coil " + str(coil) + " opened")
    else:
        print("[*] Coil " + str(coil) + " Closed")


def openr():
    client.write_single_coil(0,1)

def setdebr(n):
    client.write_single_register(32,n)

def openg():
    client.write_single_coil(1,1)

def setdebg(n):
    client.write_single_register(33,n)

def openb():
    client.write_single_coil(2,1)

def setdebb(n):
    client.write_single_register(34,n)

def openm():
    client.write_single_coil(3,1)

def setdebm(n):
    client.write_single_register(35,n)

def closm():
    client.write_single_coil(3,0)

def readr():
    return client.read_input_registers(7,1)

def readg():
    return client.read_input_registers(8,1)

def readb():
    return client.read_input_registers(9,1)

def readmr():
    return client.read_input_registers(3,1)

def readmg():
    return client.read_input_registers(4,1)

def readmb():
    return client.read_input_registers(5,1)

def closea():
    client.write_single_coil(0,1)
    client.write_single_coil(1,1)
    client.write_single_coil(2,1)

setdebr(5)
setdebg(5)
setdebb(5)
openr()
openg()
openb()
sleep(6)
setdebr(2)
setdebg(0)
setdebb(4)
sleep(1)
setdebr(0)
sleep(2)
setdebb(0)
closea()
setdebm(5)
openm()
sleep(20)
closm()
print("[*] St1 Res cuv : " + str(readr() + readg() + readb()))

sleep(1)
setdebb(2)
openb()
sleep(2)
setdebb(0)
closea()
setdebg(5)
openg()
sleep(19)
setdebg(1)
sleep(5)
closea()
print("[*] St2 m cuv : " + str(readmr() + readmg() + readmb()))
sleep(1)
setdebm(5)
openm()
sleep(20)
closm()
print("[*] St2 Res cuv : " + str(readr() + readg() + readb()))


GOAL = [32,126,42]
