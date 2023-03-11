from django.shortcuts import render,HttpResponse
from home.models import Feedmain

# from datetime import datetime
# Create your views here.
def feedmain(request):
   if request.method == "POST" :
       name=request.POST.get('name')
       email=request.POST.get('email')
       subject=request.POST.get('subject')
       message=request.POST.get('message')
       rating=request.POST.get('rating')
       feedmain=Feedmain(name=name,email=email,subject=subject,message=message,rating=rating)
       feedmain.save()
   return render(request, 'feedmain.html')


