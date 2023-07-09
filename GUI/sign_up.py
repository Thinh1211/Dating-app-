import tkinter as tk
from tkinter import *
from functools import partial
from database_controller import show_account, insert_account, insert_matching, insert_info
from GUI import secure
from GUI import basics_interests

class Sign_up:
    def __init__(self):
        self.__root = tk.Tk() # Create new window
        self.__root.title("Sign Up")
        self.__root.geometry('900x500')
        self.__root.resizable(width=False, height=False)
        

    def continue_click(self, username, password, confirm_password):
        un = username.get()
        pw = password.get()
        cpw = confirm_password.get()
        accounts = show_account()
        for account in accounts:
            if account[1] == un or un == "User Name":
                self.Error1()
        if un == pw:
            self.Error2()
        elif pw != cpw:
            self.Error3()
        else:
            insert_account(un, secure.encode(pw))
            accs = show_account()
            acc = accs[-1]
            user_id = str(acc[0])
            print(user_id)
            insert_matching(user_id)
            print("set account success")
            self.Infor_screen()
            
    def Error1(self):
        error = tk.PhotoImage(file = "GUI/sign_up_img/username_already_exist.png")
        Error = tk.Label(self.__root, image = error, borderwidth=0, highlightthickness=0).place(x = 276, y = 178)      
        Error.image = error

    def Error2(self):   
        error = tk.PhotoImage(file = "GUI/sign_up_img/cannot_match.png")
        Error = tk.Label(self.__root, image = error, borderwidth=0, highlightthickness=0).place(x = 273, y = 253)      
        Error.image = error
        
    def Error3(self):  
        password_unmatch = tk.PhotoImage(file="GUI/sign_up_img/doesnt_match.png")
        password_unmatch_Notification = tk.Label(self.__root, image = password_unmatch)
        password_unmatch_Notification.configure(bg ="#FFF7F3")
        password_unmatch_Notification.place(x=273, y=325)
        password_unmatch_Notification.configure(borderwidth=0, highlightthickness=0)
        password_unmatch_Notification.image = password_unmatch
        
        

    def sign_up_screen(self):
        #import picture
        background = tk.PhotoImage(file="GUI/sign_up_img/background_sign_up.png")    
        continue_img = tk.PhotoImage(file="GUI/sign_up_img/continue.png")


        label_background = tk.Label(self.__root, image=background)
        label_background.pack()

        #---------------------------------------------------------------------------------------------------------------------
        # Input User Name Sign up
        def Input_User_Name_Sign_Up(event):
            if  input_user_name_sign_up.get() == "User Name":
                input_user_name_sign_up.delete(0, "end") # Remove blurry text
                input_user_name_sign_up.configure(fg="#000000")
        def InputUserNameFocusOut(event):
            if not input_user_name_sign_up.get():
                input_user_name_sign_up.configure(fg="#A9A9A9") # Restore the color of the input box's watermark
                input_user_name_sign_up.insert(0, "User Name")
                
        user_name_sign_up = tk.StringVar()

        input_user_name_sign_up = tk.Entry(label_background, textvariable = user_name_sign_up, width=32,bg="#FFF9F5", fg="#A9A9A9", font=("Arial", 14))
        input_user_name_sign_up.insert(0, "User Name") # Insert opaque text into input_user_name_sign_up
        input_user_name_sign_up.bind("<FocusIn>", Input_User_Name_Sign_Up) # Attach event on click on input_user_name_sign_up
        input_user_name_sign_up.bind("<FocusOut>", InputUserNameFocusOut) # Hook event on hover out of input_user_name
        input_user_name_sign_up.place(x=290, y=210)
        input_user_name_sign_up.configure(borderwidth=0, highlightthickness=0)

        #---------------------------------------------------------------------------------------------------------------------
        # Input Password Sign Up
        def Input_Password_Sign_Up(event):
            if  input_password.get() == "Password":
                input_password.delete(0, "end") # Remove blurry text
                input_password.configure(fg="#000000")
                input_password.configure(show="*")
        def InputPasswordFocusOut(event):
            if not input_password.get():
                input_password.configure(fg="#A9A9A9") # Restore the color of the input box's watermark
                input_password.insert(0, "Password")
                input_password.configure(show="")

        password_sign_up = tk.StringVar()

        input_password = tk.Entry(label_background, textvariable = password_sign_up,width=32,bg="#FFF9F5", fg="#A9A9A9", font=("Arial", 14))
        input_password.insert(0, "Password") # Insert opaque text into input_password
        input_password.bind("<FocusIn>", Input_Password_Sign_Up) # Attach event on click on input_password
        input_password.bind("<FocusOut>", InputPasswordFocusOut) # Hook event on hover out of input_password
        input_password.place(x=290, y=285)
        input_password.configure(borderwidth=0, highlightthickness=0)

        #---------------------------------------------------------------------------------------------------------------------
        # Input Confirm Password Sign Up
        def Input_Confirm_Password_Sign_Up(event):
            if  input_cofirm_password_sign_up.get() == "Confirm Password":
                input_cofirm_password_sign_up.delete(0, "end") # Remove blurry text
                input_cofirm_password_sign_up.configure(fg="#000000")
                input_cofirm_password_sign_up.configure(show="*")
        def Input_Cofirm_Password_Sign_Up_FocusOut(event):
            if not input_cofirm_password_sign_up.get():
                input_cofirm_password_sign_up.configure(fg="#A9A9A9") # Restore the color of the input box's watermark
                input_cofirm_password_sign_up.insert(0, "Confirm Password")
                input_cofirm_password_sign_up.configure(show="")

        confirm_password_sign_up = tk.StringVar()

        input_cofirm_password_sign_up = tk.Entry(label_background, textvariable = confirm_password_sign_up,width=32,bg="#FFF9F5", fg="#A9A9A9", font=("Arial", 14))
        input_cofirm_password_sign_up.insert(0, "Confirm Password") # Insert opaque text into input_cofirm_password_sign_up
        input_cofirm_password_sign_up.bind("<FocusIn>", Input_Confirm_Password_Sign_Up) # Attach event on click on input_cofirm_password_sign_up
        input_cofirm_password_sign_up.bind("<FocusOut>", Input_Cofirm_Password_Sign_Up_FocusOut) # Hook event on hover out of input_cofirm_password_sign_up
        input_cofirm_password_sign_up.place(x=290, y=360)
        input_cofirm_password_sign_up.configure(borderwidth=0, highlightthickness=0)


        #---------------------------------------------------------------------------------------------------------------------

        con_button = partial(self.continue_click, user_name_sign_up, password_sign_up, confirm_password_sign_up)
        
        continue_button = tk.Button(label_background, image=continue_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0, command = con_button)
        continue_button.place(x=375, y=415)


        self.__root.mainloop()
        
    def continue_click2(self, input_name, input_dob, input_location, input_bio, gender):
        na = input_name.get()
        dob = input_dob.get()
        loca = input_location.get()
        bi = input_bio.get()
        if bi == "Tell something in your Bio..." or bi == '':
            bi = "Looking for short/long-term dating and new friends."
        gen = gender[0]
        insert_info(na, dob, gen, loca, bi)
        #print("set info success")
        self.__root.destroy()
        next = basics_interests.BasicsAndInterests()
        next.Basic_Infor()


    #Create user informations
    def Infor_screen(self):
        background_img = tk.PhotoImage(file = "GUI/sign_up_img/profile_information_img/new_bg.png")
        continue_img = tk.PhotoImage(file="GUI/sign_up_img/profile_information_img/continue.png")
        male_img = tk.PhotoImage(file="GUI/sign_up_img/profile_information_img/male.png")
        female_img = tk.PhotoImage(file="GUI/sign_up_img/profile_information_img/female.png")
        les_img = tk.PhotoImage(file="GUI/sign_up_img/profile_information_img/les.png")
        gay_img = tk.PhotoImage(file="GUI/sign_up_img/profile_information_img/gay.png")
        bi_img = tk.PhotoImage(file="GUI/sign_up_img/profile_information_img/bi.png")
        
        male_click_img = tk.PhotoImage(file="GUI/sign_up_img/profile_information_img/male_click.png")
        female_click_img = tk.PhotoImage(file="GUI/sign_up_img/profile_information_img/female_click.png")
        les_click_img = tk.PhotoImage(file="GUI/sign_up_img/profile_information_img/les_click.png")
        gay_click_img = tk.PhotoImage(file="GUI/sign_up_img/profile_information_img/gay_click.png")
        bi_click_img = tk.PhotoImage(file="GUI/sign_up_img/profile_information_img/bi_click.png")

        

        label_background = tk.Label(self.__root, image=background_img)
        label_background.place(x = 0, y = 0)
        #--------------------------------------------------------------------------------------------------------------------

        gender = ['None']
        
        def MALE():
            gender[0] = "Male"
            Label(self.__root, image=male_click_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0).place(x = 718, y= 250)
        def FEMALE():
            gender[0] = "Female"
            Label(self.__root, image=female_click_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0).place(x = 718, y= 250)
        def LES():
            gender[0] = "Les"
            Label(self.__root, image=les_click_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0).place(x = 720, y= 251)
        def GAY():
            gender[0] = "Gay"
            Label(self.__root, image=gay_click_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0).place(x = 719, y= 250)
        def BI():
            gender[0] = "Bi-sexual"
            Label(self.__root, image=bi_click_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0).place(x = 720, y= 250)
        

        male_button = tk.Button(label_background, image=male_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0, command = MALE)
        male_button.place(x = 480, y= 177)

        female_button = tk.Button(label_background, image=female_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0, command= FEMALE)
        female_button.place(x = 600, y= 180)

        les_button = tk.Button(label_background, image=les_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0, command= LES)
        les_button.place(x = 720, y= 179)

        gay_button = tk.Button(label_background, image=gay_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0, command= GAY)
        gay_button.place(x = 485, y= 250)

        bi_button = tk.Button(label_background, image=bi_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0, command= BI)
        bi_button.place(x = 598, y= 250)


        #--------------------------------------------------------------------------------------------------------------------
        def Input_Name(event):
            if  input_name.get() == "Full Name":
                input_name.delete(0, "end") # Remove blurry text
                input_name.configure(fg="#000000")
        def Input_Name_Focus_Out(event):
            if not input_name.get():
                input_name.configure(fg="#A9A9A9") # Restore the color of the input box's watermark
                input_name.insert(0, "Full Name")
        name = tk.StringVar()
        input_name = tk.Entry(label_background, textvariable = name, width=29,bg="#FFFDFC", fg="#A9A9A9", font=("Arial", 14))  
        input_name.insert(0, "Full Name") # Insert opaque text into input_name
        input_name.bind("<FocusIn>", Input_Name) # Attach event on click on input_name
        input_name.bind("<FocusOut>", Input_Name_Focus_Out) # Hook event on hover out of input_user_name
        input_name.place(x=74, y=196)
        input_name.configure(borderwidth=0, highlightthickness=0)

        #--------------------------------------------------------------------------------------------------------------------
        def Input_dob(event):
            if  input_dob.get() == "DOB (YYYY-MM-DD)":
                input_dob.delete(0, "end")
                input_dob.configure(fg="#000000")
        def Input_dob_Focus_Out(event):
            if not input_dob.get():
                input_dob.configure(fg="#A9A9A9")
                input_dob.insert(0, "DOB (YYYY-MM-DD)")
        dob = tk.StringVar()
    
        input_dob = tk.Entry(label_background, textvariable=dob, width=29, bg="#FFFDFC", fg ="#A9A9A9", font=("Arial, 14"))
        input_dob.insert(0, "DOB (YYYY-MM-DD)")
        input_dob.bind("<FocusIn>", Input_dob)
        input_dob.bind("<FocusOut>", Input_dob_Focus_Out)
        input_dob.place(x = 74, y = 270)
        input_dob.configure(borderwidth=0, highlightthickness=0)
        #--------------------------------------------------------------------------------------------------------------------
        def Input_Location(event):
            if input_location.get() == "Location":
                input_location.delete(0, "end")
                input_location.configure(fg = "#000000")
        def Input_Location_Focus_Out(event):
            if not input_location.get():
                input_location.configure(fg="#A9A9A9")
                input_location.insert(0,"Location")
        location = tk.StringVar()

        input_location = tk.Entry(label_background, textvariable=location, width=29,bg ="#FFFDFC", fg= "#A9A9A9", font=("Arial", 14))
        input_location.insert(0, "Location")
        input_location.bind("<FocusIn>", Input_Location)
        input_location.bind("<FocusOut>", Input_Location_Focus_Out)
        input_location.place(x = 74, y= 344)
        input_location.configure(borderwidth=0, highlightthickness=0)

        #--------------------------------------------------------------------------------------------------------------------
        
        def Input_Some_Thing_Bio(event):
            if input_bio.get() == "Tell something in your Bio...":
                input_bio.delete(0, "end")
                input_bio.configure(fg = "#000000")
        def Input_Some_Thing_Bio_Focus_Out(event):
            if not input_bio.get():
                input_bio.configure(fg="#A9A9A9")
                input_bio.insert(0,"Tell something in your Bio...")
        bio = tk.StringVar()

        input_bio = tk.Entry(label_background, textvariable = bio, width=28,bg ="#FFF3EC", fg= "#A9A9A9", font=("Arial", 14))
        input_bio.insert(0, "Tell something in your Bio...")
        input_bio.bind("<FocusIn>", Input_Some_Thing_Bio)
        input_bio.bind("<FocusOut>", Input_Some_Thing_Bio_Focus_Out)
        input_bio.place(x = 502, y= 360)
        input_bio.configure(borderwidth=0, highlightthickness=0)



        conti_button = partial(self.continue_click2, name, dob, location, bio, gender)
        
        continue_button = tk.Button(label_background, image=continue_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0, command = conti_button)
        continue_button.place(x=151, y=396)

        self.__root.mainloop()