#Wizard to be run before running main program
#importing necessary statements:
import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
import os
import time
import csv
from cryptography.fernet import Fernet

key = b'duq6gXwUm-RRsvoNTOIkfvfhl3-gT6l_kRz9pwJFAwQ='
fernet = Fernet(key)

#declaring paths in variables for easier access
file_path = os.path.dirname(os.path.realpath(__file__))
asset_path = os.path.join(file_path, "Assets")
ico_path = os.path.join(asset_path, "titleicon.ico")
theme_path = os.path.join(asset_path, "azure-dark.tcl")
secret_path = os.path.join(asset_path, "BackEnd", "secret.csv")

def wizmain():
    def makedb(list1):
        conn=mysql.connector.connect(host=list1[0], user=list1[1],  passwd=fernet.decrypt(eval(list1[2])).decode())
        cur = conn.cursor()
        cur.execute("CREATE DATABASE IF NOT EXISTS hospitaldata")
        cur.execute("use hospitaldata")
        cur.execute("CREATE TABLE IF NOT EXISTS patient(Pateint_Id int PRIMARY KEY, Name varchar(50), Age int, Ailment varchar(50), Payment_Type varchar(10), Payment_Status varchar(50), Contact decimal(10,0), Amount decimal(10,2))")
        cur.execute("CREATE TABLE IF NOT EXISTS doctor(Doctor_Id int primary key,Name varchar(50),Specialization varchar(50),DOJ date,Contact bigint, Salary Decimal(10,2)) ")
        cur.execute("CREATE TABLE IF NOT EXISTS nurse(Nurse_Id int primary key,Name varchar(50),Department varchar(50),DOJ date, Contact bigint,Salary decimal(10,2))")
        cur.execute("CREATE TABLE IF NOT EXISTS employee(Employee_Id int primary key,Name varchar(50),Job VARCHAR(50),Payment_Type varchar(50),Contact bigint,Salary Decimal(10,2))")
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
    wiz.iconbitmap(ico_path)
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

base = tk.Tk()
style = ttk.Style()
base.tk.call("source", theme_path)
base.iconbitmap(ico_path)
base.title("AsclepiusPy Wizard")
style.theme_use("azure-dark")
x = (base.winfo_screenwidth()/2)-300
y = (base.winfo_screenheight()/2)-225
base.geometry(f"600x450+{int(x)}+{int(y)}")
os.chdir(asset_path)

frm_detes = ttk.Frame(master=base)
frm_btns = ttk.Frame(master=frm_detes)

lbl_welcome = tk.Label(master=base, text="Welcome to the AsclepiusPy\nInstallation wizard", font = ("Helvetica", 25), justify="left")
lbl_proceed = ttk.Label(master=base, text="To Continue, Please login with your MySQL credentials:", justify="left")
ent_host = ttk.Entry(master=frm_detes, width=60)
ent_username = ttk.Entry(master=frm_detes, width=60)
ent_passwd = ttk.Entry(master=frm_detes, width=60, show="*")

lbl_host = ttk.Label(master=frm_detes, text="Host:")
lbl_username = ttk.Label(master=frm_detes, text="Username:")
lbl_password = ttk.Label(master=frm_detes, text="Password:")

btn_wiz = ttk.Button(master=frm_btns, text="Submit", command=wizmain)
btn_quit = ttk.Button(master=frm_btns, text="Quit", command=base.destroy)

lbl_welcome.pack(pady=10, padx=20, fill=tk.X)
lbl_proceed.pack(pady=10, padx=60, fill=tk.X)
frm_detes.pack(pady=10, padx=50, fill=tk.X)
frm_btns.grid(row=3, column=1)
lbl_host.grid(row=0, column=0, pady=20)
lbl_username.grid(row=1, column=0, pady=20)
lbl_password.grid(row=2, column=0, pady=20)
ent_host.grid(row=0, column=1, pady=20, padx=20)
ent_username.grid(row=1, column=1, pady=20, padx=20)
ent_passwd.grid(row=2, column=1, pady=20, padx=20)
btn_quit.grid(row=0, column=1, pady=20, padx=20)
btn_wiz.grid(row=0, column=0, pady=20, padx=20)


base.mainloop()