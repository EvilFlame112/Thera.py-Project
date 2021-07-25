import tkinter as tk
import os
from tkinter import Menu, ttk, messagebox
from PIL import ImageTk, Image

file_path = os.path.dirname(os.path.realpath(__file__))
ico_path = os.path.join(file_path, "Assets", "titleicon.ico")
bg_path = os.path.join(file_path, "Assets", "img24.png")
bgm_path = os.path.join(file_path, "Assets", "main.png")

def lgin():
    user = usern_ent.get()
    pwd = passwd_ent.get()
    if user == "root" and pwd == "root":
        messagebox.showinfo("Status", "Login Success")
        login.destroy()
        main = tk.Tk(className="Mainwindow")
        main.geometry("1024x650")
        main.attributes("-alpha", 0.98)
        main.title("Hospital Management Software v1.0")
        main.iconbitmap(ico_path)

        menubar = Menu(main)

        main.config(bg = "black", menu = menubar)
        main.resizable(False,False)
        main.option_add('*tearOff', False)
        menubar = Menu(main)
        main.config(menu = menubar)
        tmpbgm = Image.open(bgm_path)
        tmp1bgm = tmpbgm.resize((1024,650))
        bgm = ImageTk.PhotoImage(tmp1bgm)

        menu_file = Menu(menubar)

        menubar.add_cascade(menu=menu_file, label = "File")
        menu_file.add_command(label = "Exit", command = login.destroy)


        ntbk = ttk.Notebook(master=main)
        frm1 = ttk.Frame(master=ntbk)
        frm2 = ttk.Frame(master=ntbk)
        frm3 = ttk.Frame(master=ntbk)
        frm4 = ttk.Frame(master=ntbk)

        treedat = ttk.Treeview(master=frm1)
        treedat["columns"] = ("Patient ID", "Name", "Ailment", "Payment type", "Payment status")
        treedat.column("#0", width = 0, minwidth = 0)
        treedat.column("Patient ID", anchor="w", width = 120)
        treedat.column("Name", anchor = "center", width = 120)
        treedat.column("Ailment", anchor = "w", width = 120)
        treedat.column("Payment type", anchor = "w", width = 120)
        treedat.column("Payment status", anchor = "w", width = 120)

        treedat.heading("#0", text="", anchor="w")
        treedat.heading("Patient ID", text="Patient ID", anchor="w")
        treedat.heading("Name", text="Name", anchor="center")
        treedat.heading("Ailment", text="Ailment", anchor="w")
        treedat.heading("Payment type", text="Payment type", anchor="w")
        treedat.heading("Payment status", text="Payment status", anchor="w")

        ntbk.add(frm1, text="View DB")
        ntbk.add(frm2, text="Add Data")
        ntbk.add(frm3, text="Delete Data")
        ntbk.add(frm4, text="Update Data")

        ntbk.pack()
        treedat.pack()

        lbl_bgm1 = tk.Label(master=frm1, image = bgm)
        lbl_bgm2 = tk.Label(master=frm1, image = bgm)
        lbl_bgm3 = tk.Label(master=frm1, image = bgm)
        lbl_bgm4 = tk.Label(master=frm1, image = bgm)
        lbl_bgm1.pack()
        lbl_bgm2.pack()
        lbl_bgm3.pack()
        lbl_bgm4.pack()
        main.mainloop()
    else:
        messagebox.showinfo("Status", "Login Failed. Please check your credentials")
        usern_ent.delete(0, tk.END)
        passwd_ent.delete(0, tk.END)

tmpbg = Image.open(bg_path)
tmp1bg = tmpbg.resize((1024,650))

login = tk.Tk(className="Loginwindow")
login.geometry("1024x650")
login.title("Hospital Management Software v1.0")
login.attributes("-alpha", 0.98)
login.iconbitmap(ico_path)
login.resizable(False,False)

login.option_add('*tearOff', False)
menubar = Menu(login)
login.config(menu = menubar,bg = "black")
bg = ImageTk.PhotoImage(tmp1bg)

lbl_bg = tk.Label(master=login, image = bg)
usern_ent = tk.Entry(master=login, width = 30, font = ("SF Pro Display", 16), bg = "grey30", fg = "white")
passwd_ent = tk.Entry(master=login, width = 30, font = ("SF Pro Display", 16), bg = "grey30", fg = "white", show="*")


btn_login = tk.Button(master=login, text = "Login", command = lgin, borderwidth=2, bg = "grey15", fg = "white", relief=tk.SUNKEN, width = 25, height = 1, font = ("SF Pro Display", 20))

menu_file = Menu(menubar)

menubar.add_cascade(menu=menu_file, label = "File")
menu_file.add_command(label = "Exit", command = login.destroy)


lbl_bg.pack()
usern_ent.place(x=230, y=465)
passwd_ent.place(x=230, y=500)
btn_login.place(x=230, y=550)
login.mainloop()