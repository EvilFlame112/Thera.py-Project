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
from PIL import ImageTk, Image

key = b'duq6gXwUm-RRsvoNTOIkfvfhl3-gT6l_kRz9pwJFAwQ='
fernet = Fernet(key)

#declaring paths in variables for easier access 
file_path1 = os.path.join(os.environ['PROGRAMFILES'], "Thera")
base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
asset_path = os.path.join(base_path, "Assets")
ico_path = os.path.join(asset_path, "titleicon.ico")
zip_path = os.path.join(base_path, "Core.zip")
theme_path = os.path.join(asset_path, "azure-dark.tcl")
bg_path = os.path.join(asset_path, "main1.jpg")
btnimgpath = os.path.join(asset_path, "install.png")


def pathget():
    global file_path1
    ent_path.delete(0, tk.END)
    file_path1 = filedialog.askdirectory()
    ent_path.insert(0, os.path.join(file_path1, "Thera"))
    file_path1 = ent_path.get()

def adminmain():
    if ent_host.get() != "":
        if ent_username.get() != "":
            if ent_passwd.get() != "":
                frm_main.pack_forget()
                frm_detes.pack_forget()
                frm_btns.pack_forget()
                frm_chkbtns.pack_forget()
                lbl_welcome.pack_forget()
                lbl_proceed.pack_forget()
                ent_host.pack_forget()
                ent_username.pack_forget()
                ent_passwd.pack_forget()
                ent_path.pack_forget()
                ent_path.pack_forget()
                shortcut_chkbtn.pack_forget()
                start_shortcut_chkbtn.pack_forget()
                lbl_host.pack_forget()
                lbl_username.pack_forget()
                lbl_password.pack_forget()
                btn_wiz.pack_forget()
                btn_quit.pack_forget()
                btn_path.pack_forget()

                lblfrm = ttk.LabelFrame(master=base)
                lbl_adminprompt = tk.Label(master=base, text="Enter a secure password.\n This cannot be changed later and is \nthe primary gateway to authorize access to all database records", font=("Helvetica", 16))
                lbl_adminpwd = tk.Label(master=lblfrm, text="Enter admin password:", font=("Helvetica", 12))
                ent_adminpwd = ttk.Entry(master=lblfrm, width=30, show="*")
                lbl_reenter = tk.Label(master=lblfrm, text="Reenter admin password:", font=("Helvetica", 12))
                ent_reenter = ttk.Entry(master=lblfrm, width=30, show="*")

                def wizmain():
                    if ent_adminpwd.get() != "":
                        if ent_reenter.get() != "":
                            #shortcut tools
                            desktopdir = winshell.desktop()
                            shortcut_path = os.path.join(desktopdir, "TheraPy Hospital Software.lnk")
                            start_shortcut_path = os.path.join("C:\ProgramData\Microsoft\Windows\Start Menu\Programs", "TheraPy Hospital Software.lnk")
                            target = os.path.join(file_path1, "Thera.exe")
                            wrkdir = os.path.join(file_path1)
                            icon = os.path.join(file_path1, "Thera.exe")

                            if shortcut_toggle.get() == 1:
                                shell = Dispatch('WScript.Shell')
                                shortcut = shell.CreateShortCut(shortcut_path)
                                shortcut.Targetpath = target
                                shortcut.WorkingDirectory = wrkdir
                                shortcut.IconLocation = icon
                                shortcut.save()
                            else:
                                pass
                            if start_shortcut_toggle.get() == 1:
                                shell = Dispatch('WScript.Shell')
                                start_shortcut = shell.CreateShortcut(start_shortcut_path)
                                start_shortcut.Targetpath = target
                                start_shortcut.WorkingDirectory = wrkdir
                                start_shortcut.IconLocation = icon
                                start_shortcut.save()
                            else:
                                pass

                            if ent_adminpwd.get() == ent_reenter.get():
                                adminpass = fernet.encrypt(ent_adminpwd.get().encode())
                                lblfrm.place_forget()
                                lbl_adminprompt.place_forget()
                                lbl_adminpwd.pack_forget()
                                ent_adminpwd.pack_forget()
                                lbl_reenter.pack_forget()
                                ent_reenter.pack_forget()
                                
                                def makedb():
                                    for i in range(15):
                                        progress["value"] += 1
                                        base.update_idletasks()
                                        time.sleep(0.01)
                                    with zipfile.ZipFile(zip_path, "r") as assetzip:
                                        assetzip.extractall(file_path1[:-6])
                                    for i in range(100):
                                        progress["value"] += 0.5
                                        base.update_idletasks()
                                        time.sleep(0.01)
                                    secret_path = os.path.join(file_path1, "Assets", "BackEnd", "secret.csv")
                                    admin_path = os.path.join(file_path1, "Assets", "BackEnd", "adminpwd.csv")
                                    with open(admin_path, "w+", newline="") as adminfile:
                                        adminfile.seek(0)
                                        writer = csv.writer(adminfile)
                                        listadmin = [adminpass]
                                        writer.writerow(listadmin)
                                        adminfile.close()
                                    with open(secret_path, "w+", newline="") as secret:
                                        secret.seek(0)
                                        list1 = [host, user, password]
                                        writer = csv.writer(secret)
                                        writer.writerow(list1)
                                        secret.close()
                                    with open(secret_path, "r") as secret:
                                        secret.seek(0)
                                        reader = csv.reader(secret)
                                        vals = next(reader)
                                        secret.close()
                                    conn=mysql.connector.connect(host=vals[0], user=vals[1],  passwd=fernet.decrypt(eval(vals[2])).decode())
                                    cur = conn.cursor()
                                    cur.execute("CREATE DATABASE IF NOT EXISTS hospitaldata")
                                    cur.execute("use hospitaldata")
                                
                                    cur.execute("CREATE TABLE IF NOT EXISTS patient(Patient_Id int PRIMARY KEY, Name varchar(50), Age int, Ailment varchar(50), Admission_Status varchar(11),Payment_Type varchar(10), Payment_Status varchar(50), Contact decimal(10,0), Amount decimal(10,2))")
                                    cur.execute("CREATE TABLE IF NOT EXISTS chdoctor(Slno int PRIMARY KEY,FOREIGN KEY (Ch_Id) REFERENCES patient(Patient_Id),Name varchar(50),Specialization varchar(50),DOJ date,Contact bigint, Salary decimal(10,2)) ")
                                    cur.execute("CREATE TABLE IF NOT EXISTS doctor(Doctor_Id int primary key,Name varchar(50),Specialization varchar(50),DOJ date,Contact bigint, Salary decimal(10,2)) ")
                                    cur.execute("CREATE TABLE IF NOT EXISTS nurse(Nurse_Id int primary key,Name varchar(50),Department varchar(50),DOJ date, Contact bigint,Salary decimal(10,2))")
                                    cur.execute("CREATE TABLE IF NOT EXISTS employee(Employee_Id int primary key,Name varchar(50),Job VARCHAR(50),DOJ date, Contact bigint,Salary decimal(10,2))")
                                   
                                    
                                    for i in range(70):

                                        progress["value"] += 0.5
                                        base.update_idletasks()
                                        time.sleep(0.01)
                                    messagebox.showinfo("Status", "Installed successfully!")
                                    base.destroy()
                                    final_win = tk.Tk()
                                    style = ttk.Style()
                                    final_win.tk.call("source", theme_path)
                                    final_win.iconbitmap(ico_path)
                                    final_win.title("TheraPy Wizard")
                                    final_win.resizable(False, False)
                                    style.theme_use("azure-dark")
                                    x = (final_win.winfo_screenwidth()/2)-300
                                    y = (final_win.winfo_screenheight()/2)-300
                                    final_win.geometry(f"1080x600+{int(x)}+{int(y)}")

                                    tmpimg = Image.open(bg_path)
                                    tmp1img = tmpimg.resize((300,600))
                                    img = ImageTk.PhotoImage(tmp1img)

                                    lbl_img = tk.Label(master=final_win, image=img)
                                    lbl_finish = tk.Label(master=final_win, text="Finalization", font = ("Helvetica", 50), justify="left")
                                    lbl_note = tk.Label(master=final_win, text="Setup has successfully installed Thera.Py on your device.\nClick Finish to exit the wizard", font = ("Helvetica", 14), justify='left')
                                    btn_exit = ttk.Button(master=final_win, text="Finish", command=final_win.destroy, width=30)
                                    lbl_img.pack(side=tk.LEFT, fill="both")

                                    lbl_finish.place(x=310, y=200)
                                    lbl_note.place(x=310, y=280)
                                    btn_exit.place(x=850, y=550)
                                    final_win.mainloop()

                                host = ent_host.get()
                                user = ent_username.get()
                                password = fernet.encrypt(ent_passwd.get().encode())
                                style.theme_use('default')
                                style.configure("TProgressbar", background="green")
                                style.configure("TLabel", background="grey20", foreground="white")
                                style.configure("TLabelframe", background="grey20")
                                style.configure("TLabelframe.Label", background="grey20")
                                style.configure("TButton", background="grey40", foreground="white", borderwidth=0)
                                frm_install = ttk.Labelframe(master=base)
                                lbl_install = tk.Label(master=frm_install, text="Install", font = ("Helvetica", 25))
                                btn_install = ttk.Button(master=frm_install, command= makedb, text="Install", width=20)
                                lbl_instruct = ttk.Label(master=frm_install, text="Click the install button to install")
                                progress = ttk.Progressbar(master=frm_install, orient=tk.HORIZONTAL, length=500, mode="determinate")

                                frm_install.place(x=400, y=50)
                                lbl_install.grid(row=0, pady=20, padx=50)
                                lbl_instruct.grid(row=1, pady=20, padx=50)
                                btn_install.grid(row=3, pady=20, padx=50)
                                progress.grid(row=2, pady=100, padx=50)
                                
                            else:
                                messagebox.showinfo("Status", "Passwords do not match. Please check your password")
                                ent_adminpwd.delete(0, tk.END)
                                ent_reenter.delete(0, tk.END)  
                        else:
                            messagebox.showinfo("Status", "Please Fill all fields before proceeding")
                    else:
                        messagebox.showinfo("Status", "Please Fill all fields before proceeding")
                btn_adminsave = ttk.Button(master=lblfrm, text="Submit", command=wizmain)

                lbl_adminprompt.place(x=400,y=100)
                lblfrm.place(x=400,y=200)
                lbl_adminpwd.grid(row=0, column=0, padx=200, pady=10)
                ent_adminpwd.grid(row=1, column=0, padx=200, pady=10)
                lbl_reenter.grid(row=2, column=0, padx=200, pady=10)
                ent_reenter.grid(row=3, column=0, padx=200, pady=10)
                btn_adminsave.grid(row=4, column=0, padx=200, pady=20)
            else:
                messagebox.showinfo("Status", "Please Fill all fields before proceeding")
        else:
            messagebox.showinfo("Status", "Please Fill all fields before proceeding")
    else:
        messagebox.showinfo("Status", "Please Fill all fields before proceeding")

base = tk.Tk()
style = ttk.Style()
base.tk.call("source", theme_path)
base.iconbitmap(ico_path)
base.title("TheraPy Wizard")
base.resizable(False, False)
style.theme_use("azure-dark")
x = (base.winfo_screenwidth()/2)-300
y = (base.winfo_screenheight()/2)-300
base.geometry(f"1080x600+{int(x)}+{int(y)}")

tmpimg = Image.open(bg_path)
tmp1img = tmpimg.resize((300,600))
img = ImageTk.PhotoImage(tmp1img)

shortcut_toggle = tk.IntVar()
start_shortcut_toggle = tk.IntVar()

frm_main = ttk.Labelframe(master=base)
frm_detes = ttk.Frame(master=frm_main)
frm_btns = ttk.Frame(master=frm_main)
frm_chkbtns = ttk.Labelframe(master=frm_main)

lbl_img = tk.Label(master=base, image=img)
lbl_welcome = tk.Label(master=base, text="Welcome to the TheraPy\nInstallation wizard", font = ("Helvetica", 25), justify="left")
lbl_proceed = ttk.Label(master=base, text="To Continue, Please login with your MySQL credentials:", justify="left")
ent_host = ttk.Entry(master=frm_detes, width=55)
ent_username = ttk.Entry(master=frm_detes, width=55)
ent_passwd = ttk.Entry(master=frm_detes, width=55, show="*")
ent_path = ttk.Entry(master=frm_detes, width=55)
ent_path.insert(0, file_path1)
shortcut_chkbtn = ttk.Checkbutton(master=frm_chkbtns, text="Create Desktop Shortcut", variable=shortcut_toggle, onvalue=1, offvalue=0)
start_shortcut_chkbtn = ttk.Checkbutton(master=frm_chkbtns, text="Create Start Menu Shortcut", variable=start_shortcut_toggle, onvalue=1, offvalue=0)

lbl_host = ttk.Label(master=frm_detes, text="Host:")
lbl_username = ttk.Label(master=frm_detes, text="Username:")
lbl_password = ttk.Label(master=frm_detes, text="Password:")

btn_wiz = ttk.Button(master=frm_btns, text="Submit", command=adminmain)
btn_quit = ttk.Button(master=frm_btns, text="Quit", command=base.destroy)
btn_path = ttk.Button(master=frm_detes, text="Path:", command=pathget)

lbl_img.pack(side=tk.LEFT, fill="both")
lbl_welcome.pack(pady=10, fill=tk.X, anchor=tk.W)
lbl_proceed.pack(pady=10, padx=60, fill=tk.X)
frm_main.pack(pady=10, padx=50, fill=tk.X)
frm_detes.pack()
frm_chkbtns.pack(padx=140, fill=tk.X)
frm_btns.pack(pady=10, padx=210, fill=tk.X)
lbl_host.grid(row=0, column=0, pady=15, padx=10)
lbl_username.grid(row=1, column=0, pady=15, padx=10)
lbl_password.grid(row=2, column=0, pady=15, padx=10)
btn_path.grid(row=3, column=0, pady=15, padx=10)
ent_host.grid(row=0, column=1, pady=15, padx=20)
ent_username.grid(row=1, column=1, pady=15, padx=20)
ent_passwd.grid(row=2, column=1, pady=15, padx=20)
ent_path.grid(row=3, column=1, pady=15, padx=20)
shortcut_chkbtn.pack(fill=tk.X)
start_shortcut_chkbtn.pack(fill=tk.X)
btn_quit.grid(row=0, column=1, pady=10, padx=20)
btn_wiz.grid(row=0, column=0, pady=10, padx=20)


base.mainloop()
