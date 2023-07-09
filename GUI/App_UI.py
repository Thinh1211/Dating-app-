from functools import partial
from tkinter import *
from tkinter import ttk
from tkextrafont import Font
import datetime
from io import BytesIO
from math import floor, ceil
from PIL import Image, ImageTk
from database_controller import show_info, show_basics, show_interests, show_photo, show_matched, show_name
from Matching_Controller import Randomize, Match

class User:
    def __init__(self, user_id, status):
        self.__status = status
        self.__user_id = user_id
        self.__root = Tk()
        self.__root.geometry('1920x1080')
        self.__root.resizable(width=False, height=False)
        self.__root.attributes('-fullscreen', True)
        self.__font = Font(file="GUI/MAIN/Be_Vietnam_Pro/BeVietnamPro-ExtraBold.ttf")
        
        self.__img_index = 0
    def return_status(self):
        return self.__status

    def exit_click(self): 
        self.__status = "exit"
        self.__root.destroy()
        
    def matching_click(self):
        self.__status = "matching"
        self.Profile_screen()
        
    def profile_click(self):
        self.__status = "profile"
        self.Profile_screen()
        
    def chat_click(self):
        self.__status = "chat"
        isMatch = Match(self.__user_id)
        isMatch.isMatch()
        self.Chat_Screen()
        
        
    #Show profile method
    def Profile_screen(self):
        background = PhotoImage(file="GUI/MAIN/match_img/background.png")

        label_background = Label(self.__root, image = background)
        label_background.place(x = 0, y = 0)
        
        refresh_img = PhotoImage(file="GUI/MAIN/match_img/refresh.png")
        #----------------------------------------------------------------------------------------------------------------------------
        # Taskbar no click
        profile_img = PhotoImage(file="GUI/MAIN/match_img/task_bar_img/taskbar/open_profile_button.png")
        matching_img = PhotoImage(file="GUI/MAIN/match_img/task_bar_img/taskbar/open_matching_button.png")
        chat_img = PhotoImage(file="GUI/MAIN/match_img/task_bar_img/taskbar/open_chat_button.png")
        exit_img = PhotoImage(file="GUI/MAIN/match_img/task_bar_img/taskbar/exit_button.png")

        # Taskbar click
        profile_click_img = PhotoImage(file="GUI/MAIN/match_img/task_bar_img/taskbar_click/open_profile_button_click.png")
        matching_click_img = PhotoImage(file="GUI/MAIN/match_img/task_bar_img/taskbar_click/open_match_button_click.png")
        #----------------------------------------------------------------------------------------------------------------------------
        # LIKE - DISLIKE - CHANGE IMG
        like_img = PhotoImage(file="GUI/MAIN/match_img/button_in_match_img/like.png")
        dislike_img = PhotoImage(file="GUI/MAIN/match_img/button_in_match_img/dislike.png")
        change_img = PhotoImage(file="GUI/MAIN/match_img/button_in_match_img/swap.png")
        
        #----------------------------------------------------------------------------------------------------------------------------
        
        def display(i):
            refresh = Label(self.__root, image = refresh_img, borderwidth=0, highlightthickness=0)
            refresh.place(x = 1095, y = 270)
            refresh.image = refresh_img
            #display info
            info = show_info(i)
            name_data = info[0].split(' ')
            
            age_datas = info[1].split('-')
            today = datetime.date.today()
            year = today.year
            age_data = - int(age_datas[0]) + int(year)
            
            bio_data = info[4]
            
            gender_data = info[2]
            
            location_data = info[3]
            
            name = StringVar()
            name.set("About " + name_data[-1])
            Label(self.__root, textvariable = name, bg = "#FFEEF6", fg="#4E4E4E", font=(self.__font, 19, "bold")).place(x = 1120, y = 365)
            
            age = StringVar()
            age.set(name_data[-1] + ", " + str(age_data))
            Label(self.__root, textvariable = age, bg = "#FFEEF6", fg="#4E4E4E", font=(self.__font, 35, "bold")).place(x = 1117, y = 280)
            
            bio = StringVar()
            bio.set(bio_data)
            Label(self.__root, textvariable=bio, wraplengt = 400, justify= "left", bg = "#FFEEF6", fg="#4E4E4E", font=(self.__font, 13, "bold")).place(x = 1140, y = 430)
            
            gender = StringVar()
            gender.set(gender_data)
            Label(self.__root, textvariable=gender, bg = "#FFEEF6", fg="#4E4E4E", font=(self.__font, 16, "bold")).place(x = 1170, y = 562)
            
            location = StringVar()
            location.set(location_data)
            Label(self.__root, textvariable=location, bg = "#FFEEF6", fg="#4E4E4E", font=(self.__font, 16, "bold")).place(x = 1370, y = 615)
            
            #----------------------------------------------------------------------------------------------------------------------------
            #display basics
            basic = show_basics(i)
            
            height_data = basic[0]
            
            zodiac_data = basic[2]
            
            education_data = basic[3]
            
            workout_data = basic[4]
            
            smoke_data = basic[5]
            
            drink_data = basic[6]
            
            height = StringVar()
            height.set(height_data)
            Label(self.__root, textvariable = height, bg = "#FFEEF6", fg="#4E4E4E", font=(self.__font, 16, "bold")).place(x = 1170, y = 615)  
            
            zodiac = StringVar()
            zodiac.set(zodiac_data)
            Label(self.__root, textvariable = zodiac, bg = "#FFEEF6", fg="#4E4E4E", font=(self.__font, 16, "bold")).place(x = 1370, y = 742)     
            
            education = StringVar()
            education.set(education_data)
            Label(self.__root, textvariable = education, bg = "#FFEEF6", fg="#4E4E4E", font=(self.__font, 16, "bold")).place(x = 1370, y = 562)    
            
            workout = StringVar()
            workout.set(workout_data)
            Label(self.__root, textvariable = workout, bg = "#FFEEF6", fg="#4E4E4E", font=(self.__font, 16, "bold")).place(x = 1170, y = 742)     
            
            smoke = StringVar()
            smoke.set(smoke_data)
            Label(self.__root, textvariable = smoke, bg = "#FFEEF6", fg="#4E4E4E", font=(self.__font, 16, "bold")).place(x = 1370, y = 679)  
            
            drink = StringVar()
            drink.set(drink_data)
            Label(self.__root, textvariable = drink, bg = "#FFEEF6", fg="#4E4E4E", font=(self.__font, 16, "bold")).place(x = 1170, y = 679)    
                    
            #----------------------------------------------------------------------------------------------------------------------------
            #display interests
            interests = show_interests(i)
            
            interest1 = PhotoImage(file="GUI/MAIN/match_img/interest_match_img/All_img/" + interests[0] + ".png")
            inter_img1 = Label(self.__root, image= interest1, borderwidth=0, highlightthickness=0)
            inter_img1.place(x = 1120, y = 800)
            inter_img1.image = interest1
            
            interest2 = PhotoImage(file="GUI/MAIN/match_img/interest_match_img/All_img/" + interests[1] + ".png")
            inter_img2 = Label(self.__root, image= interest2, borderwidth=0, highlightthickness=0)
            inter_img2.place(x = 1320, y = 800)
            inter_img2.image = interest2
            
            interest3 = PhotoImage(file="GUI/MAIN/match_img/interest_match_img/All_img/" + interests[2] + ".png")
            inter_img3 = Label(self.__root, image= interest3, borderwidth=0, highlightthickness=0)
            inter_img3.place(x = 1119, y = 870) 
            inter_img3.image = interest3
            
            interest4 = PhotoImage(file="GUI/MAIN/match_img/interest_match_img/All_img/" + interests[3] + ".png")
            inter_img4 = Label(self.__root, image= interest4, borderwidth=0, highlightthickness=0)
            inter_img4.place(x = 1119, y = 940) 
            inter_img4.image = interest4
            
            interest5 = PhotoImage(file="GUI/MAIN/match_img/interest_match_img/All_img/" + interests[4] + ".png")
            inter_img5 = Label(self.__root, image= interest5, borderwidth=0, highlightthickness=0)
            inter_img5.place(x = 1321, y = 870)  
            inter_img5.image = interest5
            
            #change image button
            change = Button(self.__root, image=change_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0, command= partial(change_image, i))
            change.place(x = 900, y = 610)
            
        #----------------------------------------------------------------------------------------------------------------------------
        self.__img_index = 0
        #display photos
        def show_image(i):  
             
            def resize_img(width, height):
                wid = floor(width/585)
                hei = floor(height/796)
                ration = min(wid, hei)
                return ration
            
            def resize_img2(width, height):
                wid = ceil(585/width)
                hei = ceil(796/height)
                ration = min(wid, hei)
                return ration
            
            imgs = show_photo(i)
            img = Image.open(BytesIO(imgs[self.__img_index]))
            wi, he = img.size 
            if wi < 585 or he < 796:
                ration = resize_img2(wi, he)
                new_wid = int(wi*ration)
                new_hei = int(he*ration)
            else:
                ration = resize_img(wi, he)
                new_wid = int(wi/ration)
                new_hei = int(he/ration)
            img_resized = img.resize((new_wid, new_hei))
            left = (new_wid - 585)/2
            right = new_wid - (new_wid - 585)/2
            upper = (new_hei - 796)/2
            lower = new_hei - (new_hei - 796)/2
            img_resized = img_resized.crop([left, upper, right, lower])
            
            photo = ImageTk.PhotoImage(img_resized)        
            Photo = Label(self.__root, image= photo, borderwidth=0, highlightthickness=0)
            Photo.place(x = 305, y = 226)
            Photo.image = photo
        
        #display photos when click the change image button
        def change_image(i):    
            self.__img_index += 1
            if self.__img_index == 3: self.__img_index = 0      
                    
            show_image(i) 
        
        #----------------------------------------------------------------------------------------------------------------------------
        #display button
        exit_button = Button(self.__root, image = exit_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0, command= partial(self.exit_click))
        exit_button.place(x = 5, y = 980)
        
        profile_button = Button(self.__root, image = profile_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0, command= partial(self.profile_click))
        profile_button.place(x = 5, y = 300)
        
        matching_button = Button(self.__root, image = matching_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0, command= partial(self.matching_click))
        matching_button.place(x = 5, y = 500)
        
        chat_button = Button(self.__root, image = chat_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0, command= partial(self.chat_click))
        chat_button.place(x= 5, y = 700)
            
        match self.__status:
            case "profile":
                profile_button = Button(self.__root, image = profile_click_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
                profile_button.place(x = 5, y = 300)
                            
                edit_prof_img = PhotoImage(file = "GUI/MAIN/match_img/edit_profile_img.png")    
                edit_profile_button = Button(self.__root, image = edit_prof_img , bg="#FFFFFF", borderwidth=0, highlightthickness=0)
                edit_profile_button.place(x = 900, y = 450)       
                
                display(self.__user_id)
                show_image(self.__user_id)
            case "matching":
                random_id = Randomize(self.__user_id)
                self.__match_id = int(random_id.getMultiRandom())
                
                matching_button = Button(self.__root, image = matching_click_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
                matching_button.place(x = 5, y = 500)
                if self.__match_id != self.__user_id:
                    display(self.__match_id)
                    self.__img_index = 0
                    show_image(self.__match_id)

                    
                    def like_click():
                        random_id.setLike(self.__match_id)
                        
                        self.__match_id = int(random_id.getMultiRandom())
                        if self.__match_id == self.__user_id: self.profile_click()
                                               
                        display(self.__match_id)
                        self.__img_index = 0
                        show_image(self.__match_id)
                        
                    def dislike_click():
                        random_id.setDisliked(self.__match_id)
                        self.__match_id= int(random_id.getMultiRandom())
                        if self.__match_id == self.__user_id: self.profile_click()
                        
                        display(self.__match_id)
                        self.__img_index = 0
                        show_image(self.__match_id)
                    
                    like = Button(self.__root, image=like_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0, command= partial(like_click))
                    like.place(x = 900, y = 450)

                    dislike = Button(self.__root, image=dislike_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0, command= partial(dislike_click))
                    dislike.place(x = 900, y = 780)
        
        self.__root.mainloop()


    #Create chat screen
    def Chat_Screen(self):        
        background = PhotoImage(file="GUI/MAIN/chat_img/chat_background.png")
    
        label_background = Label(self.__root, image = background)
        label_background.place(x = 0, y = 0)
        
        #-------------------------------------------------------------------------------------------------------------------------------------------------
        # Taskbar no click -- img
        profile_img = PhotoImage(file="GUI/MAIN/chat_img/task_bar_img/taskbar/open_profile_button.png")
        matching_img = PhotoImage(file="GUI/MAIN/chat_img/task_bar_img/taskbar/open_matching_button.png")
        exit_img = PhotoImage(file="GUI/MAIN/chat_img/task_bar_img/taskbar/exit_button.png")
        # Taskbar click -- img
        chat_click_img = PhotoImage(file="GUI/MAIN/chat_img/task_bar_img/taskbar_click/open_chat_button_click.png")

        #--------------------------------------------------------------------------------------------------------------------------------------------------
        #SEND IMAGE -- ICON -- MESSAGE img
        open_image_img = PhotoImage(file="GUI/MAIN/chat_img/image_icon_send_img/open_image.png")
        open_icon_img = PhotoImage(file="GUI/MAIN/chat_img/image_icon_send_img/open_icon.png")    
        send_message_img = PhotoImage(file="GUI/MAIN/chat_img/image_icon_send_img/send_message.png")

        #--------------------------------------------------------------------------------------------------------------------------------------------------
        # Taskbar
        exit_button = Button(self.__root, image = exit_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0, command= partial(self.exit_click))
        exit_button.place(x = 5, y = 980)
        
        profile_button = Button(self.__root, image = profile_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0, command= partial(self.profile_click))
        profile_button.place(x = 5, y = 300)
        
        matching_button = Button(self.__root, image = matching_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0, command= partial(self.matching_click))
        matching_button.place(x = 5, y = 500)

        chat_click =  Button(self.__root, image=chat_click_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
        chat_click.place(x = 5, y = 700) 
        
        #--------------------------------------------------------------------------------------------------------------------------------------------------
        # Create a small scrollable window to display user conversation
        
        canvas = Canvas(self.__root, height= 820, width= 370, bg = "#FFFFFF", borderwidth=0, highlightthickness=0)
        scrollbar = Scrollbar(self.__root, orient='vertical', command=canvas.yview)
        scrollbar.config(width = 0, highlightthickness=0) #make the scroll bar invisible
        scrollbar.pack(side='right', fill='y')
        canvas.config(yscrollcommand=scrollbar.set)
        canvas.place(x = 190, y = 215)

        # Create a frame inside the canvas to hold the content
        inner_frame = Frame(canvas)
        canvas.create_window((0,0), window=inner_frame, anchor='nw')

        # Bind the MouseWheel event to the canvas
        def on_mousewheel(event):
            canvas.yview_scroll(int(-1*(event.delta/120)), 'units')

        # Bind the MouseEnter and MouseLeave events of the inner frame
        is_mouse_inside = False
        def enable_scroll(event):
            global is_mouse_inside
            is_mouse_inside = True
            canvas.bind_all('<MouseWheel>', on_mousewheel)
        def disable_scroll(event):
            global is_mouse_inside
            is_mouse_inside = False
            canvas.unbind_all('<MouseWheel>')

        inner_frame.bind('<Enter>', enable_scroll)
        inner_frame.bind('<Leave>', disable_scroll)

        # Check if the mouse is inside the inner frame when scrolling
        def check_scroll_region(event):
            if is_mouse_inside:
                canvas.yview_scroll(int(-1*(event.delta/120)), 'units')

        # Bind the MouseWheel event to the canvas and the inner frame
        canvas.bind('<MouseWheel>', check_scroll_region)
        
        # Person who chat with you 
        try:
            matched_lists = show_matched(self.__user_id)[0]
            matched_list = matched_lists[0].split(" ")
            
            for i in range(len(matched_list)):
                # Get information
                name = show_name(matched_list[i])[0]
                avatar = Image.open(BytesIO(show_photo(matched_list[i])[0]))
                
                
                # Resize the avatar image as needed
                def resize_img(width, height):
                    wid = floor(width/100)
                    hei = floor(height/100)
                    ration = min(wid, hei)
                    return ration
                
                def resize_img2(width, height):
                    wid = ceil(100/width)
                    hei = ceil(100/height)
                    ration = min(wid, hei)
                    return ration
                
                wi, he = avatar.size 
                if wi < 100 or he < 100:
                    ration = resize_img2(wi, he)
                    new_wid = int(wi*ration)
                    new_hei = int(he*ration)
                else:
                    ration = resize_img(wi, he)
                    new_wid = int(wi/ration)
                    new_hei = int(he/ration)
                img_resized = avatar.resize((new_wid, new_hei))
                left = (new_wid - 100)/2
                right = new_wid - (new_wid - 100)/2
                upper = (new_hei - 100)/2
                lower = new_hei - (new_hei - 100)/2
                img_resized = img_resized.crop([left, upper, right, lower])
                avatar_photo = ImageTk.PhotoImage(img_resized) 
                
                
                # Create user button
                style = ttk.Style()
                style.configure('Modern.TButton', foreground= '#4E4E4E', maxwidth= 370, maxheight= 114, font=(self.__font, 19, "bold"), anchor= "w")
                style.map('Modern.TButton',
                        foreground=[('active', '#FBA2D0'), ('focus', '#FBA2D0')],
                        background=[('active', '#FFA270'), ('focus', '#FFA270')]
                )

                who_chat = ttk.Button(inner_frame, text= name, image=avatar_photo, compound= "left")
                who_chat.grid(row=i, column=0, sticky="nsew")
                who_chat.config(style='Modern.TButton')
                who_chat.image = avatar_photo
                                       
        except IndexError:
            pass
        
        
        if len(matched_list) > 7:
            # Update the geometry of the inner frame and canvas
            inner_frame.update_idletasks()
            canvas.config(scrollregion=canvas.bbox('all'))
        else:
            # Calculate the height of the inner frame
            inner_frame.update_idletasks()
            frame_height = inner_frame.winfo_height()

            # Set the height of the canvas
            canvas.config(scrollregion=canvas.bbox('all'), height=frame_height)
                    
        #--------------------------------------------------------------------------------------------------------------------------------------------------
        # Face user chat
        # face_user_chat = Label(self.__root, image=face_user_chat_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
        # face_user_chat.place(x = 640, y = 225)    
        
        # OPEN IMAGE -- ICON -- SEND MESSAGE Button
        open_image= Button(self.__root, image=open_image_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
        open_image.place(x = 1450, y = 930)    

        open_icon = Button(self.__root, image=open_icon_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)  
        open_icon.place(x = 1570, y = 930)    

        send_message = Button(self.__root, image=send_message_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
        send_message.place(x = 1680, y = 920)    

        #--------------------------------------------------------------------------------------------------------------------------------------------------
        
        self.__root.mainloop()