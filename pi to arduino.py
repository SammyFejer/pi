import serial
import time
num = 0

if __name__ == '__main__':
    ser =serial.Serial('/dev/ttyUSB0',9600, timeout=1)
    ser.reset_input_buffer()

    while True:
        num = num +1 
        data = str(num) + "/n"
        encoded_bytes = data.encode("utf-8")
        ser.write((encoded_bytes))
        num = ser.readline().decode('utf-8').rstrip()
        
        print (num)
        time.sleep(1)