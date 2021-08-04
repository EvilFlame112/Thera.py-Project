import mysql.connector
conn=mysql.connector.connect(host='localhost', user="root",  passwd="", database="hospitalmgmt")
cur=conn.cursor
def addtopatient( pid, namep, age, ailment, paytypep, status, contactp, amountp):
    cur.execute(f"INSERT INTO patient values({pid}, {namep}, {age}, {ailment}, {paytypep}, {status}, {contactp}, {amountp})")
    conn.commit()
def addtodoctor(did,named,specialization,dojd,contactd,salaryd):
    cur.execute(f"insert into doctor values({did},{named},{specialization},{dojd},{contactd},{salaryd}) ")
    conn.commit()
def addtonurse(nid,namen,department,dojn,contactn,salaryn):
    cur.execute(f"insert into nurse values({nid},{namen},{department},{dojn},{contactn},{salaryn})")
    conn.commit()
def addtoemployee(eid,namee,job,paytypee,contacte,salarye):
    cur.execute(f"insert into employee values({eid},{namee},{job},{paytypee},{contacte},{salarye}")
    conn.commit()
def dele(tablename,id,idinput):
    cur.execute(f"delete from {tablename} where {id}={idinput}")