from guizero import *
from openpyxl import Workbook
import openpyxl
wb = openpyxl.load_workbook('users.xlsx')
ws=wb.active
user=None
c=ws.cell(row=1,column=3).value
if c==None:
    c=0
app=App(title="Budget Planner")
app2=Window(app,title="Sign up")
app3=Window(app,title="Login")
app4=Window(app,title="error")    
app5=Window(app,title="Error")

def signUp():
    app4.hide()
    app.hide()
    app2.show()
    app5.hide()
def saved():
    global c
    c=ws.cell(row=1,column=3).value
    if c==None:
        c=1
    global user
    count=0
    tr=False
    if tb1.value=="" or tb2.value=="":
        app2.hide()
        app4.show()
    while count<1:
        for row_pow in range(1,ws.max_row+1):
            b=ws.cell(row=row_pow,column=1).value
            if tb1.value==b:
                app2.hide()
                app5.show()
                count=1
                tr=True
        count=1
    if (tb1.value!="" and tb2.value!="") and tr==False:
        user=tb1.value
        ws.cell(row=c,column=1,value=tb1.value)
        ws.cell(row=c,column=2,value=tb2.value)
        c=c+1
        ws.cell(row=1,column=3,value=c)
        wb.save('users.xlsx')
        wb2=openpyxl.Workbook(tb1.value+".xlsx")
        wb2.save(tb1.value+".xlsx")
def close():
    global c
    c=ws.cell(row=1,column=3).value
    if c==None:
        c=1
    row_position = 1
    for row_position in range(1, ws.max_row+1):
        print(ws.cell(row=row_position,column=1).value)
        print(c)
    ws.cell(row=1,column=3,value=c)
    wb.save('users.xlsx')
    exit()

def home():
    app2.hide()
    app3.hide()
    app.show()

def loginScreen():
    app.hide()
    app2.hide()
    app3.show()
    

def login():
    c1=0
    c2=False
    c3=0
    c4=False
    count=0
    count2=0
    global user
    user=tb3.value
    ws=wb.active
    for row in ws['A']:
            c1=count
            if row.value == tb3.value:
                c2=True
                count=count+1
            elif row.value!=tb3.value or (row.value==None or row.value==""):
                c2=True
    for row in ws["B"]:
        c3=count2
        if row.value==tb4.value:
            c4=True
        count2=count2+1
    if(c1==c3) and (c2==c4):
        print("yes")

t1=Text(app,text="Do you have an account")
b1=PushButton(app,text="I do not have a account and would like to join",command=signUp)
b2=PushButton(app,text="i have an acount and would like to log in",command=loginScreen)
exits=PushButton(app,text="Exit",command=close)
t2=Text(app2,text="Type the user nane and password you would like below\nUsername")
tb1=TextBox(app2)
t3=Text(app2,text="Password")
tb2=TextBox(app2)
b3=PushButton(app2,text="sign up",command=saved)
home1=PushButton(app2,text="Home screen",command=home)
log=PushButton(app2,text="login screen",command=loginScreen)
exit2=PushButton(app2,text="Exit",command=close)
t4=Text(app3,text="type in your username and password below to log in\nusername")
tb3=TextBox(app3)
t5=Text(app3,text="password")
tb4=TextBox(app3)
b3=PushButton(app3,text="login",command=login)
home2=PushButton(app3,text="Home screen",command=home)
exit3=PushButton(app3,text="Exit",command=close)
t6=Text(app4,text="password or user name muse be filled in ")
tb5=PushButton(app4,text="Ok",command=signUp)
t7=Text(app5,text="Username is in use")
tb6=PushButton(app5,text="Ok",command=signUp)
app5.hide()
app4.hide()
app2.hide()
app3.hide()
app.display()