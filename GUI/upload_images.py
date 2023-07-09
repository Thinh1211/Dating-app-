import tkinter as tk
from functools import partial
from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from PIL import Image, ImageTk
from math import floor, ceil
from database_controller import insert_image
from GUI import letter_thanks

class Upload_img:
    def __init__(self):
        self.__root = tk.Tk()
        self.__root.title("Profile Information")
        self.__root.geometry('1440x900')
        self.__root.resizable(width=False, height=False)
        
        self.__images = ["", "", ""]
        
    def con_click(self):
        if (self.__images[0] != "" and self.__images[1] != "" and self.__images[2] != ""):
            insert_image(self.__images[0], self.__images[1], self.__images[2])
            print('set up images success')
            self.__root.destroy()
            next = letter_thanks.Letter()
            next.Letter_Thanks_Screen()
        

    def Upload_Screen(self):
        
        background= PhotoImage(file="GUI/upload_img/background_upload.png")       
        continue_img = PhotoImage(file="GUI/upload_img/continue_img.png")
        upload_img = PhotoImage(file="GUI/upload_img/upload_click_img.png")
        
        label_background = tk.Label(self.__root, image=background)
        label_background.pack()
        
        def resize_img1(width, height):
            wid = floor(width/335)
            hei = floor(height/435)
            ration = min(wid, hei)
            return ration
        def resize_img12(width, height):
                wid = ceil(335/width)
                hei = ceil(435/height)
                ration = min(wid, hei)
                return ration
        
        def resize_img2_3(width, height):
            wid = floor(width/230)
            hei = floor(height/200)
            ration = min(wid, hei)
            return ration
        def resize_img2_32(width, height):
                wid = ceil(230/width)
                hei = ceil(200/height)
                ration = min(wid, hei)
                return ration
            
        def upload_file():
            try:
                #f_types = [('JPG Files', '*.jpg'), ('JPEG Files', '*.jpeg'), ('PNG Files', '*.png')]
                f_types = [('Images', '*.jpg *.jpeg *.png *.webp')]
                filename = filedialog.askopenfilename(multiple = False, filetypes = f_types)
                
                if self.__images[0] == "":
                    self.__images[0] = filename
                    img = Image.open(filename)
                    width, height = img.size  
                    if width < 335 or height < 435:
                        ration = resize_img12(width, height)
                        new_wid = int(width*ration)
                        new_hei = int(height*ration)
                    else:
                        ration = resize_img1(width, height)
                        new_wid = int(width/ration)
                        new_hei = int(height/ration)
                    img_resized = img.resize((new_wid, new_hei))
                    left = (new_wid - 335)/2
                    right = new_wid - (new_wid - 335)/2
                    upper = (new_hei - 435)/2
                    lower = new_hei - (new_hei - 435)/2
                    img_resized = img_resized.crop([left, upper, right, lower])
                    img_resized = ImageTk.PhotoImage(img_resized)
                
                    def remove_img1():
                        display_img1.destroy()
                        self.__images[0] = ""
                
                    display_img1 = Button(self.__root, image = img_resized, borderwidth=0, highlightthickness=0, command= partial(remove_img1))
                    display_img1.place(x = 682, y = 316)
                    display_img1.image = img_resized
                    
                elif self.__images[1] == "":
                    self.__images[1] = filename
                    img = Image.open(filename)
                    width, height = img.size  
                    if width < 230 or height < 200:
                        ration = resize_img2_32(width, height)
                        new_wid = int(width*ration)
                        new_hei = int(height*ration)
                    else:
                        ration = resize_img2_3(width, height)
                        new_wid = int(width/ration)
                        new_hei = int(height/ration)
                    img_resized = img.resize((new_wid, new_hei))
                    left = (new_wid - 230)/2
                    right = new_wid - (new_wid - 230)/2
                    upper = (new_hei - 200)/2
                    lower = new_hei - (new_hei - 200)/2
                    img_resized = img_resized.crop([left, upper, right, lower])
                    img_resized = ImageTk.PhotoImage(img_resized)
                
                    def remove_img2():
                        display_img2.destroy()
                        self.__images[1] = ""
                
                    display_img2 = Button(self.__root, image = img_resized, borderwidth=0, highlightthickness=0, command= partial(remove_img2))
                    display_img2.place(x = 1060, y = 316)
                    display_img2.image = img_resized
                    
                elif self.__images[2] == "":
                    self.__images[2] = filename
                    img = Image.open(filename)
                    width, height = img.size  
                    if width < 230 or height < 200:
                        ration = resize_img2_32(width, height)
                        new_wid = int(width*ration)
                        new_hei = int(height*ration)
                    else:
                        ration = resize_img2_3(width, height)
                        new_wid = int(width/ration)
                        new_hei = int(height/ration)
                    img_resized = img.resize((new_wid, new_hei))
                    left = (new_wid - 230)/2
                    right = new_wid - (new_wid - 230)/2
                    upper = (new_hei - 200)/2
                    lower = new_hei - (new_hei - 200)/2
                    img_resized = img_resized.crop([left, upper, right, lower])
                    img_resized = ImageTk.PhotoImage(img_resized)
                
                    def remove_img3():
                        display_image3.destroy()
                        self.__images[2] = ""
                
                    display_image3 = Button(self.__root, image = img_resized, borderwidth=0, highlightthickness=0, command= partial(remove_img3))
                    display_image3.place(x = 1060, y = 550)
                    display_image3.image = img_resized
            
            except Exception:
                print(self.__images)
                pass
        
        
        upload_button= tk.Button(self.__root, image= upload_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0, command= lambda: upload_file())
        upload_button.place(x = 137, y = 370)

        continue_button = tk.Button(self.__root, image= continue_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0, command= partial(self.con_click))
        continue_button.place(x = 1170, y = 800)

        self.__root.mainloop()