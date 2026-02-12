from django.shortcuts import render,redirect
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

        user = emp.objects.filter(e=email)

        if user.exists():
            return render(req, 'admindashboard.html', {'add_employee': True})

        emp.objects.create(
            n=name,
            a=age,
            c=contact,   # 👈 ye NULL nahi hona chahiye
            e=email,
            d=department
        )
        
        return render(req, 'admindashboard.html', {'add_employee': True})
    else:
        return render(req, 'admindashboard.html', {'add_employee': True})


def employee_list(req):
    user =emp.objects.all()
    return render(req,'admindashboard.html',{'employee_list':True,'data':user})