from django.urls import path
from . import views
urlpatterns =[
    path('', views.homepage),
    path('home', views.homepage),
    path('about', views.aboutpage),
    path('contact', views.contactpage),
    path('contactprocess', views.contactprocess),
    path('shop', views.shoppage),
    path('savesessiondata', views.saveSessionData),
    path('getsessiondata', views.getSessionData),
    path('getsessiondata2', views.getSessionData2),
    path('deletesessiondata', views.deleteSessionData),
    
    path('login', views.loginpage),
    path('loginprocess', views.loginprocess),
    path('dashboard', views.dashboard),
    path('logout', views.logout)
]   