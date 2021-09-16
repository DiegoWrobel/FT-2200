from os import write
import serial
import time

ser = serial.Serial()
ser.port = 'COM9'      # Set your own serial port
ser.stopbits = serial.STOPBITS_TWO
ser.baudrate = 4800
ser.parity = serial.PARITY_NONE
ser.bytesize = serial.EIGHTBITS
ser.timeout = 1
ser.xonxoff = 0
ser.rtscts = 0
ser.dsrdtr = 0
delay = 0.002

def set_frequency(frequency): # Sends the frequency (Validate before with frec_valid)
    comando = []
    comando[:0]=frequency
    print(comando)
    
    ser.open()
    ser.write(chr(20).encode())
    for index in comando:
        time.sleep(0.002)
        ser.write(chr(int(index)).encode())
    time.sleep(0.002)
    ser.write(chr(20).encode())
    ser.close()

def frec_valid(frec): # Validates if the frequency is valid to send
    if frec >= 110000 and frec <= 180000:                       #If it's in the range of the radio
        if int(str(frec)[-1]) == 0 or int(str(frec)[-1]) == 5:  #If it ends in 0 or 5
            return True

i=1
while i==1:
    frecuencia = input("frequency:")
    if frec_valid(int(frecuencia)) == True:
        set_frequency(frecuencia)
    else:
        print('Frequency', int(frecuencia), 'is invalid')





