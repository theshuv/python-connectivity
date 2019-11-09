# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import sys
import sqlite3
con = sqlite3.connect('mydb.db')
print("connection done")
cursor=con.cursor()


def displayAll():
    cursor.execute("select * from mytable1")
    for row in cursor.fetchall():
        print(str(row[0])+","+row[1]+","+str(row[2]))
       
def insertRec():
    id1=input("Enter Employee id :")
    name=input("Enter Employee name :")
    sal=input("Enter Employee Salary :")
    cursor.execute('Insert into mytable1 values(?,?,?)',(id1,name,sal))
    con.commit
    
def deleteRec():
    id1=int(input("Enter Employee id: "))
    cursor.execute("delete from mytable1 where id=?",(id1,))
    con.commit

def updateRec():
    id1=int(input("Enter Emp id to Delete :"))
    nm=input("Enter Emp name :")
    sal=input("Enter Emp Salary :")
    cursor.execute("Update mytable1 set name=?,sal=? where id=?",(nm,sal,id1))
    con.commit

def displaybyid():
    id1=int(input("Enter Emp id to view :"))
    cursor.execute("select * from mytable1 where id=?",(id1,))
    row=cursor.fetchone()
    print(str(row[0])+","+row[1]+","+str(row[2]))            


while(True):
    selection=input("\n1.Insert Employee Data \n2.Delete Employee Data\n3.Update Employee Data \n4.Display Employee Data  \n5.Display by Id  \n6.Exit :")
    
    if selection=="1":
        insertRec()
    elif selection=="2":
        deleteRec()
    elif selection=="3":
        updateRec()
    elif selection=="4":
        displayAll()
    elif selection=="5":
        displaybyid()
    elif selection=="6":
        print("Exiting program...")
        sys.exit();
    else:
        print("\n INVALID SELECTION \n") 
        