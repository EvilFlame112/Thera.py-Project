import mysql.connector
import csv
import os
from cryptography.fernet import Fernet

file_path = os.path.dirname(os.path.realpath(__file__))
secret_path = os.path.join(file_path, "secret.csv")

key = b'duq6gXwUm-RRsvoNTOIkfvfhl3-gT6l_kRz9pwJFAwQ='
fernet = Fernet(key)

with open(secret_path, "r") as secret:
    secret.seek(0)
    reader = csv.reader(secret)
    vals = next(reader)
    secret.close()

conn=mysql.connector.connect(host=vals[0], user=vals[1],  passwd=fernet.decrypt(eval(vals[2])).decode(), database="hospitaldata")
cur=conn.cursor()
def addtopatient(pid, namep, age, ailment, paytypep, status, contactp, amountp):
    cur.execute(f"INSERT INTO patient values({pid}, '{namep}', {age}, '{ailment}', '{paytypep}', '{status}', {contactp}, {amountp})")
    conn.commit()
def addtodoctor(did,named,specialization,dojd,contactd,salaryd):
    cur.execute(f"insert into doctor values({did},'{named}','{specialization}','{dojd}',{contactd},{salaryd}) ")
    conn.commit()
def addtonurse(nid,namen,department,dojn,contactn,salaryn):
    cur.execute(f"insert into nurse values({nid},'{namen}','{department}','{dojn}',{contactn},{salaryn})")
    conn.commit()
def addtoemployee(eid,namee,job,doje,contacte,salarye):
    cur.execute(f"insert into employee values({eid},'{namee}','{job}','{doje}',{contacte},{salarye})")
    conn.commit()
def dele(tablename,id,idinput):
    cur.execute(f"delete from {tablename} where {id}={idinput}")
    conn.commit()
def purgeP():
    cur.execute("drop table patient")
    cur.execute("CREATE TABLE IF NOT EXISTS patient(Pateint_Id int PRIMARY KEY, Name varchar(50), Age int, Ailment varchar(50), Payment_Type varchar(10), Payment_Status varchar(50), Contact decimal(10,0), Amount decimal(10,2))")
def purgeD():
    cur.execute("drop table doctor")
    cur.execute("CREATE TABLE IF NOT EXISTS doctor(Doctor_Id int primary key,Name varchar(50),Specialization varchar(50),DOJ date,Contact bigint, Salary Decimal(10,2)) ")
def purgeN():
    cur.execute("drop table nurse")
    cur.execute("CREATE TABLE IF NOT EXISTS nurse(Nurse_Id int primary key,Name varchar(50),Department varchar(50),DOJ date, Contact bigint,Salary decimal(10,2))")
def purgeE():
    cur.execute("drop table employee")
    cur.execute("CREATE TABLE IF NOT EXISTS employee(Employee_Id int primary key,Name varchar(50),Job VARCHAR(50),Payment_Type varchar(50),Contact bigint,Salary Decimal(10,2))")
def query(tablename):
    cur.execute(f"SELECT * FROM {tablename}")
    return cur.fetchall()
def delemany(tablename,id,idlist):
    for i in idlist:
        querydel = f"delete from {tablename} where {id}={i}"
        cur.execute(querydel)
        conn.commit()
def closeconnection(main):
    conn.close()
    main.destroy()