from flask import Flask, render_template, redirect, request
import serial.tools.list_ports
import serial
import time
import threading


last_input = time.time()
dev = serial.tools.list_ports.comports()[0].device

ser = serial.Serial(dev)

app = Flask(__name__)


# def send(cmd):
#     ser = serial.Serial()
#     ser.rts = False
#     ser.dtr = False
#     ser.port = "COM9"
#     ser.open()
#     ser.write(cmd)
#     ser.close()


@app.route('/led', methods=["POST"])
def led():
    cmd = request.form.get("cmd")
    # send(cmd.encode())
    print(cmd)
    ser.write(cmd.encode())
    return redirect('/')


@app.route('/')
def hello_world():
    # ser.write(b" ")
    # olek = ser.readline()
    # ser.reset_input_buffer()
    olek = False
    return render_template("index.html", olek=olek)


@app.route('/red')
def on():
    ser.write(b"r")
    return redirect('/')


@app.route('/blue')
def off():
    ser.write(b"t")
    return redirect('/')


@app.route('/blink')
def blink():
    ser.write(b"l")
    return redirect('/')


@app.route('/toggle', methods=["POST"])
def toggle():
    request.form.get("tuli")
    ser.write(b" ")
    read = ser.readline().strip()
    print(read)
    if read == b'a':
        ser.write(b"r")
    else:
        ser.write(b"t")
    # if request.form.get("tuli") == "1":
    #     on()
    # else:
    #     off()
    return redirect('/')


if __name__ == '__main__':
    app.run()

