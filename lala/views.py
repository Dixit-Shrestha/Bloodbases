
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

def index(request):
    return render(request, 'lala/index.html')
# def nav(request):
#    s=''' Navigation Bar <br> </h2>
#     <a href= "https://www.youtube.com/playlist?list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9" > Django Code With Harry Bhai </a><br>
#     <a href="https://www.facebook.com/"> Facebook </a> <br>
#     <a href="https://www.flipkart.com/"> Flipkart </a> <br>
#     <a href="https://www.hindustantimes.com/"> News </a> <br>
#     <a href="https://www.google.com/"> Google </a> <br>
#     '''
#    return HttpResponse((s))
def analyze(request):
    djtext = request.GET.get('text', 'default')  
    removepunc = request.GET.get('removepunc', 'off')  
    fullcaps = request.GET.get('fullcaps', 'off')  
    newline = request.GET.get('newline', 'off')  
    spaceremove = request.GET.get('spaceremove', 'off')  

    analyzed = djtext

    print(removepunc)
    print(djtext)

   
    if (removepunc == "on"):
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~''' 
        analyzed = ""
        for char in djtext:
         if char not in punctuations:
            analyzed = analyzed + char
            djtext = analyzed
        params = {'purpose': "Removing Punctuations", 'analyzed_text': analyzed}
        return render(request, 'lala/analyze.html', params)
    elif (fullcaps=="on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
            djtext = analyzed
        params = {'purpose': "Changed to Uppercase", 'analyzed_text': analyzed}
        return render(request, 'lala/analyze.html', params)
    elif(newline=="on"):
        analyzed = ""
        for char in djtext:
            if char != "\n":
               analyzed = analyzed + char
               djtext = analyzed
    params = {'purpose': "Remove NewLine", 'analyzed_text': analyzed}
    return render(request, 'lala/analyze.html', params)
 



def signin(request):
    if request.method=='POST':
        firstName=request.POST['firstName']
        lastName=request.POST['lastName']
        userName=request.POST['userName']
        gender=request.POST['gender']
        bloodGroup=request.POST['bloodGroup']
        phone=request.POST['phone']
        address=request.POST['address']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        myuser = User.objects.create_user(username=userName, email=email, password= password1)
        
        myuser.first_name=firstName
        myuser.last_name=lastName
        myuser.save()
        return redirect('index')
    return render(request, 'signin.html')