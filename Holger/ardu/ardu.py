import serial.tools.list_ports
import serial
import time
import threading


last_input = time.time()
dev = serial.tools.list_ports.comports()[0].device

ser = serial.Serial(dev)


def read_input():
    while True:
        input2 = input("valgus: ")
        if input2 == "1":
            ser.write(b'A')
        else:
            ser.write(b'a')

        global last_input
        last_input = time.time()


the = threading.Thread(target=read_input)
the.start()

while True:
    # print(time.time() - last_input)
    # time.sleep(1)
    if (time.time() - last_input) >= 3:
        ser.write(b'A')
        time.sleep(0.3)
        ser.write(b'a')
        time.sleep(0.5)
