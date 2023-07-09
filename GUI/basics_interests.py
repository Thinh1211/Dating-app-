import tkinter as tk
import textwrap
from functools import partial
from tkinter import *
from database_controller import show_info, insert_baiscs, insert_interest, show_new_added_dob
from GUI import upload_images

class BasicsAndInterests:
    def __init__(self):
        self.__root = tk.Tk()
        self.__root.title("Basics Information")

        self.__root.geometry('1280x720')
        self.__root.resizable(width=False, height=False)
        
        self.__workout = "None"
        self.__smoke = "None"
        self.__education = "None"
        self.__education_index = 0
        self.__drink = "None"

    def continue_click(self, input_height, input_weight, zodiac, workout, smoke, drink, education):
        he = input_height.get()
        we = input_weight.get()
        wo = self.__workout
        smo = self.__smoke
        dri = self.__drink
        edu = self.__education
        #print("set up basics success")
        insert_baiscs(he, we, zodiac, edu, wo, smo, dri)
        self.__root.destroy()
        self.__init__()
        self.Interest_Screen()


    def Basic_Infor(self):
        
        background = tk.PhotoImage(file="GUI/sign_up_img/basic_information_img/back_ground_basic_information.png")
        education_img = tk.PhotoImage(file="GUI/sign_up_img/basic_information_img/Education_img/education_img.png")
        continue_img = tk.PhotoImage(file="GUI/sign_up_img/basic_information_img/continue.png")


        label_background = tk.Label(self.__root, image = background)
        label_background.pack()
        # SKIP img of WorkOut,Smoke,Drink
        wo_smoke_drink_skip_img = tk.PhotoImage(file="GUI/sign_up_img/basic_information_img/wo_smoke_drink_skip.png")
        wo_smoke_drink_skip_push__img = tk.PhotoImage(file="GUI/sign_up_img/basic_information_img/wo_smoke_drink_skip_push.png")




        #---------------------------------------------------------------------------------------------------------------------------------
        # Workout NO PUSH
        wo_active_img = tk.PhotoImage(file="GUI/sign_up_img/basic_information_img/wo_img/wo_no_push/wo_active.png")
        wo_sometimes_img = tk.PhotoImage(file="GUI/sign_up_img/basic_information_img/WO_img/wo_no_push/wo_sometimes.png")
        wo_almost_never_img = tk.PhotoImage(file="GUI/sign_up_img/basic_information_img/wo_img/wo_no_push/wo_almost_never.png")
        
        # Workout PUSH
        wo_active_push_img = tk.PhotoImage(file="GUI/sign_up_img/basic_information_img/wo_img/wo_push/wo_active_push.png")
        wo_sometimes_push_img = tk.PhotoImage(file="GUI/sign_up_img/basic_information_img/wo_img/wo_push/wo_sometimes_push.png")
        wo_almost_push_never_img = tk.PhotoImage(file="GUI/sign_up_img/basic_information_img/wo_img/wo_push/wo_almost_never_push.png")
        
        
        def wo_active_click():
            wo_active_push = tk.Button(self.__root, image=wo_active_push_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
            wo_active_push.place(x=171,y=475)
            
            wo_sometimes = tk.Button(self.__root, image=wo_sometimes_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0, command= wo_sometimes_clickk)
            wo_sometimes.place(x=171,y=525)
        
            wo_almost_never = tk.Button(self.__root, image=wo_almost_never_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0, command= wo_never_clickk)
            wo_almost_never.place(x=171,y=575)

            wo_skip_no_push = tk.Button(self.__root, image=wo_smoke_drink_skip_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0, command= wo_skip_clickk)
            wo_skip_no_push.place(x=171,y=625)
            
            self.__workout = "Active"
        wo_active_clickk = partial(wo_active_click)
        wo_active = tk.Button(self.__root, image=wo_active_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0, command= wo_active_clickk)
        wo_active.place(x=171,y=475)

        def wo_sometimes_click():
            wo_active = tk.Button(self.__root, image=wo_active_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0, command= wo_active_clickk)
            wo_active.place(x=171,y=475)
            
            wo_sometimes_push = tk.Button(self.__root, image=wo_sometimes_push_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
            wo_sometimes_push.place(x=171,y=525)
        
            wo_almost_never = tk.Button(self.__root, image=wo_almost_never_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0, command= wo_never_clickk)
            wo_almost_never.place(x=171,y=575)

            wo_skip_no_push = tk.Button(self.__root, image=wo_smoke_drink_skip_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0, command= wo_skip_clickk)
            wo_skip_no_push.place(x=171,y=625)
            
            self.__workout = "Sometimes"
        wo_sometimes_clickk = partial(wo_sometimes_click)
        wo_sometimes = tk.Button(self.__root, image=wo_sometimes_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0, command= wo_sometimes_clickk)
        wo_sometimes.place(x=171,y=525)
        
        def wo_never_click():
            wo_active = tk.Button(self.__root, image=wo_active_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0, command= wo_active_clickk)
            wo_active.place(x=171,y=475)
            
            wo_sometimes = tk.Button(self.__root, image=wo_sometimes_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0, command= wo_sometimes_clickk)
            wo_sometimes.place(x=171,y=525)
        
            wo_almost_push_never = tk.Button(self.__root, image=wo_almost_push_never_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
            wo_almost_push_never.place(x=171,y=575)

            wo_skip_no_push = tk.Button(self.__root, image=wo_smoke_drink_skip_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0, command= wo_skip_clickk)
            wo_skip_no_push.place(x=171,y=625)
            
            self.__workout = "Almost never"
        wo_never_clickk = partial(wo_never_click)
        wo_almost_never = tk.Button(self.__root, image=wo_almost_never_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0, command= wo_never_clickk)
        wo_almost_never.place(x=171,y=575)
        
        def wo_skip_click():
            wo_active = tk.Button(self.__root, image=wo_active_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0, command= wo_active_clickk)
            wo_active.place(x=171,y=475)
            
            wo_sometimes = tk.Button(self.__root, image=wo_sometimes_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0, command= wo_sometimes_clickk)
            wo_sometimes.place(x=171,y=525)
        
            wo_almost_never = tk.Button(self.__root, image=wo_almost_never_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0, command= wo_never_clickk)
            wo_almost_never.place(x=171,y=575)

            wo_skip_push = tk.Button(self.__root, image=wo_smoke_drink_skip_push__img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
            wo_skip_push.place(x=171,y=625)
            
            self.__workout = "None"
        wo_skip_clickk = partial(wo_skip_click)
        wo_skip_no_push = tk.Button(self.__root, image=wo_smoke_drink_skip_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0, command= wo_skip_clickk)
        wo_skip_no_push.place(x=171,y=625)



        #---------------------------------------------------------------------------------------------------------------------------------
        # Smoke NO PUSH
        smoke_socially_img = tk.PhotoImage(file="GUI/sign_up_img/basic_information_img/Smoke_img/smoke_no_push/smoke_socially.png")
        smoke_never_img = tk.PhotoImage(file="GUI/sign_up_img/basic_information_img/Smoke_img/smoke_no_push/never.png")
        smoke_regularly_img = tk.PhotoImage(file="GUI/sign_up_img/basic_information_img/Smoke_img/smoke_no_push/smoke_regularly.png")
        
        # Smoke PUSH
        smoke_socially_push_img = tk.PhotoImage(file="GUI/sign_up_img/basic_information_img/Smoke_img/smoke_push/smoke_socially_push.png")
        smoke_never_push_img = tk.PhotoImage(file="GUI/sign_up_img/basic_information_img/Smoke_img/smoke_push/never_push.png")
        smoke_regularly_push_img = tk.PhotoImage(file="GUI/sign_up_img/basic_information_img/Smoke_img/smoke_push/regularly_push.png")
        
        
        
        def smoke_social_click():
            smoke_socially_push = tk.Button(self.__root, image=smoke_socially_push_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
            smoke_socially_push.place(x=485,y=475)

            smoke_never = tk.Button(self.__root, image=smoke_never_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0, command= smoke_never_clickk)
            smoke_never.place(x=485,y=525)

            smoke_regularly = tk.Button(self.__root, image=smoke_regularly_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0, command= smoke_regu_clickk)
            smoke_regularly.place(x=485,y=575)

            smoke_skip_no_push = tk.Button(self.__root, image=wo_smoke_drink_skip_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0, command= smoke_skip_clickk)
            smoke_skip_no_push.place(x=485,y=625)
            
            self.__smoke = "Socially"
        smoke_social_clickk = partial(smoke_social_click)
        smoke_socially = tk.Button(self.__root, image=smoke_socially_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0, command= smoke_social_clickk)
        smoke_socially.place(x=485,y=475)

        def smoke_never_click():
            smoke_socially = tk.Button(self.__root, image=smoke_socially_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0, command= smoke_social_clickk)
            smoke_socially.place(x=485,y=475)

            smoke_never_push = tk.Button(self.__root, image=smoke_never_push_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
            smoke_never_push.place(x=485,y=525)

            smoke_regularly = tk.Button(self.__root, image=smoke_regularly_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0, command= smoke_regu_clickk)
            smoke_regularly.place(x=485,y=575)

            smoke_skip_no_push = tk.Button(self.__root, image=wo_smoke_drink_skip_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0, command= smoke_skip_clickk)
            smoke_skip_no_push.place(x=485,y=625)
            
            self.__smoke = "Never"
        smoke_never_clickk = partial(smoke_never_click)
        smoke_never = tk.Button(self.__root, image=smoke_never_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0, command= smoke_never_clickk)
        smoke_never.place(x=485,y=525)

        def smoke_regu_click():
            smoke_socially = tk.Button(self.__root, image=smoke_socially_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0, command= smoke_social_clickk)
            smoke_socially.place(x=485,y=475)

            smoke_never = tk.Button(self.__root, image=smoke_never_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0, command= smoke_never_clickk)
            smoke_never.place(x=485,y=525)

            smoke_regularly_push = tk.Button(self.__root, image=smoke_regularly_push_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
            smoke_regularly_push.place(x=485,y=575)

            smoke_skip_no_push = tk.Button(self.__root, image=wo_smoke_drink_skip_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0, command= smoke_skip_clickk)
            smoke_skip_no_push.place(x=485,y=625)
            
            self.__smoke = "Regularly"
        smoke_regu_clickk = partial(smoke_regu_click)
        smoke_regularly = tk.Button(self.__root, image=smoke_regularly_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0, command= smoke_regu_clickk)
        smoke_regularly.place(x=485,y=575)
        
        def smoke_skip_click():
            smoke_socially = tk.Button(self.__root, image=smoke_socially_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0, command= smoke_social_clickk)
            smoke_socially.place(x=485,y=475)

            smoke_never = tk.Button(self.__root, image=smoke_never_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0, command= smoke_never_clickk)
            smoke_never.place(x=485,y=525)

            smoke_regularly = tk.Button(self.__root, image=smoke_regularly_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0, command= smoke_regu_clickk)
            smoke_regularly.place(x=485,y=575)

            smoke_skip_push = tk.Button(self.__root, image=wo_smoke_drink_skip_push__img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
            smoke_skip_push.place(x=485,y=625)
            
            self.__smoke = "None"
        smoke_skip_clickk = partial(smoke_skip_click)
        smoke_skip_no_push = tk.Button(self.__root, image=wo_smoke_drink_skip_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0, command= smoke_skip_clickk)
        smoke_skip_no_push.place(x=485,y=625)
        
        
        #---------------------------------------------------------------------------------------------------------------------------------




        #---------------------------------------------------------------------------------------------------------------------------------
        # Drink NO PUSH
        drink_frequently_img = tk.PhotoImage(file="GUI/sign_up_img/basic_information_img/Drink_img/drink_no_push_img/drink_frequently.png")
        drink_rarely_img = tk.PhotoImage(file="GUI/sign_up_img/basic_information_img/Drink_img/drink_no_push_img/drink_rarely.png")
        drink_regularly_img = tk.PhotoImage(file="GUI/sign_up_img/basic_information_img/Drink_img/drink_no_push_img/drink_regularly.png")
        
        # Drink PUSH
        drink_frequently_push_img = tk.PhotoImage(file="GUI/sign_up_img/basic_information_img/Drink_img/drink_push_img/drink_frequently_push.png")
        drink_rarely_push_img = tk.PhotoImage(file="GUI/sign_up_img/basic_information_img/Drink_img/drink_push_img/drink_rarely_push.png")
        drink_regularly_push_img = tk.PhotoImage(file="GUI/sign_up_img/basic_information_img/Drink_img/drink_push_img/drink_regularly_push.png")
        
        
        def drink_feq_click():
            drink_frequently_push = tk.Button(self.__root, image=drink_frequently_push_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
            drink_frequently_push.place(x=805,y=475)

            drink_rarely = tk.Button(self.__root, image=drink_rarely_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0, command= drink_rar_clickk)
            drink_rarely.place(x=805,y=525)

            drink_regularly = tk.Button(self.__root, image=drink_regularly_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0, command= drink_reg_clickk)
            drink_regularly.place(x=805,y=575)

            drink_skip_no_push = tk.Button(self.__root, image=wo_smoke_drink_skip_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0, command= drink_skip_clickk)
            drink_skip_no_push.place(x=805,y=625)
            
            self.__drink = "Frequently"
        drink_feq_clickk = partial(drink_feq_click)
        drink_frequently = tk.Button(self.__root, image=drink_frequently_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0, command= drink_feq_clickk)
        drink_frequently.place(x=805,y=475)

        def drink_rar_click():
            drink_frequently = tk.Button(self.__root, image=drink_frequently_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0, command= drink_feq_clickk)
            drink_frequently.place(x=805,y=475)

            drink_rarely_push = tk.Button(self.__root, image=drink_rarely_push_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
            drink_rarely_push.place(x=805,y=525)

            drink_regularly = tk.Button(self.__root, image=drink_regularly_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0, command= drink_reg_clickk)
            drink_regularly.place(x=805,y=575)

            drink_skip_no_push = tk.Button(self.__root, image=wo_smoke_drink_skip_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0, command= drink_skip_clickk)
            drink_skip_no_push.place(x=805,y=625)
            
            self.__drink = "Rarely"
        drink_rar_clickk = partial(drink_rar_click)
        drink_rarely = tk.Button(self.__root, image=drink_rarely_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0, command= drink_rar_clickk)
        drink_rarely.place(x=805,y=525)

        def drink_reg_click():
            drink_frequently = tk.Button(self.__root, image=drink_frequently_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0, command= drink_feq_clickk)
            drink_frequently.place(x=805,y=475)

            drink_rarely = tk.Button(self.__root, image=drink_rarely_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0, command= drink_rar_clickk)
            drink_rarely.place(x=805,y=525)

            drink_regularly_push = tk.Button(self.__root, image=drink_regularly_push_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
            drink_regularly_push.place(x=805,y=575)

            drink_skip_no_push = tk.Button(self.__root, image=wo_smoke_drink_skip_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0, command= drink_skip_clickk)
            drink_skip_no_push.place(x=805,y=625)
            
            self.__drink = "Regularly"
        drink_reg_clickk = partial(drink_reg_click)
        drink_regularly = tk.Button(self.__root, image=drink_regularly_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0, command= drink_reg_clickk)
        drink_regularly.place(x=805,y=575)

        def drink_skip_click():
            drink_frequently = tk.Button(self.__root, image=drink_frequently_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0, command= drink_feq_clickk)
            drink_frequently.place(x=805,y=475)

            drink_rarely = tk.Button(self.__root, image=drink_rarely_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0, command= drink_rar_clickk)
            drink_rarely.place(x=805,y=525)

            drink_regularly = tk.Button(self.__root, image=drink_regularly_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0, command= drink_reg_clickk)
            drink_regularly.place(x=805,y=575)

            drink_skip_no_push = tk.Button(self.__root, image=wo_smoke_drink_skip_push__img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
            drink_skip_no_push.place(x=805,y=625)
            
            self.__drink = "None"
        drink_skip_clickk = partial(drink_skip_click)
        drink_skip_no_push = tk.Button(self.__root, image=wo_smoke_drink_skip_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0, command= drink_skip_clickk)
        drink_skip_no_push.place(x=805,y=625)

        #---------------------------------------------------------------------------------------------------------------------------------
        high_school_img = tk.PhotoImage(file="GUI/sign_up_img/basic_information_img/Education_img/no_push/high_school.png")
        professional_college_img = tk.PhotoImage(file="GUI/sign_up_img/basic_information_img/Education_img/no_push/professional_college.png")
        university_img = tk.PhotoImage(file="GUI/sign_up_img/basic_information_img/Education_img/no_push/university.png")
        master_degree_img = tk.PhotoImage(file="GUI/sign_up_img/basic_information_img/Education_img/no_push/master_degree.png")
        professor_img = tk.PhotoImage(file="GUI/sign_up_img/basic_information_img/Education_img/no_push/professor.png")
        education_skip_img = tk.PhotoImage(file="GUI/sign_up_img/basic_information_img/skip.png")
        vocational_school_img = tk.PhotoImage(file="GUI/sign_up_img/basic_information_img/Education_img/no_push/vocational_school.png")
        
        def education_click():
            match self.__education_index:
                case 0:
                    high_school = tk.Button(self.__root, image=high_school_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
                    high_school.place(x=521,y=263)
                    self.__education = "High school"
                case 1:
                    professional_college = tk.Button(self.__root, image=professional_college_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
                    professional_college.place(x=520,y=261)
                    self.__education = "Professional college"
                case 2:
                    university = tk.Button(self.__root, image=university_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
                    university.place(x=522,y=262)
                    self.__education = "University"
                case 3:
                    master_degree = tk.Button(self.__root, image=master_degree_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
                    master_degree.place(x=520,y=262)
                    self.__education = "Master degree"
                case 4:
                    professor = tk.Button(self.__root, image=professor_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
                    professor.place(x=522,y=261)
                    self.__education = "Professor"
                case 5:
                    vocational_school = tk.Button(self.__root, image=vocational_school_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
                    vocational_school.place(x=519,y=260)
                    self.__education = "Vocational school"
                case 6:
                    education_skip = tk.Button(self.__root, image=education_skip_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
                    education_skip.place(x=522,y=261)
                    self.__education = "None"
            self.__education_index += 1
            if self.__education_index == 7: self.__education_index = 0
            
        education_clickk = partial(education_click)
        education_button = tk.Button(self.__root, image =education_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0, command= education_clickk)
        education_button.place(x=645,y=180)

        #---------------------------------------------------------------------------------------------------------------------------------
        
        #set zodiac
        dob = show_new_added_dob()
        components = dob.split('-')
        year, month, day = [int(item) for item in components]
        match month:
            case 12:
                zodiac = "Sagittarius" if (day < 22) else "Capricorn"
            case 1:
                zodiac = "Capricorn" if (day < 20) else "Aquarius"
            case 2:
                zodiac = "Aquarius" if (day < 19) else "Pisces"
            case 3:
                zodiac = "Pisces" if (day < 21) else "Aries"
            case 4:
                zodiac = "Aries" if (day < 20) else "Taurus"
            case 5:
                zodiac = "Taurus" if (day < 21) else "Gemini"
            case 6:
                zodiac = "Gemini" if (day < 21) else "Cancer"
            case 7:
                zodiac = "Cancer" if (day < 23) else "Leo"
            case 8:
                zodiac = "Leo" if (day < 23) else "Virgo"
            case 9:
                zodiac = "Virgo" if (day < 23) else "Libra"
            case 10:
                zodiac = "Libra" if (day < 23) else "Scorpio"
            case 11:
                zodiac = "Scorpio" if (day < 22) else "Sagittarius"
        
        #Zodiac
        aries_img = tk.PhotoImage(file="GUI/sign_up_img/basic_information_img/Zodiac/aries.png")
        taurus_img = tk.PhotoImage(file="GUI/sign_up_img/basic_information_img/Zodiac/taurus.png")
        gemini_img = tk.PhotoImage(file="GUI/sign_up_img/basic_information_img/Zodiac/gemini.png")
        cancer_img = tk.PhotoImage(file="GUI/sign_up_img/basic_information_img/Zodiac/cancer.png")
        leo_img = tk.PhotoImage(file="GUI/sign_up_img/basic_information_img/Zodiac/leo.png")
        virgo_img = tk.PhotoImage(file="GUI/sign_up_img/basic_information_img/Zodiac/virgo.png")
        libra_img = tk.PhotoImage(file="GUI/sign_up_img/basic_information_img/Zodiac/libra.png")
        scorpio_img = tk.PhotoImage(file="GUI/sign_up_img/basic_information_img/Zodiac/scorpio.png")
        sagittarius_img = tk.PhotoImage(file="GUI/sign_up_img/basic_information_img/Zodiac/sagittarius.png")
        capricorn_img = tk.PhotoImage(file="GUI/sign_up_img/basic_information_img/Zodiac/capricorn.png")
        aquarius_img = tk.PhotoImage(file="GUI/sign_up_img/basic_information_img/Zodiac/aquarius.png")
        pisces_img = tk.PhotoImage(file="GUI/sign_up_img/basic_information_img/Zodiac/pisces.png")
        
        match zodiac:
            case "Aries":
                aries = tk.Label(label_background, image=aries_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
                aries.place(x=861,y=260)
            case "Taurus":
                taurus = tk.Label(label_background, image=taurus_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
                taurus.place(x=859,y=260)
            case "Gemini":
                gemini = tk.Label(label_background, image=gemini_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
                gemini.place(x=861,y=260)
            case "Cancer":
                cancer = tk.Label(label_background, image=cancer_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
                cancer.place(x=859,y=260)
            case "Leo":
                leo = tk.Label(label_background, image=leo_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
                leo.place(x=861,y=260)
            case "Virgo":
                virgo = tk.Label(label_background, image=virgo_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
                virgo.place(x=860,y=260)
            case "Libra":
                libra = tk.Label(label_background, image=libra_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
                libra.place(x=859,y=260)
            case "Scorpio":
                scorpio = tk.Label(label_background, image=scorpio_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
                scorpio.place(x=861,y=260)
            case "Sagittarius":
                sagittarius = tk.Label(label_background, image=sagittarius_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
                sagittarius.place(x=861,y=260)
            case "Capricorn":
                capricorn = tk.Label(label_background, image=capricorn_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
                capricorn.place(x=861,y=260)
            case "Aquarius":
                aquarius = tk.Label(label_background, image=aquarius_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
                aquarius.place(x=860,y=260)
            case "Pisces":
                pisces = tk.Label(label_background, image=pisces_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
                pisces.place(x=859,y=260)
        


        #----------------------------------------------------------------------------------------------------------------------------
        def Input_Height(event):
            if  input_height.get() == "1m??":
                input_height.delete(0, "end") # Remove blurry text
                input_height.configure(fg="#000000")
        def Input_Height_Focus_Out(event):
            if not input_height.get():
                input_height.configure(fg="#A9A9A9") # Restore the color of the input box's watermark
                input_height.insert(0, "1m??")

        height = StringVar()
        input_height = tk.Entry(label_background, textvariable = height,width=18,bg="#FFFFFF", fg="#A9A9A9", font=("Arial", 14))
        input_height.insert(0, "1m??") # Insert opaque text into input_height
        input_height.bind("<FocusIn>", Input_Height) # Attach event on click on input_height
        input_height.bind("<FocusOut>", Input_Height_Focus_Out) # Hook event on hover out of input_height
        input_height.place(x=230, y=170)
        input_height.configure(borderwidth=0, highlightthickness=0)
        #----------------------------------------------------------------------------------------------------------------------------
        def Input_Weight(event):
            if  input_weight.get() == " ?kg":
                input_weight.delete(0, "end") # Remove blurry text
                input_weight.configure(fg="#000000")
        def Input_Weight_Focus_Out(event):
            if not input_weight.get():
                input_weight.configure(fg="#A9A9A9") # Restore the color of the input box's watermark
                input_weight.insert(0, " ?kg")

        weight = StringVar()
        input_weight = tk.Entry(label_background, textvariable = weight,width=18,bg="#FFFFFF", fg="#A9A9A9", font=("Arial", 14))
        input_weight.insert(0, " ?kg") # Insert opaque text into input_weight
        input_weight.bind("<FocusIn>", Input_Weight) # Attach event on click on input_weight
        input_weight.bind("<FocusOut>", Input_Weight_Focus_Out) # Hook event on hover out of input_weight
        input_weight.place(x=230, y=253)
        input_weight.configure(borderwidth=0, highlightthickness=0)
        
        
        #----------------------------------------------------------------------------------------------------------------------------
        #Continue Button
        
        continue_clickk = partial(self.continue_click, height, weight, zodiac, self.__workout, self.__smoke, self.__drink, self.__education)
        
        continue_button = tk.Button(label_background, image=continue_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0, command= continue_clickk)
        continue_button.place(x = 1050, y = 500)
        
        self.__root.mainloop()
        
    def continue_click2(self, interests):
        if len(interests) == 5:
            insert_interest(interests[0], interests[1], interests[2], interests[3], interests[4])
            self.__root.destroy()
            #print("set up interests success")
            Upload = upload_images.Upload_img()
            Upload.Upload_Screen()
            
            
    def Interest_Screen(self):
        background = tk.PhotoImage(file="GUI/sign_up_img/interest_img/background_interests.png")

        continue_img = tk.PhotoImage(file="GUI/sign_up_img/interest_img/continue_img.png")

        main_frame = Frame(self.__root)
        main_frame.pack(fill=BOTH, expand=1)
        my_canvas = Canvas(main_frame)
        my_canvas.pack(side=LEFT, fill=BOTH, expand=1)
        my_scrollbar = tk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
        my_scrollbar.pack(side=RIGHT, fill=Y)
        my_canvas.configure(yscrollcommand=my_scrollbar.set)
        
        def on_mousewheel(event):
            my_canvas.yview_scroll(-1*int((event.delta/120)), "units")
        
        my_canvas.bind(
            "<Configure>", lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all"))
        )
        
        my_canvas.bind_all(
            "<MouseWheel>", on_mousewheel
        )

        second_frame = Frame(my_canvas, width = 1280, height = 1921)
        label_background = tk.Label(second_frame, image = background)
        label_background.pack()
        my_canvas.create_window((0, 0), window= second_frame, anchor="nw")




        interests = []
        def addInter(inter):
            interests.append(inter)
            #print(len(interests))
        def removeInter(inter):
            if inter in interests:
                interests.remove(inter)
            #print(len(interests))
        def isFull():
            return len(interests) != 5



        #----------------------------------------------------------------------------------------------------------------------------    
        #Interest 

        #Sport
        gym_img = tk.PhotoImage(file="GUI/sign_up_img/interest_img/interest_no_click_img/sport_img/gym.png")
        badminton_img = tk.PhotoImage(file="GUI/sign_up_img/interest_img/interest_no_click_img/sport_img/badminton.png")
        boxing_img = tk.PhotoImage(file="GUI/sign_up_img/interest_img/interest_no_click_img/sport_img/boxing.png")
        basketball_img = tk.PhotoImage(file="GUI/sign_up_img/interest_img/interest_no_click_img/sport_img/basketball.png")

        #Creativity
        design_img = tk.PhotoImage(file="GUI/sign_up_img/interest_img/interest_no_click_img/creativity_img/design.png")
        photograph_img = tk.PhotoImage(file="GUI/sign_up_img/interest_img/interest_no_click_img/creativity_img/photography.png")
        art_img = tk.PhotoImage(file="GUI/sign_up_img/interest_img/interest_no_click_img/creativity_img/art.png")
        make_up_img = tk.PhotoImage(file="GUI/sign_up_img/interest_img/interest_no_click_img/creativity_img/make-up.png")

        #Going out
        bars_img = tk.PhotoImage(file="GUI/sign_up_img/interest_img/interest_no_click_img/going_out_img/bars.png")
        concerts_img = tk.PhotoImage(file="GUI/sign_up_img/interest_img/interest_no_click_img/going_out_img/concerts.png")
        museums_img = tk.PhotoImage(file="GUI/sign_up_img/interest_img/interest_no_click_img/going_out_img/museums.png") 
        cafe_img = tk.PhotoImage(file="GUI/sign_up_img/interest_img/interest_no_click_img/going_out_img/cake.png")

        #Stayng in
        baking_img = tk.PhotoImage(file="GUI/sign_up_img/interest_img/interest_no_click_img/staying_in_img/baking.png") 
        cooking_img = tk.PhotoImage(file="GUI/sign_up_img/interest_img/interest_no_click_img/staying_in_img/cooking.png")
        board_game_img = tk.PhotoImage(file="GUI/sign_up_img/interest_img/interest_no_click_img/staying_in_img/board_game.png") 
        gardening_img = tk.PhotoImage(file="GUI/sign_up_img/interest_img/interest_no_click_img/staying_in_img/gardening.png")
        
        #----------------------------------------------------------------------------------------------------------------------------   
        #Sport CLICK
        gym_click_img = tk.PhotoImage(file="GUI/sign_up_img/interest_img/interest_click_img/sport_img/gym.png")
        badminton_click_img = tk.PhotoImage(file="GUI/sign_up_img/interest_img/interest_click_img/sport_img/badminton.png")
        boxing_click_img = tk.PhotoImage(file="GUI/sign_up_img/interest_img/interest_click_img/sport_img/boxing.png")
        basketball_click_img = tk.PhotoImage(file="GUI/sign_up_img/interest_img/interest_click_img/sport_img/basketball.png")

        #Creativity CLICK
        design_click_img = tk.PhotoImage(file="GUI/sign_up_img/interest_img/interest_click_img/creativity_img/design.png")
        photograph_click_img = tk.PhotoImage(file="GUI/sign_up_img/interest_img/interest_click_img/creativity_img/photograph.png")
        art_click_img = tk.PhotoImage(file="GUI/sign_up_img/interest_img/interest_click_img/creativity_img/art.png")
        make_up_click_img = tk.PhotoImage(file="GUI/sign_up_img/interest_img/interest_click_img/creativity_img/make_up.png")

        #Going out CLICK
        bars_click_img = tk.PhotoImage(file="GUI/sign_up_img/interest_img/interest_click_img/going_out_img/bars.png")
        concerts_click_img = tk.PhotoImage(file="GUI/sign_up_img/interest_img/interest_click_img/going_out_img/concerts.png")
        museums_click_img = tk.PhotoImage(file="GUI/sign_up_img/interest_img/interest_click_img/going_out_img/museums.png") 
        cafe_click_img = tk.PhotoImage(file="GUI/sign_up_img/interest_img/interest_click_img/going_out_img/cafe.png")

        #Stayng in CLICK
        baking_click_img = tk.PhotoImage(file="GUI/sign_up_img/interest_img/interest_click_img/staying_in_img/baking.png") 
        cooking_click_img = tk.PhotoImage(file="GUI/sign_up_img/interest_img/interest_click_img/staying_in_img/cooking.png")
        board_game_click_img = tk.PhotoImage(file="GUI/sign_up_img/interest_img/interest_click_img/staying_in_img/board_game.png") 
        gardening_click_img = tk.PhotoImage(file="GUI/sign_up_img/interest_img/interest_click_img/staying_in_img/gardening.png")








        #----------------------------------------------------------------------------------------------------------------------------

        #Sport
        def gym_click():
            if isFull():
                gym = tk.Button(second_frame, image=gym_click_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0, command= partial(gym_unclick))
                gym.place(x=130,y=248)
                addInter("gym")
        def gym_unclick():
            gym = tk.Button(second_frame, image=gym_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0, command= partial(gym_click))
            gym.place(x = 131, y = 250)
            removeInter("gym")
        gym_unclick()
        
        def badminton_click():
            if isFull():
                badminton = tk.Button(second_frame, image=badminton_click_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0, command= partial(badminton_unclick))
                badminton.place(x = 130, y = 335)
                addInter("badminton")
        def badminton_unclick():
            badminton = tk.Button(second_frame, image=badminton_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0, command= partial(badminton_click))
            badminton.place(x = 130, y = 335)
            removeInter("badminton")
        badminton_unclick()    
        
        def boxing_click():
            if isFull():
                boxing = tk.Button(second_frame, image=boxing_click_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0, command= partial(boxing_unclick))
                boxing.place(x= 352, y= 246)
                addInter("boxing")
        def boxing_unclick():
            boxing = tk.Button(second_frame, image=boxing_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0, command= partial(boxing_click))
            boxing.place(x = 355, y = 250)
            removeInter("boxing")
        boxing_unclick()
        
        def basketball_click():
            if isFull():
                basketball = tk.Button(second_frame, image=basketball_click_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0, command= partial(basketball_unclick))
                basketball.place(x= 353, y= 332)
                addInter("basketball")
        def basketball_unclick():
            basketball = tk.Button(second_frame, image=basketball_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0, command= partial(basketball_click))
            basketball.place(x = 355, y = 335)
            removeInter("basketball")
        basketball_unclick()

        #------------------------------------------------------------------------------------------------------------------------------------------------------------------
        #Creativity
        def design_click():
            if isFull():
                design_click = tk.Button(second_frame, image=design_click_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0, command= partial(design_unclick))
                design_click.place(x = 732, y = 251)
                addInter("design")
        def design_unclick():
            design = tk.Button(second_frame, image=design_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0, command= partial(design_click))
            design.place(x = 731, y = 250)
            removeInter("design")
        design_unclick()
        
        def photograph_click():
            if isFull():
                photograph = tk.Button(second_frame, image=photograph_click_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0,command= partial(photograph_unclick))
                photograph.place(x = 731, y = 334)
                addInter("photograph")
        def photograph_unclick():
            photograph = tk.Button(second_frame, image=photograph_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0,command= partial(photograph_click))
            photograph.place(x = 730, y = 335)
            removeInter("photograph")
        photograph_unclick()
        
        def art_click():
            if isFull():
                art = tk.Button(second_frame, image=art_click_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0,command= partial(art_unclick))
                art.place(x = 957, y = 250)
                addInter("art")
        def art_unclick():
            art = tk.Button(second_frame, image=art_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0,command= partial(art_click))
            art.place(x = 955, y = 250)
            removeInter("art")
        art_unclick()

        def make_up_click():
            if isFull():
                make_up = tk.Button(second_frame, image=make_up_click_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0,command= partial(make_up_unclick))
                make_up.place(x = 955, y = 335)
                addInter("make_up")
        def make_up_unclick():
            make_up = tk.Button(second_frame, image=make_up_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0,command= partial(make_up_click))
            make_up.place(x = 955, y = 333)
            removeInter("make_up")
        make_up_unclick()
        
        #------------------------------------------------------------------------------------------------------------------------------------------------------------------
        #Going out
        def bars_click():
            if isFull():
                bars = tk.Button(second_frame, image=bars_click_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0,command= partial(bars_unclick))
                bars.place(x = 129, y = 557)
                addInter("bars")
        def bars_unclick():
            bars = tk.Button(second_frame, image=bars_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0,command= partial(bars_click))
            bars.place(x = 132, y = 560)
            removeInter("bars")
        bars_unclick()

        def concerts_click():
            if isFull():
                concerts = tk.Button(second_frame, image=concerts_click_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0,command= partial(concerts_unclick))
                concerts.place(x = 128, y = 638)
                addInter("concerts")
        def concerts_unclick():
            concerts = tk.Button(second_frame, image=concerts_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0,command= partial(concerts_click))
            concerts.place(x = 130, y = 639)
            removeInter("concerts")
        concerts_unclick() 

        def museums_click():
            if isFull():
                museums = tk.Button(second_frame, image=museums_click_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0,command= partial(museums_unclick))
                museums.place(x = 353, y = 558)
                addInter("museums")
        def museums_unclick():
            museums = tk.Button(second_frame, image=museums_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0,command= partial(museums_click))
            museums.place(x = 355, y = 560)
            removeInter("museums")
        museums_unclick() 

        def cafe_click():
            if isFull():
                cafe = tk.Button(second_frame, image=cafe_click_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0,command= partial(cafe_unclick))
                cafe.place(x = 354, y = 638)
                addInter("cafe")
        def cafe_unclick():
            cafe = tk.Button(second_frame, image=cafe_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0,command= partial(cafe_click))
            cafe.place(x = 355, y = 639)
            removeInter("cafe")
        cafe_unclick() 
        
        #------------------------------------------------------------------------------------------------------------------------------------------------------------------
        #Stayng in CLICK
        def baking_click():
            if isFull():
                baking = tk.Button(second_frame, image=baking_click_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0,command= partial(baking_unclick))
                baking.place(x = 732, y = 560)
                addInter("baking")
        def baking_unclick():
            baking = tk.Button(second_frame, image=baking_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0,command= partial(baking_click))
            baking.place(x = 732, y = 563)
            removeInter("baking")
        baking_unclick() 

        def cooking_click():
            if isFull():
                cooking = tk.Button(second_frame, image=cooking_click_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0,command= partial(cooking_unclick))
                cooking.place(x = 730, y = 641)
                addInter("cooking")
        def cooking_unclick():
            cooking = tk.Button(second_frame, image=cooking_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0,command= partial(cooking_click))
            cooking.place(x = 731, y = 640)
            removeInter("cooking")
        cooking_unclick() 

        def board_game_click():
            if isFull():
                board_game = tk.Button(second_frame, image=board_game_click_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0,command= partial(board_game_unclick))
                board_game.place(x = 954, y = 559)
                addInter("board_game")
        def board_game_unclick():
            board_game = tk.Button(second_frame, image=board_game_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0,command= partial(board_game_click))
            board_game.place(x = 955, y = 560)
            removeInter("board_game")
        board_game_unclick() 

        def gardening_click():
            if isFull():
                gardening = tk.Button(second_frame, image=gardening_click_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0,command= partial(gardening_unclick))
                gardening.place(x = 952, y = 638)
                addInter("gardening")
        def gardening_unclick():
            gardening = tk.Button(second_frame, image=gardening_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0,command= partial(gardening_click))
            gardening.place(x = 954, y = 640)
            removeInter("gardening")
        gardening_unclick() 
        






        #----------------------------------------------------------------------------------------------------------------------------------------------------------------
        #Traveling
        backpacking_img = tk.PhotoImage(file="GUI/sign_up_img/interest_img/interest_no_click_img/traveling_img/backpacking.png") 
        beaches_img = tk.PhotoImage(file="GUI/sign_up_img/interest_img/interest_no_click_img/traveling_img/beaches.png") 
        winter_sports_img = tk.PhotoImage(file="GUI/sign_up_img/interest_img/interest_no_click_img/traveling_img/winter_sports.png") 
        camping_img = tk.PhotoImage(file="GUI/sign_up_img/interest_img/interest_no_click_img/traveling_img/camping.png")

        #Food & Drink
        sushi_img = tk.PhotoImage(file="GUI/sign_up_img/interest_img/interest_no_click_img/food_drink_img/sushi.png")
        pizza_img = tk.PhotoImage(file="GUI/sign_up_img/interest_img/interest_no_click_img/food_drink_img/pizza.png") 
        sweet_tooth_img = tk.PhotoImage(file="GUI/sign_up_img/interest_img/interest_no_click_img/food_drink_img/sweet_tooth.png")
        tea_img = tk.PhotoImage(file="GUI/sign_up_img/interest_img/interest_no_click_img/food_drink_img/tea.png")
        
        #Music
        classical_img = tk.PhotoImage(file="GUI/sign_up_img/interest_img/interest_no_click_img/music_img/classical.png") 
        r_b_img = tk.PhotoImage(file="GUI/sign_up_img/interest_img/interest_no_click_img/music_img/R&B.png")
        edm_img = tk.PhotoImage(file="GUI/sign_up_img/interest_img/interest_no_click_img/music_img/edm.png")
        rap_img = tk.PhotoImage(file="GUI/sign_up_img/interest_img/interest_no_click_img/music_img/rap.png")

        #Flim & TV
        action_img = tk.PhotoImage(file="GUI/sign_up_img/interest_img/interest_no_click_img/film_tv_img/action.png")
        romance_img = tk.PhotoImage(file="GUI/sign_up_img/interest_img/interest_no_click_img/film_tv_img/romance.png")
        comedy_img = tk.PhotoImage(file="GUI/sign_up_img/interest_img/interest_no_click_img/film_tv_img/comedy.png")
        horror_img = tk.PhotoImage(file="GUI/sign_up_img/interest_img/interest_no_click_img/film_tv_img/horror.png")
        #----------------------------------------------------------------------------------------------------------------------------------------------------------------
        # Button no Click of Traveling -- Food & Drink --  Music -- Flim & TV
        #Traveling CLICK
        backpacking_click_img = tk.PhotoImage(file="GUI/sign_up_img/interest_img/interest_click_img/traveling_img/backpacking.png") 
        beaches_click_img = tk.PhotoImage(file="GUI/sign_up_img/interest_img/interest_click_img/traveling_img/beaches.png") 
        winter_sports_click_img = tk.PhotoImage(file="GUI/sign_up_img/interest_img/interest_click_img/traveling_img/winter_sports.png") 
        camping_click_img = tk.PhotoImage(file="GUI/sign_up_img/interest_img/interest_click_img/traveling_img/camping.png")

        #Food & Drink CLICK
        sushi_click_img = tk.PhotoImage(file="GUI/sign_up_img/interest_img/interest_click_img/food_drink_img/sushi.png")
        pizza_click_img = tk.PhotoImage(file="GUI/sign_up_img/interest_img/interest_click_img/food_drink_img/pizza.png") 
        sweet_tooth_click_img = tk.PhotoImage(file="GUI/sign_up_img/interest_img/interest_click_img/food_drink_img/sweet_tooth.png")
        tea_click_img = tk.PhotoImage(file="GUI/sign_up_img/interest_img/interest_click_img/food_drink_img/tea.png")
        
        #Music CLICK
        classical_click_img = tk.PhotoImage(file="GUI/sign_up_img/interest_img/interest_click_img/music_img/classical.png") 
        r_b_click_img = tk.PhotoImage(file="GUI/sign_up_img/interest_img/interest_click_img/music_img/R&B.png")
        edm_click_img = tk.PhotoImage(file="GUI/sign_up_img/interest_img/interest_click_img/music_img/edm.png")
        rap_click_img = tk.PhotoImage(file="GUI/sign_up_img/interest_img/interest_click_img/music_img/rap.png")

        #Flim & TV CLICK
        action_click_img = tk.PhotoImage(file="GUI/sign_up_img/interest_img/interest_click_img/film_tv_img/action.png")
        romance_click_img = tk.PhotoImage(file="GUI/sign_up_img/interest_img/interest_click_img/film_tv_img/romance.png")
        comedy_click_img = tk.PhotoImage(file="GUI/sign_up_img/interest_img/interest_click_img/film_tv_img/comedy.png")
        horror_click_img = tk.PhotoImage(file="GUI/sign_up_img/interest_img/interest_click_img/film_tv_img/horror.png")


        #--------------------------------------------------------------------------------------------------------------------------------------------------------------------

        #Traveling
        def backpacking_click():
            if isFull():
                backpacking = tk.Button(second_frame, image=backpacking_click_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0,command= partial(backpacking_unclick))
                backpacking.place(x = 130, y = 864)
                addInter("backpacking")
        def backpacking_unclick():
            backpacking = tk.Button(second_frame, image=backpacking_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0,command= partial(backpacking_click))
            backpacking.place(x = 131, y = 865)
            removeInter("backpacking")
        backpacking_unclick() 

        def beaches_click():
            if isFull():
                beaches = tk.Button(second_frame, image=beaches_click_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0,command= partial(beaches_unclick))
                beaches.place(x = 128, y = 943)
                addInter("beaches")
        def beaches_unclick():
            beaches = tk.Button(second_frame, image=beaches_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0,command= partial(beaches_click))
            beaches.place(x = 131, y = 944)
            removeInter("beaches")
        beaches_unclick() 

        def winter_sports_click():
            if isFull():
                winter_sports = tk.Button(second_frame, image=winter_sports_click_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0,command= partial(winter_sports_unclick))
                winter_sports.place(x = 354, y = 866)
                addInter("winter_sports")
        def winter_sports_unclick():
            winter_sports = tk.Button(second_frame, image=winter_sports_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0,command= partial(winter_sports_click))
            winter_sports.place(x = 355, y = 865)
            removeInter("winter_sports")
        winter_sports_unclick() 

        def camping_click():
            if isFull():
                camping = tk.Button(second_frame, image=camping_click_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0,command= partial(camping_unclick))
                camping.place(x = 354, y = 944)
                addInter("camping")
        def camping_unclick():
            camping = tk.Button(second_frame, image=camping_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0,command= partial(camping_click))
            camping.place(x = 355, y = 945)
            removeInter("camping")
        camping_unclick() 
        
        # Food & Drink
        def sushi_click():
            if isFull():
                sushi = tk.Button(second_frame, image=sushi_click_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0,command= partial(sushi_unclick))
                sushi.place(x = 732, y = 867)
                addInter("sushi")
        def sushi_unclick():
            sushi = tk.Button(second_frame, image=sushi_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0,command= partial(sushi_click))
            sushi.place(x = 731, y = 867)
            removeInter("sushi")
        sushi_unclick() 
        
        def pizza_click():
            if isFull():
                pizza = tk.Button(second_frame, image=pizza_click_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0,command= partial(pizza_unclick))
                pizza.place(x = 730, y = 945)
                addInter("pizza")
        def pizza_unclick():
            pizza = tk.Button(second_frame, image=pizza_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0,command= partial(pizza_click))
            pizza.place(x = 732, y = 949)
            removeInter("pizza")
        pizza_unclick() 

        def sweet_tooth_click():
            if isFull():
                sweet_tooth = tk.Button(second_frame, image=sweet_tooth_click_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0,command= partial(sweet_tooth_unclick))
                sweet_tooth.place(x = 955, y = 864)
                addInter("sweet_tooth")
        def sweet_tooth_unclick():
            sweet_tooth = tk.Button(second_frame, image=sweet_tooth_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0,command= partial(sweet_tooth_click))
            sweet_tooth.place(x = 955, y = 866)
            removeInter("sweet_tooth")
        sweet_tooth_unclick() 
        
        def tea_click():
            if isFull():
                tea = tk.Button(second_frame, image=tea_click_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0,command= partial(tea_unclick))
                tea.place(x = 952, y = 945)
                addInter("tea")
        def tea_unclick():
            tea = tk.Button(second_frame, image=tea_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0,command= partial(tea_click))
            tea.place(x = 954, y = 948)
            removeInter("tea")
        tea_unclick()


        
        #Music
        def classical_click():
            if isFull():
                classical = tk.Button(second_frame, image=classical_click_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0,command= partial(classical_unclick))
                classical.place(x = 127, y = 1171)
                addInter("classical")
        def classical_unclick():
            classical = tk.Button(second_frame, image=classical_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0,command= partial(classical_click))
            classical.place(x = 130, y = 1173)
            removeInter("classical")
        classical_unclick()

        def r_b_click():
            if isFull():
                r_b = tk.Button(second_frame, image=r_b_click_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0,command= partial(r_b_unclick))
                r_b.place(x = 128, y = 1251)
                addInter("r_b")
        def r_b_unclick():
            r_b = tk.Button(second_frame, image=r_b_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0,command= partial(r_b_click))
            r_b.place(x = 130, y = 1254)
            removeInter("r_b")
        r_b_unclick()

        def edm_click():
            if isFull():
                edm = tk.Button(second_frame, image=edm_click_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0,command= partial(edm_unclick))
                edm.place(x = 355, y = 1170)
                addInter("edm")
        def edm_unclick():
            edm = tk.Button(second_frame, image=edm_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0,command= partial(edm_click))
            edm.place(x = 355, y = 1174)
            removeInter("edm")
        edm_unclick()
        
        def rap_click():
            if isFull():
                rap = tk.Button(second_frame, image=rap_click_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0,command= partial(rap_unclick))
                rap.place(x = 356, y = 1253)
                addInter("rap")
        def rap_unclick():
            rap = tk.Button(second_frame, image=rap_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0,command= partial(rap_click))
            rap.place(x = 356, y = 1255)
            removeInter("rap")
        rap_unclick()
        

        #Flim & TV
        def action_click():
            if isFull():
                action = tk.Button(second_frame, image=action_click_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0,command= partial(action_unclick))
                action.place(x = 734, y = 1173)
                addInter("action")
        def action_unclick():
            action = tk.Button(second_frame, image=action_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0,command= partial(action_click))
            action.place(x = 732, y = 1172)
            removeInter("action")
        action_unclick()
        
        def romance_click():
            if isFull():
                romance = tk.Button(second_frame, image=romance_click_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0,command= partial(romance_unclick))
                romance.place(x = 731, y = 1253)
                addInter("romance")
        def romance_unclick():
            romance = tk.Button(second_frame, image=romance_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0,command= partial(romance_click))
            romance.place(x = 731, y = 1253)
            removeInter("romance")
        romance_unclick()
        
        def comedy_click():
            if isFull():
                comedy = tk.Button(second_frame, image=comedy_click_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0,command= partial(comedy_unclick))
                comedy.place(x = 957, y = 1173)
                addInter("comedy")
        def comedy_unclick():
            comedy = tk.Button(second_frame, image=comedy_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0,command= partial(comedy_click))
            comedy.place(x = 955, y = 1172)
            removeInter("comedy")
        comedy_unclick()
        
        def horror_click():
            if isFull():
                horror = tk.Button(second_frame, image=horror_click_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0,command= partial(horror_unclick))
                horror.place(x = 954, y = 1254)
                addInter("horror")
        def horror_unclick():
            horror = tk.Button(second_frame, image=horror_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0,command= partial(horror_click))
            horror.place(x = 955, y = 1253)
            removeInter("horror")
        horror_unclick()
        
        #-------------------------------------------------------------------------------------------------------------------------------------------------------

        #Reading
        history_img = tk.PhotoImage(file="GUI/sign_up_img/interest_img/interest_no_click_img/reading_img/history.png")
        novel_img = tk.PhotoImage(file="GUI/sign_up_img/interest_img/interest_no_click_img/reading_img/novel.png")
        poetry_img = tk.PhotoImage(file="GUI/sign_up_img/interest_img/interest_no_click_img/reading_img/poetry.png")
        pschology_img = tk.PhotoImage(file="GUI/sign_up_img/interest_img/interest_no_click_img/reading_img/pschology.png")

        #Pets
        dog_img = tk.PhotoImage(file="GUI/sign_up_img/interest_img/interest_no_click_img/pets_img/dog.png")
        cat_img = tk.PhotoImage(file="GUI/sign_up_img/interest_img/interest_no_click_img/pets_img/cat.png")
        snake_img = tk.PhotoImage(file="GUI/sign_up_img/interest_img/interest_no_click_img/pets_img/snake.png")
        bird_img = tk.PhotoImage(file="GUI/sign_up_img/interest_img/interest_no_click_img/pets_img/bird.png")

        #Reading CLICK
        history_click_img = tk.PhotoImage(file="GUI/sign_up_img/interest_img/interest_click_img/reading_img/history.png")
        novel_click_img = tk.PhotoImage(file="GUI/sign_up_img/interest_img/interest_click_img/reading_img/novel.png")
        poetry_click_img = tk.PhotoImage(file="GUI/sign_up_img/interest_img/interest_click_img/reading_img/poetry.png")
        pschology_click_img = tk.PhotoImage(file="GUI/sign_up_img/interest_img/interest_click_img/reading_img/psychology.png")

        #Pets CLICK
        dog_click_img = tk.PhotoImage(file="GUI/sign_up_img/interest_img/interest_click_img/pets_img/dog.png")
        cat_click_img = tk.PhotoImage(file="GUI/sign_up_img/interest_img/interest_click_img/pets_img/cat.png")
        snake_click_img = tk.PhotoImage(file="GUI/sign_up_img/interest_img/interest_click_img/pets_img/snake.png")
        bird_click_img = tk.PhotoImage(file="GUI/sign_up_img/interest_img/interest_click_img/pets_img/bird.png")
        #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

        # Button no Click of Reading and Pets

        def history_click():
            if isFull():
                history = tk.Button(second_frame, image=history_click_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0,command= partial(history_unclick))
                history.place(x = 129, y = 1477)
                addInter("history")
        def history_unclick():
            history = tk.Button(second_frame, image=history_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0,command= partial(history_click))
            history.place(x = 130, y = 1478)
            removeInter("history")
        history_unclick()
        
        def novel_click():
            if isFull():
                novel = tk.Button(second_frame, image=novel_click_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0,command= partial(novel_unclick))
                novel.place(x = 128, y = 1558)
                addInter("novel")
        def novel_unclick():
            novel = tk.Button(second_frame, image=novel_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0,command= partial(novel_click))
            novel.place(x = 129, y = 1561)
            removeInter("novel")
        novel_unclick()

        def poetry_click():
            if isFull():
                poetry = tk.Button(second_frame, image=poetry_click_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0,command= partial(poetry_unclick))
                poetry.place(x = 353, y = 1476)
                addInter("poetry")
        def poetry_unclick():
            poetry = tk.Button(second_frame, image=poetry_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0,command= partial(poetry_click))
            poetry.place(x = 355, y = 1478)
            removeInter("poetry")
        poetry_unclick()

        def pschology_click():
            if isFull():
                pschology = tk.Button(second_frame, image=pschology_click_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0,command= partial(pschology_unclick))
                pschology.place(x = 349, y = 1557)
                addInter("psychology")
        def pschology_unclick():
            pschology = tk.Button(second_frame, image=pschology_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0,command= partial(pschology_click))
            pschology.place(x = 354, y = 1561)
            removeInter("psychology")
        pschology_unclick()



        # Button no Click of Reading and Pets
        def dog_click():
            if isFull():
                dog = tk.Button(second_frame, image=dog_click_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0,command= partial(dog_unclick))
                dog.place(x = 729, y = 1480)
                addInter("dog")
        def dog_unclick():
            dog = tk.Button(second_frame, image=dog_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0,command= partial(dog_click))
            dog.place(x = 732, y = 1482)
            removeInter("dog")
        dog_unclick()
        
        def cat_click():
            if isFull():
                cat = tk.Button(second_frame, image=cat_click_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0,command= partial(cat_unclick))
                cat.place(x = 730, y = 1560)
                addInter("cat")
        def cat_unclick():
            cat = tk.Button(second_frame, image=cat_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0,command= partial(cat_click))
            cat.place(x = 732, y = 1564)
            removeInter("cat")
        cat_unclick()
        
        def snake_click():
            if isFull():
                snake = tk.Button(second_frame, image=snake_click_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0,command= partial(snake_unclick))
                snake.place(x = 954, y = 1479)
                addInter("snake")
        def snake_unclick():
            snake = tk.Button(second_frame, image=snake_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0,command= partial(snake_click))
            snake.place(x = 957, y = 1480)
            removeInter("snake")
        snake_unclick()
        
        def bird_click():
            if isFull():
                bird = tk.Button(second_frame, image=bird_click_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0,command= partial(bird_unclick))
                bird.place(x = 955, y = 1562)
                addInter("bird")
        def bird_unclick():
            bird = tk.Button(second_frame, image=bird_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0,command= partial(bird_click))
            bird.place(x = 955, y = 1563)
            removeInter("bird")
        bird_unclick()

        #----------------------------------------------------------------------------------------------------------------------------
        #Continue Button
        
        # continue_click2k = partial(continue_click2, height, weight, zodiac, workout, smoke, drink, education, second_frame)
        
        con_click = partial(self.continue_click2, interests)
        
        continue_button = tk.Button(second_frame, image=continue_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0, command= con_click)
        continue_button.place(x = 539, y = 1750)
        self.__root.mainloop()