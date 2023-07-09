import tkinter as tk
from functools import partial
from tkinter import *


class Letter:
    def __init__(self):
        self.__root = tk.Tk()
        self.__root.title("Basics Information")

        self.__root.geometry('900x500')
        self.__root.resizable(width=False, height=False)
        
    def next_click(self):
        self.__root.destroy()

    def Letter_Thanks_Screen(self):
        background = tk.PhotoImage(file="GUI/letter_thanks_img/background.png")
        next_img = tk.PhotoImage(file="GUI/letter_thanks_img/next.png")


        label_background = tk.Label(self.__root, image = background)
        label_background.pack()

        #----------------------------------------------------------------------------------------------------------------------------
        
        #Continue Button
        
        
        next_button = tk.Button(label_background, image=next_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0, command= partial(self.next_click))
        next_button.place(x = 370, y = 400)
        
        
        self.__root.mainloop()