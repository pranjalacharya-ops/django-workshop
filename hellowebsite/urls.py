from django.urls import path
from . import views
urlpatterns =[
    path('', views.homepage),
    path('home', views.homepage),
    path('about', views.aboutpage),
    path('contact', views.contactpage),
    path('contactprocess', views.contactprocess),
    path('shop', views.shoppage)
]