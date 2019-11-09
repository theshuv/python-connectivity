# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 08:56:20 2019

@author: shuv
"""

def insert():
    try:
        db=client.EmployeeData
        employeeId = input('Enter Employee id :')
        employeeName = input("Enter Emp Name  :")
        employeeAge = input("Enter Emp Age :")
        employeeCountry = input("Enter Emp Country :")
        db.Employee.insert_one({
                "Id": employeeId,"Name":employeeName,
                "Age":employeeAge,"Country":employeeCountry
                })
        print("successfully inserted details.")
    except Exception as e:
        print(str(e))
    
def read() :
    try:
        db=client.EmployeeData
        empCol=db.Employee.find()
        print("\n All data from EmployeeData Database")
        for emp in empCol:
            print(emp)
    except Exception as e:
        print(str(e))

def update():
    try:
        db=client.EmployeeData
        criteria=input("\nEnter id to update :\n")
        name=input("\nEnter name to update :\n")
        age=input("\nEnter age to update :\n")
        country=input("\nEnter country to update :\n")        
        db.Employee.update_one(
                {"id":criteria},
                {"$set":{
                        "name":name,
                        "age":age,
                        "country":country}
                        })
        print("\nRecords updated successfully\n")
    except Exception as e:
        print(str(e))
        
def delete():
    try:
        db=client.EmployeeData
        criteria = input("Enter Employee-Id to Delete :")
        db.Employee.delete_many({"Id":criteria})
        print("Deletion successfull.\n")
    except Exception as e:
        print(str(e))
                       
        
        
    
from pymongo import MongoClient
client=MongoClient('localhost:27017')
print("connection done.")    


while(True):
    selection=input("\n1.Insert Employee Data \n2.Update Employee Data\n3.View Employee Data \n4.Delete Employee Data :")
    
    if selection=="1":
        insert()
    elif selection=="2":
        update()
    elif selection=="3":
        read()
    elif selection=="4":
        delete()
    else:
        print("\n INVALID SELECTION \n")   