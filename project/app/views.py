from django.shortcuts import render,redirect
from django.contrib import messages
from app.models import emp,dep,submit_que
from django.db.models import Q




# Create your views here.


def landing(req):
    return render(req,'landing.html')

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
        if not name or not age or not contact or not email or not department:
            return render(req, 'admindashboard.html', {
                'add_employee': True,
                'error': "All fields are required"
            })

        user = emp.objects.filter(email=email)

        if user.exists():
            return render(req, 'admindashboard.html', {'add_employee': True})

        data=emp.objects.create(
            name=name,
            age=age,
            contact=contact, 
            email=email,
            department=department
        )
        
        return render(req, 'admindashboard.html', {'add_employee': True,user:'data'})
    else:
        return render(req, 'admindashboard.html', {'add_employee': True})


def employee_list(req):
    user =emp.objects.all()
    return render(req,'admindashboard.html',{'employee_list':True,'data':user})


def add_department(req):
    return render(req,'admindashboard.html',{'add_department':True})

def add_d(req):
    if req.method=="POST":
        d=req.POST.get('dept')
        h=req.POST.get('h_dept')
        dep.objects.create(d=d,h=h)
    return render(req,'admindashboard.html',{'add_d':True})

def department_list(req):
    data=dep.objects.all()
    return render(req,'admindashboard.html',{'department_list':True,'data':data})



def userpanel(req):
    return render(req,'userpanel.html')


def submit_q(req):
    if req.method=='POST':
        n=req.POST.get('name')
        e=req.POST.get('email')
        c=req.POST.get('contact')
        d=req.POST.get('dep')
        q=req.POST.get('que')
        data1=submit_que.objects.create(name=n,email=e,contact=c,dep=d,que=q)
        return render(req,'userpanel.html',{'submit_q':True})
        
    return render(req,'userpanel.html',{'submit_q':True})



def show_q(req):
    data1=submit_que.objects.all()
    return render (req,'userpanel.html',{'show_q':True,'data1':data1})

def search(req):
    if req.method=="POST":
        n=req.POST.get('name')
        e=req.POST.get('email')
        c=req.POST.get('contact')
        d=req.POST.get('dep')
        q=req.POST.get('que')
        data1=submit_que.objects.filter(n__contains=n,e__contains=e,c__contains=c,d__contains=d,q__contains=q)    
        print(data1)
        return render(req,'userpanel.html',{'show_q':True,'data1':data1})
    