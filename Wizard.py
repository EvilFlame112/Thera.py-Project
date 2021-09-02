#Wizard to be run before running main program
#importing necessary statements:
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import mysql.connector
import os
import time
import sys
import csv
from cryptography.fernet import Fernet
import zipfile
import winshell
from win32com.client import Dispatch

key = b'duq6gXwUm-RRsvoNTOIkfvfhl3-gT6l_kRz9pwJFAwQ='
fernet = Fernet(key)

#declaring paths in variables for easier access 
file_path1 = ""
base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
asset_path = os.path.join(base_path, "Assets")
ico_path = os.path.join(asset_path, "titleicon.ico")
zip_path = os.path.join(base_path, "Core.zip")
theme_path = os.path.join(asset_path, "azure-dark.tcl")


def pathget():
    global file_path1
    ent_path.delete(0, tk.END)
    file_path1 = filedialog.askdirectory()
    ent_path.insert(0, file_path1)
    file_path1 = ent_path.get()

def adminmain():
    admin = tk.Toplevel(master=base)
    admin.title("TheraPy Wizard")
    admin.iconbitmap(ico_path)
    x = (admin.winfo_screenwidth()/2)-315
    y = (admin.winfo_screenheight()/2)-225
    admin.resizable(False,False)
    admin.geometry(f"630x450+{int(x)}+{int(y)}")
    lblfrm = ttk.LabelFrame(master=admin)
    lbl_adminprompt = tk.Label(master=admin, text="Enter a secure password.\n This cannot be changed later and is \nthe primary gateway to authorize access to all database records", font=("Helvetica", 16))
    lbl_adminpwd = tk.Label(master=lblfrm, text="Enter admin password:", font=("Helvetica", 12))
    ent_adminpwd = ttk.Entry(master=lblfrm, width=30, show="*")
    lbl_reenter = tk.Label(master=lblfrm, text="Reenter admin password:", font=("Helvetica", 12))
    ent_reenter = ttk.Entry(master=lblfrm, width=30, show="*")

    def wizmain():
        with zipfile.ZipFile(zip_path, "r") as assetzip:
            assetzip.extractall(file_path1)
        secret_path = os.path.join(file_path1, "Thera", "Assets", "BackEnd", "secret.csv")
        admin_path = os.path.join(file_path1, "Thera", "Assets", "BackEnd", "adminpwd.csv")

        if shortcut_toggle.get() == 1:
            #shortcut tools
            desktopdir = winshell.desktop()
            shortcut_path = os.path.join(desktopdir, "TheraPy Hospital Software.lnk")
            target = os.path.join(file_path1, "Thera", "Thera.exe")
            wrkdir = os.path.join(file_path1, "Thera")
            icon = os.path.join(file_path1, "Thera", "Thera.exe")

            shell = Dispatch('WScript.Shell')
            shortcut = shell.CreateShortCut(shortcut_path)
            shortcut.Targetpath = target
            shortcut.WorkingDirectory = wrkdir
            shortcut.IconLocation = icon
            shortcut.save()
        else:
            pass

        if ent_adminpwd.get() == ent_reenter.get():
            with open(admin_path, "w+", newline="") as adminfile:
                adminfile.seek(0)
                writer = csv.writer(adminfile)
                listadmin = [fernet.encrypt(ent_adminpwd.get().encode())]
                writer.writerow(listadmin)
                adminfile.close()
            admin.destroy()
            def makedb(list1):
                conn=mysql.connector.connect(host=list1[0], user=list1[1],  passwd=fernet.decrypt(eval(list1[2])).decode())
                cur = conn.cursor()
                cur.execute("CREATE DATABASE IF NOT EXISTS hospitaldata")
                cur.execute("use hospitaldata")
                cur.execute("CREATE TABLE IF NOT EXISTS patient(Patient_Id int PRIMARY KEY, Name varchar(50), Age int, Ailment varchar(50), Payment_Type varchar(10), Payment_Status varchar(50), Contact decimal(10,0), Amount decimal(10,2))")
                cur.execute("CREATE TABLE IF NOT EXISTS doctor(Doctor_Id int primary key,Name varchar(50),Specialization varchar(50),DOJ date,Contact bigint, Salary decimal(10,2)) ")
                cur.execute("CREATE TABLE IF NOT EXISTS nurse(Nurse_Id int primary key,Name varchar(50),Department varchar(50),DOJ date, Contact bigint,Salary decimal(10,2))")
                cur.execute("CREATE TABLE IF NOT EXISTS employee(Employee_Id int primary key,Name varchar(50),Job VARCHAR(50),DOJ date, Contact bigint,Salary decimal(10,2))")
                for i in range(200):
                    progress["value"] += 0.5
                    wiz.update_idletasks()
                    time.sleep(0.01)
                messagebox.showinfo("Status", "Installed successfully!")
                wiz.destroy()


            with open(secret_path, "w+", newline="") as secret:
                secret.seek(0)
                list1 = [ent_host.get(), ent_username.get(), fernet.encrypt(ent_passwd.get().encode())]
                writer = csv.writer(secret)
                writer.writerow(list1)
                secret.close()

            base.destroy()
            wiz = tk.Tk()
            style = ttk.Style()
            wiz.tk.call("source", theme_path)
            wiz.title("TheraPy Wizard")
            wiz.iconbitmap(ico_path)
            wiz.resizable(False,False)
            style.theme_use("azure-dark")
            x = (wiz.winfo_screenwidth()/2)-175
            y = (wiz.winfo_screenheight()/2)-175
            wiz.geometry(f"350x350+{int(x)}+{int(y)}")

            with open(secret_path, "r") as secret:
                secret.seek(0)
                reader = csv.reader(secret)
                vals = next(reader)
                secret.close()

            lbl_install = tk.Label(master=wiz, text="Install", font = ("Helvetica", 25))
            btn_install = ttk.Button(master=wiz, text="Install", width=30, command= lambda: makedb(vals))
            lbl_instruct = ttk.Label(master=wiz, text="Click the install button to install")
            progress = ttk.Progressbar(master=wiz, orient=tk.HORIZONTAL, length=250, mode="determinate")

            lbl_install.grid(row=0, pady=20, padx=50)
            lbl_instruct.grid(row=1, pady=20, padx=50)
            progress.grid(row=2, pady=20, padx=50)
            btn_install.grid(row=3, pady=40, padx=50)

            wiz.mainloop()
        else:
            messagebox.showinfo("Status", "Passwords do not match. Please check your password")
            ent_adminpwd.delete(0, tk.END)
            ent_reenter.delete(0, tk.END)  
    btn_adminsave = ttk.Button(master=lblfrm, text="Submit", command=wizmain)

    lbl_adminprompt.pack()
    lblfrm.pack()
    lbl_adminpwd.grid(row=0, column=0, padx=15, pady=10)
    ent_adminpwd.grid(row=1, column=0, padx=15, pady=10)
    lbl_reenter.grid(row=2, column=0, padx=15, pady=10)
    ent_reenter.grid(row=3, column=0, padx=15, pady=10)
    btn_adminsave.grid(row=4, column=0, padx=15, pady=20)

    admin.mainloop()

base = tk.Tk()
style = ttk.Style()
base.tk.call("source", theme_path)
base.iconbitmap(ico_path)
base.title("TheraPy Wizard")
base.resizable(False, False)
style.theme_use("azure-dark")
x = (base.winfo_screenwidth()/2)-300
y = (base.winfo_screenheight()/2)-300
base.geometry(f"600x600+{int(x)}+{int(y)}")

shortcut_toggle = tk.IntVar()

frm_main = ttk.Labelframe(master=base)
frm_detes = ttk.Frame(master=frm_main)
frm_btns = ttk.Frame(master=frm_main)

lbl_welcome = tk.Label(master=base, text="Welcome to the TheraPy\nInstallation wizard", font = ("Helvetica", 25), justify="left")
lbl_proceed = ttk.Label(master=base, text="To Continue, Please login with your MySQL credentials:", justify="left")
ent_host = ttk.Entry(master=frm_detes, width=55)
ent_username = ttk.Entry(master=frm_detes, width=55)
ent_passwd = ttk.Entry(master=frm_detes, width=55, show="*")
ent_path = ttk.Entry(master=frm_detes, width=55)
shortcut_chkbtn = ttk.Checkbutton(master=frm_detes, text="Create Desktop Shortcut", variable=shortcut_toggle, onvalue=1, offvalue=0)

lbl_host = ttk.Label(master=frm_detes, text="Host:")
lbl_username = ttk.Label(master=frm_detes, text="Username:")
lbl_password = ttk.Label(master=frm_detes, text="Password:")

btn_wiz = ttk.Button(master=frm_btns, text="Submit", command=adminmain)
btn_quit = ttk.Button(master=frm_btns, text="Quit", command=base.destroy)
btn_path = ttk.Button(master=frm_detes, text="Path:", command=pathget)


lbl_welcome.pack(pady=10, padx=20, fill=tk.X)
lbl_proceed.pack(pady=10, padx=60, fill=tk.X)
frm_main.pack(pady=10, padx=50, fill=tk.X)
frm_detes.pack()
frm_btns.pack(pady=10, padx=120, fill=tk.X)
lbl_host.grid(row=0, column=0, pady=20, padx=10)
lbl_username.grid(row=1, column=0, pady=20, padx=10)
lbl_password.grid(row=2, column=0, pady=20, padx=10)
btn_path.grid(row=3, column=0, pady=20, padx=10)
ent_host.grid(row=0, column=1, pady=20, padx=20)
ent_username.grid(row=1, column=1, pady=20, padx=20)
ent_passwd.grid(row=2, column=1, pady=20, padx=20)
ent_path.grid(row=3, column=1, pady=20, padx=20)
shortcut_chkbtn.grid(row=4, column=1, padx=20, pady=5)
btn_quit.grid(row=0, column=1, pady=20, padx=20)
btn_wiz.grid(row=0, column=0, pady=20, padx=20)


base.mainloop()