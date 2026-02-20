"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views


urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('services/',views.services,name='services'),
    path('contact/',views.contact,name='contact'),
    
    
    path('signup/',views.signup,name='signup'),
    path('login/',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('admindashboard/',views.admindashboard,name='admindashboard'),
    path('add_empolyee',views.add_empolyee,name='add_empolyee'),
    path('add_e',views.add_e,name='add_e'),
    path('employee_list',views.employee_list,name='employee_list'),
    path('add_department',views.add_department,name='add_department'),
    path('department_list',views.department_list,name='department_list'),
    path('add_d',views.add_d,name='add_d'),
    path('userpanel/',views.userpanel,name='userpanel'),
    path('submit_q',views.submit_q,name='submit_q'),
    path('show_q',views.show_q,name='show_q'),
    path('search',views.search,name='search'),
    path('search1',views.search1,name='search1'),
    path('search2',views.search2,name='search2'),
    path('edit/<int:pk>',views.delete,name='edit'),
    path('delete/<int:pk>',views.delete,name='delete'),

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
]
