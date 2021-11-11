from django.shortcuts import render
from django.http import HttpResponse
import random 
import string
# Create your views here.

def home(request):
    return render(request, 'generator/home.html') 

    # {'password':'hashabjhdv'} this is used to create varibale which can be used in template



def password(request):

    characters = list(string.ascii_lowercase) #abcd...

    if request.GET.get('uppercase'):
        characters.extend(list(string.ascii_uppercase)) #ABCD...

    if request.GET.get('special'):
        characters.extend(list(string.punctuation))  #!@#$$...

    if request.GET.get('numbers'):
        characters.extend(list(string.digits)) #1223...

    length = int(request.GET.get('length',12)) #form name

    thepassword = ''

    for x in range(length):
        thepassword += random.choice(characters)
        
    return render(request, 'generator/password.html', {'password' : thepassword } )
    

def about(request):
    return render(request, 'generator/about.html')