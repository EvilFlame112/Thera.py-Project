#Hospital management system v1.0
#Source code credits:
#       Frontend/GUI - Ram
#       Backend/SQL - Sai
#       Documentation - Yash


#Importing necessary modules
import tkinter as tk
import os
from tkinter import Menu, ttk, messagebox
from PIL import ImageTk, Image
from ttkthemes import themed_tk

#Declaring path variables for extensive support with asset folder
file_path = os.path.dirname(os.path.realpath(__file__))
ico_path = os.path.join(file_path, "Assets", "titleicon.ico")
bg_path = os.path.join(file_path, "Assets", "img24.png")
bgm_path = os.path.join(file_path, "Assets", "main.png")
theme_path = os.path.join(file_path, "Assets", "sun-valley.tcl")

#defining function to be triggered on perfect login to execute main window
def lgin():
    #grabbing username and password and referencing it with database
    user = usern_ent.get()
    pwd = passwd_ent.get()
    if user == "" and pwd == "":
        messagebox.showinfo("Status", "Login Success")

        #destroying login and loading main window
        #Giving it a theme and attributes with ttkthemes
        login.destroy()
        main = themed_tk.ThemedTk(className="Mainwindow")
        main.get_themes()
        main.set_theme("equilux")
        main.geometry("1024x650")
        main.attributes("-alpha", 0.98)
        main.title("Hospital Management Software v1.0")
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

        #set of internal tabs for accessing in view tab
        internalntbk = ttk.Notebook(master=frm1)
        intfrm1 = ttk.Frame(master=internalntbk)
        intfrm2 = ttk.Frame(master=internalntbk)
        intfrm3 = ttk.Frame(master=internalntbk)
        intfrm4 = ttk.Frame(master=internalntbk)

        #set of internal tabs for accessing in add tab
        internalntbk1 = ttk.Notebook(master=frm2)
        intfrm5 = ttk.Frame(master=internalntbk1, width = 1024, height = 650)
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

        #scrollbar for scrolling (-_-)
        scrlbrfrm1 = ttk.Frame(master=intfrm1)
        scrlbr1 = ttk.Scrollbar(master=scrlbrfrm1)
        scrlbrfrm2 = ttk.Frame(master=intfrm2)
        scrlbr2 = ttk.Scrollbar(master=scrlbrfrm2)
        scrlbrfrm3 = ttk.Frame(master=intfrm3)
        scrlbr3 = ttk.Scrollbar(master=scrlbrfrm3)
        scrlbrfrm4 = ttk.Frame(master=intfrm4)
        scrlbr4 = ttk.Scrollbar(master=scrlbrfrm4)

        #Making tables with treeview
        treedat1 = ttk.Treeview(master=scrlbrfrm1, yscrollcommand=scrlbr1.set)
        scrlbr1.config(command = treedat1.yview)
        treedat1["columns"] = ("Patient ID", "Name", "Ailment", "Payment type", "Payment status", "Amount")
        treedat1.column("#0", width = 0, minwidth = 0, stretch=0)
        treedat1.column("Patient ID", anchor="center", width = 120)
        treedat1.column("Name", anchor = "center", width = 120)
        treedat1.column("Ailment", anchor = "center", width = 120)
        treedat1.column("Payment type", anchor = "center", width = 120)
        treedat1.column("Payment status", anchor = "center", width = 120)
        treedat1.column("Amount", anchor = "center", width = 120)

        treedat1.heading("#0", text="", anchor="center")
        treedat1.heading("Patient ID", text="Patient ID", anchor="center")
        treedat1.heading("Name", text="Name", anchor="center")
        treedat1.heading("Ailment", text="Ailment", anchor="center")
        treedat1.heading("Payment type", text="Payment type", anchor="center")
        treedat1.heading("Payment status", text="Payment status", anchor="center")
        treedat1.heading("Amount", text="Amount", anchor="center")

        treedat2 = ttk.Treeview(master=scrlbrfrm2, yscrollcommand=scrlbr2.set)
        treedat2["columns"] = ("Doctor ID", "Name", "Specialization", "DOJ", "Salary")
        treedat2.column("#0", width = 0, minwidth = 0, stretch=0)
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

        treedat3 = ttk.Treeview(master=scrlbrfrm3, yscrollcommand=scrlbr3.set)
        treedat3["columns"] = ("Nurse ID", "Name", "Department", "DOJ", "Salary")
        treedat3.column("#0", width = 0, minwidth = 0, stretch=0)
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

        treedat4 = ttk.Treeview(master=scrlbrfrm4, yscrollcommand=scrlbr4.set)
        treedat4["columns"] = ("Employee ID", "Name", "Job", "DOJ", "Salary")
        treedat4.column("#0", width = 0, minwidth = 0, stretch=0)
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

        #code fragment for adding data to SQL and to Treeview
        paymentval = tk.IntVar()
        statusval = tk.IntVar()
        ent_PID = ttk.Entry(master=intfrm5, width = 30)
        ent_Name = ttk.Entry(master=intfrm5, width = 30)
        ent_ailment = ttk.Entry(master=intfrm5, width = 30)
        ent_amt = ttk.Entry(master=intfrm5, width = 30)
        rdb_cash = ttk.Radiobutton(master=intfrm5, text="Cash", value=1, variable=paymentval)
        rdb_card = ttk.Radiobutton(master=intfrm5, text="Card", value=2, variable=paymentval)
        rdb_cheque = ttk.Radiobutton(master=intfrm5, text="Cheque", value=3, variable=paymentval)
        rdb_paid = ttk.Radiobutton(master=intfrm5, text="Paid", value=1, variable=statusval)
        rdb_pending = ttk.Radiobutton(master=intfrm5, text="Pending", value=2, variable=statusval)

        payment = ""
        status = ""

        if paymentval == 1:
            payment = "Cash"
        elif paymentval == 2:
            payment = "Card"
        else:
            payment = "Cheque"
        
        if statusval == 1:
            status = "Paid"
        else:
            status = "Pending"

        def addrec():
            PID_val = ent_PID.get()
            Name_val = ent_Name.get()
            ailment_val = ent_ailment.get()
            amt_val = ent_amt.get()
            treedat1.insert(parent="", index=tk.END, text = "", values = (PID_val, Name_val, ailment_val, payment, status, amt_val))
            messagebox.showinfo("Add", message="Added Successfully")
            ent_PID.delete(0, tk.END)
            ent_Name.delete(0, tk.END)
            ent_ailment.delete(0, tk.END)
            ent_amt.delete(0, tk.END)
        addbtn = ttk.Button(master=intfrm5, text = "Add Data", command = addrec)

        #Packing and adding everything
        ntbk.add(frm1, text="View DB")
        ntbk.add(frm2, text="Add Data")
        ntbk.add(frm3, text="Delete Data")
        ntbk.add(frm4, text="Update Data")

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

        ntbk.pack()
        internalntbk.pack()
        internalntbk1.pack()
        internalntbk2.pack()
        internalntbk3.pack()
        scrlbrfrm1.pack()
        scrlbr1.pack(fill = tk.Y, side = tk.RIGHT)
        scrlbrfrm2.pack()
        scrlbr2.pack(fill = tk.Y, side = tk.RIGHT)
        scrlbrfrm3.pack()
        scrlbr3.pack(fill = tk.Y, side = tk.RIGHT)
        scrlbrfrm4.pack()
        scrlbr4.pack(fill = tk.Y, side = tk.RIGHT)
        treedat1.pack()
        treedat2.pack()
        treedat3.pack()
        treedat4.pack()

        ent_PID.pack()
        ent_Name.pack()
        ent_ailment.pack()
        
        rdb_cash.pack()
        rdb_card.pack()
        rdb_cheque.pack()
        rdb_paid.pack()
        rdb_pending.pack()
        ent_amt.pack()
        addbtn.pack()

        l1 = [frm1, frm2, frm3, frm4]
        for i in l1:
            lbl_bgm = tk.Label(master=i, width = 1024, height = 650, image = bgm)
            lbl_bgm.pack()

        main.mainloop()
    else:
        #Executes on login failure
        fin = messagebox.askyesno("Status", "Login Failed. Would you like to try again?")
        if fin == True:    
            usern_ent.delete(0, tk.END)
            passwd_ent.delete(0, tk.END)
        else:
            login.destroy()

#Defining background
tmpbg = Image.open(bg_path)
tmp1bg = tmpbg.resize((1024,650))

#defining login window and its attributes
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

#taking username and password from user
usern_ent = tk.Entry(master=login, width = 30, font = ("SF Pro Display", 16), bg = "grey30", fg = "white")
passwd_ent = tk.Entry(master=login, width = 30, font = ("SF Pro Display", 16), bg = "grey30", fg = "white", show="*")

#login button
btn_login = tk.Button(master=login, text = "Login", command = lgin, borderwidth=2, bg = "grey15", fg = "white", relief=tk.SUNKEN, width = 25, height = 1, font = ("SF Pro Display", 20))

#file menu
menu_file = Menu(menubar)

menubar.add_cascade(menu=menu_file, label = "File")
menu_file.add_command(label = "Exit", command = login.destroy)

#pack everything
lbl_bg.pack()
usern_ent.place(x=230, y=465)
passwd_ent.place(x=230, y=500)
btn_login.place(x=230, y=550)
login.mainloop()

###########################################################################################################################################################################################################################################################################################################################################################################################