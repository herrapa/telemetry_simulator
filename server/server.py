import socket
import struct
from enum import Enum
import serial

class DataDirt(Enum):
    suspRL = 18
    suspRR = 19
    suspFL = 20
    suspFR = 21
    gear = 33
    fLat = 34
    fLon = 35

class DataLfs(Enum):
    speed = 11
    fLat = 5
    fLon = 6
    heading = 4 #or direction 5
    
    

UDP_IP = "127.0.0.1"
UDP_PORT = 20777

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

ser = serial.Serial(2, 115200)

print ("listening on port: ", UDP_PORT)

while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes

    

    telemetry = struct.unpack("38f", data) # means little endian
    #print ("DATA")
    #for d in telemetry:
    #    print (d)
    #print ("speed: ", telemetry[5])
    
    #f_lat = [int(telemetry[Data.fLat.value] * 16.0) + 128] 
    #f_lon = [int(telemetry[Data.fLon.value] * 16.0) + 128]

    #print ("gear: ", telemetry[Data.gear.value])
    #print ("Force lat: ", f_lat)
    #print ("Force lon: ", f_lon)
    val_str = struct.pack("2f", telemetry[DataDirt.fLat.value], telemetry[DataDirt.fLon.value])
    ser.write(val_str)
    #print (ser_val)
    #ser.write(f_lon)

    
    #print("Length: ", len(data), len(data) % 4)

print("program ended")

