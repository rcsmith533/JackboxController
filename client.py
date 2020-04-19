import socket
import tkinter as tk 

def sendUp():
    s.sendall(b'Up')

def sendDown():
    s.sendall(b'Down')

def sendEnter():
    s.sendall(b'Enter')

def sendEscape():
    s.sendall(b'Escape')

def sendQuit():
    s.sendall(b'q')
    s.close()
    exit()

HOST = '192.168.0.7'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    window = tk.Tk()
    #window.minsize(200,200)
    up = tk.Button(window,text='Up',command = sendUp)
    up.pack()
    down = tk.Button(window,text='Down',command = sendDown)
    down.pack()
    enter = tk.Button(window,text='Enter',command = sendEnter)
    enter.pack()
    escape = tk.Button(window,text='Escape',command = sendEscape)
    escape.pack()
    myExit = tk.Button(window,text='Quit',command = sendQuit)
    myExit.pack()
    while True:
        window.mainloop()
    