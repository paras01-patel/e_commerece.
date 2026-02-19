from django.shortcuts import render,redirect
from django.contrib import messages
from app.models import emp,dep,submit_que,con
from django.db.models import Q




# Create your views here.

def home(req):
    return render(req,'home.html')

def about(req):
    return render(req,'about.html')


def services(req):
    return render(req,'services.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        sav=con.objects.create(name=name,email=email,subject=subject)
        return render(request, "contact.html",{'sav':sav})
    return render(request, "contact.html")

def signup(req):
    return render(req,'signup.html')


def login(req):
    if req.method == 'POST':
        e = req.POST.get('email')
        p = req.POST.get('password')
        if e == 'admin@gmail.com' and p == 'admin':
            req.session['admin_n'] = 'admin'
            return render(req, 'admindashboard.html')
        else:
            if req.method =='POST':
                e=req.POST.get('email')
                p=req.POST.get('password')
            return render(req, 'userpanel.html', {'error': 'Invalid Email or Password'})
    return render(req, 'login.html')

def logout(req):
    
    return render(req,'login.html')






# admindashboard ---------------

def admindashboard(req):
    return render(req,"admindashboard.html")

def add_empolyee(req):
    return render(req,'admindashboard.html',{'add_empolyee':True})



def add_e(req):
    if req.method == "POST":
        name = req.POST.get('name')
        age = req.POST.get('age')
        contact = req.POST.get('contact')
        email = req.POST.get('email')
        department = req.POST.get('department')
        data=emp.objects.create(n=name,a=age,c=contact,e=email,d=department)
    return render(req, 'admindashboard.html', {
                'add_empolyee': True,
                'data':data
            })

def search2(req):
    if req.method=="POST":
        name = req.POST.get('name')
        age = req.POST.get('age')
        contact = req.POST.get('contact')
        email = req.POST.get('email')
        department = req.POST.get('department')
        data=emp.objects.filter(n__contains=name,a__contains=age,c__contains=contact,e__contains=email,d__contains=department)
        return render(req,'admindashboard.html',{'employee_list':True,'data':data})
    return render(req, 'admindashboard.html',{'employee_list': True})
    


def employee_list(req):
    data=emp.objects.all()
    return render(req,'admindashboard.html',{'employee_list':True,'data':data})



def add_department(req):
    return render(req,'admindashboard.html',{'add_department':True})

def add_d(req):
    if req.method=="POST":
        d=req.POST.get('dept')
        h=req.POST.get('h_dept')
        data2=dep.objects.create(d=d,h=h)
    return render(req,'admindashboard.html',{'add_d':True,'data2':data2})

def search1(req):
    if req.method=="POST":
        de=req.POST.get('dept')
        h=req.POST.get('h_head')
        data2=dep.objects.filter(d__contains=de,h__contains=h)
        return render(req,'admindashboard.html',{'department_list':True,'data2':data2})

def department_list(req):
    data2=dep.objects.all()
    return render(req,'admindashboard.html',{'department_list':True,'data2':data2})






# userpanel------------------


def userpanel(req):
    return render(req,'userpanel.html')



def submit_q(req):
    if req.method=='POST':
        n=req.POST.get('name')
        e=req.POST.get('email')
        c=req.POST.get('contact')
        d=req.POST.get('dep')
        q=req.POST.get('que')
        data1=submit_que.objects.create(n=n,e=e,c=c,d=d,q=q)
        return render(req,'userpanel.html',{'submit_q':True,'data1':data1})
    return render(req,'userpanel.html',{'submit_q':True})
    
        
def search(req):
    if req.method=="POST":
        n=req.POST.get('name')
        e=req.POST.get('email')
        c=req.POST.get('contact')
        d=req.POST.get('dep')
        q=req.POST.get('que')
        data1=submit_que.objects.filter(n__contains=n,e__contains=e,c__contains=c,d__contains=d,q__contains=q)    
        
        return render(req,'userpanel.html',{'show_q':True,'data1':data1})
    
    return render(req,'userpanel.html',{'submit_q':True})



def show_q(req):
    data1=submit_que.objects.all()
    return render (req,'userpanel.html',{'show_q':True,'data1':data1})

