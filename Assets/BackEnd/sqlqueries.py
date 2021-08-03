import mysql.connector
conn=mysql.connector.connect(host='localhost', user="root",  passwd="", database="hospitalmgmt")
cur=conn.cursor
def addtotable(tablename, PID, Name, age, Ailment, paymentT, status, contact, amount):
    cur.execute(f"INSERT INTO {tablename} values({PID}, {Name}, {age}, {Ailment}, {paymentT}, {status}, {contact}, {amount})")
    conn.commit()