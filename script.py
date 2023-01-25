from tkinter import *
import tkinter as tk
import threading
import random
import time
import ctypes

def screenSize():
    user32 = ctypes.windll.user32
    screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
    return screensize


def ver():
    val = ctypes.windll.user32.MessageBoxW(0, 'You are idiot', 'Hello',4)
    if val == 6:
        ctypes.windll.user32.MessageBoxW(0, "I already Known this bro, let's rock", 'H-18_Virus')
    else:
        ctypes.windll.user32.MessageBoxW(0, 'But i think so', 'H-18_Virus')



def disable_event():
    pass



def move_window():
    root = Tk()
    root.title('MALWARE')
    root.attributes('-toolwindow',True)

    x = random.randint(0,screenSize()[0]-100)
    y = random.randint(0,screenSize()[1]-100)
    root.resizable(0,0)
    root.geometry(f'235x200+{x}+{y}')
    root.configure(background = 'black')

    Label(root,text='Malwareman' ,fg='white', font=('Terminal',13) , bg='black').place(x=50,y=20)
    Label(root,text='You Are Idiot' ,fg='red', font=('Terminal',13) , bg='black').place(x=40,y=100)

    root.protocol('WM_DELETE_WINDOWS', disable_event)
    root.mainloop()

if __name__ == "__main__":
    ver()

    for i in range(60):
        threading.Thread(target=move_window).start()
        time.sleep(0.1)
    time.sleep(5)
    while True:
        pass
