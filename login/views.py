from django.shortcuts import render
import mysql.connector as sql
em=''
pwd=''
# Create your views here.
def loginaction(request):
    global em,pwd
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",passwd="vishnu",database='website')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="email":
                em=value
            if key=="password":
                pwd=value
        
        c="select * from users where email='{}' and password='{}'".format(em,pwd)
        cursor.execute(c)
        t=tuple(cursor.fetchall())
        if t==():
            return render(request,'error.html')
        else:
            #own
            user="select First_Name,Last_Name from users where email='{}'".format(em)
            cursor.execute(user)
            u=cursor.fetchall()
            u=str(u)
            print(u)
            user_name=''
            for i in u:
                if i in ['(',')','[',']',',']:
                   pass
                else:
                    user_name+=i
            ### for passing user name to html page
            return render(request,"welcome.html",{"user_name":user_name})

    return render(request,'login_page.html')