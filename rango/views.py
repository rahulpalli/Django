#from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    context_dict = {'boldmessage': "Crunchy, creamy, cookie, candy, cupcake!"}
    return render(request,'rango/index.html', context=context_dict)
    #return HttpResponse("Rango says hey there partner!")
# Create your views here.
def AboutUs(request):
    return render(request,'rango/Aboutus.html')#, context=context_dict)
