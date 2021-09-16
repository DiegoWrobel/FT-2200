<<<<<<< HEAD
from os import write
import serial
import time

#CMD_READ_RX_STATUS = [0x00, 0x00, 0x00, 0x00, 0xE7]
#CMD_SET_FREC = [0x0e ,0x37, 0x00, 0x00, 0x01]
#comando = [0x14, 0x55, 0x00, 0x00, 0x01]
#comando2= [0x01, 0x00, 0x00, 0x55, 0x14]
#comando3= [0x00, 0x00, 0x00, 0x00, 0x18]
#comando4= [0x18, 0x00, 0x00, 0x00, 0x00]
#comando5= '28 28 28 28 28'
#ser = serial.Serial(SERIAL_PORT)
ser = serial.Serial()
ser.port = 'COM9'
ser.stopbits = serial.STOPBITS_TWO
ser.baudrate = 4800
ser.parity = serial.PARITY_NONE
ser.bytesize = serial.EIGHTBITS
ser.timeout = 1
ser.xonxoff = 0
ser.rtscts = 0
ser.dsrdtr = 0
delay = 0.002

def set_frecuency(frecuencia): # Envia la frecuencia (Validar antes con frec_valid)
    comando = []
    comando[:0]=frecuencia
    print(comando)
    
    ser.open()
    ser.write(chr(20).encode())
    for index in comando:
        time.sleep(0.002)
        ser.write(chr(int(index)).encode())
    time.sleep(0.002)
    ser.write(chr(20).encode())
    ser.close()

def comando(dato): # Envia datos 
    ser.open()
    ser.write(chr(int(dato)).encode())
    ser.close()

def frec_valid(frec): # Valida si la frecuencia es valida para enviar a la radio
    if frec >= 110000 and frec <= 180000:                       #Si esta dentro del rango de la radio
        if int(str(frec)[-1]) == 0 or int(str(frec)[-1]) == 5:  #Si termina en 0 o 5
            return True

i=1
while i==1:
#    entrada = input("COMANDO:") # Comandos Directos
#    comando(entrada)            # En la funcion comando    
    
    frecuencia = input("Frecuencia:")
    if frec_valid(int(frecuencia)) == True:
        print('Frecuencia a enviar:', int(frecuencia))
    #    #set_frecuency(frecuencia)
    else:
        print('Frecuencia', int(frecuencia), 'Invalida')





=======
from os import write
import serial
import time

#CMD_READ_RX_STATUS = [0x00, 0x00, 0x00, 0x00, 0xE7]
#CMD_SET_FREC = [0x0e ,0x37, 0x00, 0x00, 0x01]
#comando = [0x14, 0x55, 0x00, 0x00, 0x01]
#comando2= [0x01, 0x00, 0x00, 0x55, 0x14]
#comando3= [0x00, 0x00, 0x00, 0x00, 0x18]
#comando4= [0x18, 0x00, 0x00, 0x00, 0x00]
#comando5= '28 28 28 28 28'
#ser = serial.Serial(SERIAL_PORT)
ser = serial.Serial()
ser.port = 'COM9'
ser.stopbits = serial.STOPBITS_TWO
ser.baudrate = 4800
ser.parity = serial.PARITY_NONE
ser.bytesize = serial.EIGHTBITS
ser.timeout = 1
ser.xonxoff = 0
ser.rtscts = 0
ser.dsrdtr = 0
delay = 0.002

def set_frecuency(frecuencia): # Envia la frecuencia (Validar antes con frec_valid)
    comando = []
    comando[:0]=frecuencia
    print(comando)
    
    ser.open()
    ser.write(chr(20).encode())
    for index in comando:
        time.sleep(0.002)
        ser.write(chr(int(index)).encode())
    time.sleep(0.002)
    ser.write(chr(20).encode())
    ser.close()

def comando(dato): # Envia datos 
    ser.open()
    ser.write(chr(int(dato)).encode())
    ser.close()

def frec_valid(frec): # Valida si la frecuencia es valida para enviar a la radio
    if frec >= 110000 and frec <= 180000:                       #Si esta dentro del rango de la radio
        if int(str(frec)[-1]) == 0 or int(str(frec)[-1]) == 5:  #Si termina en 0 o 5
            return True

i=1
while i==1:
#    entrada = input("COMANDO:") # Comandos Directos
#    comando(entrada)            # En la funcion comando    
    
    frecuencia = input("Frecuencia:")
    if frec_valid(int(frecuencia)) == True:
        print('Frecuencia a enviar:', int(frecuencia))
    #    #set_frecuency(frecuencia)
    else:
        print('Frecuencia', int(frecuencia), 'Invalida')





>>>>>>> 0464bd7d7b6311920ac96fd6e4f6505f6b68f8ed
