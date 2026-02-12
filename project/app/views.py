from django.shortcuts import render
from django.contrib import messages
from app.models import emp




# Create your views here.


def landing(req):
    return render(req,'landing.html')
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
    if req.method=="POST":
        n=req.POST.get('name')
        a=req.POST.get('age')
        c=req.POST.get('contact')
        e=req.POST.get('email')
        d=req.POST.get('department')
        
        user=e.objects.filter(email=e)
        if user:
            return render(req,'admindashboard.html',{'add_employee':True})
        else:
            emp.objects.create(name=n,age=a,contact=c,email=e,Department=d)
            return render(req,'admindashboard.html',{'add_employee':True})   
    return render(req,'admindasahboard.html',{'add_empolyee':True})

