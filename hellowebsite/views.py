from django.shortcuts import render
from django.http import HttpResponse
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


      