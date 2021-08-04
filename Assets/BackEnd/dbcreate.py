import mysql.connector
conn=mysql.connector.connect(host='localhost', user="root",  passwd="tar$1402")
cur = conn.cursor()
def chkdb(db):
    cur.execute("show databases;")
    listdb = []
    for i in cur:
        listdb.append(i)
        print (i)
    if db not in listdb:
        return True
    else:
        return False

def makedb():
    cur.execute("CREATE DATABASE hospitaldata")
    cur.execute("use hospitaldata")
    cur.execute("create table patient(Pateint_Id int PRIMARY KEY, Name varchar(50), Age int, Ailment varchar(50), Payment_Type varchar(10), Payment_Status varchar(50), Contact decimal(10,0), Amount decimal(10,2))")
    cur.execute("create table doctor(Doctor_Id int primary key,Name varchar(50),Specialization varchar(50),DOJ date,Contact bigint, Salary Decimal(10,2)) ")
    cur.execute("create table nurse(Nurse_Id int primary key,Name varchar(50),Department varchar(50),DOJ date, Contact bigint,Salary decimal(10,2))")
    cur.execute("create table employee(Employee_Id int primary key,Name varchar(50),Job VARCHAR(50),Payment_Type varchar(50),Contact bigint,Salary Decimal(10,2))")

makedb()