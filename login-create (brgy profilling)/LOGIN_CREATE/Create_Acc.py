# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer

import tkinter as tk
import mysql.connector as Mysql
from mysql.connector import Error
from pathlib import Path
import customtkinter as Ctkinter

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"J:\admin\Documents\Andrei_Property\College\2nd Year\1st Sem\1st term\IT 5 (3100)\Brgy-profilling\Brgy-Profiling\assets\create_asset\assets\frame1")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class CreateClass():
    def __init__(self):
        self.window = Tk()
        self.window.geometry("1000x700")
        self.window.configure(bg = "#75181A")
        self.create_widgets()


    def create_widgets(self):
        self.canvas = Canvas(
            self.window,
            bg = "#75181A",
            height = 700,
            width = 1000,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )
        self.canvas.place(x = 0, y = 0)

        self.image_image_1 = PhotoImage(
            file=relative_to_assets("image_1.png"))
        self.image_1 = self.canvas.create_image(
            500.0,
            350.0,
            image=self.image_image_1
        )

        self.button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png"))
        self.button_1 = Button(
            self.window,
            bg="#75181A",
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: toggle_password(self), #print("button_1 clicked"),
            relief="flat"
        )
        self.button_1.place(
            x=281.0,
            y=366.0,
            width=53.0,
            height=53.0
        )

        self.button_image_2 = PhotoImage(
            file=relative_to_assets("button_2.png"))
        self.button_2 = Button(
            self.window,
            bg="#75181A",
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: toggle_password(self), #print("button_2 clicked"),
            relief="flat"
        )
        self.button_2.place(
            x=281.0,
            y=434.0,
            width=53.0,
            height=53.0
        )

        self.fullname_icon = PhotoImage(
            file=relative_to_assets("fullname_icon.png"))
        self.fullname_icon_place = self.canvas.create_image(
            307.0,
            254.0,
            image=self.fullname_icon
        )

        self.entry_1 = Ctkinter.CTkEntry(
            master=self.window,
            width=330, height=45,
            placeholder_text='Fullname', 
            font=("Helvetica", 16), 
            corner_radius=20,
            border_color="#75181A",
            fg_color="#FFFFFF", 
            placeholder_text_color="#808080", 
            text_color="#000716")
        self.entry_1.place(
            x=360,
            y=239.00000202152603,
        )

        self.user_icon = PhotoImage(
            file=relative_to_assets("user_icon.png"))
        self.user_icon_place = self.canvas.create_image(
            307.0,
            322.0,
            image=self.user_icon 
        )

        self.entry_2 = Ctkinter.CTkEntry(
            master=self.window,
            width=330, height=45,
            placeholder_text='Username', 
            font=("Helvetica", 16), 
            corner_radius=20,
            border_color="#75181A",
            fg_color="#FFFFFF", 
            placeholder_text_color="#808080", 
            text_color="#000716")
        self.entry_2.place(
            x=360,
            y=307.00000202152603,
        )

        self.entry_3 = Ctkinter.CTkEntry(
            master=self.window,
            width=330, height=45,
            placeholder_text='Password', 
            show='✶',
            font=("Helvetica", 16), 
            corner_radius=20,
            border_color="#75181A",
            fg_color="#FFFFFF", 
            placeholder_text_color="#808080", 
            text_color="#000716")
        self.entry_3.place(
            x=360,
            y=372.00000202152603,
        )

        self.entry_4 = Ctkinter.CTkEntry(
            master=self.window,
            width=330, height=45,
            placeholder_text='Retype Password', 
            show='✶',
            font=("Helvetica", 16), 
            corner_radius=20,
            border_color="#75181A",
            fg_color="#FFFFFF", 
            placeholder_text_color="#808080", 
            text_color="#000716")
            
        self.entry_4.place(
            x=360,
            y=440.00000202152603,
        )

        self.canvas.create_text(
            440.0,
            181.0,
            anchor="nw",
            text="Create Admin",
            fill="#FFFFFF",
            font=("OpenSans Bold", 25 * -1)
        )

        self.button_image_3 = PhotoImage(
            file=relative_to_assets("button_3.png"))
        self.button_3 = Button(
            self.window,
            bg="#75181A",
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: open_login_form(self),
            relief="flat"
        )
        self.button_3.place(
            x=438.0,
            y=559.0,
            width=172.0,
            height=43.22072219848633
        )

        self.button_image_hover_3 = PhotoImage(
            file=relative_to_assets("button_hover_1.png"))

        def button_3_hover(e):
            self.button_3.config(
                image=self.button_image_hover_3
            )
        def button_3_leave(e):
            self.button_3.config(
                image=self.button_image_3
            )

        self.button_3.bind('<Enter>', button_3_hover)
        self.button_3.bind('<Leave>', button_3_leave)

        self.button_image_4 = PhotoImage(
            file=relative_to_assets("button_4.png"))
        self.button_4 = Button(
            self.window,
            bg="#75181A",
            image=self.button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: insertAdmin(self), #print("button_4 clicked"),
            relief="flat"
        )
        self.button_4.place(
            x=424.0,
            y=502.0,
            width=199.32337951660156,
            height=43.025814056396484
        )

        self.button_image_hover_4 = PhotoImage(
            file=relative_to_assets("button_hover_2.png"))

        def button_4_hover(e):
            self.button_4.config(
                image=self.button_image_hover_4
            )
        def button_4_leave(e):
            self.button_4.config(
                image=self.button_image_4
            )

        self.button_4.bind('<Enter>', button_4_hover)
        self.button_4.bind('<Leave>', button_4_leave)

        def toggle_password(self):
            if self.entry_3.cget('show') == '✶' or self.entry_4.cget('show') == '✶' :
                self.entry_3.configure(show='')
                self.entry_4.configure(show='')
            
            else:
                self.entry_3.configure(show="✶")
                self.entry_4.configure(show="✶")     

        def open_login_form(self):
            self.window.destroy()
            import Login 
            Login.login_class().run()

        try:
            connect = Mysql.connect(
                host = 'localhost',
                user = 'root',
                database = 'db_brgyprofilling'
            )
            cursor = connect.cursor()
            def insertAdmin(self):
                fullname = self.entry_1.get()
                username = self.entry_2.get()
                password1 = self.entry_3.get()
                password2 = self.entry_4.get()

                if not (fullname and username and password2):
                    tk.messagebox.showwarning("Error","All fields must be filled!")
                    return
                
                elif (password1 != password2):
                    tk.messagebox.showwarning("Error","Password doesn't match")
                    return
                
                elif len(password1) < 8:
                    tk.messagebox.showwarning("Error", "Password must be at least 8 characters long")
                    return
                
                else:
                    try:
                        insert_query = """
                            INSERT INTO tbl_adminlogin (Full_name,Username,Password)
                            VALUES (%s,%s,%s)
                            """
                        values = (fullname,username,password2)
                        cursor.execute(insert_query, values)
                        connect.commit()           
                        tk.messagebox.showinfo("Notice","Account Registered Successfully")

                    except Error as e:
                            print(f"Error inserting data: {e}")   

        except Error as e:
            print(f"Error connecting to MySQL: {e}")

    def run(self):
        try:
            self.window.resizable(False, False)
            self.window.mainloop()
        except Exception as e:
            print(f"Error in main loop: {e}")


if __name__ == "__main__":
    create_class = CreateClass()
    create_class.run()