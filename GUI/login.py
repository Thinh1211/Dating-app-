import tkinter as tk
from functools import partial
from database_controller import show_account, get_password_w_username, delete_user
from GUI import sign_up
from GUI import secure

class Login:
    def __init__(self):
        self.__user_id = 0
        self.__status = "none"
        
        self.__root = tk.Tk()  # Create new window
        
        self.__root.geometry('900x500')
        self.__root.resizable(width=False, height=False)
        
        def on_closing():
            if tk.messagebox.askokcancel("Quit", "Do you want to quit?"):
                self.__root.destroy()
                self.__status = "exit"

        self.__root.protocol("WM_DELETE_WINDOW", on_closing)
                
    def get_user_id(self):
        return self.__user_id
    
    def get_status(self):
        return self.__status
    
    def confirm_click(self, username, password):
        un = username.get()
        pw = password.get()
        accounts = show_account()
        for account in accounts:
            if un == account[1] and pw == secure.decode(account[2]):
                print("login success")
                isSuccess = True
                self.__user_id = account[0]
                self.__status = "login success"
                self.__root.destroy()
            else:
                isSuccess = False
        if isSuccess == False:
            self.confirm_error()
                
    def confirm_error(self):
        error = tk.PhotoImage(file = "GUI/login_img/Error_message.png")
        Error = tk.Label(self.__root, image = error, borderwidth = 0, highlightthickness = 0).place(x = 80, y = 140)
        Error.image = error
        
    def sign_up_click(self):
        self.__root.destroy()
        sign_up.Sign_up().sign_up_screen()

    def forgot_password_click(self):
        if tk.messagebox.askokcancel("Forgot password", "Please contact admin! Enter admin mode?"):
            self.__root.destroy()
            self.__init__()   
            self.__root.title("ADMIN MODE") 
                        
            label = tk.Label(self.__root, text= "Enter andmin password: ", font= ("Arial", 20))
            label.place(relx=0.5, rely=0.40, anchor='center')
            
            password = tk.Entry(self.__root, font= ("Arial", 20), show= "*")
            password.place(relx=0.5, rely=0.5, anchor='center')

            
            def confirm_click():
                if password.get() != secure.decode("00 0 0 00 00 000 0 0 00 0 0 00 00 00 0 0 00 00 0 00 00 00 0 00 00 0 0 00 00 0 0 0 00 000 0 00 00 0 0 0 00 0 0 0 00 0 0 00 00 0 0 00 00 0"):
                    tk.messagebox.showinfo("", "Wrong password!!!")
                    self.__root.destroy()
                else:
                    label.destroy()
                    password.destroy()
                    confirm.destroy()
                    
                    new_label = tk.Label(self.__root, text= "Enter username: ", font= ("Arial", 20))
                    new_label.place(relx=0.5, rely=0.40, anchor='center')
                    
                    username = tk.Entry(self.__root, font= ("Arial", 20))
                    username.place(relx=0.5, rely=0.5, anchor='center')
                    
                    def confirm2_click():     
                        try:                  
                            un = username.get()
                            password = "password: " + secure.decode(get_password_w_username(un))
                        except IndexError:
                            password = "unknow username"
                        
                        show_pass = tk.Label(self.__root, text= " "*1000 + password + " "*1000, font= ("Arial", 20))
                        show_pass.place(relx=0.5, rely=0.30, anchor='center')
                        

                    def ban_click():

                        new_label.destroy()
                        username.destroy()
                        new_confirm.destroy()
                        ban_button.destroy()

                        new_layer = tk.Label(self.__root, text= " "*2000, font= ("Arial", 20))
                        new_layer.place(relx=0.5, rely=0.30, anchor='center')

                        def ban_click():
                            delete_id = delete_id_label.get()
                            if tk.messagebox.askokcancel("DELETE USER", "Are you sure to delete user with id " + delete_id + "?"):
                                delete_user(delete_id)

                                success = tk.Label(self.__root, text= "Delete successfull", font= ("Arial", 20))
                                success.place(relx= 0.5, rely= 0.3, anchor= "center")

                        ban_label = tk.Label(self.__root, text= "Enter User ID: ", font= ("Arial", 20))
                        ban_label.place(relx= 0.5, rely= 0.4, anchor="center")
                        delete_id_label = tk.Entry(self.__root, font= ("Arial", 20))
                        delete_id_label.place(relx=0.5, rely=0.5, anchor='center')
                        ban_confirm = tk.Button(self.__root, text = "CONFIRM", font= ("Arial", 20), command= partial(ban_click))
                        ban_confirm.place(relx= 0.5, rely= 0.6, anchor='center')
                    
                    new_confirm = tk.Button(self.__root, text = "CONFIRM", font= ("Arial", 20), command= partial(confirm2_click))
                    new_confirm.place(relx=0.5, rely=0.60, anchor='center')

                    ban_button = tk.Button(self.__root, text= "Delete Account", font= ("Arial", 20), command= partial(ban_click))
                    ban_button.place(relx= 0.5, rely= 0.7, anchor= "center")
              
                    
            confirm = tk.Button(self.__root, text = "CONFIRM", font= ("Arial", 20), command= partial(confirm_click))
            confirm.place(relx=0.5, rely=0.60, anchor='center')
                        
            self.__root.mainloop()  
            

    def login_screen(self):
        
        self.__root.title('Sign In')
        
        background = tk.PhotoImage(file="GUI/login_img/Background.png")                 # Export Background image from available photo library
        sign_up = tk.PhotoImage(file="GUI/login_img/Sign_up_button.png")                     # Export Sign image from available photo library
        confirm = tk.PhotoImage(file="GUI/login_img/Confirm_button.png")                     # Export Confirm image from available photo library
        forgot_password = tk.PhotoImage(file="GUI/login_img/Forgot_password_button.png")    # Export Forgot Password image from available photo library


        #------------------------------------------------------
        label_background = tk.Label(self.__root, image=background)
        label_background.pack()
        
        #------------------------------------------------------
        
        def InputUserName(event):
            if input_user_name.get() == "User Name":
                input_user_name.delete(0, "end") # Remove blurry text
                input_user_name.configure(fg="#000000")
        def InputUserNameFocusOut(event):
            if not input_user_name.get():
                input_user_name.configure(fg="#A9A9A9") # Restore the color of the input box's watermark
                input_user_name.insert(0, "User Name")

        username = tk.StringVar()

        input_user_name = tk.Entry(label_background, textvariable = username, width=25, fg="#A9A9A9", font=("Arial", 14))
        input_user_name.insert(0, "User Name") # Insert opaque text into input_user_name
        input_user_name.bind("<FocusIn>", InputUserName) # Attach event on click on input_user_name
        input_user_name.bind("<FocusOut>", InputUserNameFocusOut) # Hook event on hover out of input_user_name
        input_user_name.place(x=95, y=175)
        input_user_name.configure(borderwidth=0, highlightthickness=0)

        #------------------------------------------------------
        
        def InputPassword(event):
            if input_password.get() == "Password":
                input_password.delete(0, "end") # Remove blurry text
                input_password.configure(fg="#000000", show = "*")
        def InputPasswordFocusOut(event):
            if not input_password.get():
                input_password.configure(fg="#A9A9A9") # Restore the color of the input box's watermark
                input_password.insert(0, "Password")
                input_password.configure(show="")

        password = tk.StringVar()

        input_password = tk.Entry(label_background, textvariable = password, width=25, fg="#A9A9A9", font=("Arial", 14))
        input_password.insert(0, "Password") # Insert opaque text into input_password
        input_password.bind("<FocusIn>", InputPassword) # Attach event on click on input_password
        input_password.bind("<FocusOut>", InputPasswordFocusOut) # Hook event on hover out of input_password
        input_password.place(x=95, y=260)
        input_password.configure(borderwidth=0, highlightthickness=0)

        #------------------------------------------------------
        signup = partial(self.sign_up_click)
        
        sign_up_button = tk.Button(label_background, image=sign_up, borderwidth=0, highlightthickness=0, command = signup)
        sign_up_button.place(x=291, y=462)
        sign_up_button.configure(highlightthickness=0)

        con_button = partial(self.confirm_click, username, password)
        confirm_button = tk.Button(label_background, image=confirm, borderwidth=0, highlightthickness=0, command = con_button)
        confirm_button.place(x=230, y=330)
        confirm_button.configure(highlightthickness=0)

        forgot_password_button = tk.Button(label_background, image=forgot_password, bg = "#F4E0EA",  borderwidth=0, highlightthickness=0, command = self.forgot_password_click, activebackground="#F4E0EA")
        forgot_password_button.place(x=89, y=348)
        forgot_password_button.configure(highlightthickness=0)

        self.__root.mainloop()    