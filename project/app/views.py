from django.shortcuts import render,redirect
from django.contrib import messages
from app.models import emp,dep




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
            return render(req, 'login.html', {'error': 'Invalid Email or Password'})
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

        user = emp.objects.filter(email=e)

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
    return render(req,'admindashboard.html',{'add_d':True})

def department_list(req):
    return render(req,'admindashboard.html',{'department_list':True})