import serial
from flask import Flask, render_template, redirect, request


def send(cmd):
    ser = serial.Serial()
    ser.rts = False
    ser.dtr = False
    ser.port = "COM3"
    ser.open()
    ser.write(cmd)
    ser.close()


app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("index.html")


@app.route('/red')
def red():
    send(b"r")
    return redirect('/')


@app.route('/blue')
def blue():
    send(b"t")
    return redirect('/')


@app.route('/led', methods=["POST"])
def led():
    cmd = request.form["cmd"]
    send(cmd.encode())
    return redirect("/")


if __name__ == '__main__':
    app.run(host="0.0.0.0")
