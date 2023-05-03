from guizero import *
from openpyxl import Workbook
import openpyxl
import re
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
app8=Window(app,title="Error",height=50,width=300)
app9=Window(app,title="Error",height=50,width=300)
app10=Window(app,title="Expenses")
app11=Window(app,title="Error",height=50,width=300)
app12=Window(app,title="show")
app13=Window(app,title="Error",height=50,width=300)
app14=Window(app,title="Error",height=50,width=300)


def signUp():
    app4.hide()
    app.hide()
    app2.show()
    app5.hide()
    app8.hide()

def saved():
    global c
    c=ws.cell(row=1,column=3).value
    if c==None:
        c=1
    count2=0
    count=0
    ut=False
    pt=False
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
                ut=True
        count=1
    while count2<1:
        for row_pow2 in range(1,ws.max_row+1):
            a=ws.cell(row=row_pow2,column=2).value
            if tb2.value==a:
                app2.hide()
                app8.show()
                count2=1
                pt=True
        count2=1
    if tb1.value!="":
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
    app5.hide()
    app12.hide()
    app8.hide()
    app10.hide()
    app11.hide()
    app6.hide()
    app7.hide()
    app4.hide()
    app9.hide()
    app2.hide()
    app3.hide()
    app.show()
    tb3.clear()
    tb4.clear()

def loginScreen():
    app.hide()
    app2.hide()
    app3.show()

    

def login():
    t8.clear()
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
                break
            elif col!=tb3.value:
                c2=False
    for row_pow3 in range(1,ws.max_row+1):
        col2=ws.cell(row=row_pow3,column=2).value
        c3=count2
        if col2==tb4.value:
            c4=True
            count2=count2+1
            break
    if(c1==c3) and (c2==c4):
        app6.show()
        app3.hide()

def loggedIn():
    app6.show()
    app7.hide()
    app12.hide()
    app10.hide()

def incomescreen():
    app6.hide()
    app7.show()
    app13.hide()
    app9.hide()

def income():
    date_pattern=r"^\d{2}/\d{2}/\d{4}$"
    print(date_pattern)
    if re.match(tb6.value,date_pattern):
        app7.hide()
        app13.show()
    if (tb5.value==""or tb6.value==""):
        app7.hide()
        app9.show()
    else:
        if tb7.value=="":
            tb7.append(text="No Description")
        t=0
        wb2=openpyxl.load_workbook(t8.value+".xlsx")
        ws2=wb2.active
        for row_p in range(1,ws2.max_row+1):
            a=ws2.cell(row=row_p,column=1).value
            b=ws2.cell(row=row_p,column=2).value
            c=ws2.cell(row=row_p,column=3).value
            if a ==None or a==" ":
                ws2.cell(row=row_p,column=1,value=tb5.value)
            if b==None:
                ws2.cell(row=row_p,column=2,value=tb6.value)
            if c==None and t==0 :
                ws2.cell(row=row_p,column=3,value=tb7.value)
            ws2.cell(row=row_p+1,column=1,value=" ")
            wb2.save(t8.value+".xlsx")
        tb5.clear()
        tb6.clear()
        tb7.clear()
    
def expensesscreen():
    app10.show()
    app6.hide()
    app11.hide()
    app14.hide()

def expenses():
    date_pattern=r"^\d{2}/\d{2}/\d{4}$"
    if re.match(tb11.value,date_pattern):
        app10.hide()
        app13.show()
    if (tb10.value==""or tb11.value==""):
        app10.hide()
        app11.show()
    else:
        if tb12.value=="":
            tb12.append(text="No Description")
        t=0
        wb3=openpyxl.load_workbook(t8.value+".xlsx")
        ws2=wb3.active
        for row_p in range(1,ws2.max_row+1):
            a=ws2.cell(row=row_p,column=4).value
            b=ws2.cell(row=row_p,column=5).value
            c=ws2.cell(row=row_p,column=6).value
            if a ==None or a==" ":
                ws2.cell(row=row_p,column=4,value=tb10.value)
            if b==None:
                ws2.cell(row=row_p,column=5,value=tb11.value)
            if c==None and t==0 :
                ws2.cell(row=row_p,column=6,value=tb12.value)
            ws2.cell(row=row_p+1,column=1,value=" ")
            wb3.save(t8.value+".xlsx")
        tb10.clear()
        tb11.clear()
        tb12.clear()

def show():
    app6.hide()
    app12.show()
    wb4=openpyxl.load_workbook(t8.value+".xlsx")
    ws4=wb4.active
    for row_pow in range(1,ws4.max_row+1):
        a=ws4.cell(row=row_pow,column=1).value
        b=ws4.cell(row=row_pow,column=2).value
        c2=ws4.cell(row=row_pow,column=3).value
        d=ws4.cell(row=row_pow,column=4).value
        e=ws4.cell(row=row_pow,column=5).value
        f=ws4.cell(row=row_pow,column=6).value
        if a!=None and b!=None and c2!=None:
            lst.append(a+","+b+","+c2)
        if d!=None and e!=None and f!=None:
            lst2.append(d+","+e+","+f)


t1=Text(app,text="Do you have an account")
b1=PushButton(app,text="I do not have a account and would like to join",command=signUp)
b2=PushButton(app,text="i have an acount and would like to log in",command=loginScreen)
exits=PushButton(app,text="Exit",command=close)
t2=Text(app2,text="Type the user nane and password you would like below\nUsername")
tb1=TextBox(app2)
t3=Text(app2,text="Password")
tb2=TextBox(app2,hide_text=True)
b3=PushButton(app2,text="sign up",command=saved)
home1=PushButton(app2,text="Home screen",command=home)
log=PushButton(app2,text="login screen",command=loginScreen)
exit2=PushButton(app2,text="Exit",command=close)
t4=Text(app3,text="type in your username and password below to log in\nusername")
tb3=TextBox(app3)
t5=Text(app3,text="password")
tb4=TextBox(app3,hide_text=True)
b3=PushButton(app3,text="login",command=login)
home2=PushButton(app3,text="Home screen",command=home)
exit3=PushButton(app3,text="Exit",command=close)
t6=Text(app4,text="password or user name must be filled in ")
b5=PushButton(app4,text="Ok",command=signUp)
t7=Text(app5,text="Username is in use")
b6=PushButton(app5,text="Ok",command=signUp)
t9=Text(app7)
b4=PushButton(app6,text="add income",command=incomescreen)
t8=Text(app6)
t10=Text(app7,text="you should type in the amount of income \ngotten and when you got it \nand if you want a description")
t11=Text(app7,text="income")
tb5=TextBox(app7)
t12=Text(app7,text="Date(In fotmat DD/MM/YYYY)")
tb6=TextBox(app7)
t13=Text(app7,text="Description")
tb7=TextBox(app7)
add=PushButton(app7,text="Add the income",command=income)
home3=PushButton(app7,text="Home screen",command=loggedIn)
exit5=PushButton(app7,text="Exit",command=close)
t8=Text(app8,text="password already used")
tb8=PushButton(app8,text="Ok",command=signUp)
t9=Text(app9,text="Must input income and date atleats")
tb9=PushButton(app9,text="Ok",command=incomescreen)
b5=PushButton(app6,text="Add expensives",command=expensesscreen)
b6=PushButton(app6,text="to show all incomes and expenses",command=show)
home6=PushButton(app6,text="Home",command=home)
exit4=PushButton(app6,text="Exit",command=close)
t20=Text(app11,text="Must input expenses and date atleast")
tb13=PushButton(app11,text="Ok",command=expensesscreen )

t14=Text(app10,text="Add your expenses the \ndate you paid it and if\n you want a description")
t15=Text(app10,text="Expenses")
tb10=TextBox(app10)
t16=Text(app10,text="date(in format DD/MM/YYYY)")
tb11=TextBox(app10)
t17=Text(app10,text="description")
tb12=TextBox(app10)
b7=PushButton(app10,text="Expenses",command=expenses)
home4=PushButton(app10,text="Home screen",command=loggedIn)

t18=Text(app12,text="Income,date \nand description")
lst=ListBox(app12,width=120,height="fill")
t19=Text(app12,text="Expenses,\ndate and description")
lst2=ListBox(app12,width=120,height="fill")
home5=PushButton(app12,text="Home screen",command=loggedIn)
exit6=PushButton(app12,text="Exit",command=close)

t20=Text(app13,text="date must be in format DD/MM/YYYY")
b8=PushButton(app13,text="Ok",command=incomescreen)

t21=Text(app14,text="date must be in format DD/MM/YYYY")
b9=PushButton(app14,text="ok",command=expensesscreen)

app5.hide()
app13.hide()
app14.hide()
app12.hide()
app8.hide()
app10.hide()
app11.hide()
app6.hide()
app7.hide()
app4.hide()
app9.hide()
app2.hide()
app3.hide()
app.display()