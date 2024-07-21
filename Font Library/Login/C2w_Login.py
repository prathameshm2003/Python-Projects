import tkinter as tk
from PIL import ImageTk, Image
from google.cloud import firestore
import json
from tkinter import messagebox

class MainFrame():
    def __init__(self, parent, main_frame, userData):
        self.useData = userData
        self.root = tk.Tk()
        self.root.geometry('1400x800')
        self.root.resizable(0, 0)
        self.root.title("Font Library by Core2web")
        self.root.iconbitmap("./assests/images/core2web.png")
        self.logIn()

    def logIn(self):
        # Create a frame to hold the UI
        self.main_frame = tk.Frame(self.root, height=700 , width=100)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        self.bg_frame = Image.open("./assests/images/background1.png")
        photo = ImageTk.PhotoImage(self.bg_frame)
        self.bg_panel = tk.Label(self.main_frame, image=photo)
        self.bg_panel.image = photo
        self.bg_panel.pack(fill='both', expand='yes')

        self.lgn_frame = tk.Frame(self.main_frame, bg='#040405', width=990, height=650)
        self.lgn_frame.place(x=200, y=70)

        self.txt = "WELCOME"
        self.txt = "Prathamesh"
        self.heading = tk.Label(self.lgn_frame, text=self.txt, font=('yu gothic ui', 25, "bold"), bg="#040405", fg='white', bd=5, relief=tk.FLAT)
        self.heading.place(x=80, y=30, width=300, height=30)

        self.side_image = Image.open("./assests/images/core2web.png")
        photo = ImageTk.PhotoImage(self.side_image)
        self.side_image_label = tk.Label(self.lgn_frame, image=photo, bg='#040405')
        self.side_image_label.image = photo
        self.side_image_label.place(x=5, y=100)

        self.sign_in_image = Image.open("./assests/images/hyy.png")
        photo = ImageTk.PhotoImage(self.sign_in_image)
        self.sign_in_image_label = tk.Label(self.lgn_frame, image=photo, bg='#040405')
        self.sign_in_image_label.image = photo
        self.sign_in_image_label.place(x=620, y=130)

        self.sign_in_label = tk.Label(self.lgn_frame, text="Sign In", bg="#040405", fg="white", font=("yu gothic ui", 17, "bold"))
        self.sign_in_label.place(x=650, y=240)

        self.username_label = tk.Label(self.lgn_frame, text="Username", bg="#040405", fg="#4f4e4d", font=("yu gothic ui", 13, "bold"))
        self.username_label.place(x=550, y=300)
        self.username_entry = tk.Entry(self.lgn_frame, highlightthickness=0, relief=tk.FLAT, bg="#040405", fg="#6b6a69", font=("yu gothic ui ", 12, "bold"), insertbackground='#6b6a69')
        self.username_entry.place(x=580, y=335, width=270)
        self.username_line = tk.Canvas(self.lgn_frame, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0)
        self.username_line.place(x=550, y=359)

        self.username_icon = Image.open("./assests/images/username_icon.png")
        photo = ImageTk.PhotoImage(self.username_icon)
        self.username_icon_label = tk.Label(self.lgn_frame, image=photo, bg='#040405')
        self.username_icon_label.image = photo
        self.username_icon_label.place(x=550, y=332)

        self.lgn_button = Image.open("./assests/images/btn1.png")
        photo = ImageTk.PhotoImage(self.lgn_button)
        self.lgn_button_label = tk.Label(self.lgn_frame, image=photo, bg='#040405')
        self.lgn_button_label.image = photo
        self.lgn_button_label.place(x=550, y=450)
        self.login = tk.Button(self.lgn_button_label, text='LOGIN', font=("yu gothic ui", 13, "bold"), width=25, bd=0, bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white', command=self.switch_to_homeLabel)
        self.login.place(x=20, y=10)

        self.password_label = tk.Label(self.lgn_frame, text="Password", bg="#040405", fg="#4f4e4d", font=("yu gothic ui", 13, "bold"))
        self.password_label.place(x=550, y=380)
        self.password_entry = tk.Entry(self.lgn_frame, highlightthickness=0, relief=tk.FLAT, bg="#040405", fg="#6b6a69", font=("yu gothic ui", 12, "bold"), show="*", insertbackground='#6b6a69')
        self.password_entry.place(x=580, y=416, width=244)
        self.password_line = tk.Canvas(self.lgn_frame, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0)
        self.password_line.place(x=550, y=440)

        self.password_icon = Image.open("./assests/images/password_icon.png")
        photo = ImageTk.PhotoImage(self.password_icon)
        self.password_icon_label = tk.Label(self.lgn_frame, image=photo, bg='#040405')
        self.password_icon_label.image = photo
        self.password_icon_label.place(x=550, y=414)

        self.show_image = ImageTk.PhotoImage(file="./assests/images/show.png")
        self.hide_image = ImageTk.PhotoImage(file="./assests/images/hide.png")
        self.show_button = tk.Button(self.lgn_frame, image=self.show_image, command=self.show, relief=tk.FLAT, activebackground="white", borderwidth=0, background="white", cursor="hand2")
        self.show_button.place(x=860, y=420)

    def show(self):
        self.hide_button = tk.Button(self.lgn_frame, image=self.hide_image, command=self.hide, relief=tk.FLAT, activebackground="white", borderwidth=0, background="white", cursor="hand2")
        self.hide_button.place(x=860, y=420)
        self.password_entry.config(show='')

    def hide(self):
        self.show_button = tk.Button(self.lgn_frame, image=self.show_image, command=self.show, relief=tk.FLAT, activebackground="white", borderwidth=0, background="white", cursor="hand2")
        self.show_button.place(x=860, y=420)
        self.password_entry.config(show='*')

    def switch_to_homeLabel(self):
        from Home.C2w_home import homeLabel
        username_value = self.username_entry.get()
        userpassword_value = self.password_entry.get()
        if username_value == 'Prathamesh' and userpassword_value == 'pm@16':
            messagebox.showinfo("Successful", "Login successfully")
            self.main_frame.destroy()
            class1_instance = homeLabel(self.root, self, None)
            class1_instance.pack(fill=tk.BOTH, expand=True)
        elif username_value != 'Prathamesh':
            messagebox.showinfo("Error", "Incorrect Username")
        elif userpassword_value == 'pm@16':
            messagebox.showinfo("Error", "Incorrect Password")

    def run(self):
        self.root.mainloop()
