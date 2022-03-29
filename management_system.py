# -*- coding: utf-8 -*-
"""
Created on Mon Feb 21 17:43:23 2022

@author: Diwanshu & Shaurya
"""

from tkinter import *
import sqlite3
import tkinter as tk
from tkinter import messagebox
var1=[1,2]
var2=[3,4,5,6]
var3=[7,8]

r = tk.Tk()
r.configure(background='light blue')
r.title('AIRPORT MANAGMENT SYSTEM')

con=sqlite3.connect('DBMS447_473.db')

t1=StringVar()
t2=StringVar()
t3=StringVar()
t4=IntVar()
t5=IntVar()
t6=StringVar()
t7=IntVar()
t8=IntVar()
t9=StringVar()
t10=IntVar()
t11=IntVar()
t12=IntVar()
t16=IntVar()

def database():
    ln=t1.get()
    fn=t2.get()
    sw=t3.get()
    bno=t4.get()
    mno=t5.get()
    email=t6.get()
    doa=t7.get()
    dod=t8.get()
    nocc=t9.get()
    ccno=t10.get()
    expd=t11.get()
    cvv=t12.get()
    total=t16.get()

    db_447_473 = sqlite3.connect('DBMS447_473.db')
    cursor447_473=db_447_473.cursor()
    cursor447_473.execute('CREATE TABLE IF NOT EXISTS HOTBOOK(t1 TEXT,t2 TEXT,t3 INT,t4 INT,t5 INT,t6 TEXT,t7 INT,t8 INT,t9 TEXT,t10 INT,t11 INT,t12 INT,t16 INT)')
    cursor447_473.execute('INSERT INTO HOTBOOK(t1,t2,t3,t4,t5,t6,t7,t8,t9,t10,t11,t12,t16) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)',(ln,fn,sw,bno,mno,email,doa,dod,nocc,ccno,expd,cvv,total))
    db_447_473.commit()
    msg = messagebox.showinfo( "DB Demo","SUBMITTED SUCCESSFULLY")

def display():
    db_447_473=sqlite3.connect('DBMS447_473.db')
    with db_447_473:
        cursor447_473=db_447_473.cursor()
        my447_473=tk.Tk()
        my447_473.geometry("1400x500")

        r_set447_473=cursor447_473.execute('''SELECT * from HOTBOOK ''');
        i=0
        for HOTBOOK in r_set447_473:
            for j in range(len(HOTBOOK)):
                e = Entry(my447_473, width=10, fg='blue') 
                e.grid(row=i, column=j) 
                e.insert(END, HOTBOOK[j])
            i=i+1

def delete():
    a1=tk.Entry(r)
    cursor447_473=con.execute("DELETE FROM HOTBOOK ;")
    print("Deleted  All Record")

l1=tk.Label(r,text="TICKET BOOKING")
l1.grid(row=0 ,column=1)
l1.configure(background='light blue')

l2=tk.Label(r,text="First Name")
l2.grid(row=1)
l2.configure(background='light blue')
t2=tk.Entry(r)
t2.grid(row=1,column=1)
l3=tk.Label(r,text="Last Name")
l3.grid(row=2)
l3.configure(background='light blue')
t3=tk.Entry(r)
t3.grid(row=2,column=1)
l4=tk.Label(r,text="Mobile Number")
l4.grid(row=3)
l4.configure(background='light blue')
t4=tk.Entry(r)
t4.grid(row=3,column=1)
l5=tk.Label(r,text="Journey From")
l5.grid(row=4)
l5.configure(background='light blue')
t5=tk.Entry(r)
t5.grid(row=4,column=1)
l6=tk.Label(r,text="Journey To")
l6.grid(row=5)
l6.configure(background='light blue')
t6=tk.Entry(r)
t6.grid(row=5,column=1)
l7=tk.Label(r,text="Date of Arrival")
l7.grid(row=6)
l7.configure(background='light blue')
t7=tk.Entry(r)
t7.grid(row=6,column=1)
l8=tk.Label(r,text="Date of Departure")
l8.grid(row=7)
l8.configure(background='light blue')
t8=tk.Entry(r)
t8.grid(row=7,column=1)

l13=tk.Label(r,text="Payment through")
l13.grid(row=8)
l13.configure(background='light blue')
r13=tk.Radiobutton(r,text="Credit Card",variable=var1,value=1)
r13.grid(row=8,column=1)
r13.configure(background='yellow')
r13=tk.Radiobutton(r,text="Direct Bank Transfer",variable=var1,value=2)
r13.grid(row=8,column=2)
r13.configure(background='yellow')

l9=tk.Label(r,text="Name on Credit Card")
l9.grid(row=9)
l9.configure(background='light blue')
t9=tk.Entry(r)
t9.grid(row=9,column=1)
l10=tk.Label(r,text="Credit Card Number")
l10.grid(row=10)
l10.configure(background='light blue')
t10=tk.Entry(r)
t10.grid(row=10,column=1)
l11=tk.Label(r,text="Expiry Date")
l11.grid(row=11)
l11.configure(background='light blue')
t11=tk.Entry(r)
t11.grid(row=11,column=1)
l12=tk.Label(r,text="CVV Number")
l12.grid(row=12)
l12.configure(background='light blue')
t12=tk.Entry(r)
t12.grid(row=12,column=1)


l15=tk.Label(r,text="Seat Preference:")
l15.grid(row=18)
l15.configure(background='light blue')
r15=tk.Radiobutton(r,text="Window Side",variable=var3,value=7)
r15.grid(row=19,column=1)
r15.configure(background='yellow')
r15=tk.Radiobutton(r,text="No Choice",variable=var3,value=8)
r15.grid(row=19,column=2)
r15.configure(background='yellow')
l16=tk.Label(r,text="Grand total = ")
l16.grid(row=21)
l16.configure(background='light blue')
t16=tk.Entry(r)
t16.grid(row=21,column=1)
l17=tk.Label(r,text="Do you confirm your booking?")
l17.grid(row=23)
l17.configure(background='light blue')
b17=tk.Button(r,text="Yes, save it",command=database)
b17.grid(row=23,column=1)
b17.configure(background='light green')
b18=tk.Button(r,text="No, leave this window",command=r.destroy)
b18.grid(row=23,column=2)
b18.configure(background='light green')
msg=tk.Button(r,text="Show bookings",command=display).grid(row=25)
msg2=tk.Button(r,text="Delete entries",command=delete).grid(row=26)
msg3=tk.Button(r,text="Update").grid(row=27)
r.mainloop()
