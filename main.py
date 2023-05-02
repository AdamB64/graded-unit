from guizero import *
from openpyxl import Workbook
import openpyxl
wb = openpyxl.load_workbook('users.xlsx')
ws=wb.active
c=ws.cell(row=1,column=3).value
if c==None:
    c=0
app=App(title="Budget Planner")
app2=Window(app,title="Sign up")
app3=Window(app,title="Login")
app4=Window(app,title="error",height=50,width=300)    
app5=Window(app,title="Error",height=50,width=300)
app6=Window(app,title="Logged in")
app7=Window(app,title="Income")

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
    t8.append(text=tb3.value)
    t8.hide()
    c1=0
    c2=False
    c3=0
    c4=False
    count=0
    count2=0
    for row_pow2 in range(1,ws.max_row+1):
            c1=count
            col=ws.cell(row=row_pow2,column=1).value
            if col==tb3.value:
                c2=True
                count=count+1
            elif col!=tb3.value or (col==None or col==""):
                c2=False
    for row_pow3 in range(1,ws.max_row+1):
        col2=ws.cell(row=row_pow3,column=2).value
        c3=count2
        if col2==tb4.value:
            c4=True
            count2=count2+2887
    if(c1==c3) and (c2==True)and (c4==True):
        app6.show()
        app3.hide()


def incomescreen():
    app6.hide()
    app7.show()

def income():
    c1=0
    c2=0
    c3=0
    wb2=openpyxl.load_workbook(t8.value+".xlsx")
    ws2=wb2.active
    for row_p in range(1,ws.max_row+1):
        A=ws2.cell(row=row_p,column=1).value
        B=ws2.cell(row=row_p,column=2).value
        C=ws2.cell(row=row_p,column=3).value
        if (A==None or A=="") and c1==0:
            ws2.cell(row=row_p,column=1,value=tb5.value)
            c1=+1
        if (B==None or B=="") and c2==0:
            ws2.cell(row=row_p,column=2,value=tb6.value)
            c2=+1
        if (C==None or C=="") and c3==0:
            ws2.cell(row=row_p,column=3,value=tb7.value)
            c3=+1
    wb2.save(t8.value+".xlsx")

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
t6=Text(app4,text="password or user name must be filled in ")
tb5=PushButton(app4,text="Ok",command=signUp)
t7=Text(app5,text="Username is in use")
tb6=PushButton(app5,text="Ok",command=signUp)
exit4=PushButton(app6,text="Exit",command=close)
t9=Text(app7)
b4=PushButton(app6,text="add income",command=incomescreen)
t8=Text(app6)
t10=Text(app7,text="you should type in the amount of income \ngotten and when you got it \nand if you want a description")
t11=Text(app7,text="income")
tb5=TextBox(app7)
t12=Text(app7,text="Date")
tb6=TextBox(app7)
t13=Text(app7,text="Description")
tb7=TextBox(app7)
add=PushButton(app7,text="Add the income",command=income)
exit5=PushButton(app7,text="Exit",command=close)
app5.hide()
app6.hide()
app7.hide()
app4.hide()
app2.hide()
app3.hide()
app.display()