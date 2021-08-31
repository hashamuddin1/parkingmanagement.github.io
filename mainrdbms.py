import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="hashamsql",
    database="rdbms"
    )
print(mydb)

mycursor=mydb.cursor()


#mycursor.execute("create table employee11 (employee_name VARCHAR(20),employee_id VARCHAR(20),cnic_number varchar(35),date_of_joining date,salary int,duty_status VARCHAR(20),primary key(employee_id))")

#mycursor.execute("create table customer11 (customer_name VARCHAR(20),customer_id VARCHAR(20),cnic_number varchar(35),slip_no varchar(20),amount int,primary key(customer_id))")

#mycursor.execute("create table vehicle11 (owner_name VARCHAR(20),vehicle_id VARCHAR(20),number_plate varchar(35),vehicle_type varchar(20),color VARCHAR(20),primary key(vehicle_id))")

#mycursor.execute("create table challan11 (challan_id VARCHAR(20),owner_name varchar(35),amount int,date_of_issue date,primary key(challan_id))")

#mycursor.execute("create table contact11 (contact_number VARCHAR(20),sim_name varchar(35),another_contact varchar(30),person varchar(20))")

#mycursor.execute("create table parking11 (parking_name VARCHAR(20),parking_id varchar(35),location varchar(30),primary key(parking_id))")




from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
from tkhtmlview import HTMLLabel
import tkinter.font as font
from tkinter import ttk
from tkinter import colorchooser
import time

#import tkFont

root=Tk()
root.geometry("1340x680+0+0")
root.title("PARKING MANAGEMENT INSTITUDE")
my_label1 = Label(root, text="""WELCOME TO PARKING SYSTEM\n\nCREATED BY:\n\nMARIUM NASIR\n\nBI BI MARIUM""",font=("comicsansms",19,"bold"),fg="white",bg="grey",padx=40,pady=233)
#my_label=font=("comicsansms",19,"bold")
my_label1.pack()
my_label1.place(x=0,y=0)


#def update():
#    ml.config(text="D")
#ml=Label(root,text="R")
#ml.pack()
#ml.after(3000,update)
  
# Adjust label
def clock():
    hour=time.strftime("%I")
    minute=time.strftime("%M")
    second=time.strftime("%S")
    am_pm=time.strftime("%p")
    ml.config(text=hour + ":" + minute + ":" + second + " " + am_pm)
    ml.after(1000,clock)

ml=Label(root,text="",font=("Helvetica",48),fg="green",bg="black")
ml.pack(pady=10)
ml.place(x=700,y=0)

clock()
    

"""
import cv2
capture=cv2.VideoCapture(0)

if capture.isOpened():
    ret,frame=capture.read()
    cv2.imwrite("osman1.jpg",frame)

l=cv2.imread("osman1.jpg")

aaa=0
while aaa<=0:
    aaa+=1
    #cv2.imshow("window",l)
    if cv2.waitKey()=="q":
        break

capture.release()
cv2.destroyAllWindows()
"""

def call_me1():
    window=Tk()
    window.title("EMPLOYEE FORM")
    window.geometry("1340x680+0+0")
    window.configure(bg="grey")
    b=Label(window,text="EMPLOYEE NAME")
    b.place(x=10,y=120)
    c=Label(window,text="EMPLOYEE ID")
    c.place(x=10,y=160)
    d=Label(window,text="CNIC NUMBER")
    d.place(x=10,y=200)
    e=Label(window,text="JOINING DATE")
    e.place(x=10,y=240)
    f=Label(window,text="SALARY")
    f.place(x=10,y=280)
    g=Label(window,text="DUTY STATUS")
    g.place(x=10,y=320)
    """
    h=Label(window,text="WAY OF PAYMENT")
    h.place(x=10,y=520)
    i=Label(window,text="AMOUNT OF PAYMENT")
    i.place(x=10,y=560)
    j=Label(window,text="NUMBER OF TICKET")
    j.place(x=10,y=440)
    k=Label(window,text="ADDRESS")
    k.place(x=10,y=480)
    """
    b_entry=Entry(window)
    b_entry.place(x=150,y=120)
    c_entry=Entry(window)
    c_entry.place(x=150,y=160)
    d_entry=Entry(window)
    d_entry.place(x=150,y=200)
    e_entry=Entry(window)
    e_entry.place(x=150,y=240)
    f_entry=Entry(window)
    f_entry.place(x=150,y=280)
    g_entry=Entry(window)
    g_entry.place(x=150,y=320)
    """
    h_entry=Entry(window)
    h_entry.place(x=150,y=520)
    i_entry=Entry(window)
    i_entry.place(x=150,y=560)
    j_entry=Entry(window)
    j_entry.place(x=150,y=440)
    k_entry=Entry(window)
    k_entry.place(x=150,y=480)
    m=StringVar(window)
    m.set("           SELECT THE TRAIN")
    l=OptionMenu(window,m,"SHALIMAR EXPRESS","LAHORE EXPRESS","TEEZ GAM","AWAM EXPRESS","RAWALPINDI EXPRESS")
    l.pack()
    l.place(x=80,y=248)
    """
    #employee_name employee_id cnic_number date_of_joining salary duty_status 

    def save_info():
        try:
            sql = "INSERT INTO employee11(employee_name,employee_id,cnic_number,date_of_joining,salary,duty_status) VALUES (%s,%s,%s,%s,%s,%s)"
            val = (b_entry.get(),c_entry.get(),d_entry.get(),e_entry.get(),f_entry.get(),g_entry.get())
            mycursor.execute(sql, val)
            mydb.commit()
            print(mycursor.rowcount, "record inserted.")
        except Exception as e:
            p=Label(window,text=e)
            p.place(x=80,y=600)
            p.pack()
    q=Button(window,text="SUMBIT",width="25",fg="white",bg="blue",command=save_info)
    q.pack()
    q.place(x=70,y=400)
    def sql1():
        sql_a=Tk()
        sql_a.title("VIEW")
        sql_a.geometry("1340x680+0+0")
        
        import mysql.connector
        mydb=mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="hashamsql",
            database="rdbms"
            )
        print(mydb)
        cursor=mydb.cursor()
        import tkinter as tk
        from tkinter import ttk
        sql="SELECT * FROM employee11 where salary>80000"
        cursor.execute(sql)
        rows=cursor.fetchall()
        frn=Frame(sql_a)
        frn.pack(side=tk.LEFT,padx=0)
        tv=ttk.Treeview(frn,columns=(1,2,3,4,5,6),show="headings",height="26")
        tv.pack()
        #employee_name employee_id cnic_number date_of_joining salary duty_status
        tv.heading(1,text="EMPLOYEE NAME")
        tv.heading(2,text="EMPLOYEE ID")
        tv.heading(3,text="CNIC NUMBER")
        tv.heading(4,text="DATE OF JOINING")
        tv.heading(5,text="SALARY")
        tv.heading(6,text="DUTY STATUS")
        for i in rows:
            tv.insert("",'end',values=i)
        hor_scroll=ttk.Scrollbar(frn,orient="horizontal",command=tv.xview)
        hor_scroll.pack(side=BOTTOM,fill=X)
        tv.config(xscrollcommand=hor_scroll)
        
    buttonFont = font.Font(family='Helvetica', size=26, weight='bold')
    bbb=Button(window,text="     VIEW    ",command=sql1,font=buttonFont)
    bbb.pack()
    bbb.place(x=500,y=100)
    def sql50():
        sql_a=Tk()
        sql_a.title("VIEW")
        sql_a.geometry("1340x680+0+0")
        
        import mysql.connector
        mydb=mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="hashamsql",
            database="rdbms"
            )
        print(mydb)
        cursor=mydb.cursor()
        import tkinter as tk
        from tkinter import ttk
        sql="SELECT * FROM employee11"
        cursor.execute(sql)
        rows=cursor.fetchall()
        frn=Frame(sql_a)
        frn.pack(side=tk.LEFT,padx=0)
        tv=ttk.Treeview(frn,columns=(1,2,3,4,5,6),show="headings",height="26")
        tv.pack()
        #employee_name employee_id cnic_number date_of_joining salary duty_status
        tv.heading(1,text="EMPLOYEE NAME")
        tv.heading(2,text="EMPLOYEE ID")
        tv.heading(3,text="CNIC NUMBER")
        tv.heading(4,text="DATE OF JOINING")
        tv.heading(5,text="SALARY")
        tv.heading(6,text="DUTY STATUS")
        for i in rows:
            tv.insert("",'end',values=i)
        hor_scroll=ttk.Scrollbar(frn,orient="horizontal",command=tv.xview)
        hor_scroll.pack(side=BOTTOM,fill=X)
        tv.config(xscrollcommand=hor_scroll)
        
    buttonFont = font.Font(family='Helvetica', size=26, weight='bold')
    bbb=Button(window,text="     ALL    ",command=sql50,font=buttonFont)
    bbb.pack()
    bbb.place(x=500,y=300)




buttonFont = font.Font(family='Helvetica', size=26, weight='bold')
b=Button(root,text="   EMPLOYEE  ",command=call_me1,font=buttonFont,bg="grey",fg="white")
b.pack()
b.place(x=550,y=100)

def call_me2():
    window1=Tk()
    window1.geometry("1340x680+0+0")
    window1.title("CUSTOMER FORM")
    window1.configure(bg="grey")
    bemp=Label(window1,text="CUSTOMER NAME")
    bemp.place(x=10,y=120)
    cemp=Label(window1,text="CUSTOMER ID")
    cemp.place(x=10,y=160)
    demp=Label(window1,text="CNIC NUMBER")
    demp.place(x=10,y=200)
    eemp=Label(window1,text="SLIP NUMBER")
    eemp.place(x=10,y=240)
    femp=Label(window1,text="AMOUNT")
    femp.place(x=10,y=280)
    """
    gemp=Label(window1,text="SALARY")
    gemp.place(x=10,y=400)
    hemp=Label(window1,text="FATHER NAME")
    hemp.place(x=10,y=520)
    iemp=Label(window1,text="DATE OF BIRTH")
    iemp.place(x=10,y=560)
    jemp=Label(window1,text="JOINING DATE")
    jemp.place(x=10,y=440)
    kemp=Label(window1,text="ADDRESS")
    kemp.place(x=10,y=480)
    """
    bemp_entry=Entry(window1)
    bemp_entry.place(x=150,y=120)
    cemp_entry=Entry(window1)
    cemp_entry.place(x=150,y=160)
    demp_entry=Entry(window1)
    demp_entry.place(x=150,y=200)
    eemp_entry=Entry(window1)
    eemp_entry.place(x=150,y=240)
    femp_entry=Entry(window1)
    femp_entry.place(x=150,y=280)
    #gemp_entry=Entry(window1)
    """
    gemp_entry.place(x=150,y=400)
    hemp_entry=Entry(window1)
    hemp_entry.place(x=150,y=520)
    iemp_entry=Entry(window1)
    iemp_entry.place(x=150,y=560)
    jemp_entry=Entry(window1)
    jemp_entry.place(x=150,y=440)
    kemp_entry=Entry(window1)
    kemp_entry.place(x=150,y=480)




    memp=StringVar(window1)
    memp.set("           SELECT THE DEPARTMENT")
    lemp=OptionMenu(window1,memp,"ACCOUNTS","MANUFACTURING","SALES","REPAIRING","FINANCIAL")
    lemp.pack()
    lemp.place(x=80,y=248)

#mycursor.execute("create table employee (first_name VARCHAR(20),last_name VARCHAR(20),mobile varchar(20),department varchar(20),email varchar(35),employee_id varchar(15),salary int,joining_date date,address VARCHAR(30),father_name varchar(25),date_of_birth date,primary key(employee_id))")
"""
    #mycursor.execute("create table customer11 (customer_name VARCHAR(20),customer_id VARCHAR(20),cnic_number varchar(35),slip_no varchar(20),amount int,primary key(customer_id))")

    def save_info1():
        try:
            sql = "INSERT INTO customer11(customer_name,customer_id ,cnic_number,slip_no,amount) VALUES (%s,%s,%s,%s,%s)"
            val = (bemp_entry.get(),cemp_entry.get(),demp_entry.get(),eemp_entry.get(),femp_entry.get())
            mycursor.execute(sql, val)
            mydb.commit()
            print(mycursor.rowcount, "record inserted.")
        except Exception as e:
            p=Label(window1,text=e)
            p.place(x=80,y=600)
            p.pack()

    q=Button(window1,text="SUMBIT",fg="white",bg="blue",width="25",command=save_info1)
    q.pack()
    q.place(x=70,y=400)
    def sql3():
        sql_a=Tk()
        sql_a.title("VIEW")
        sql_a.geometry("1340x680+0+0")
        
        import mysql.connector
        mydb=mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="hashamsql",
            database="rdbms"
            )
        print(mydb)
        cursor=mydb.cursor()
        import tkinter as tk
        from tkinter import ttk
        sql="SELECT * FROM customer11"
        cursor.execute(sql)
        rows=cursor.fetchall()
        frn=Frame(sql_a)
        frn.pack(side=tk.LEFT,padx=0)
        tv=ttk.Treeview(frn,columns=(1,2,3,4,5),show="headings",height="26")
        tv.pack()
        tv.heading(1,text="CUSTOMER NAME")
        tv.heading(2,text="CUSTOMER ID")
        tv.heading(3,text="CNIC NUMBER")
        tv.heading(4,text="SLIP NUMBER")
        tv.heading(5,text="AMOUNT")
        
        for i in rows:
            tv.insert("",'end',values=i)
        hor_scroll=ttk.Scrollbar(frn,orient="horizontal",command=tv.xview)
        hor_scroll.pack(side=BOTTOM,fill=X)
        tv.config(xscrollcommand=hor_scroll)
        
    buttonFont = font.Font(family='Helvetica', size=26, weight='bold')
    bbb=Button(window1,text="     VIEW    ",command=sql3,font=buttonFont)
    bbb.pack()
    bbb.place(x=500,y=100)
    def sql3():
        
        
        import mysql.connector
        mydb=mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="hashamsql",
            database="rdbms"
            )
        print(mydb)
        cursor=mydb.cursor()
        import tkinter as tk
        from tkinter import ttk
        sql="TRUNCATE customer11"
        cursor.execute(sql)
      
    buttonFont = font.Font(family='Helvetica', size=26, weight='bold')
    bbb=Button(window1,text="     DELETE RECORD    ",command=sql3,font=buttonFont)
    bbb.pack()
    bbb.place(x=1000,y=100)



buttonFont = font.Font(family='Helvetica', size=26, weight='bold')
c=Button(root,text="  CUSTOMER  ",command=call_me2,font=buttonFont,bg="grey",fg="white")
c.pack()
c.place(x=550,y=220)

def call_me3():
    window2=Tk()
    window2.geometry("1340x680+0+0")
    window2.title("VEHICLE FORM")
    window2.configure(bg="grey")

    
    btra=Label(window2,text="OWNER NAME")
    btra.place(x=10,y=120)
    ctra=Label(window2,text="VEHICLE ID")
    ctra.place(x=10,y=160)
    dtra=Label(window2,text="NUMBER PLATE")
    dtra.place(x=10,y=200)
    etra=Label(window2,text="VEHICLE TYPE")
    etra.place(x=10,y=240)
    ftra=Label(window2,text="COLOR")
    ftra.place(x=10,y=280)
    """
    gtra=Label(window2,text="STATION ID")
    gtra.place(x=10,y=400)
    htra=Label(window2,text="NEXT JOURNEY")
    htra.place(x=10,y=520)
    itra=Label(window2,text="RECENT JOURNEY")
    itra.place(x=10,y=560)
    jtra=Label(window2,text="NUMBER OF STATIONS")
    jtra.place(x=10,y=440)
    ktra=Label(window2,text="FAULT")
    ktra.place(x=10,y=480)
    """

    btra_entry=Entry(window2)
    btra_entry.place(x=150,y=120)
    ctra_entry=Entry(window2)
    ctra_entry.place(x=150,y=160)
    dtra_entry=Entry(window2)
    dtra_entry.place(x=150,y=200)
    etra_entry=Entry(window2)
    etra_entry.place(x=150,y=240)
    ftra_entry=Entry(window2)
    ftra_entry.place(x=150,y=280)
    
        
    """
    ftra_entry=Entry(window2)
    ftra_entry.place(x=150,y=360)
    gtra_entry=Entry(window2)
    gtra_entry.place(x=150,y=400)
    htra_entry=Entry(window2)
    htra_entry.place(x=150,y=520)
    itra_entry=Entry(window2)
    itra_entry.place(x=150,y=560)
    jtra_entry=Entry(window2)
    jtra_entry.place(x=150,y=440)
    ktra_entry=Entry(window2)
    ktra_entry.place(x=150,y=480)


    mtra=StringVar(window2)
    mtra.set("           SELECT THE ROUTE OF TRAIN")
    ltra=OptionMenu(window2,mtra,"KARACHI TO LAHORE","LAHORE TO PINDI","PINDI TO MULTAN","MULTAN TO QUETTA","QUETTA TO FAISLABAD")
    ltra.pack()
    ltra.place(x=80,y=248)
    """
   


    def save_info2():
        try:
            sql = "INSERT INTO vehicle11(owner_name,vehicle_id,number_plate,vehicle_type,color) VALUES (%s, %s,%s,%s,%s)"
            val = (btra_entry.get(),ctra_entry.get(),dtra_entry.get(),etra_entry.get(),ftra_entry.get())
            mycursor.execute(sql, val)
            mydb.commit()
            print(mycursor.rowcount, "record inserted.")
        except Exception as e:
            p=Label(window2,text=e)
            p.place(x=80,y=600)
            p.pack()

    q=Button(window2,text="SUMBIT",fg="white",bg="blue",width="25",command=save_info2)
    q.pack()
    q.place(x=70,y=400)

    def sql4():
        sql_a=Tk()
        sql_a.title("VIEW")
        sql_a.geometry("1340x680+0+0")
        
        import mysql.connector
        mydb=mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="hashamsql",
            database="rdbms"
            )
        print(mydb)
        cursor=mydb.cursor()
        import tkinter as tk
        from tkinter import ttk
        sql="SELECT count(*),vehicle_type FROM vehicle11 group by vehicle_type"
        cursor.execute(sql)
        rows=cursor.fetchall()
        frn=Frame(sql_a)
        frn.pack(side=tk.LEFT,padx=0)
        tv=ttk.Treeview(frn,columns=(1,2),show="headings",height="26")
        tv.pack()
        tv.heading(1,text="TOTAL NUMBER")
        tv.heading(2,text="VEHICLE TYPE")
        
        
        for i in rows:
            tv.insert("",'end',values=i)
        hor_scroll=ttk.Scrollbar(frn,orient="horizontal",command=tv.xview)
        hor_scroll.pack(side=BOTTOM,fill=X)
        tv.config(xscrollcommand=hor_scroll)
        
    buttonFont = font.Font(family='Helvetica', size=26, weight='bold')
    bbb=Button(window2,text="     VIEW    ",command=sql4,font=buttonFont)
    bbb.pack()
    bbb.place(x=500,y=100)





buttonFont = font.Font(family='Helvetica', size=26, weight='bold')
d=Button(root,text="    VEHICLE     ",command=call_me3,font=buttonFont,bg="grey",fg="white")
d.pack()
d.place(x=550,y=340)

def call_me4():
    window4=Tk()
    window4.geometry("1340x680+0+0")
    window4.title("INVENTORY FORM")
    window4.configure(bg="grey")

            
    b=Label(window4,text="INVENTORY NAME")
    b.place(x=10,y=120)
    c=Label(window4,text="INVENTORY ID")
    c.place(x=10,y=160)
    d=Label(window4,text="STATION ID")
    d.place(x=10,y=200)
    e=Label(window4,text="NUMBER OF MATERIAL")
    e.place(x=10,y=320)
    f=Label(window4,text="ITEM ID")
    f.place(x=10,y=360)

    g=Label(window4,text="MODIFIED DATE")
    g.place(x=10,y=400)


    b_entry=Entry(window4)
    b_entry.place(x=170,y=120)
    c_entry=Entry(window4)
    c_entry.place(x=170,y=160)
    d_entry=Entry(window4)
    d_entry.place(x=170,y=200)
    e_entry=Entry(window4)
    e_entry.place(x=170,y=320)
    f_entry=Entry(window4)
    f_entry.place(x=170,y=360)
    g_entry=Entry(window4)
    g_entry.place(x=170,y=400)


    k=StringVar(window4)
    k.set("           PRODUCT NEEDED")
    j=OptionMenu(window4,k,"STEEL","CONTAINER","FIRE EXTINGUISHERS","CHAIN","NONE")
    j.pack()
    j.place(x=80,y=250)
#mycursor.execute("create table inventory (inventory_name,inventory_id ,station_id,product_needed ,no_of_material ,item_id,modified_date date
    def save_info():
        try:
            sql = "INSERT INTO inventory1 (inventory_name,inventory_id,station_id,product_needed,no_of_material,item_id,modified_date) VALUES (%s,%s,%s,%s,%s,%s,%s)"
            val = (b_entry.get(),c_entry.get(),d_entry.get(),k.get(),e_entry.get(),f_entry.get(),g_entry.get())
            mycursor.execute(sql, val)
            mydb.commit()
            print(mycursor.rowcount, "record inserted.")
        except Exception as e:
            p=Label(window4,text=e)
            p.place(x=80,y=600)
            p.pack()
   
    q=Button(window4,text="SUMBIT",fg="white",bg="blue",width="25",command=save_info)
    q.pack()
    q.place(x=70,y=610)

    def sql5():
        sql_a=Tk()
        sql_a.title("VIEW")
        sql_a.geometry("1340x680+0+0")
        
        import mysql.connector
        mydb=mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="hashamsql",
            database="railwaystation"
            )
        print(mydb)
        cursor=mydb.cursor()
        import tkinter as tk
        from tkinter import ttk
        sql="SELECT * FROM inventory1"
        cursor.execute(sql)
        rows=cursor.fetchall()
        frn=Frame(sql_a)
        frn.pack(side=tk.LEFT,padx=0)
        tv=ttk.Treeview(frn,columns=(1,2,3,4,5,6,7),show="headings",height="26")
        tv.pack()
        tv.heading(1,text="INVENTORY NAME")
        tv.heading(2,text="INVENTORY ID")
        tv.heading(3,text="STATION ID")
        tv.heading(4,text="PRODUCT NEEDED")
        tv.heading(5,text="NUMBER OF MATERIAL")
        tv.heading(6,text="ITEM ID")
        tv.heading(7,text="MODIFIED DATE")

        for i in rows:
            tv.insert("",'end',values=i)
        hor_scroll=ttk.Scrollbar(frn,orient="horizontal",command=tv.xview)
        hor_scroll.pack(side=BOTTOM,fill=X)
        tv.config(xscrollcommand=hor_scroll)
        
    buttonFont = font.Font(family='Helvetica', size=26, weight='bold')
    bbb=Button(window4,text="    VIEW  ",command=sql5,font=buttonFont)
    bbb.pack()
    bbb.place(x=500,y=100)


    
    


#buttonFont = font.Font(family='Helvetica', size=26, weight='bold')
#e=Button(root,text="PARKING",command=call_me4,font=buttonFont)
#e.pack()
#e.place(x=100,y=460)

def call_me5():
    window5=Tk()
    window5.geometry("1340x680+0+0")
    window5.title("CHALLAN FORM")
    window5.configure(bg="grey")

    b=Label(window5,text="CHALLAN ID")
    b.place(x=10,y=120)
    c=Label(window5,text="OWNER NAME")
    c.place(x=10,y=160)
    d=Label(window5,text="AMOUNT")
    d.place(x=10,y=200)
    #k=StringVar(window5)

    #k=StringVar(window5)
    #k.set("           SELECT THE ROUTE")
    #j=OptionMenu(window5,k,"KARACHI TO LAHORE","LAHORE TO KARACHI","ISLAMABAD TO SUKKUR","LARKANA TO MULTAN","MULTAN TO FAISLABAD","SUKKUR TO HYDERABAD")
    #j.pack()
    #j.place(x=80,y=240)
    f=Label(window5,text="ISSUE DATE")
    f.place(x=10,y=240)
    """
    x=Label(window5,text="TICKET CATEGORY")
    x.place(x=10,y=340)
    y=Label(window5,text="TIMING")
    y.place(x=10,y=380)
    """


    b_entry=Entry(window5)
    b_entry.place(x=150,y=120)
    c_entry=Entry(window5)
    c_entry.place(x=150,y=160)
    d_entry=Entry(window5)
    d_entry.place(x=150,y=200)

    f_entry=Entry(window5)
    f_entry.place(x=150,y=240)
    
    """
    x_entry.place(x=150,y=340)
    y_entry=Entry(window5)
    y_entry.place(x=150,y=380)
 


#ticket_id,train_id ,issue_date,route ,payment,ticket_category ,timing
"""
    def save_info():
        sql = "INSERT INTO challan11 (challan_id,owner_name,amount,date_of_issue) VALUES (%s, %s,%s,%s)"
        val = (b_entry.get(),c_entry.get(),d_entry.get(),f_entry.get())
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "record inserted.")
    q=Button(window5,text="SUMBIT",fg="white",bg="blue",width="25",command=save_info)
    q.pack()
    q.place(x=70,y=400)

    def sql5():
        sql_a=Tk()
        sql_a.title("VIEW")
        sql_a.geometry("1340x680+0+0")
        
        import mysql.connector
        mydb=mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="hashamsql",
            database="rdbms"
            )
        print(mydb)
        cursor=mydb.cursor()
        import tkinter as tk
        from tkinter import ttk
        sql="SELECT * FROM challan11"
        cursor.execute(sql)
        rows=cursor.fetchall()
        frn=Frame(sql_a)
        frn.pack(side=tk.LEFT,padx=0)
        tv=ttk.Treeview(frn,columns=(1,2,3,4),show="headings",height="26")
        tv.pack()
        tv.heading(1,text="CHALLAN ID")
        tv.heading(2,text="OWNER NAME")
        tv.heading(3,text="AMOUNT")
        tv.heading(4,text="DATE OF ISSUE")


        for i in rows:
            tv.insert("",'end',values=i)
        hor_scroll=ttk.Scrollbar(frn,orient="horizontal",command=tv.xview)
        hor_scroll.pack(side=BOTTOM,fill=X)
        tv.config(xscrollcommand=hor_scroll)
    buttonFont = font.Font(family='Helvetica', size=26, weight='bold')
    bbb=Button(window5,text="     VIEW    ",command=sql5,font=buttonFont)
    bbb.pack()
    bbb.place(x=500,y=100)

buttonFont = font.Font(family='Helvetica', size=26, weight='bold')
f=Button(root,text="     CHALLAN      ",command=call_me5,font=buttonFont,bg="grey",fg="white")
f.pack()
f.place(x=1000,y=100)

def call_me6():
    window6=Tk()
    window6.geometry("1340x680+0+0")
    window6.title("CONTACT FORM")
    window6.configure(bg="grey")

    b=Label(window6,text="CONTACT NUMBER")
    b.place(x=10,y=120)
    c=Label(window6,text="SIM NAME")
    c.place(x=10,y=160)
    d=Label(window6,text="ANOTHER CONTACT NO")
    d.place(x=10,y=200)
    k=StringVar(window6)

    k=StringVar(window6)
    k.set("           SELECT THE PERSON")
    j=OptionMenu(window6,k,"CUSTOMER","MANAGER","EMPLOYEE","OTHER")
    j.pack()
    j.place(x=80,y=250)
    """
    e=Label(window6,text="CUSTOMER ID")
    e.place(x=10,y=240)
    f=Label(window6,text="RECEIVING DATE")
    f.place(x=10,y=280)
    g=Label(window6,text="WAY OF PAYMENT")
    g.place(x=10,y=320)
    """

    b_entry=Entry(window6)
    b_entry.place(x=170,y=120)
    c_entry=Entry(window6)
    c_entry.place(x=170,y=160)
    d_entry=Entry(window6)
    d_entry.place(x=170,y=200)
    """
    e_entry=Entry(window6)
    e_entry.place(x=170,y=240)
    f_entry=Entry(window6)
    f_entry.place(x=170,y=280)
    g_entry=Entry(window6)
    g_entry.place(x=170,y=320)
#payment_id,payment_date,tax,customer_id,receiving_date,way_of_payment
"""
    



    def save_info():
        sql = "INSERT INTO contact11 (contact_number,sim_name,another_contact,person) VALUES (%s, %s,%s,%s)"
        val = (b_entry.get(),c_entry.get(),d_entry.get(),k.get())
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "record inserted.")
    q=Button(window6,text="SUMBIT",fg="white",bg="blue",width="25",command=save_info)
    q.pack()
    q.place(x=70,y=400)

    def sql6():
        sql_a=Tk()
        sql_a.title("VIEW")
        sql_a.geometry("1340x680+0+0")
        
        import mysql.connector
        mydb=mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="hashamsql",
            database="rdbms"
            )
        print(mydb)
        cursor=mydb.cursor()
        import tkinter as tk
        from tkinter import ttk
        sql="SELECT count(*),person FROM contact11 group by person"
        cursor.execute(sql)
        rows=cursor.fetchall()
        frn=Frame(sql_a)
        frn.pack(side=tk.LEFT,padx=0)
        tv=ttk.Treeview(frn,columns=(1,2),show="headings",height="26")
        tv.pack()
        tv.heading(1,text="TOTAL")
        tv.heading(2,text="PERSON")
        

        for i in rows:
            tv.insert("",'end',values=i)
        hor_scroll=ttk.Scrollbar(frn,orient="horizontal",command=tv.xview)
        hor_scroll.pack(side=BOTTOM,fill=X)
        tv.config(xscrollcommand=hor_scroll)
        
    buttonFont = font.Font(family='Helvetica', size=26, weight='bold')
    bbb=Button(window6,text="     VIEW    ",command=sql6,font=buttonFont)
    bbb.pack()
    bbb.place(x=500,y=100)


buttonFont = font.Font(family='Helvetica', size=26, weight='bold')
g=Button(root,text="     CONTACT      ",command=call_me6,font=buttonFont,bg="grey",fg="white")
g.pack()
g.place(x=1000,y=220)


def call_me7():
    window7=Tk()
    window7.geometry("1340x680+0+0")
    window7.title("PARKING FORM")
    window7.configure(bg="grey")

        
    b5=Label(window7,text="PARKING NAME")
    b5.place(x=10,y=120)
    c5=Label(window7,text="PARKING ID")
    c5.place(x=10,y=160)
    d5=Label(window7,text="LOCATION")
    d5.place(x=10,y=200)
    """
    e=Label(window7,text="NUMBER OF RAILWAY TRACK")
    e.place(x=10,y=320)
    f=Label(window7,text="NUMBER OF TRAIN")
    f.place(x=10,y=360)

    g=Label(window7,text="MANAGER NAME")
    g.place(x=10,y=400)
"""

    b5_entry=Entry(window7)
    b5_entry.place(x=200,y=120)
    c5_entry=Entry(window7)
    c5_entry.place(x=200,y=160)
    d5_entry=Entry(window7)
    d5_entry.place(x=200,y=200)
    """
    e_entry=Entry(window7)
    e_entry.place(x=200,y=320)
    f_entry=Entry(window7)
    f_entry.place(x=200,y=360)
    g_entry=Entry(window7)
    g_entry.place(x=200,y=400)


    k=StringVar(window7)
    k.set("           CITY")
    j=OptionMenu(window7,k,"KARACHI","LAHORE","MULTAN","QUETTA","HYDERABAD","SUKKUR","LARKANA","ISLAMABAD")
    j.pack()
    j.place(x=80,y=250)
    """
    # parking11 (parking_name,parking_id,location varchar(30),primary key(parking_id))")

    def save_info():
        try:
            sql = "INSERT INTO parking11 (parking_name,parking_id,location) VALUES (%s,%s,%s)"
            val = (b5_entry.get(),c5_entry.get(),d5_entry.get())
            mycursor.execute(sql, val)
            mydb.commit()
            print(mycursor.rowcount, "record inserted.")
        except Exception as e:
            p=Label(window7,text=e)
            p.place(x=80,y=600)
            p.pack()
   
    q=Button(window7,text="SUMBIT",fg="white",bg="blue",width="25",command=save_info)
    q.pack()
    q.place(x=70,y=400)
    def sql30():
        import mysql.connector
        mydb=mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="hashamsql",
            database="rdbms"
            )
        print(mydb)
        cursor=mydb.cursor()
        import tkinter as tk
        from tkinter import ttk
        sql="TRUNCATE parking11"
        cursor.execute(sql)
      
    buttonFont = font.Font(family='Helvetica', size=26, weight='bold')
    bbb=Button(window7,text="     DELETE PARKING    ",command=sql30,font=buttonFont)
    bbb.pack()
    bbb.place(x=1000,y=300)

    def sql7():
        sql_a=Tk()
        sql_a.title("VIEW")
        sql_a.geometry("1340x680+0+0")
        
        import mysql.connector
        mydb=mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="hashamsql",
            database="rdbms"
            )
        print(mydb)
        cursor=mydb.cursor()
        import tkinter as tk
        from tkinter import ttk
        sql="SELECT * FROM parking11"
        cursor.execute(sql)
        rows=cursor.fetchall()
        frn=Frame(sql_a)
        frn.pack(side=tk.LEFT,padx=0)
        tv=ttk.Treeview(frn,columns=(1,2,3),show="headings",height="26")
        tv.pack()
        tv.heading(1,text="PARKING NAME")
        tv.heading(2,text="PARKING ID")
        tv.heading(3,text="LOCATION")
        

        for i in rows:
            tv.insert("",'end',values=i)
        hor_scroll=ttk.Scrollbar(frn,orient="horizontal",command=tv.xview)
        hor_scroll.pack(side=BOTTOM,fill=X)
        tv.config(xscrollcommand=hor_scroll)
        
    buttonFont = font.Font(family='Helvetica', size=26, weight='bold')
    bbb=Button(window7,text="     VIEW    ",command=sql7,font=buttonFont)
    bbb.pack()
    bbb.place(x=500,y=100)


buttonFont = font.Font(family='Helvetica', size=26, weight='bold')
h=Button(root,text="    PARKING       ",command=call_me7,font=buttonFont,bg="grey",fg="white")
h.pack()
h.place(x=1000,y=340)

def call_me8():
    window8=Tk()
    window8.geometry("1340x680+0+0")
    window8.title("NEW SCHEDULE")
        
    b=Label(window8,text="TRAIN NAME")
    b.place(x=10,y=120)
    c=Label(window8,text="TRAIN ID")
    c.place(x=10,y=160)
    e=Label(window8,text="PASSENGER CAPACITY")
    e.place(x=10,y=200)
    f=Label(window8,text="JOURNEY DATE")
    f.place(x=10,y=240)

    g=Label(window8,text="TIMING")
    g.place(x=10,y=280)


    b_entry=Entry(window8)
    b_entry.place(x=200,y=120)
    c_entry=Entry(window8)
    c_entry.place(x=200,y=160)
    e_entry=Entry(window8)
    e_entry.place(x=200,y=200)
    f_entry=Entry(window8)
    f_entry.place(x=200,y=240)
    g_entry=Entry(window8)
    g_entry.place(x=200,y=280)
    k=StringVar(window8)
    k.set("           SELECT THE ROUTE")
    j=OptionMenu(window8,k,"KARACHI TO LAHORE","LAHORE TO KARACHI","ISLAMABAD TO SUKKUR","LARKANA TO MULTAN","MULTAN TO FAISLABAD","SUKKUR TO HYDERABAD")
    j.pack()
    j.place(x=80,y=320)

#train_name,train_id,route,passenger_capacity ,journey_date,timing
    def save_info():
        try:
            sql = "INSERT INTO newschedule (train_name,train_id,route,passenger_capacity ,journey_date,timing) VALUES (%s,%s,%s,%s,%s,%s)"
            val = (b_entry.get(),c_entry.get(),k.get(),e_entry.get(),f_entry.get(),g_entry.get())
            mycursor.execute(sql, val)
            mydb.commit()
            print(mycursor.rowcount, "record inserted.")
        except Exception as e:
            p=Label(window7,text=e)
            p.place(x=80,y=600)
            p.pack()
   
    q=Button(window8,text="SUMBIT",fg="white",bg="blue",width="25",command=save_info)
    q.pack()
    q.place(x=70,y=610)


    def sql8():
        sql_a=Tk()
        sql_a.title("VIEW")
        sql_a.geometry("1340x680+0+0")
        
        import mysql.connector
        mydb=mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="hashamsql",
            database="railwaystation"
            )
        print(mydb)
        cursor=mydb.cursor()
        import tkinter as tk
        from tkinter import ttk
        sql="SELECT * FROM newschedule"
        cursor.execute(sql)
        rows=cursor.fetchall()
        frn=Frame(sql_a)
        frn.pack(side=tk.LEFT,padx=0)
        tv=ttk.Treeview(frn,columns=(1,2,3,4,5,6),show="headings",height="26")
        tv.pack()
        tv.heading(1,text="TRAIN NAME")
        tv.heading(2,text="TRAIN ID")
        tv.heading(3,text="ROUTE")
        tv.heading(4,text="PASSENGER CAPACITY")
        tv.heading(5,text="JOURNEY DATE")
        tv.heading(6,text="TIMING")

        for i in rows:
            tv.insert("",'end',values=i)
        hor_scroll=ttk.Scrollbar(frn,orient="horizontal",command=tv.xview)
        hor_scroll.pack(side=BOTTOM,fill=X)
        tv.config(xscrollcommand=hor_scroll)
        
    buttonFont = font.Font(family='Helvetica', size=26, weight='bold')
    bbb=Button(window8,text="     VIEW    ",command=sql8,font=buttonFont)
    bbb.pack()
    bbb.place(x=500,y=100)

#buttonFont = font.Font(family='Helvetica', size=26, weight='bold')
#i=Button(root,text="NEW SCHEDULE",command=call_me8,font=buttonFont)
#i.pack()
#i.place(x=800,y=460)

mainloop()
