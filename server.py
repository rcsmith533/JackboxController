import socket
import pyautogui
import time

HOST = '0.0.0.0'
PORT = 65432

def main():
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
        s.bind((HOST,PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            while True:
                data = conn.recv(1024)
                if data != 'q':
                    print(data.decode('utf-8'))
                if data == b'Up':
                    pyautogui.typewrite(['up'])
                elif data == b'Down':
                    pyautogui.typewrite(['down'])
                elif data == b'Left':
                    pyautogui.typewrite(['left'])
                elif data == b'Right':
                    pyautogui.typewrite(['right'])
                elif data == b'Escape':
                    pyautogui.typewrite(['esc'])
                elif data == b'Enter':
                    pyautogui.typewrite(['enter'])
                elif data == b'q':
                    main()

main()