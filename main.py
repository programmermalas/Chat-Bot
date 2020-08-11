"""
Made by Rafli
Please dont delete this credit
"""
from tkinter import *

root = Tk()

def send():
    send = "You => " + e.get()
    bot = "Bot => "
    txt.insert(END, "\n" + send)
    if(e.get() == "Halo" or e.get() == "halo"):
        txt.insert(END, "\n" + f"{bot}Hi")
    
    elif(e.get() == "Hai" or e.get() == "hai"):
        txt.insert(END, "\n" + f"{bot}Halo")

    elif(e.get() == "apa kabar?" or e.get() == "Apa kabar?"):
        txt.insert(END, "\n" + f"{bot}Baik")
    
    elif(e.get() == "mau main?" or e.get() == "Mau main?"):
        txt.insert(END, "\n" + f"{bot}tidak")
    
    else:
        txt.insert(END, "\n" + f"{bot}Maaf saya tidak mengerti apa yang maksud")

txt = Text(root)
txt.grid(row=0, column=0, columnspan=2)
e = Entry(root, width=100)
send = Button(root, text="Send", command = send).grid(row = 1, column = 1)
e.grid(row = 1, column = 0)
root.title("Simple Chat Bot")
root.mainloop()
