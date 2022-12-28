import os
import serial

ser = serial.Serial('/dev/ttyACM1', 115200)


def main():
    while True:
        data = ser.read_until().decode('ASCII')
        ser.reset_input_buffer()
        if data is None or 'Is this thing working':
            continue
        print("Data is:" +data)
        
if __name__ == '__main__':
    main()
