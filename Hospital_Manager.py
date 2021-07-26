import tkinter as tk
import os
from tkinter import Menu, ttk, messagebox
from PIL import ImageTk, Image
from ttkthemes import themed_tk

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
        main = themed_tk.ThemedTk(className="Mainwindow")
        main.get_themes()
        main.set_theme("adapta")
        main.geometry("1024x650")
        main.attributes("-alpha", 0.98)
        main.title("Hospital Management Software v1.0")
        main.iconbitmap(ico_path)

        menubar = Menu(main)

        main.config(bg = "grey1", menu = menubar)
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

        styles = ttk.Style(master=main)
        styles.theme_use("adapta")
        styles.configure("Treeview", background="grey15", foreground="white", rowheight = 25, fieldbackground = "grey30")
        styles.configure("TNotebook.Tab", background="cyan4")
        styles.map("Treeview", background=[("selected", "grey40")])
        styles.map("TNotebook.Tab", background=[("selected", "cyan")])

        ntbk = ttk.Notebook(master=main)
        frm1 = ttk.Frame(master=ntbk)
        frm2 = ttk.Frame(master=ntbk)
        frm3 = ttk.Frame(master=ntbk)
        frm4 = ttk.Frame(master=ntbk)

        internalntbk = ttk.Notebook(master=frm1)
        intfrm1 = ttk.Frame(master=internalntbk)
        intfrm2 = ttk.Frame(master=internalntbk)
        intfrm3 = ttk.Frame(master=internalntbk)
        intfrm4 = ttk.Frame(master=internalntbk)

        treedat1 = ttk.Treeview(master=intfrm1)
        treedat1["columns"] = ("Patient ID", "Name", "Ailment", "Payment type", "Payment status")
        treedat1.column("#0", width = 0, minwidth = 0)
        treedat1.column("Patient ID", anchor="center", width = 120)
        treedat1.column("Name", anchor = "center", width = 120)
        treedat1.column("Ailment", anchor = "center", width = 120)
        treedat1.column("Payment type", anchor = "center", width = 120)
        treedat1.column("Payment status", anchor = "center", width = 120)

        treedat1.heading("#0", text="", anchor="center")
        treedat1.heading("Patient ID", text="Patient ID", anchor="center")
        treedat1.heading("Name", text="Name", anchor="center")
        treedat1.heading("Ailment", text="Ailment", anchor="center")
        treedat1.heading("Payment type", text="Payment type", anchor="center")
        treedat1.heading("Payment status", text="Payment status", anchor="center")

        treedat2 = ttk.Treeview(master=intfrm2)
        treedat2["columns"] = ("Doctor ID", "Name", "Specialization", "DOJ", "Salary")
        treedat2.column("#0", width = 0, minwidth = 0)
        treedat2.column("Doctor ID", anchor="center", width = 120)
        treedat2.column("Name", anchor = "center", width = 120)
        treedat2.column("Specialization", anchor = "center", width = 120)
        treedat2.column("DOJ", anchor = "center", width = 120)
        treedat2.column("Salary", anchor = "center", width = 120)

        treedat2.heading("#0", text="", anchor="center")
        treedat2.heading("Doctor ID", text="Doctor ID", anchor="center")
        treedat2.heading("Name", text="Name", anchor="center")
        treedat2.heading("Specialization", text="Specialization", anchor="center")
        treedat2.heading("DOJ", text="DOJ", anchor="center")
        treedat2.heading("Salary", text="Salary", anchor="center")

        treedat3 = ttk.Treeview(master=intfrm3)
        treedat3["columns"] = ("Nurse ID", "Name", "Department", "DOJ", "Salary")
        treedat3.column("#0", width = 0, minwidth = 0)
        treedat3.column("Nurse ID", anchor="center", width = 120)
        treedat3.column("Name", anchor = "center", width = 120)
        treedat3.column("Department", anchor = "center", width = 120)
        treedat3.column("DOJ", anchor = "center", width = 120)
        treedat3.column("Salary", anchor = "center", width = 120)

        treedat3.heading("#0", text="", anchor="center")
        treedat3.heading("Nurse ID", text="Nurse ID", anchor="center")
        treedat3.heading("Name", text="Name", anchor="center")
        treedat3.heading("Department", text="Department", anchor="center")
        treedat3.heading("DOJ", text="DOJ", anchor="center")
        treedat3.heading("Salary", text="Salary", anchor="center")

        treedat4 = ttk.Treeview(master=intfrm4)
        treedat4["columns"] = ("Employee ID", "Name", "Job", "DOJ", "Salary")
        treedat4.column("#0", width = 0, minwidth = 0)
        treedat4.column("Employee ID", anchor="center", width = 120)
        treedat4.column("Name", anchor = "center", width = 120)
        treedat4.column("Job", anchor = "center", width = 120)
        treedat4.column("DOJ", anchor = "center", width = 120)
        treedat4.column("Salary", anchor = "center", width = 120)

        treedat4.heading("#0", text="", anchor="center")
        treedat4.heading("Employee ID", text="Employee ID", anchor="center")
        treedat4.heading("Name", text="Name", anchor="center")
        treedat4.heading("Job", text="Job", anchor="center")
        treedat4.heading("DOJ", text="Payment type", anchor="center")
        treedat4.heading("Salary", text="Salary", anchor="center")

        ntbk.add(frm1, text="View DB")
        ntbk.add(frm2, text="Add Data")
        ntbk.add(frm3, text="Delete Data")
        ntbk.add(frm4, text="Update Data")

        internalntbk.add(intfrm1, text="Patient Table")
        internalntbk.add(intfrm2, text="Doctor Table")
        internalntbk.add(intfrm3, text="Nurse Table")
        internalntbk.add(intfrm4, text="Employee Table")

        ntbk.pack()
        internalntbk.pack()
        treedat1.pack()
        treedat2.pack()
        treedat3.pack()
        treedat4.pack()

        lbl_bgm1 = tk.Label(master=frm1, image = bgm)
        lbl_bgm2 = tk.Label(master=frm2, image = bgm)
        lbl_bgm3 = tk.Label(master=frm3, image = bgm)
        lbl_bgm4 = tk.Label(master=frm4, image = bgm)
        lbl_bgm1.pack()
        lbl_bgm2.pack()
        lbl_bgm3.pack()
        lbl_bgm4.pack()
        main.mainloop()
    else:
        fin = messagebox.askyesno("Status", "Login Failed. Would you like to try again?")
        if fin == True:    
            usern_ent.delete(0, tk.END)
            passwd_ent.delete(0, tk.END)
        else:
            login.destroy()

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