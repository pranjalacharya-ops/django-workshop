from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

def homepage(request):
      return render(request, 'home.html')
def aboutpage(request):
      return render(request, 'about.html')
def contactpage(request):
      return render(request, 'contact.html')
def shoppage(request):
      return render(request, 'shop.html')
def contactprocess(request):
      a = int(request.POST['txt1'])
      b = int(request.POST['txt2'])
      c = int(request.POST['txt3'])
      d = int(request.POST['txt4'])
      e = int(request.POST['txt5'])
      sum =a+b+c+d+e
      per= (sum/500)*100
      msg = " MATHS MARKS is: ", a ," SCIENCE MARKS is: " , b ,
      " ENGLISH MARKS is: " , c , " SOCIAL SCIENCE MARKS is: " , d , " HINDI MARKS is: " , e , " Sum is: " , sum ,
      " PERCENTAGE is: " , per
      f = ""
      if per >= 90:
            f = "GRADE A+"
      elif per >= 80:
            f = "GRADE A"
      elif per >= 70:
            f = "GRADE B"
      elif per >= 60:
            f = "GRADE C"
      elif per >= 50:
            f = "GRADE D"
      
      else:
            f = "FAIL"
      return render(request, 'ans.html', {'mya':a, 'myb':b, 'myc':c, 'myd':d, 'mye':e, 'mysum':sum, 'myper':per, 'myf':f})

def saveSessionData(request):
      request.session['username'] = "Pranjal Acharya"
      return HttpResponse("Session created")
def getSessionData(request):
      if request.session.has_key('username'):
            msg = request.session['username']
            return HttpResponse( msg)
      else:
            return HttpResponse("No session data found")            
def getSessionData2(request):
      msg = request.session['username']
      return HttpResponse(msg)
def deleteSessionData(request):
      del request.session['username']
      return HttpResponse("Session deleted")

def loginpage(request):
      return render(request, 'login.html')
def loginprocess(request):
      txt1= request.POST['username']
      request.session['username'] = txt1
      return redirect(dashboard)

def dashboard(request):
      if request.session.has_key('username'):
            return render(request, "dashboard.html")
      else:
            return redirect(loginpage)
def logout(request):
     del request.session['username']
     return redirect(loginpage)

def mailsenddemo(request):
      subject = 'Django Mail Demo'
      message = ' Hello How are you ?'
      email_from = settings.EMAIL_HOST_USER
      recipient_list = ['pranjalacharya10@gmail.com',]
      send_mail( subject, message, email_from, recipient_list )
      return HttpResponse("Mail Sent")
#dynamic mail
def contactuspageview(request):
      return render(request, 'contactus.html')
def mailsendprocess(request):
      subject = request.POST['txt2']
      message = request.POST['txt3']
      recipient_list = [request.POST['txt1'],]
      email_from = settings.EMAIL_HOST_USER
      send_mail( subject, message, email_from, recipient_list )
      return HttpResponse("Mail Sent")

#contactuss
# Create your views here.
def contactusspage(request):
      return render(request, 'contactuss.html')

def contactusspageprocess(request) :
      txt1 = request.POST['txt1']
      txt2 = request.POST['txt2']
      txt3 = request.POST['txt3' ]

      mymsg = "Hello has Contact you",txt1," Mobile No is ",txt2," Message is ",txt3

      subject = 'Contact us From Website'
      email_from = settings.EMAIL_HOST_USER

      message = mymsg
      recipient_list = ['pranjalacharya10@gmail.com',]
      send_mail( subject, message, email_from, recipient_list )
      return HttpResponse("Thank you for Contacting us.")
#student
from . models import Student

def addstudentform(request):
      return render(request, 'add-student.html')

def addstudentformprocess(request):
      txt1 = request. POST[ 'txt1' ]
      txt2 = request. POST[ 'txt2' ]
      txt3 = request.POST[ 'txt3' ]
      txt4 = request.POST['txt4' ]
      Student .objects.create(name=txt1, mobile=txt2, email=txt3, address=txt4)
      
      mymsg = "Hello has Contact you",txt1," Mobile No is ",txt2," Message is ",txt3

      subject = 'Contact us From Website'
      email_from = settings.EMAIL_HOST_USER

      message = mymsg
      recipient_list = ['pranjalacharya10@gmail.com',]
      send_mail( subject, message, email_from, recipient_list )
      return HttpResponse("Thank you for Contacting us.")
    
