#Hospital management system v1.0
#Code credits:
#       Frontend/GUI - Ram
#       Backend/SQL - Sai
#       Documentation - Yash


#Importing necessary modules
import tkinter as tk
import os
import random
from tkinter import Menu, ttk, messagebox
from PIL import ImageTk, Image
import csv
from cryptography.fernet import Fernet
import datetime

#custom sql module
from Assets.BackEnd import sqlqueries

#Declaring path variables for extensive support with asset folder
file_path = os.path.dirname(os.path.realpath(__file__))
asset_path = os.path.join(file_path, "Assets")
ico_path = os.path.join(asset_path, "titleicon.ico")
bg_path = os.path.join(asset_path, "img24.png")
bgm_path = os.path.join(asset_path, random.choice(["main.png","main.jpg"]))
theme_path = os.path.join(asset_path, "azure-dark.tcl")
userdat_path = os.path.join(asset_path, "usernamepwd.csv")
admin_path = os.path.join(asset_path, "Backend", "adminpwd.csv")

#fernet encoding:
key = b'duq6gXwUm-RRsvoNTOIkfvfhl3-gT6l_kRz9pwJFAwQ='
fernet = Fernet(key)

#registering into csv:
def reg():
    try:
        msgbox_yesnoregister.destroy()
    except NameError:
        pass
    reg_window = tk.Toplevel(master=login)
    x = (reg_window.winfo_screenwidth()/2)-200
    y = (reg_window.winfo_screenheight()/2)-110
    reg_window.geometry(f"400x220+{int(x)}+{int(y)}")
    reg_window.attributes("-alpha", 0.98)
    reg_window.title("TheraPy v1.0 Registering")
    reg_window.iconbitmap(ico_path)
    reg_window.option_add('*tearOff', False)
    lbl_title = tk.Label(master=reg_window, text="Register:", font=("SF Pro Display", 21))
    ent_newuser = ttk.Entry(master=reg_window, width=30)
    lbl_newuser = ttk.Label(master=reg_window, text="Username: ")
    ent_newpwd = ttk.Entry(master=reg_window, width=30, show="*")
    lbl_newpwd = ttk.Label(master=reg_window, text="Password: ")
    ent_renewpwd = ttk.Entry(master=reg_window, width=30, show="*")
    lbl_renewpwd = ttk.Label(master=reg_window, text="Reenter Password: ")

    def checknadddat():
        admin = tk.Toplevel(master=reg_window)
        x = (admin.winfo_screenwidth()/2)-200
        y = (admin.winfo_screenheight()/2)-110
        admin.geometry(f"400x220+{int(x)}+{int(y)}")
        admin.attributes("-alpha", 0.98)
        admin.title("TheraPy v1.0 Registering")
        admin.iconbitmap(ico_path)
        admin.option_add('*tearOff', False)
        lblfrm_0 = ttk.Label(master=admin)
        lbl_adminpwd = tk.Label(master=lblfrm_0, text="Enter admin password:", font=("Helvetica", 12))
        ent_adminpwd = ttk.Entry(master=lblfrm_0, width=30, show="*")
        with open(admin_path, "r") as adminfile:
            reader = csv.reader(adminfile)
            adminpasskey = next(reader)
            adminfile.close()
        def adddat():
            if ent_adminpwd.get() == fernet.decrypt(eval(adminpasskey[0])).decode():
                if ent_newpwd.get() == ent_renewpwd.get():
                    newpwd = ent_newpwd.get()
                    with open(userdat_path, "a+", newline="") as lgindetes:
                        writer = csv.writer(lgindetes)
                        reader = csv.reader(lgindetes)
                        temp = []
                        for i in reader:
                            temp.append(i)
                        if ent_newuser.get() not in temp:
                            if ent_newuser.get() != "":
                                writer.writerow([ent_newuser.get(), fernet.encrypt(newpwd.encode())])
                                messagebox.showinfo("Status", "Registered successfully")
                                reg_window.destroy()
                                lgindetes.close()
                            elif ent_newuser.get() == "":
                                messagebox.showinfo("Status", "Username cannot be empty")
                        elif ent_newuser.get() in temp:
                            messagebox.showinfo("Status", "User already exists")
                else:
                    messagebox.showinfo("Status", "Please check your password and confirm that the same password is entered in both fields.")
                    ent_newuser.delete(0, tk.END)
                    ent_newpwd.delete(0, tk.END)
                    ent_renewpwd.delete(0, tk.END)
            else:
                messagebox.showinfo("Status", "Admin Password is Incorrect.")
                ent_newuser.delete(0, tk.END)
                ent_newpwd.delete(0, tk.END)
                ent_renewpwd.delete(0, tk.END)
                ent_adminpwd.delete(0, tk.END)
                admin.destroy()
                reg_window.destroy()
        btn_check = ttk.Button(master=lblfrm_0, text="Submit", command=adddat)
        lblfrm_0.pack()
        lbl_adminpwd.grid(row=0, column=0, pady=10)
        ent_adminpwd.grid(row=1, column=0, pady=10)
        btn_check.grid(row=2, column=0, pady=10)

    
    btn_submit = ttk.Button(master=reg_window, text="Submit", command=checknadddat, width=10)

    lbl_title.grid(row=0, column=1, padx=5, pady=5)
    lbl_newuser.grid(row=1, column=0, padx=5, pady=5)
    ent_newuser.grid(row=1, column=1, padx=5, pady=5)
    lbl_newpwd.grid(row=2, column=0, padx=5, pady=5)
    ent_newpwd.grid(row=2, column=1, padx=5, pady=5)
    lbl_renewpwd.grid(row=3, column=0, padx=5, pady=5)
    ent_renewpwd.grid(row=3, column=1, padx=5, pady=5)
    btn_submit.grid(row=4, column=1, padx=5, pady=5)
    reg_window.mainloop()
    

#defining main window
def mainwindow():
    main = tk.Tk(className="Mainwindow")
    x = (main.winfo_screenwidth()/2)-512
    y = (main.winfo_screenheight()/2)-325
    style = ttk.Style()
    main.tk.call("source", theme_path)
    style.theme_use("azure-dark")
    main.geometry(f"1024x650+{int(x)}+{int(y)}")
    main.attributes("-alpha", 0.98)
    main.title("Thera.py v1.0")
    main.iconbitmap(ico_path)

    #making a menubar with "file" as an option
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

    #making a notebook with tabs for accessing different tables from database
    ntbk = ttk.Notebook(master=main)
    frm1 = ttk.Frame(master=ntbk)
    frm2 = ttk.Frame(master=ntbk)
    frm3 = ttk.Frame(master=ntbk)
    frm4 = ttk.Frame(master=ntbk)
    frm5 = ttk.Frame(master=ntbk)

    #set of internal tabs for accessing in view tab
    internalntbk = ttk.Notebook(master=frm1)
    intfrm1 = ttk.Frame(master=internalntbk)
    intfrm2 = ttk.Frame(master=internalntbk)
    intfrm3 = ttk.Frame(master=internalntbk)
    intfrm4 = ttk.Frame(master=internalntbk)

    #set of internal tabs for accessing in add tab
    internalntbk1 = ttk.Notebook(master=frm2)
    intfrm5 = ttk.Frame(master=internalntbk1)
    intfrm6 = ttk.Frame(master=internalntbk1)
    intfrm7 = ttk.Frame(master=internalntbk1)
    intfrm8 = ttk.Frame(master=internalntbk1)

    #set of internal tabs for accessing in delete tab
    internalntbk2 = ttk.Notebook(master=frm3)
    intfrm9 = ttk.Frame(master=internalntbk2)
    intfrm10 = ttk.Frame(master=internalntbk2)
    intfrm11 = ttk.Frame(master=internalntbk2)
    intfrm12= ttk.Frame(master=internalntbk2)

    #set of internal tabs for accessing in update tab
    internalntbk3 = ttk.Notebook(master=frm4)
    intfrm13 = ttk.Frame(master=internalntbk3)
    intfrm14 = ttk.Frame(master=internalntbk3)
    intfrm15 = ttk.Frame(master=internalntbk3)
    intfrm16 = ttk.Frame(master=internalntbk3)

    #set of internal tabs for accessing in search tab
    internalntbk4 = ttk.Notebook(master=frm5)
    intfrm17 = ttk.Frame(master=internalntbk4)
    intfrm18 = ttk.Frame(master=internalntbk4)
    intfrm19 = ttk.Frame(master=internalntbk4)
    intfrm20 = ttk.Frame(master=internalntbk4)

    #scrollbar for scrolling (-_-)
    scrlbrfrm1 = ttk.Frame(master=intfrm1)
    scrlbr1 = ttk.Scrollbar(master=scrlbrfrm1)
    scrlbrfrm2 = ttk.Frame(master=intfrm2)
    scrlbr2 = ttk.Scrollbar(master=scrlbrfrm2)
    scrlbrfrm3 = ttk.Frame(master=intfrm3)
    scrlbr3 = ttk.Scrollbar(master=scrlbrfrm3)
    scrlbrfrm4 = ttk.Frame(master=intfrm4)
    scrlbr4 = ttk.Scrollbar(master=scrlbrfrm4)
    scrlbrfrm5 = ttk.Frame(master=intfrm9)
    scrlbr5 = ttk.Scrollbar(master=scrlbrfrm5)
    scrlbrfrm6 = ttk.Frame(master=intfrm10)
    scrlbr6 = ttk.Scrollbar(master=scrlbrfrm6)
    scrlbrfrm7 = ttk.Frame(master=intfrm11)
    scrlbr7 = ttk.Scrollbar(master=scrlbrfrm7)
    scrlbrfrm8 = ttk.Frame(master=intfrm12)
    scrlbr8 = ttk.Scrollbar(master=scrlbrfrm8)
    scrlbrfrm9 = ttk.Frame(master=intfrm13)
    scrlbr9 = ttk.Scrollbar(master=scrlbrfrm9)
    scrlbrfrm10 = ttk.Frame(master=intfrm14)
    scrlbr10 = ttk.Scrollbar(master=scrlbrfrm10)
    scrlbrfrm11 = ttk.Frame(master=intfrm15)
    scrlbr11 = ttk.Scrollbar(master=scrlbrfrm11)
    scrlbrfrm12 = ttk.Frame(master=intfrm16)
    scrlbr12 = ttk.Scrollbar(master=scrlbrfrm12)
    scrlbrfrm13 = ttk.Frame(master=intfrm17)
    scrlbr13 = ttk.Scrollbar(master=scrlbrfrm13)
    scrlbrfrm14 = ttk.Frame(master=intfrm18)
    scrlbr14 = ttk.Scrollbar(master=scrlbrfrm14)
    scrlbrfrm15 = ttk.Frame(master=intfrm19)
    scrlbr15 = ttk.Scrollbar(master=scrlbrfrm15)
    scrlbrfrm16 = ttk.Frame(master=intfrm20)
    scrlbr16 = ttk.Scrollbar(master=scrlbrfrm16)

    #Making tables with treeview
    treedat1 = ttk.Treeview(master=scrlbrfrm1, yscrollcommand=scrlbr1.set)
    scrlbr1.config(command = treedat1.yview)
    treedat1["columns"] = ("Patient ID", "Name", "Age", "Ailment", "Payment type", "Payment status", "Contact", "Amount")
    treedat1.column("#0", width = 0, minwidth = 0, stretch=0)
    treedat1.column("Patient ID", anchor="center", width = 120)
    treedat1.column("Name", anchor = "center", width = 120)
    treedat1.column("Age", anchor = "center", width = 120)
    treedat1.column("Ailment", anchor = "center", width = 120)
    treedat1.column("Payment type", anchor = "center", width = 120)
    treedat1.column("Payment status", anchor = "center", width = 120)
    treedat1.column("Contact", anchor = "center", width = 120)
    treedat1.column("Amount", anchor = "center", width = 120)

    treedat1.heading("#0", text="", anchor="center")
    treedat1.heading("Patient ID", text="Patient ID", anchor="center")
    treedat1.heading("Name", text="Name", anchor="center")
    treedat1.heading("Age", text="Age", anchor="center")
    treedat1.heading("Ailment", text="Ailment", anchor="center")
    treedat1.heading("Payment type", text="Payment type", anchor="center")
    treedat1.heading("Payment status", text="Payment status", anchor="center")
    treedat1.heading("Contact", text="Contact", anchor="center")
    treedat1.heading("Amount", text="Amount", anchor="center")

    treedat2 = ttk.Treeview(master=scrlbrfrm2, yscrollcommand=scrlbr2.set)
    scrlbr2.config(command = treedat2.yview)
    treedat2["columns"] = ("Doctor ID", "Name", "Specialization", "DOJ", "Contact", "Salary")
    treedat2.column("#0", width = 0, minwidth = 0, stretch=0)
    treedat2.column("Doctor ID", anchor="center", width = 120)
    treedat2.column("Name", anchor = "center", width = 120)
    treedat2.column("Specialization", anchor = "center", width = 120)
    treedat2.column("DOJ", anchor = "center", width = 120)
    treedat2.column("Contact", anchor = "center", width = 120)
    treedat2.column("Salary", anchor = "center", width = 120)

    treedat2.heading("#0", text="", anchor="center")
    treedat2.heading("Doctor ID", text="Doctor ID", anchor="center")
    treedat2.heading("Name", text="Name", anchor="center")
    treedat2.heading("Specialization", text="Specialization", anchor="center")
    treedat2.heading("DOJ", text="DOJ", anchor="center")
    treedat2.heading("Contact", text="Contact", anchor="center")
    treedat2.heading("Salary", text="Salary", anchor="center")

    treedat3 = ttk.Treeview(master=scrlbrfrm3, yscrollcommand=scrlbr3.set)
    scrlbr3.config(command = treedat3.yview)
    treedat3["columns"] = ("Nurse ID", "Name", "Department", "DOJ", "Contact", "Salary")
    treedat3.column("#0", width = 0, minwidth = 0, stretch=0)
    treedat3.column("Nurse ID", anchor="center", width = 120)
    treedat3.column("Name", anchor = "center", width = 120)
    treedat3.column("Department", anchor = "center", width = 120)
    treedat3.column("DOJ", anchor = "center", width = 120)
    treedat3.column("Contact", anchor = "center", width = 120)
    treedat3.column("Salary", anchor = "center", width = 120)

    treedat3.heading("#0", text="", anchor="center")
    treedat3.heading("Nurse ID", text="Nurse ID", anchor="center")
    treedat3.heading("Name", text="Name", anchor="center")
    treedat3.heading("Department", text="Department", anchor="center")
    treedat3.heading("DOJ", text="DOJ", anchor="center")
    treedat3.heading("Contact", text="Contact", anchor="center")
    treedat3.heading("Salary", text="Salary", anchor="center")

    treedat4 = ttk.Treeview(master=scrlbrfrm4, yscrollcommand=scrlbr4.set)
    scrlbr4.config(command = treedat4.yview)
    treedat4["columns"] = ("Employee ID", "Name", "Job", "DOJ", "Contact", "Salary")
    treedat4.column("#0", width = 0, minwidth = 0, stretch=0)
    treedat4.column("Employee ID", anchor="center", width = 120)
    treedat4.column("Name", anchor = "center", width = 120)
    treedat4.column("Job", anchor = "center", width = 120)
    treedat4.column("DOJ", anchor = "center", width = 120)
    treedat4.column("Contact", anchor = "center", width = 120)
    treedat4.column("Salary", anchor = "center", width = 120)

    treedat4.heading("#0", text="", anchor="center")
    treedat4.heading("Employee ID", text="Employee ID", anchor="center")
    treedat4.heading("Name", text="Name", anchor="center")
    treedat4.heading("Job", text="Job", anchor="center")
    treedat4.heading("DOJ", text="DOJ", anchor="center")
    treedat4.heading("Contact", text="Contact", anchor="center")
    treedat4.heading("Salary", text="Salary", anchor="center")

    treedat5 = ttk.Treeview(master=scrlbrfrm5, yscrollcommand=scrlbr5.set)
    scrlbr5.config(command = treedat5.yview)
    treedat5["columns"] = ("Patient ID", "Name", "Age", "Ailment", "Payment type", "Payment status", "Contact", "Amount")
    treedat5.column("#0", width = 0, minwidth = 0, stretch=0)
    treedat5.column("Patient ID", anchor="center", width = 120)
    treedat5.column("Name", anchor = "center", width = 120)
    treedat5.column("Age", anchor = "center", width = 120)
    treedat5.column("Ailment", anchor = "center", width = 120)
    treedat5.column("Payment type", anchor = "center", width = 120)
    treedat5.column("Payment status", anchor = "center", width = 120)
    treedat5.column("Contact", anchor = "center", width = 120)
    treedat5.column("Amount", anchor = "center", width = 120)

    treedat5.heading("#0", text="", anchor="center")
    treedat5.heading("Patient ID", text="Patient ID", anchor="center")
    treedat5.heading("Name", text="Name", anchor="center")
    treedat5.heading("Age", text="Age", anchor="center")
    treedat5.heading("Ailment", text="Ailment", anchor="center")
    treedat5.heading("Payment type", text="Payment type", anchor="center")
    treedat5.heading("Payment status", text="Payment status", anchor="center")
    treedat5.heading("Contact", text="Contact", anchor="center")
    treedat5.heading("Amount", text="Amount", anchor="center")

    treedat6 = ttk.Treeview(master=scrlbrfrm6, yscrollcommand=scrlbr6.set)
    scrlbr6.config(command = treedat6.yview)
    treedat6["columns"] = ("Doctor ID", "Name", "Specialization", "DOJ", "Contact", "Salary")
    treedat6.column("#0", width = 0, minwidth = 0, stretch=0)
    treedat6.column("Doctor ID", anchor="center", width = 120)
    treedat6.column("Name", anchor = "center", width = 120)
    treedat6.column("Specialization", anchor = "center", width = 120)
    treedat6.column("DOJ", anchor = "center", width = 120)
    treedat6.column("Contact", anchor = "center", width = 120)
    treedat6.column("Salary", anchor = "center", width = 120)

    treedat6.heading("#0", text="", anchor="center")
    treedat6.heading("Doctor ID", text="Doctor ID", anchor="center")
    treedat6.heading("Name", text="Name", anchor="center")
    treedat6.heading("Specialization", text="Specialization", anchor="center")
    treedat6.heading("DOJ", text="DOJ", anchor="center")
    treedat6.heading("Contact", text="Contact", anchor="center")
    treedat6.heading("Salary", text="Salary", anchor="center")

    treedat7 = ttk.Treeview(master=scrlbrfrm7, yscrollcommand=scrlbr7.set)
    scrlbr7.config(command = treedat7.yview)
    treedat7["columns"] = ("Nurse ID", "Name", "Department", "DOJ", "Contact", "Salary")
    treedat7.column("#0", width = 0, minwidth = 0, stretch=0)
    treedat7.column("Nurse ID", anchor="center", width = 120)
    treedat7.column("Name", anchor = "center", width = 120)
    treedat7.column("Department", anchor = "center", width = 120)
    treedat7.column("DOJ", anchor = "center", width = 120)
    treedat7.column("Contact", anchor = "center", width = 120)
    treedat7.column("Salary", anchor = "center", width = 120)

    treedat7.heading("#0", text="", anchor="center")
    treedat7.heading("Nurse ID", text="Nurse ID", anchor="center")
    treedat7.heading("Name", text="Name", anchor="center")
    treedat7.heading("Department", text="Department", anchor="center")
    treedat7.heading("DOJ", text="DOJ", anchor="center")
    treedat7.heading("Contact", text="Contact", anchor="center")
    treedat7.heading("Salary", text="Salary", anchor="center")

    treedat8 = ttk.Treeview(master=scrlbrfrm8, yscrollcommand=scrlbr8.set)
    scrlbr8.config(command = treedat8.yview)
    treedat8["columns"] = ("Employee ID", "Name", "Job", "DOJ", "Contact", "Salary")
    treedat8.column("#0", width = 0, minwidth = 0, stretch=0)
    treedat8.column("Employee ID", anchor="center", width = 120)
    treedat8.column("Name", anchor = "center", width = 120)
    treedat8.column("Job", anchor = "center", width = 120)
    treedat8.column("DOJ", anchor = "center", width = 120)
    treedat8.column("Contact", anchor = "center", width = 120)
    treedat8.column("Salary", anchor = "center", width = 120)

    treedat8.heading("#0", text="", anchor="center")
    treedat8.heading("Employee ID", text="Employee ID", anchor="center")
    treedat8.heading("Name", text="Name", anchor="center")
    treedat8.heading("Job", text="Job", anchor="center")
    treedat8.heading("DOJ", text="DOJ", anchor="center")
    treedat8.heading("Contact", text="Contact", anchor="center")
    treedat8.heading("Salary", text="Salary", anchor="center")

    treedat9 = ttk.Treeview(master=scrlbrfrm9, yscrollcommand=scrlbr9.set)
    scrlbr9.config(command = treedat9.yview)
    treedat9["columns"] = ("Patient ID", "Name", "Age", "Ailment", "Payment type", "Payment status", "Contact", "Amount")
    treedat9.column("#0", width = 0, minwidth = 0, stretch=0)
    treedat9.column("Patient ID", anchor="center", width = 120)
    treedat9.column("Name", anchor = "center", width = 120)
    treedat9.column("Age", anchor = "center", width = 120)
    treedat9.column("Ailment", anchor = "center", width = 120)
    treedat9.column("Payment type", anchor = "center", width = 120)
    treedat9.column("Payment status", anchor = "center", width = 120)
    treedat9.column("Contact", anchor = "center", width = 120)
    treedat9.column("Amount", anchor = "center", width = 120)

    treedat9.heading("#0", text="", anchor="center")
    treedat9.heading("Patient ID", text="Patient ID", anchor="center")
    treedat9.heading("Name", text="Name", anchor="center")
    treedat9.heading("Age", text="Age", anchor="center")
    treedat9.heading("Ailment", text="Ailment", anchor="center")
    treedat9.heading("Payment type", text="Payment type", anchor="center")
    treedat9.heading("Payment status", text="Payment status", anchor="center")
    treedat9.heading("Contact", text="Contact", anchor="center")
    treedat9.heading("Amount", text="Amount", anchor="center")

    treedat10 = ttk.Treeview(master=scrlbrfrm10, yscrollcommand=scrlbr10.set)
    scrlbr10.config(command = treedat10.yview)
    treedat10["columns"] = ("Doctor ID", "Name", "Specialization", "DOJ", "Contact", "Salary")
    treedat10.column("#0", width = 0, minwidth = 0, stretch=0)
    treedat10.column("Doctor ID", anchor="center", width = 120)
    treedat10.column("Name", anchor = "center", width = 120)
    treedat10.column("Specialization", anchor = "center", width = 120)
    treedat10.column("DOJ", anchor = "center", width = 120)
    treedat10.column("Contact", anchor = "center", width = 120)
    treedat10.column("Salary", anchor = "center", width = 120)

    treedat10.heading("#0", text="", anchor="center")
    treedat10.heading("Doctor ID", text="Doctor ID", anchor="center")
    treedat10.heading("Name", text="Name", anchor="center")
    treedat10.heading("Specialization", text="Specialization", anchor="center")
    treedat10.heading("DOJ", text="DOJ", anchor="center")
    treedat10.heading("Contact", text="Contact", anchor="center")
    treedat10.heading("Salary", text="Salary", anchor="center")

    treedat11 = ttk.Treeview(master=scrlbrfrm11, yscrollcommand=scrlbr11.set)
    scrlbr11.config(command = treedat11.yview)
    treedat11["columns"] = ("Nurse ID", "Name", "Department", "DOJ", "Contact", "Salary")
    treedat11.column("#0", width = 0, minwidth = 0, stretch=0)
    treedat11.column("Nurse ID", anchor="center", width = 120)
    treedat11.column("Name", anchor = "center", width = 120)
    treedat11.column("Department", anchor = "center", width = 120)
    treedat11.column("DOJ", anchor = "center", width = 120)
    treedat11.column("Contact", anchor = "center", width = 120)
    treedat11.column("Salary", anchor = "center", width = 120)

    treedat11.heading("#0", text="", anchor="center")
    treedat11.heading("Nurse ID", text="Nurse ID", anchor="center")
    treedat11.heading("Name", text="Name", anchor="center")
    treedat11.heading("Department", text="Department", anchor="center")
    treedat11.heading("DOJ", text="DOJ", anchor="center")
    treedat11.heading("Contact", text="Contact", anchor="center")
    treedat11.heading("Salary", text="Salary", anchor="center")

    treedat12 = ttk.Treeview(master=scrlbrfrm12, yscrollcommand=scrlbr12.set)
    scrlbr12.config(command = treedat12.yview)
    treedat12["columns"] = ("Employee ID", "Name", "Job", "DOJ", "Contact", "Salary")
    treedat12.column("#0", width = 0, minwidth = 0, stretch=0)
    treedat12.column("Employee ID", anchor="center", width = 120)
    treedat12.column("Name", anchor = "center", width = 120)
    treedat12.column("Job", anchor = "center", width = 120)
    treedat12.column("DOJ", anchor = "center", width = 120)
    treedat12.column("Contact", anchor = "center", width = 120)
    treedat12.column("Salary", anchor = "center", width = 120)

    treedat12.heading("#0", text="", anchor="center")
    treedat12.heading("Employee ID", text="Employee ID", anchor="center")
    treedat12.heading("Name", text="Name", anchor="center")
    treedat12.heading("Job", text="Job", anchor="center")
    treedat12.heading("DOJ", text="DOJ", anchor="center")
    treedat12.heading("Contact", text="Contact", anchor="center")
    treedat12.heading("Salary", text="Salary", anchor="center")

    treedat13 = ttk.Treeview(master=scrlbrfrm13, yscrollcommand=scrlbr13.set)
    scrlbr13.config(command = treedat13.yview)
    treedat13["columns"] = ("Patient ID", "Name", "Age", "Ailment", "Payment type", "Payment status", "Contact", "Amount")
    treedat13.column("#0", width = 0, minwidth = 0, stretch=0)
    treedat13.column("Patient ID", anchor="center", width = 120)
    treedat13.column("Name", anchor = "center", width = 120)
    treedat13.column("Age", anchor = "center", width = 120)
    treedat13.column("Ailment", anchor = "center", width = 120)
    treedat13.column("Payment type", anchor = "center", width = 120)
    treedat13.column("Payment status", anchor = "center", width = 120)
    treedat13.column("Contact", anchor = "center", width = 120)
    treedat13.column("Amount", anchor = "center", width = 120)

    treedat13.heading("#0", text="", anchor="center")
    treedat13.heading("Patient ID", text="Patient ID", anchor="center")
    treedat13.heading("Name", text="Name", anchor="center")
    treedat13.heading("Age", text="Age", anchor="center")
    treedat13.heading("Ailment", text="Ailment", anchor="center")
    treedat13.heading("Payment type", text="Payment type", anchor="center")
    treedat13.heading("Payment status", text="Payment status", anchor="center")
    treedat13.heading("Contact", text="Contact", anchor="center")
    treedat13.heading("Amount", text="Amount", anchor="center")

    treedat14 = ttk.Treeview(master=scrlbrfrm14, yscrollcommand=scrlbr14.set)
    scrlbr14.config(command = treedat14.yview)
    treedat14["columns"] = ("Doctor ID", "Name", "Specialization", "DOJ", "Contact", "Salary")
    treedat14.column("#0", width = 0, minwidth = 0, stretch=0)
    treedat14.column("Doctor ID", anchor="center", width = 120)
    treedat14.column("Name", anchor = "center", width = 120)
    treedat14.column("Specialization", anchor = "center", width = 120)
    treedat14.column("DOJ", anchor = "center", width = 120)
    treedat14.column("Contact", anchor = "center", width = 120)
    treedat14.column("Salary", anchor = "center", width = 120)

    treedat14.heading("#0", text="", anchor="center")
    treedat14.heading("Doctor ID", text="Doctor ID", anchor="center")
    treedat14.heading("Name", text="Name", anchor="center")
    treedat14.heading("Specialization", text="Specialization", anchor="center")
    treedat14.heading("DOJ", text="DOJ", anchor="center")
    treedat14.heading("Contact", text="Contact", anchor="center")
    treedat14.heading("Salary", text="Salary", anchor="center")

    treedat15 = ttk.Treeview(master=scrlbrfrm15, yscrollcommand=scrlbr15.set)
    scrlbr15.config(command = treedat15.yview)
    treedat15["columns"] = ("Nurse ID", "Name", "Department", "DOJ", "Contact", "Salary")
    treedat15.column("#0", width = 0, minwidth = 0, stretch=0)
    treedat15.column("Nurse ID", anchor="center", width = 120)
    treedat15.column("Name", anchor = "center", width = 120)
    treedat15.column("Department", anchor = "center", width = 120)
    treedat15.column("DOJ", anchor = "center", width = 120)
    treedat15.column("Contact", anchor = "center", width = 120)
    treedat15.column("Salary", anchor = "center", width = 120)

    treedat15.heading("#0", text="", anchor="center")
    treedat15.heading("Nurse ID", text="Nurse ID", anchor="center")
    treedat15.heading("Name", text="Name", anchor="center")
    treedat15.heading("Department", text="Department", anchor="center")
    treedat15.heading("DOJ", text="DOJ", anchor="center")
    treedat15.heading("Contact", text="Contact", anchor="center")
    treedat15.heading("Salary", text="Salary", anchor="center")

    treedat16 = ttk.Treeview(master=scrlbrfrm16, yscrollcommand=scrlbr16.set)
    scrlbr16.config(command = treedat16.yview)
    treedat16["columns"] = ("Employee ID", "Name", "Job", "DOJ", "Contact", "Salary")
    treedat16.column("#0", width = 0, minwidth = 0, stretch=0)
    treedat16.column("Employee ID", anchor="center", width = 120)
    treedat16.column("Name", anchor = "center", width = 120)
    treedat16.column("Job", anchor = "center", width = 120)
    treedat16.column("DOJ", anchor = "center", width = 120)
    treedat16.column("Contact", anchor = "center", width = 120)
    treedat16.column("Salary", anchor = "center", width = 120)

    treedat16.heading("#0", text="", anchor="center")
    treedat16.heading("Employee ID", text="Employee ID", anchor="center")
    treedat16.heading("Name", text="Name", anchor="center")
    treedat16.heading("Job", text="Job", anchor="center")
    treedat16.heading("DOJ", text="DOJ", anchor="center")
    treedat16.heading("Contact", text="Contact", anchor="center")
    treedat16.heading("Salary", text="Salary", anchor="center")

    #query for loading data
    def loadpatient():
        recordP = sqlqueries.query("patient")
        for patient in recordP:
            treedat1.insert(parent="", index=tk.END, text = "", values = (patient[0], patient[1], patient[2], patient[3], patient[4], patient[5], patient[6], patient[7]))
            treedat5.insert(parent="", index=tk.END, text = "", values = (patient[0], patient[1], patient[2], patient[3], patient[4], patient[5], patient[6], patient[7]))
            treedat9.insert(parent="", index=tk.END, text = "", values = (patient[0], patient[1], patient[2], patient[3], patient[4], patient[5], patient[6], patient[7]))
            treedat13.insert(parent="", index=tk.END, text = "", values = (patient[0], patient[1], patient[2], patient[3], patient[4], patient[5], patient[6], patient[7]))

    def loaddoctor():
        recordP = sqlqueries.query("doctor")
        for doctor in recordP:
            treedat2.insert(parent="", index=tk.END, text = "", values = (doctor[0], doctor[1], doctor[2], doctor[3], doctor[4], doctor[5]))
            treedat6.insert(parent="", index=tk.END, text = "", values = (doctor[0], doctor[1], doctor[2], doctor[3], doctor[4], doctor[5]))
            treedat10.insert(parent="", index=tk.END, text = "", values = (doctor[0], doctor[1], doctor[2], doctor[3], doctor[4], doctor[5]))
            treedat14.insert(parent="", index=tk.END, text = "", values = (doctor[0], doctor[1], doctor[2], doctor[3], doctor[4], doctor[5]))
        
    def loadnurse():
        recordP = sqlqueries.query("nurse")
        for nurse in recordP:
            treedat3.insert(parent="", index=tk.END, text = "", values = (nurse[0], nurse[1], nurse[2], nurse[3], nurse[4], nurse[5]))
            treedat7.insert(parent="", index=tk.END, text = "", values = (nurse[0], nurse[1], nurse[2], nurse[3], nurse[4], nurse[5]))
            treedat11.insert(parent="", index=tk.END, text = "", values = (nurse[0], nurse[1], nurse[2], nurse[3], nurse[4], nurse[5]))
            treedat15.insert(parent="", index=tk.END, text = "", values = (nurse[0], nurse[1], nurse[2], nurse[3], nurse[4], nurse[5]))

    def loademployee():
        recordP = sqlqueries.query("employee")
        for employee in recordP:
            treedat4.insert(parent="", index=tk.END, text = "", values = (employee[0], employee[1], employee[2], employee[3], employee[4], employee[5]))
            treedat8.insert(parent="", index=tk.END, text = "", values = (employee[0], employee[1], employee[2], employee[3], employee[4], employee[5]))
            treedat12.insert(parent="", index=tk.END, text = "", values = (employee[0], employee[1], employee[2], employee[3], employee[4], employee[5]))
            treedat16.insert(parent="", index=tk.END, text = "", values = (employee[0], employee[1], employee[2], employee[3], employee[4], employee[5]))

    loadpatient()
    loaddoctor()
    loadnurse()
    loademployee()

    #query commit for patient data
    def patcomm(PID_val, Name_val, age_val, ailment_val, payment, status, contactdet, amt_val):
        sqlqueries.addtopatient(PID_val, Name_val, age_val, ailment_val, payment, status, contactdet, amt_val)
        treedat1.delete(*treedat1.get_children())
        treedat5.delete(*treedat5.get_children())
        treedat9.delete(*treedat9.get_children())
        treedat13.delete(*treedat13.get_children())
        loadpatient()

    #query commit for doctor data
    def doccomm(DID_val, Name_Doc_val, spec_val, DOJ_val_doc, contactdet, sal_val):
        sqlqueries.addtodoctor(DID_val, Name_Doc_val, spec_val, DOJ_val_doc, contactdet, sal_val)
        treedat2.delete(*treedat2.get_children())
        treedat6.delete(*treedat6.get_children())
        treedat10.delete(*treedat10.get_children())
        treedat14.delete(*treedat14.get_children())
        loaddoctor()
    
    #query commit for nurse data
    def nurcomm(NID_val, Name_Nur_val, dept_val, DOJ_val_nur, contactdet, sal_val):
        sqlqueries.addtonurse(NID_val, Name_Nur_val, dept_val, DOJ_val_nur, contactdet, sal_val)
        treedat3.delete(*treedat3.get_children())
        treedat7.delete(*treedat7.get_children())
        treedat11.delete(*treedat11.get_children())
        treedat15.delete(*treedat15.get_children())
        loadnurse()
    
    #query commit for employee data
    def empcomm(EID_val, Name_emp_val, job_val, DOJ_val_emp, contactdet, sal_val):
        sqlqueries.addtoemployee(EID_val, Name_emp_val, job_val, DOJ_val_emp, contactdet, sal_val)
        treedat4.delete(*treedat4.get_children())
        treedat8.delete(*treedat8.get_children())
        treedat12.delete(*treedat12.get_children())
        treedat16.delete(*treedat16.get_children())
        loademployee()

    #code fragment for adding data to SQL and to Treeview (Patient table)
    paymentval = tk.IntVar()
    statusval = tk.IntVar()
    age_val = tk.IntVar()
    ent_PID = ttk.Entry(master=intfrm5, width = 30)
    lbl_PID = ttk.Label(master=intfrm5, text = "Patient ID: ")
    ent_Name = ttk.Entry(master=intfrm5, width = 30)
    lbl_Name = ttk.Label(master=intfrm5, text = "Name: ")
    ent_ailment = ttk.Entry(master=intfrm5, width = 30)
    lbl_ailment = ttk.Label(master=intfrm5, text = "Ailments: ")
    ent_amt = ttk.Entry(master=intfrm5, width = 30)
    lbl_amt = ttk.Label(master=intfrm5, text = "Amount: ")
    lbl_payment = ttk.Label(master=intfrm5, text = "Payment Type:")
    rdb_cash = ttk.Radiobutton(master=intfrm5, text="Cash", value=1, variable=paymentval)
    rdb_card = ttk.Radiobutton(master=intfrm5, text="Card", value=2, variable=paymentval)
    rdb_cheque = ttk.Radiobutton(master=intfrm5, text="Cheque", value=3, variable=paymentval)
    lbl_status = ttk.Label(master=intfrm5, text = "Payment Status: ")
    rdb_paid = ttk.Radiobutton(master=intfrm5, text="Paid", value=1, variable=statusval)
    rdb_pending = ttk.Radiobutton(master=intfrm5, text="Pending", value=2, variable=statusval)
    age_cbbx = ttk.Combobox(master=intfrm5, textvariable=age_val, width=5)
    agelis = [int(i) for i in range(1,120)]
    age_cbbx["values"] = tuple(agelis)
    age_cbbx.state(["readonly"])
    lbl_age = ttk.Label(master=intfrm5, text="Age: ")
    ent_contact = ttk.Entry(master=intfrm5, width=30)
    lbl_contact = ttk.Label(master=intfrm5, text="Contact: ")

    #separators and beautification
    sep_pay_stat = ttk.Separator(master=intfrm5, orient=tk.HORIZONTAL)
    sep_pay_stat1 = ttk.Separator(master=intfrm5, orient=tk.HORIZONTAL)

    def addrecpat():
        try:
            PID_val = int(ent_PID.get())
            amt_val = float(ent_amt.get())
            age = int(age_val.get())
            contact = int(ent_contact.get())
            Name_val = ent_Name.get()
            ailment_val = ent_ailment.get()
            if paymentval.get() == 1:
                payment = "Cash"
            elif paymentval.get() == 2:
                payment = "Card"
            elif paymentval.get() == 3:
                payment = "Cheque"
            else:
                pass
            
            if statusval.get() == 1:
                status = "Paid"
            elif statusval.get() == 2:
                status = "Pending"
            else:
                pass
            patcomm(PID_val, Name_val, age, ailment_val, payment, status, contact, amt_val)
            messagebox.showinfo("Add", message="Added Successfully")
            ent_PID.delete(0, tk.END)
            ent_Name.delete(0, tk.END)
            ent_ailment.delete(0, tk.END)
            ent_contact.delete(0, tk.END)
            ent_amt.delete(0, tk.END)
        except ValueError:
            messagebox.showinfo("Status", "Incorrect Datatypes entered. Please check the data entered and ensure they are of the correct datatype")
        
    addbtnpat = ttk.Button(master=intfrm5, text = "Add Data", command = addrecpat)

    #code fragment for adding data to SQL and to Treeview (Doctors)
    datevar_doc = tk.StringVar()
    monthvar_doc = tk.StringVar()
    yearvar_doc = tk.StringVar()
    ent_DID = ttk.Entry(master=intfrm6, width = 30)
    lbl_DID = ttk.Label(master=intfrm6, text = "Doctor ID: ")
    ent_Name_doc = ttk.Entry(master=intfrm6, width = 30)
    lbl_Name_doc = ttk.Label(master=intfrm6, text = "Name: ")
    ent_spec = ttk.Entry(master=intfrm6, width = 30)
    lbl_spec = ttk.Label(master=intfrm6, text = "Specialization: ")
    lbl_DOJ = ttk.Label(master=intfrm6, text = "Date Of Joining: ")

    #small frame for DOJ
    dojfrm_doc = ttk.Frame(master=intfrm6)

    date_cbbx1 = ttk.Combobox(master=dojfrm_doc, textvariable = datevar_doc, width = 3)
    date_cbbx1["values"] = ("01", "02", "03", "04", "05", "06", "07", "08", "09", 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31)
    date_cbbx1.state(["readonly"])
    month_cbbx1 = ttk.Combobox(master=dojfrm_doc, textvariable = monthvar_doc, width = 9)
    month_cbbx1["values"] = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")
    month_cbbx1.state(["readonly"])
    ylist = []
    for i in range(1950, 2022):
        ylist.append(i)
    year_cbbx1 = ttk.Combobox(master=dojfrm_doc, textvariable = yearvar_doc, width = 5)
    year_cbbx1["values"] = tuple(ylist)
    year_cbbx1.state(["readonly"])
    ent_contact_doc = ttk.Entry(master=intfrm6, width = 30)
    lbl_contact_doc = ttk.Label(master=intfrm6, text="Contact: ")
    ent_sal = ttk.Entry(master=intfrm6, width = 30)
    lbl_sal = ttk.Label(master=intfrm6, text = "Salary:")

    def addrecdoc():
        try:
            DID_val = int(ent_DID.get())
            contact_doc = int(ent_contact_doc.get())
            sal_val = float(ent_sal.get())
            months = {"January":1, "February":2, "March":3, "April":4, "May":5, "June":6, "July":7, "August":8, "September":9, "October":10, "November":11, "December":12}
            DOJ_val_doc = datetime.date(int(yearvar_doc.get()),int(months[monthvar_doc.get()]), int(datevar_doc.get()))
            Name_Doc_val = ent_Name_doc.get()
            spec_val = ent_spec.get()
            doccomm(DID_val, Name_Doc_val, spec_val, DOJ_val_doc, contact_doc, sal_val)
            messagebox.showinfo("Add", message="Added Successfully")
            ent_DID.delete(0, tk.END)
            ent_Name_doc.delete(0, tk.END)
            ent_spec.delete(0, tk.END)
            ent_contact_doc.delete(0, tk.END)
            ent_sal.delete(0, tk.END)
        except ValueError:
            messagebox.showinfo("Status", "Incorrect Datatypes entered. Please check the data entered and ensure they are of the correct datatype")

    addbtndoc = ttk.Button(master=intfrm6, text = "Add Data", command = addrecdoc)

    #code fragment for adding data to SQL and to Treeview (Nurses)
    datevar_nur = tk.StringVar()
    monthvar_nur = tk.StringVar()
    yearvar_nur = tk.StringVar()
    ent_NID = ttk.Entry(master=intfrm7, width = 30)
    lbl_NID = ttk.Label(master=intfrm7, text = "Nurse ID: ")
    ent_Name_nur = ttk.Entry(master=intfrm7, width = 30)
    lbl_Name_nur = ttk.Label(master=intfrm7, text = "Name: ")
    ent_dept = ttk.Entry(master=intfrm7, width = 30)
    lbl_dept = ttk.Label(master=intfrm7, text = "Department: ")
    lbl_DOJ_nur = ttk.Label(master=intfrm7, text = "Date Of Joining: ")

    #small frame for DOJ
    dojfrm_nur = ttk.Frame(master=intfrm7)

    date_cbbx2 = ttk.Combobox(master=dojfrm_nur, textvariable = datevar_nur, width = 3)
    date_cbbx2["values"] = ("01", "02", "03", "04", "05", "06", "07", "08", "09", 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31)
    date_cbbx2.state(["readonly"])
    month_cbbx2 = ttk.Combobox(master=dojfrm_nur, textvariable = monthvar_nur, width = 9)
    month_cbbx2["values"] = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")
    month_cbbx2.state(["readonly"])
    ylist = []
    for i in range(1950, 2022):
        ylist.append(i)
    year_cbbx2 = ttk.Combobox(master=dojfrm_nur, textvariable = yearvar_nur, width = 5)
    year_cbbx2["values"] = tuple(ylist)
    year_cbbx2.state(["readonly"])
    ent_sal_nur = ttk.Entry(master=intfrm7, width = 30)
    ent_contact_nur = ttk.Entry(master=intfrm7, width=30)
    lbl_sal_nur = ttk.Label(master=intfrm7, text = "Salary:")
    lbl_contact_nur = ttk.Label(master=intfrm7, text="Contact:")

    def addrecnur():
        try:
            NID_val = int(ent_NID.get())
            sal_val = float(ent_sal_nur.get())
            contact_nur = int(ent_contact_nur.get())
            months = {"January":1, "February":2, "March":3, "April":4, "May":5, "June":6, "July":7, "August":8, "September":9, "October":10, "November":11, "December":12}
            DOJ_val_nur = datetime.date(int(yearvar_nur.get()),int(months[monthvar_nur.get()]), int(datevar_nur.get()))
            Name_Nur_val = ent_Name_nur.get()
            dept_val = ent_dept.get()
            nurcomm(NID_val, Name_Nur_val, dept_val, DOJ_val_nur, contact_nur, sal_val)
            messagebox.showinfo("Add", message="Added Successfully")
            ent_NID.delete(0, tk.END)
            ent_Name_nur.delete(0, tk.END)
            ent_dept.delete(0, tk.END)
            ent_contact_nur.delete(0, tk.END)
            ent_sal_nur.delete(0, tk.END)
        except ValueError:
            messagebox.showinfo("Status", "Incorrect Datatypes entered. Please check the data entered and ensure they are of the correct datatype")

    addbtnnur = ttk.Button(master=intfrm7, text = "Add Data", command = addrecnur)

    #code fragment for adding data to SQL and to Treeview (Employees)
    datevar_emp = tk.StringVar()
    monthvar_emp = tk.StringVar()
    yearvar_emp = tk.StringVar()
    ent_EID = ttk.Entry(master=intfrm8, width = 30)
    lbl_EID = ttk.Label(master=intfrm8, text = "Employee ID: ")
    ent_Name_emp = ttk.Entry(master=intfrm8, width = 30)
    lbl_Name_emp = ttk.Label(master=intfrm8, text = "Name: ")
    ent_job = ttk.Entry(master=intfrm8, width = 30)
    lbl_job = ttk.Label(master=intfrm8, text = "Job: ")
    lbl_DOJ_emp = ttk.Label(master=intfrm8, text = "Date Of Joining: ")

    #small frame for DOJ
    dojfrm_emp = ttk.Frame(master=intfrm8)

    date_cbbx3 = ttk.Combobox(master=dojfrm_emp, textvariable = datevar_emp, width = 3)
    date_cbbx3["values"] = ("01", "02", "03", "04", "05", "06", "07", "08", "09", 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31)
    date_cbbx3.state(["readonly"])
    month_cbbx3 = ttk.Combobox(master=dojfrm_emp, textvariable = monthvar_emp, width = 9)
    month_cbbx3["values"] = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")
    month_cbbx3.state(["readonly"])
    ylist = []
    for i in range(1950, 2022):
        ylist.append(i)
    year_cbbx3 = ttk.Combobox(master=dojfrm_emp, textvariable = yearvar_emp, width = 5)
    year_cbbx3["values"] = tuple(ylist)
    year_cbbx3.state(["readonly"])
    ent_contact_emp = ttk.Entry(master=intfrm8, width = 30)
    lbl_contact_emp = ttk.Label(master=intfrm8, text = "Contact:")
    ent_sal_emp = ttk.Entry(master=intfrm8, width = 30)
    lbl_sal_emp = ttk.Label(master=intfrm8, text = "Salary:")

    def addrecemp():
        try:
            EID_val = int(ent_EID.get())
            Name_emp_val = ent_Name_emp.get()
            job_val = ent_job.get()
            sal_val = float(ent_sal_emp.get())
            contact_emp = int(ent_contact_emp.get())
            months = {"January":1, "February":2, "March":3, "April":4, "May":5, "June":6, "July":7, "August":8, "September":9, "October":10, "November":11, "December":12}
            DOJ_val_emp = datetime.date(int(yearvar_emp.get()),int(months[monthvar_emp.get()]), int(datevar_emp.get()))
            empcomm(EID_val, Name_emp_val, job_val, DOJ_val_emp, contact_emp, sal_val)
            messagebox.showinfo("Add", message="Added Successfully")
            ent_EID.delete(0, tk.END)
            ent_Name_emp.delete(0, tk.END)
            ent_job.delete(0, tk.END)
            ent_contact_emp.delete(0, tk.END)
            ent_sal_emp.delete(0, tk.END)
        except ValueError:
            messagebox.showinfo("Status", "Incorrect Datatypes entered. Please check the data entered and ensure they are of the correct datatype")

    addbtnemp = ttk.Button(master=intfrm8, text = "Add Data", command = addrecemp)

    #Deleting a record (Patient)
    def deleteallp():
        x = messagebox.askyesno("Warning", "Are you sure you want to delete all patient records? \n This action is IRREVERSIBLE.")
        if x == True:    
            treedat5.delete(*treedat5.get_children())
            treedat9.delete(*treedat9.get_children())
            treedat13.delete(*treedat13.get_children())
            treedat1.delete(*treedat1.get_children())
            sqlqueries.purgeP()
        else:
            pass
    def deleteselectedp():
        x = messagebox.askyesno("Warning", "Are you sure you want to delete the selected patient records? \n This action is IRREVERSIBLE.")
        if x == True:    
            templist = []
            selectedrec = treedat5.selection()
            for patient in selectedrec:
                valuegrabber = treedat5.item(patient, "values")
                templist.append(valuegrabber[0])
            sqlqueries.delemany("patient", "Patient_Id", templist)
            treedat5.delete(*treedat5.get_children())
            treedat9.delete(*treedat9.get_children())
            treedat13.delete(*treedat13.get_children())
            treedat1.delete(*treedat1.get_children())
            loadpatient()
        else:
            pass
    
    frm_delp = ttk.Frame(master=intfrm9)
    btn_delall = ttk.Button(master=frm_delp, text="Delete All", command=deleteallp)
    btn_delsel = ttk.Button(master=frm_delp, text="Delete Selected", command=deleteselectedp)

    #Deleting a record (Doctor)
    def deletealld():
        x = messagebox.askyesno("Warning", "Are you sure you want to delete all patient records? \n This action is IRREVERSIBLE.")
        if x == True:    
            treedat6.delete(*treedat6.get_children())
            treedat10.delete(*treedat10.get_children())
            treedat14.delete(*treedat14.get_children())
            treedat2.delete(*treedat2.get_children())
            sqlqueries.purgeD()
        else:
            pass
    def deleteselectedd():
        x = messagebox.askyesno("Warning", "Are you sure you want to delete the selected patient records? \n This action is IRREVERSIBLE.")
        if x == True:    
            templist = []
            selectedrec = treedat6.selection()
            for doctor in selectedrec:
                valuegrabber = treedat6.item(doctor, "values")
                templist.append(valuegrabber[0])
            sqlqueries.delemany("doctor", "Doctor_Id", templist)
            treedat6.delete(*treedat6.get_children())
            treedat10.delete(*treedat10.get_children())
            treedat14.delete(*treedat14.get_children())
            treedat2.delete(*treedat2.get_children())
            loaddoctor()
        else:
            pass
    
    frm_deld = ttk.Frame(master=intfrm10)
    btn_delalld = ttk.Button(master=frm_deld, text="Delete All", command=deletealld)
    btn_delseld = ttk.Button(master=frm_deld, text="Delete Selected", command=deleteselectedd)

    #Deleting a record (Nurse)
    def deletealln():
        x = messagebox.askyesno("Warning", "Are you sure you want to delete all patient records? \n This action is IRREVERSIBLE.")
        if x == True:    
            treedat7.delete(*treedat7.get_children())
            treedat11.delete(*treedat11.get_children())
            treedat15.delete(*treedat15.get_children())
            treedat3.delete(*treedat3.get_children())
            sqlqueries.purgeN()
        else:
            pass
    def deleteselectedn():
        x = messagebox.askyesno("Warning", "Are you sure you want to delete the selected patient records? \n This action is IRREVERSIBLE.")
        if x == True:    
            templist = []
            selectedrec = treedat7.selection()
            for nurse in selectedrec:
                valuegrabber = treedat7.item(nurse, "values")
                templist.append(valuegrabber[0])
            sqlqueries.delemany("nurse", "Nurse_Id", templist)
            treedat7.delete(*treedat7.get_children())
            treedat11.delete(*treedat11.get_children())
            treedat15.delete(*treedat15.get_children())
            treedat3.delete(*treedat3.get_children())
            loadnurse()
        else:
            pass
    
    frm_deln = ttk.Frame(master=intfrm11)
    btn_delalln = ttk.Button(master=frm_deln, text="Delete All", command=deletealln)
    btn_delseln = ttk.Button(master=frm_deln, text="Delete Selected", command=deleteselectedn)

    #Deleting a record (Employee)
    def deletealle():
        x = messagebox.askyesno("Warning", "Are you sure you want to delete all patient records? \n This action is IRREVERSIBLE.")
        if x == True:    
            treedat8.delete(*treedat8.get_children())
            treedat12.delete(*treedat12.get_children())
            treedat16.delete(*treedat16.get_children())
            treedat4.delete(*treedat4.get_children())
            sqlqueries.purgeE()
        else:
            pass
    def deleteselectede():
        x = messagebox.askyesno("Warning", "Are you sure you want to delete the selected patient records? \n This action is IRREVERSIBLE.")
        if x == True:    
            templist = []
            selectedrec = treedat8.selection()
            for employee in selectedrec:
                valuegrabber = treedat8.item(employee, "values")
                templist.append(valuegrabber[0])
            sqlqueries.delemany("employee", "Employee_Id", templist)
            treedat8.delete(*treedat8.get_children())
            treedat12.delete(*treedat12.get_children())
            treedat16.delete(*treedat16.get_children())
            treedat4.delete(*treedat4.get_children())
            loademployee()
        else:
            pass
    
    frm_dele = ttk.Frame(master=intfrm12)
    btn_delalle = ttk.Button(master=frm_dele, text="Delete All", command=deletealle)
    btn_delsele = ttk.Button(master=frm_dele, text="Delete Selected", command=deleteselectede)

    #query commit for patient data update
    def patcommU(PID_val, Name_val, age_val, ailment_val, payment, status, contactdet, amt_val):
        sqlqueries.uppatient(PID_val, Name_val, age_val, ailment_val, payment, status, contactdet, amt_val)
        treedat1.delete(*treedat1.get_children())
        treedat5.delete(*treedat5.get_children())
        treedat9.delete(*treedat9.get_children())
        treedat13.delete(*treedat13.get_children())
        loadpatient()

    #query commit for doctor data update
    def doccommU(DID_val, Name_Doc_val, spec_val, DOJ_val_doc, contactdet, sal_val):
        sqlqueries.updoctor(DID_val, Name_Doc_val, spec_val, DOJ_val_doc, contactdet, sal_val)
        treedat2.delete(*treedat2.get_children())
        treedat6.delete(*treedat6.get_children())
        treedat10.delete(*treedat10.get_children())
        treedat14.delete(*treedat14.get_children())
        loaddoctor()
    
    #query commit for nurse data update
    def nurcommU(NID_val, Name_Nur_val, dept_val, DOJ_val_nur, contactdet, sal_val):
        sqlqueries.upnurse(NID_val, Name_Nur_val, dept_val, DOJ_val_nur, contactdet, sal_val)
        treedat3.delete(*treedat3.get_children())
        treedat7.delete(*treedat7.get_children())
        treedat11.delete(*treedat11.get_children())
        treedat15.delete(*treedat15.get_children())
        loadnurse()
    
    #query commit for employee data update
    def empcommU(EID_val, Name_emp_val, job_val, DOJ_val_emp, contactdet, sal_val):
        sqlqueries.upemployee(EID_val, Name_emp_val, job_val, DOJ_val_emp, contactdet, sal_val)
        treedat4.delete(*treedat4.get_children())
        treedat8.delete(*treedat8.get_children())
        treedat12.delete(*treedat12.get_children())
        treedat16.delete(*treedat16.get_children())
        loademployee()


    #code fragment for updating data in SQL and in Treeview (Patient table)
    paymentvalU = tk.StringVar()
    statusvalU = tk.StringVar()
    age_valU = tk.IntVar()
    frm_updateP = ttk.Frame(master=intfrm13)
    #labelframes:
    lblfrm1 = ttk.LabelFrame(master=frm_updateP, padding=7)
    lblfrm2 = ttk.LabelFrame(master=frm_updateP, padding=45)
    ent_PIDU = ttk.Entry(master=lblfrm1, width = 30, state="disabled")
    lbl_PIDU = ttk.Label(master=lblfrm1, text = "Patient ID: ")
    ent_NameU = ttk.Entry(master=lblfrm1, width = 30)
    lbl_NameU = ttk.Label(master=lblfrm1, text = "Name: ")
    ent_ailmentU = ttk.Entry(master=lblfrm1, width = 30)
    lbl_ailmentU = ttk.Label(master=lblfrm1, text = "Ailments: ")
    ent_amtU = ttk.Entry(master=lblfrm1, width = 30)
    lbl_amtU = ttk.Label(master=lblfrm1, text = "Amount: ")
    lbl_paymentU = ttk.Label(master=lblfrm2, text = "Payment Type:")
    ptype_cbbx = ttk.Combobox(master=lblfrm2, textvariable=paymentvalU)
    ptypevals = ("Cash", "Card", "Cheque")
    ptype_cbbx["values"] = ptypevals
    ptype_cbbx.state(["readonly"])
    lbl_statusU = tk.Label(master=lblfrm2, text = "Payment Status: ")
    pstatus_cbbx = ttk.Combobox(master=lblfrm2, textvariable=statusvalU)
    pstatus_cbbx.state(["readonly"])
    pstatusvals = ("Paid", "Pending")
    pstatus_cbbx["values"] = pstatusvals
    age_cbbxU = ttk.Combobox(master=lblfrm1, textvariable=age_valU, width=5)
    agelisU = [int(i) for i in range(1,120)]
    age_cbbxU["values"] = tuple(agelisU)
    age_cbbxU.state(["readonly"])
    lbl_ageU = ttk.Label(master=lblfrm1, text="Age: ")
    ent_contactU = ttk.Entry(master=lblfrm1, width=30)
    lbl_contactU = ttk.Label(master=lblfrm1, text="Contact: ")

    def selp():
        ent_PIDU.config(state="normal")
        ent_PIDU.delete(0, tk.END)
        ent_NameU.delete(0, tk.END)
        ent_ailmentU.delete(0, tk.END)
        ent_contactU.delete(0, tk.END)
        ent_amtU.delete(0, tk.END)
        selectedP = treedat9.focus()
        valuesP = treedat9.item(selectedP, "values")
        ent_PIDU.insert(0, valuesP[0])
        ent_PIDU.config(state="disabled")
        ent_NameU.insert(0, valuesP[1])
        ent_ailmentU.insert(0, valuesP[3])
        ent_contactU.insert(0, valuesP[6])
        ent_amtU.insert(0, valuesP[7])
        ageindex = 0
        for i in range(0, len(agelisU)):
            if int(valuesP[2]) == agelisU[i]:
                ageindex = i
        age_cbbxU.current(ageindex)
        ptypeindex = 0
        for i in range(0, len(ptypevals)):
            if str(valuesP[4]) == ptypevals[i]:
                ptypeindex = i
        ptype_cbbx.current(ptypeindex)
        pstatusindex = 0
        for i in range(0, len(pstatusvals)):
            if str(valuesP[5]) == pstatusvals[i]:
                pstatusindex = i
        pstatus_cbbx.current(pstatusindex)

    sel_btn_P = ttk.Button(master=frm_updateP, command=selp, text="Select Highlighted Record")


    def updatepat():
        try:
            ent_PIDU.config(state="normal")
            PID_val = ent_PIDU.get()
            Name_val = ent_NameU.get()
            ailment_val = ent_ailmentU.get()
            amt_val = float(ent_amtU.get())
            age = age_valU.get()
            contact = int(ent_contactU.get())
            payment = paymentvalU.get()
            status = statusvalU.get()
            patcommU(PID_val, Name_val, age, ailment_val, payment, status, contact, amt_val)
            messagebox.showinfo("Update", message="Updated Successfully")
            ent_PIDU.delete(0, tk.END)
            ent_PIDU.config(state="disabled")
            ent_NameU.delete(0, tk.END)
            ent_ailmentU.delete(0, tk.END)
            ent_contactU.delete(0, tk.END)
            ent_amtU.delete(0, tk.END)
        except ValueError:
            messagebox.showinfo("Status", "Incorrect Datatypes entered. Please check the data entered and ensure they are of the correct datatype")

    updatebtnpat = ttk.Button(master=frm_updateP, text = "Update Data", command = updatepat)


    #code fragment for updating data in SQL and in Treeview (Doctor table)
    frm_updateD = ttk.Frame(master=intfrm14)
    lblfrm3 = ttk.LabelFrame(master=frm_updateD)
    datevar_docU = tk.StringVar()
    monthvar_docU = tk.StringVar()
    yearvar_docU = tk.StringVar()
    ent_DIDU = ttk.Entry(master=lblfrm3, width = 30, state="disabled")
    lbl_DIDU = ttk.Label(master=lblfrm3, text = "Doctor ID: ")
    ent_Name_docU = ttk.Entry(master=lblfrm3, width = 30)
    lbl_Name_docU = ttk.Label(master=lblfrm3, text = "Name: ")
    ent_specU = ttk.Entry(master=lblfrm3, width = 30)
    lbl_specU = ttk.Label(master=lblfrm3, text = "Specialization: ")
    lbl_DOJU = ttk.Label(master=lblfrm3, text = "Date Of Joining: ")

    #small frame for DOJ
    dojfrm_docU = ttk.Frame(master=lblfrm3)

    date_cbbx1U = ttk.Combobox(master=dojfrm_docU, textvariable = datevar_docU, width = 3)
    datevals1 = ("01", "02", "03", "04", "05", "06", "07", "08", "09", 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31)
    date_cbbx1U["values"] = datevals1
    date_cbbx1U.state(["readonly"])
    month_cbbx1U = ttk.Combobox(master=dojfrm_docU, textvariable = monthvar_docU, width = 9)
    monthvals1 = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")
    month_cbbx1U["values"] = monthvals1
    month_cbbx1U.state(["readonly"])
    ylistU = []
    for i in range(1950, 2022):
        ylistU.append(i)
    year_cbbx1U = ttk.Combobox(master=dojfrm_docU, textvariable = yearvar_docU, width = 5)
    year_cbbx1U["values"] = tuple(ylistU)
    year_cbbx1U.state(["readonly"])
    ent_contact_docU = ttk.Entry(master=lblfrm3, width = 30)
    lbl_contact_docU = ttk.Label(master=lblfrm3, text="Contact: ")
    ent_salU = ttk.Entry(master=lblfrm3, width = 30)
    lbl_salU = ttk.Label(master=lblfrm3, text = "Salary:")

    btn_frm_updoc = ttk.Frame(master=frm_updateD)

    def seld():
        ent_DIDU.config(state="normal")
        ent_DIDU.delete(0, tk.END)
        ent_Name_docU.delete(0, tk.END)
        ent_specU.delete(0, tk.END)
        ent_contact_docU.delete(0, tk.END)
        ent_salU.delete(0, tk.END)
        selectedD = treedat10.focus()
        valuesD = treedat10.item(selectedD, "values")
        ent_DIDU.insert(0, valuesD[0])
        ent_DIDU.config(state="disabled")
        ent_Name_docU.insert(0, valuesD[1])
        ent_specU.insert(0, valuesD[2])
        ent_contact_docU.insert(0, valuesD[4])
        ent_salU.insert(0, valuesD[5])
        dateindex = 0
        for i in range(0, len(datevals1)):
            if int(str(valuesD[3])[9:]) == int(datevals1[i]):
                dateindex = i
        date_cbbx1U.current(dateindex)
        months = {"January":1, "February":2, "March":3, "April":4, "May":5, "June":6, "July":7, "August":8, "September":9, "October":10, "November":11, "December":12}
        monthindex = 0
        for i in range(0, len(monthvals1)):
            if int(str(valuesD[3])[5:7]) == months.get(monthvals1[i]):
                monthindex=i
        month_cbbx1U.current(monthindex)
        yearindex = 0
        for i in range(0, len(ylistU)):
            if int(str(valuesD[3])[:4]) == ylistU[i]:
                yearindex = i
        year_cbbx1U.current(yearindex)

    sel_btn_D = ttk.Button(master=btn_frm_updoc, command=seld, text="Select Highlighted Record")


    def updatedoc():
        try:
            ent_DIDU.config(state="normal")
            DID_val = ent_DIDU.get()
            Name_val = ent_Name_docU.get()
            spec_val = ent_specU.get()
            sal_val = float(ent_salU.get())
            contact = int(ent_contact_docU.get())
            months = {"January":1, "February":2, "March":3, "April":4, "May":5, "June":6, "July":7, "August":8, "September":9, "October":10, "November":11, "December":12}
            DOJ_val_doc = datetime.date(int(yearvar_docU.get()),int(months[monthvar_docU.get()]), int(datevar_docU.get()))
            doccommU(DID_val, Name_val, spec_val, DOJ_val_doc, contact, sal_val)
            messagebox.showinfo("Update", message="Updated Successfully")
            ent_DIDU.delete(0, tk.END)
            ent_DIDU.config(state="disabled")
            ent_Name_docU.delete(0, tk.END)
            ent_specU.delete(0, tk.END)
            ent_contact_docU.delete(0, tk.END)
            ent_salU.delete(0, tk.END)
        except ValueError:
            messagebox.showinfo("Status", "Incorrect Datatypes entered. Please check the data entered and ensure they are of the correct datatype")

    updatebtndoc = ttk.Button(master=btn_frm_updoc, text = "Update Data", command = updatedoc)

    #code fragment for updating data in SQL and in Treeview (Nurse table)
    frm_updateN = ttk.Frame(master=intfrm15)
    lblfrm4 = ttk.LabelFrame(master=frm_updateN)
    datevar_nurU = tk.StringVar()
    monthvar_nurU = tk.StringVar()
    yearvar_nurU = tk.StringVar()
    ent_NIDU = ttk.Entry(master=lblfrm4, width = 30, state="disabled")
    lbl_NIDU = ttk.Label(master=lblfrm4, text = "Nurse ID: ")
    ent_Name_nurU = ttk.Entry(master=lblfrm4, width = 30)
    lbl_Name_nurU = ttk.Label(master=lblfrm4, text = "Name: ")
    ent_deptU = ttk.Entry(master=lblfrm4, width = 30)
    lbl_deptU = ttk.Label(master=lblfrm4, text = "Department: ")
    lbl_DOJ_nurU = ttk.Label(master=lblfrm4, text = "Date Of Joining: ")

    #small frame for DOJ
    dojfrm_nurU = ttk.Frame(master=lblfrm4)

    date_cbbx2U = ttk.Combobox(master=dojfrm_nurU, textvariable = datevar_nurU, width = 3)
    datevals2 = ("01", "02", "03", "04", "05", "06", "07", "08", "09", 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31)
    date_cbbx2U["values"] = datevals2
    date_cbbx2U.state(["readonly"])
    month_cbbx2U = ttk.Combobox(master=dojfrm_nurU, textvariable = monthvar_nurU, width = 9)
    monthvals2 = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")
    month_cbbx2U["values"] = monthvals2
    month_cbbx2U.state(["readonly"])
    ylist1U = []
    for i in range(1950, 2022):
        ylist1U.append(i)
    year_cbbx2U = ttk.Combobox(master=dojfrm_nurU, textvariable = yearvar_nurU, width = 5)
    year_cbbx2U["values"] = tuple(ylist1U)
    year_cbbx2U.state(["readonly"])
    ent_contact_nurU = ttk.Entry(master=lblfrm4, width = 30)
    lbl_contact_nurU = ttk.Label(master=lblfrm4, text="Contact: ")
    ent_sal_nurU = ttk.Entry(master=lblfrm4, width = 30)
    lbl_sal_nurU = ttk.Label(master=lblfrm4, text = "Salary:")

    btn_frm_upnur = ttk.Frame(master=frm_updateN)

    def selN():
        ent_NIDU.config(state="normal")
        ent_NIDU.delete(0, tk.END)
        ent_Name_nurU.delete(0, tk.END)
        ent_deptU.delete(0, tk.END)
        ent_contact_nurU.delete(0, tk.END)
        ent_sal_nurU.delete(0, tk.END)
        selectedN = treedat11.focus()
        valuesN = treedat11.item(selectedN, "values")
        ent_NIDU.insert(0, valuesN[0])
        ent_NIDU.config(state="disabled")
        ent_Name_nurU.insert(0, valuesN[1])
        ent_deptU.insert(0, valuesN[2])
        ent_contact_nurU.insert(0, valuesN[4])
        ent_sal_nurU.insert(0, valuesN[5])
        dateindex = 0
        for i in range(0, len(datevals2)):
            if int(str(valuesN[3])[9:]) == int(datevals2[i]):
                dateindex = i
        date_cbbx2U.current(dateindex)
        months = {"January":1, "February":2, "March":3, "April":4, "May":5, "June":6, "July":7, "August":8, "September":9, "October":10, "November":11, "December":12}
        monthindex = 0
        for i in range(0, len(monthvals2)):
            if int(str(valuesN[3])[5:7]) == months.get(monthvals2[i]):
                monthindex=i
        month_cbbx2U.current(monthindex)
        yearindex = 0
        for i in range(0, len(ylist1U)):
            if int(str(valuesN[3])[:4]) == ylist1U[i]:
                yearindex = i
        year_cbbx2U.current(yearindex)

    sel_btn_N = ttk.Button(master=btn_frm_upnur, command=selN, text="Select Highlighted Record")


    def updatenur():
        try:
            ent_NIDU.config(state="normal")
            NID_val = ent_NIDU.get()
            Name_val = ent_Name_nurU.get()
            dept_val = ent_deptU.get()
            sal_val = float(ent_sal_nurU.get())
            contact = int(ent_contact_nurU.get())
            months = {"January":1, "February":2, "March":3, "April":4, "May":5, "June":6, "July":7, "August":8, "September":9, "October":10, "November":11, "December":12}
            DOJ_val_nur = datetime.date(int(yearvar_nurU.get()),int(months[monthvar_nurU.get()]), int(datevar_nurU.get()))
            nurcommU(NID_val, Name_val, dept_val, DOJ_val_nur, contact, sal_val)
            messagebox.showinfo("Update", message="Updated Successfully")
            ent_NIDU.delete(0, tk.END)
            ent_NIDU.config(state="disabled")
            ent_Name_nurU.delete(0, tk.END)
            ent_deptU.delete(0, tk.END)
            ent_contact_nurU.delete(0, tk.END)
            ent_sal_nurU.delete(0, tk.END)
        except ValueError:
            messagebox.showinfo("Status", "Incorrect Datatypes entered. Please check the data entered and ensure they are of the correct datatype")

    updatebtnnur = ttk.Button(master=btn_frm_upnur, text = "Update Data", command = updatenur)

    #code fragment for updating data in SQL and in Treeview (Employee table)
    frm_updateE = ttk.Frame(master=intfrm16)
    lblfrm5 = ttk.LabelFrame(master=frm_updateE)
    datevar_empU = tk.StringVar()
    monthvar_empU = tk.StringVar()
    yearvar_empU = tk.StringVar()
    ent_EIDU = ttk.Entry(master=lblfrm5, width = 30, state="disabled")
    lbl_EIDU = ttk.Label(master=lblfrm5, text = "Employee ID: ")
    ent_Name_empU = ttk.Entry(master=lblfrm5, width = 30)
    lbl_Name_empU = ttk.Label(master=lblfrm5, text = "Name: ")
    ent_jobU = ttk.Entry(master=lblfrm5, width = 30)
    lbl_jobU = ttk.Label(master=lblfrm5, text = "Job: ")
    lbl_DOJ_empU = ttk.Label(master=lblfrm5, text = "Date Of Joining: ")

    #small frame for DOJ
    dojfrm_empU = ttk.Frame(master=lblfrm5)

    date_cbbx3U = ttk.Combobox(master=dojfrm_empU, textvariable = datevar_empU, width = 3)
    datevals3 = ("01", "02", "03", "04", "05", "06", "07", "08", "09", 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31)
    date_cbbx3U["values"] = datevals3
    date_cbbx3U.state(["readonly"])
    month_cbbx3U = ttk.Combobox(master=dojfrm_empU, textvariable = monthvar_empU, width = 9)
    monthvals3 = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")
    month_cbbx3U["values"] = monthvals3
    month_cbbx3U.state(["readonly"])
    ylist2U = []
    for i in range(1950, 2022):
        ylist2U.append(i)
    year_cbbx3U = ttk.Combobox(master=dojfrm_empU, textvariable = yearvar_empU, width = 5)
    year_cbbx3U["values"] = tuple(ylist2U)
    year_cbbx3U.state(["readonly"])
    ent_contact_empU = ttk.Entry(master=lblfrm5, width = 30)
    lbl_contact_empU = ttk.Label(master=lblfrm5, text="Contact: ")
    ent_sal_empU = ttk.Entry(master=lblfrm5, width = 30)
    lbl_sal_empU = ttk.Label(master=lblfrm5, text = "Salary:")

    btn_frm_upemp = ttk.Frame(master=frm_updateE)

    def selE():
        ent_EIDU.config(state="normal")
        ent_EIDU.delete(0, tk.END)
        ent_Name_empU.delete(0, tk.END)
        ent_jobU.delete(0, tk.END)
        ent_contact_empU.delete(0, tk.END)
        ent_sal_empU.delete(0, tk.END)
        selectedE = treedat12.focus()
        valuesE = treedat12.item(selectedE, "values")
        ent_EIDU.insert(0, valuesE[0])
        ent_EIDU.config(state="disabled")
        ent_Name_empU.insert(0, valuesE[1])
        ent_jobU.insert(0, valuesE[2])
        ent_contact_empU.insert(0, valuesE[4])
        ent_sal_empU.insert(0, valuesE[5])
        dateindex = 0
        for i in range(0, len(datevals3)):
            if int(str(valuesE[3])[9:]) == int(datevals3[i]):
                dateindex = i
        date_cbbx3U.current(dateindex)
        months = {"January":1, "February":2, "March":3, "April":4, "May":5, "June":6, "July":7, "August":8, "September":9, "October":10, "November":11, "December":12}
        monthindex = 0
        for i in range(0, len(monthvals3)):
            if int(str(valuesE[3])[5:7]) == months.get(monthvals3[i]):
                monthindex=i
        month_cbbx3U.current(monthindex)
        yearindex = 0
        for i in range(0, len(ylist2U)):
            if int(str(valuesE[3])[:4]) == ylist2U[i]:
                yearindex = i
        year_cbbx3U.current(yearindex)

    sel_btn_E = ttk.Button(master=btn_frm_upemp, command=selE, text="Select Highlighted Record")


    def updateemp():
        try:
            ent_EIDU.config(state="normal")
            EID_val = ent_EIDU.get()
            Name_val = ent_Name_empU.get()
            job_val = ent_jobU.get()
            sal_val = float(ent_sal_empU.get())
            contact = int(ent_contact_empU.get())
            months = {"January":1, "February":2, "March":3, "April":4, "May":5, "June":6, "July":7, "August":8, "September":9, "October":10, "November":11, "December":12}
            DOJ_val_emp = datetime.date(int(yearvar_empU.get()),int(months[monthvar_empU.get()]), int(datevar_empU.get()))
            empcommU(EID_val, Name_val, job_val, DOJ_val_emp, contact, sal_val)
            messagebox.showinfo("Update", message="Updated Successfully")
            ent_EIDU.delete(0, tk.END)
            ent_EIDU.config(state="disabled")
            ent_Name_empU.delete(0, tk.END)
            ent_jobU.delete(0, tk.END)
            ent_contact_empU.delete(0, tk.END)
            ent_sal_empU.delete(0, tk.END)
        except ValueError:
            messagebox.showinfo("Status", "Incorrect Datatypes entered. Please check the data entered and ensure they are of the correct datatype")

    updatebtnemp = ttk.Button(master=btn_frm_upemp, text = "Update Data", command = updateemp)

    #Search a record(Patient)
    def searchP():
        if ent_SearchP.get() != 0:
            selections = []
            for patient in treedat13.get_children():
                if ent_SearchP.get() in treedat13.item(patient, "values"):
                    selections.append(patient)
        treedat13.selection_set(selections)
        if len(selections) == 0:
            messagebox.showinfo("Search", "No results found")

    frm_SP = ttk.Frame(master=intfrm17)

    ent_SearchP = ttk.Entry(master=frm_SP, width=30)
    lbl_SearchP = ttk.Label(master=frm_SP, text="Search: ")
    btn_searchP = ttk.Button(master=frm_SP, text="Search", width=25, command=searchP)

    #Search a record(Doctor)
    def searchD():
        if ent_SearchD.get() != 0:
            selections = []
            for doctor in treedat14.get_children():
                if ent_SearchD.get() in treedat14.item(doctor, "values"):
                    selections.append(doctor)
        treedat14.selection_set(selections)
        if len(selections) == 0:
            messagebox.showinfo("Search", "No results found")

    frm_SD = ttk.Frame(master=intfrm18)

    ent_SearchD = ttk.Entry(master=frm_SD, width=30)
    lbl_SearchD = ttk.Label(master=frm_SD, text="Search: ")
    btn_searchD = ttk.Button(master=frm_SD, text="Search", width=25, command=searchD)

    #Search a record(Nurse)
    def searchN():
        if ent_SearchN.get() != 0:
            selections = []
            for nurse in treedat15.get_children():
                if ent_SearchN.get() in treedat5.item(nurse, "values"):
                    selections.append(nurse)
        treedat13.selection_set(selections)
        if len(selections) == 0:
            messagebox.showinfo("Search", "No results found")

    frm_SN = ttk.Frame(master=intfrm19)

    ent_SearchN = ttk.Entry(master=frm_SN, width=30)
    lbl_SearchN = ttk.Label(master=frm_SN, text="Search: ")
    btn_searchN = ttk.Button(master=frm_SN, text="Search", width=25, command=searchN)

    #Search a record(Employee)
    def searchE():
        if ent_SearchE.get() != 0:
            selections = []
            for employee in treedat16.get_children():
                if ent_SearchE.get() in treedat16.item(employee, "values"):
                    selections.append(employee)
        treedat16.selection_set(selections)
        if len(selections) == 0:
            messagebox.showinfo("Search", "No results found")

    frm_SE = ttk.Frame(master=intfrm20)

    ent_SearchE = ttk.Entry(master=frm_SE, width=30)
    lbl_SearchE= ttk.Label(master=frm_SE, text="Search: ")
    btn_searchE = ttk.Button(master=frm_SE, text="Search", width=25, command=searchE)
        
    #Packing and adding everything
    ntbk.add(frm1, text="View DB")
    ntbk.add(frm2, text="Add Data")
    ntbk.add(frm3, text="Delete Data")
    ntbk.add(frm4, text="Update Data")
    ntbk.add(frm5, text="Search")

    internalntbk.add(intfrm1, text="Patient Table")
    internalntbk.add(intfrm2, text="Doctor Table")
    internalntbk.add(intfrm3, text="Nurse Table")
    internalntbk.add(intfrm4, text="Employee Table")

    internalntbk1.add(intfrm5, text="Patient Table")
    internalntbk1.add(intfrm6, text="Doctor Table")
    internalntbk1.add(intfrm7, text="Nurse Table")
    internalntbk1.add(intfrm8, text="Employee Table")

    internalntbk2.add(intfrm9, text="Patient Table")
    internalntbk2.add(intfrm10, text="Doctor Table")
    internalntbk2.add(intfrm11, text="Nurse Table")
    internalntbk2.add(intfrm12, text="Employee Table")

    internalntbk3.add(intfrm13, text="Patient Table")
    internalntbk3.add(intfrm14, text="Doctor Table")
    internalntbk3.add(intfrm15, text="Nurse Table")
    internalntbk3.add(intfrm16, text="Employee Table")

    internalntbk4.add(intfrm17, text="Patient Table")
    internalntbk4.add(intfrm18, text="Doctor Table")
    internalntbk4.add(intfrm19, text="Nurse Table")
    internalntbk4.add(intfrm20, text="Employee Table")

    ntbk.pack()
    internalntbk.pack()
    internalntbk1.pack()
    internalntbk2.pack()
    internalntbk3.pack()
    internalntbk4.pack()
    scrlbrfrm1.pack()
    scrlbr1.pack(fill = tk.Y, side = tk.RIGHT)
    scrlbrfrm2.pack()
    scrlbr2.pack(fill = tk.Y, side = tk.RIGHT)
    scrlbrfrm3.pack()
    scrlbr3.pack(fill = tk.Y, side = tk.RIGHT)
    scrlbrfrm4.pack()
    scrlbr4.pack(fill = tk.Y, side = tk.RIGHT)
    scrlbrfrm5.pack()
    scrlbr5.pack(fill = tk.Y, side = tk.RIGHT)
    scrlbrfrm6.pack()
    scrlbr6.pack(fill = tk.Y, side = tk.RIGHT)
    scrlbrfrm7.pack()
    scrlbr7.pack(fill = tk.Y, side = tk.RIGHT)
    scrlbrfrm8.pack()
    scrlbr8.pack(fill = tk.Y, side = tk.RIGHT)
    scrlbrfrm9.pack()
    scrlbr9.pack(fill = tk.Y, side = tk.RIGHT)
    scrlbrfrm10.pack()
    scrlbr10.pack(fill = tk.Y, side = tk.RIGHT)
    scrlbrfrm11.pack()
    scrlbr11.pack(fill = tk.Y, side = tk.RIGHT)
    scrlbrfrm12.pack()
    scrlbr12.pack(fill = tk.Y, side = tk.RIGHT)
    scrlbrfrm13.pack()
    scrlbr13.pack(fill = tk.Y, side = tk.RIGHT)
    scrlbrfrm14.pack()
    scrlbr14.pack(fill = tk.Y, side = tk.RIGHT)
    scrlbrfrm15.pack()
    scrlbr15.pack(fill = tk.Y, side = tk.RIGHT)
    scrlbrfrm16.pack()
    scrlbr16.pack(fill = tk.Y, side = tk.RIGHT)
    treedat1.pack()
    treedat2.pack()
    treedat3.pack()
    treedat4.pack()
    treedat5.pack()
    treedat6.pack()
    treedat7.pack()
    treedat8.pack()
    treedat9.pack()
    treedat10.pack()
    treedat11.pack()
    treedat12.pack()
    treedat13.pack()
    treedat14.pack()
    treedat15.pack()
    treedat16.pack()


    ent_PID.grid(row=0, column=1, pady=5)
    lbl_PID.grid(row=0, column=0, pady=5)
    ent_Name.grid(row=1, column=1, pady=5)
    lbl_Name.grid(row=1, column=0, pady=5)
    lbl_age.grid(row=2, column=0)
    age_cbbx.grid(row=2, column=1)
    ent_ailment.grid(row=3, column=1, pady=5)
    lbl_ailment.grid(row=3, column=0, pady=5) 
    lbl_payment.grid(row=4, column=0, pady=5)
    rdb_cash.grid(row=4, column=1, sticky="w", pady=5)
    rdb_card.grid(row=5, column=1, sticky="w", pady=5)
    rdb_cheque.grid(row=6, column=1, sticky="w", pady=5)
    sep_pay_stat.grid(row=7, column=1, sticky='ew', pady=5)
    sep_pay_stat1.grid(row=7, column=0, sticky='ew', pady=5)
    lbl_status.grid(row=8, column=0, pady=5)
    rdb_paid.grid(row=8, column=1, sticky="w")
    rdb_pending.grid(row=9, column=1, sticky="w")
    ent_contact.grid(row=10, column=1, pady=5)
    lbl_contact.grid(row=10, column=0, pady=5)
    lbl_amt.grid(row=11, column=0, pady=5)
    ent_amt.grid(row=11, column=1, pady=5)
    addbtnpat.grid(row=12, column=1, pady=5)

    ent_DID.grid(row=0, column=1, pady=5)
    lbl_DID.grid(row=0, column=0, pady=5)
    ent_Name_doc.grid(row=1, column=1, pady=5)
    lbl_Name_doc.grid(row=1, column=0, pady=5)
    ent_spec.grid(row=2, column=1, pady=5)
    lbl_spec.grid(row=2, column=0, pady=5)
    dojfrm_doc.grid(row=3, column=1, pady=5)
    date_cbbx1.grid(row=0, column=0, padx=10, pady=5)
    month_cbbx1.grid(row=0, column=2, padx=10, pady=5)
    year_cbbx1.grid(row=0, column=4, padx=10, pady=5)
    lbl_DOJ.grid(row=3, column=0, pady=5)
    ent_contact_doc.grid(row=4, column=1, pady=5)
    lbl_contact_doc.grid(row=4, column=0, pady=5)
    ent_sal.grid(row=5, column=1, pady=5)
    lbl_sal.grid(row=5, column=0, pady=5)
    addbtndoc.grid(row=6, column=1, pady=5)

    ent_NID.grid(row=0, column=1, pady=5)
    lbl_NID.grid(row=0, column=0, pady=5)
    ent_Name_nur.grid(row=1, column=1, pady=5)
    lbl_Name_nur.grid(row=1, column=0, pady=5)
    ent_dept.grid(row=2, column=1, pady=5)
    lbl_dept.grid(row=2, column=0, pady=5)
    lbl_DOJ_nur.grid(row=3, column=0, pady=5)
    dojfrm_nur.grid(row=3, column=1, pady=5)
    date_cbbx2.grid(row=0, column=0, padx=10, pady=5)
    month_cbbx2.grid(row=0, column=1, padx=10, pady=5)
    year_cbbx2.grid(row=0, column=2, padx=10, pady=5)
    ent_contact_nur.grid(row=4, column=1, pady=5)
    lbl_contact_nur.grid(row=4, column=0, pady=5)
    ent_sal_nur.grid(row=5, column=1, pady=5)
    lbl_sal_nur.grid(row=5, column=0, pady=5)
    addbtnnur.grid(row=6, column=1, pady=5)

    ent_EID.grid(row=0, column=1, pady=5)
    lbl_EID.grid(row=0, column=0, pady=5)
    ent_Name_emp.grid(row=1, column=1, pady=5)
    lbl_Name_emp.grid(row=1, column=0, pady=5)
    ent_job.grid(row=2, column=1, pady=5)
    lbl_job.grid(row=2, column=0, pady=5)
    lbl_DOJ_emp.grid(row=3, column=0, pady=5)
    dojfrm_emp.grid(row=3, column=1, pady=5)
    date_cbbx3.grid(row=0, column=0, padx=10, pady=5)
    month_cbbx3.grid(row=0, column=1, padx=10, pady=5)
    year_cbbx3.grid(row=0, column=2, padx=10, pady=5)
    ent_contact_emp.grid(row=4, column=1, pady=5)
    lbl_contact_emp.grid(row=4, column=0, pady=5)
    ent_sal_emp.grid(row=5, column=1, pady=5)
    lbl_sal_emp.grid(row=5, column=0, pady=5)
    addbtnemp.grid(row=6, column=1, pady=5)

    frm_delp.pack(pady=20)
    btn_delall.pack(pady=10)
    btn_delsel.pack(pady=10)

    frm_deld.pack(pady=20)
    btn_delalld.pack(pady=10)
    btn_delseld.pack(pady=10)

    frm_deln.pack(pady=20)
    btn_delalln.pack(pady=10)
    btn_delseln.pack(pady=10)

    frm_dele.pack(pady=20)
    btn_delalle.pack(pady=10)
    btn_delsele.pack(pady=10)


    frm_updateP.pack()
    lblfrm1.grid(row=0, column=0)
    lblfrm2.grid(row=0, column=1)
    ent_PIDU.grid(row=0, column=1, pady=5)
    lbl_PIDU.grid(row=0, column=0, pady=5)
    ent_NameU.grid(row=1, column=1, pady=5)
    lbl_NameU.grid(row=1, column=0, pady=5)
    lbl_ageU.grid(row=2, column=0)
    age_cbbxU.grid(row=2, column=1)
    ent_ailmentU.grid(row=3, column=1, pady=5)
    lbl_ailmentU.grid(row=3, column=0, pady=5) 
    lbl_paymentU.grid(row=0, column=0, pady=5)
    ptype_cbbx.grid(row=0, column=1, pady=25)
    lbl_statusU.grid(row=1, column=0, pady=5)
    pstatus_cbbx.grid(row=1, column=1, pady=25)
    ent_contactU.grid(row=4, column=1, pady=5)
    lbl_contactU.grid(row=4, column=0, pady=5)
    lbl_amtU.grid(row=5, column=0, pady=5)
    ent_amtU.grid(row=5, column=1, pady=5)
    updatebtnpat.grid(row=1, column=1, pady=5, padx=5)
    sel_btn_P.grid(row=1, column=0, pady=5, padx=5)

    frm_updateD.pack()
    lblfrm3.pack()
    btn_frm_updoc.pack()
    ent_DIDU.grid(row=0, column=1, pady=5)
    lbl_DIDU.grid(row=0, column=0, pady=5)
    ent_Name_docU.grid(row=1, column=1, pady=5)
    lbl_Name_docU.grid(row=1, column=0, pady=5)
    ent_specU.grid(row=2, column=1, pady=5)
    lbl_specU.grid(row=2, column=0, pady=5)
    dojfrm_docU.grid(row=3, column=1, pady=5)
    date_cbbx1U.grid(row=0, column=0, padx=10, pady=5)
    month_cbbx1U.grid(row=0, column=2, padx=10, pady=5)
    year_cbbx1U.grid(row=0, column=4, padx=10, pady=5)
    lbl_DOJU.grid(row=3, column=0, pady=5)
    ent_contact_docU.grid(row=4, column=1, pady=5)
    lbl_contact_docU.grid(row=4, column=0, pady=5)
    ent_salU.grid(row=5, column=1, pady=5)
    lbl_salU.grid(row=5, column=0, pady=5)
    updatebtndoc.grid(row=0, column=1, padx=5, pady=5)
    sel_btn_D.grid(row=0, column=0, padx=5, pady=5)

    frm_updateN.pack()
    lblfrm4.pack()
    btn_frm_upnur.pack()
    ent_NIDU.grid(row=0, column=1, pady=5)
    lbl_NIDU.grid(row=0, column=0, pady=5)
    ent_Name_nurU.grid(row=1, column=1, pady=5)
    lbl_Name_nurU.grid(row=1, column=0, pady=5)
    ent_deptU.grid(row=2, column=1, pady=5)
    lbl_deptU.grid(row=2, column=0, pady=5)
    dojfrm_nurU.grid(row=3, column=1, pady=5)
    date_cbbx2U.grid(row=0, column=0, padx=10, pady=5)
    month_cbbx2U.grid(row=0, column=2, padx=10, pady=5)
    year_cbbx2U.grid(row=0, column=4, padx=10, pady=5)
    lbl_DOJ_nurU.grid(row=3, column=0, pady=5)
    ent_contact_nurU.grid(row=4, column=1, pady=5)
    lbl_contact_nurU.grid(row=4, column=0, pady=5)
    ent_sal_nurU.grid(row=5, column=1, pady=5)
    lbl_sal_nurU.grid(row=5, column=0, pady=5)
    updatebtnnur.grid(row=0, column=1, padx=5, pady=5)
    sel_btn_N.grid(row=0, column=0, padx=5, pady=5)

    frm_updateE.pack()
    lblfrm5.pack()
    btn_frm_upemp.pack()
    ent_EIDU.grid(row=0, column=1, pady=5)
    lbl_EIDU.grid(row=0, column=0, pady=5)
    ent_Name_empU.grid(row=1, column=1, pady=5)
    lbl_Name_empU.grid(row=1, column=0, pady=5)
    ent_jobU.grid(row=2, column=1, pady=5)
    lbl_jobU.grid(row=2, column=0, pady=5)
    dojfrm_empU.grid(row=3, column=1, pady=5)
    date_cbbx3U.grid(row=0, column=0, padx=10, pady=5)
    month_cbbx3U.grid(row=0, column=2, padx=10, pady=5)
    year_cbbx3U.grid(row=0, column=4, padx=10, pady=5)
    lbl_DOJ_empU.grid(row=3, column=0, pady=5)
    ent_contact_empU.grid(row=4, column=1, pady=5)
    lbl_contact_empU.grid(row=4, column=0, pady=5)
    ent_sal_empU.grid(row=5, column=1, pady=5)
    lbl_sal_empU.grid(row=5, column=0, pady=5)
    updatebtnemp.grid(row=0, column=1, padx=5, pady=5)
    sel_btn_E.grid(row=0, column=0, padx=5, pady=5)
    

    frm_SP.pack()
    lbl_SearchP.grid(row=0, column=0, pady=15)
    ent_SearchP.grid(row=0, column=1, pady=15)
    btn_searchP.grid(row=1, column=1, pady=15)

    frm_SD.pack()
    lbl_SearchD.grid(row=0, column=0, pady=15)
    ent_SearchD.grid(row=0, column=1, pady=15)
    btn_searchD.grid(row=1, column=1, pady=15)

    frm_SN.pack()
    lbl_SearchN.grid(row=0, column=0, pady=15)
    ent_SearchN.grid(row=0, column=1, pady=15)
    btn_searchN.grid(row=1, column=1, pady=15)

    frm_SE.pack()
    lbl_SearchE.grid(row=0, column=0, pady=15)
    ent_SearchE.grid(row=0, column=1, pady=15)
    btn_searchE.grid(row=1, column=1, pady=15)


    l1 = [frm1, frm2, frm3, frm4, frm5]
    for i in l1:
        lbl_bgm = tk.Label(master=i, width = 1024, height = 650, image = bgm)
        lbl_bgm.pack()

    main.protocol("WM_DELETE_WINDOW", lambda: sqlqueries.closeconnection(main))

    main.mainloop()

#defining function to be triggered on perfect login to execute main window
def lgin():
    #grabbing username and password and referencing it with csv
    user = usern_ent.get()
    pwd = passwd_ent.get()
    with open(userdat_path, "r") as logindetes:
        reader = csv.reader(logindetes)
        found = False
        try:
            for row in reader:
                if row[0] == user and fernet.decrypt(eval(row[1])).decode() == pwd:
                    messagebox.showinfo("Status", "Login Success")
                    #destroying login and loading main window
                    found = True
                    logindetes.close()
                    login.destroy()
                    mainwindow()
        except ValueError:
            pass

    if found == False:
        #Executes on login failure
        global msgbox_yesnoregister
        msgbox_yesnoregister = tk.Toplevel(login)
        msgbox_yesnoregister.title("Hospital Management Software v1.0")
        msgbox_yesnoregister.iconbitmap(ico_path)
        msgbox_yesnoregister.geometry("270x130+500+500")
        msgbox_yesnoregister.resizable(False, False)
        def yes():
            usern_ent.delete(0, tk.END)
            passwd_ent.delete(0, tk.END)
            msgbox_yesnoregister.destroy()
        def no():
            msgbox_yesnoregister.destroy()
            login.destroy()
        btn_yes = ttk.Button(master=msgbox_yesnoregister, text="Yes", command=yes, width=7)
        btn_no = ttk.Button(master=msgbox_yesnoregister, text="No", command=no, width=7)
        btn_reg1 = ttk.Button(master=msgbox_yesnoregister, text="Register", command=reg, width=7)
        lbl_1 = tk.Label(master=msgbox_yesnoregister, text="Login Failed.\n Would you like to try again or register?", font = ("Helvetica", 11), anchor="n")
        lbl_1.pack(pady=30)
        btn_yes.place(x=20, y=80)
        btn_no.place(x=180, y=80)
        btn_reg1.place(x=100, y=80)




#Defining background
tmpbg = Image.open(bg_path)
tmp1bg = tmpbg.resize((1024,650))

#defining login window and its attributes
login = tk.Tk(className="Loginwindow")
x = (login.winfo_screenwidth()/2)-512
y = (login.winfo_screenheight()/2)-325
login.geometry(f"1024x650+{int(x)}+{int(y)}")
login.title("Thera.py v1.0")
style = ttk.Style()
os.chdir(asset_path)
login.tk.call("source", theme_path)
style.theme_use("azure-dark")
login.attributes("-alpha", 0.98)
login.iconbitmap(ico_path)
login.resizable(False,False)

login.option_add('*tearOff', False)
menubar = Menu(login)
login.config(menu = menubar,bg = "black")
bg = ImageTk.PhotoImage(tmp1bg)

lbl_bg = tk.Label(master=login, image = bg)

#taking username and password from user
usern_ent = ttk.Entry(master=login, width = 75)
passwd_ent = ttk.Entry(master=login, width = 75, show="*")

#login button
btn_login = ttk.Button(master=login, text = "Login", command = lgin, width = 25)

#register button
btn_reg = ttk.Button(master=login, text = "Register", command = reg, width = 25)

#file menu
menu_file = Menu(menubar)

menubar.add_cascade(menu=menu_file, label = "File")
menu_file.add_command(label = "Exit", command = login.destroy)

#pack everything
lbl_bg.pack()
usern_ent.place(x=230, y=465)
passwd_ent.place(x=230, y=500)
btn_login.place(x=230, y=550)
btn_reg.place(x=430, y=550)
login.mainloop()

###########################################################################################################################################################################################################################################################################################################################################################################################