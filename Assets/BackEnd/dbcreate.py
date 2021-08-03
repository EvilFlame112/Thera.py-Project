import mysql.connector
conn=mysql.connector.connect(host='localhost', user="root",  passwd="")
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
    cur.execute("CREATE TABLE patient(PatientID int PRIMARY KEY, Name varchar(50), Age tinyint, Ailment varchar(50), Payment type varchar(10), Payment status varchar(10), Contact decimal(10,0), Amount decimal(10,2))")
    cur.execute("CREATE TABLE doctor(DoctorID int PRIMARY KEY, Name varchar(50), Ailment varchar(50), Payment type varchar(10), Payment status varchar(10), Contact decimal(10,0), Amount decimal(10,2))")

