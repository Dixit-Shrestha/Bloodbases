from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from .models import det,donor,receipent
from django.contrib.auth import authenticate,login as ln,logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
def index(request):
    return render(request, "toto/index.html")

def user_signin(request):
    if request.method=='POST':
        username=request.POST['username']
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        gender=request.POST['gender']
        address=request.POST['address']
        bloodgroup=request.POST['bloodgroup']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        print("Creating user:", username) 
         
        if not username.isalnum():
            messages.success(request,'username must be alphanumeric')
            return redirect('signin')
        if (password1 != password2):
            messages.success(request,'password doesnt match')
            return redirect('signin')
        
        myuser=User.objects.create_user(username=username, email=email, password=password1)
        myuser.first_name=firstname
        myuser.last_name=lastname
        myuser.save()
        
        messages.success(request,'your account has been logged in')
        return redirect('main')
    else:
        return render(request, 'toto/signin.html')


def user_login(request):
    if request.method=='POST':
        loginusername=request.POST['lusername']
        loginpassword=request.POST['lpassword']
        user= authenticate(username=loginusername,password=loginpassword)
        
        if user is not None:
            ln(request,user)
            messages.success(request,"successfully logged in.")
            return redirect('main')
        else:
            messages.error(request,'invalid credentials.')
            return redirect('login')
    return render(request,'toto/login.html')

@login_required
def donor_req(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname', '')
        middlename = request.POST.get('middlename', '')
        lastname = request.POST.get('lastname', '')
        gender = request.POST.get('gender', '')
        address = request.POST.get('address', '')
        image = request.FILES.get('image')
        bloodgroup = request.POST.get('bloodgroup', '')
        phone = request.POST.get('phone', '')
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')

        new_donor = donor(
            firstname=firstname,
            middlename=middlename,
            lastname=lastname,
            gender=gender,
            address=address,
            image=image,
            bloodgroup=bloodgroup,
            phone=phone,
            email=email,
            password=password
        )
        new_donor.save()

    return render(request, 'toto/register.html')




def receipent_req(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname', '')
        middlename = request.POST.get('middlename', '')
        lastname = request.POST.get('lastname', '')
        gender = request.POST.get('gender', '')
        address = request.POST.get('address', '')
        image = request.FILES.get('image')
        bloodgroup = request.POST.get('bloodgroup', '')
        phone = request.POST.get('phone', '')
        email = request.POST.get('email', '')

        new_receipent = receipent(
            firstname=firstname,
            middlename=middlename,
            lastname=lastname,
            gender=gender,
            address=address,
            image=image,
            bloodgroup=bloodgroup,
            phone=phone,
            email=email,
        )
        new_receipent.save()

        # Find donors matching this recipient's bloodgroup and address
        matched_donors = donor.objects.filter(
            bloodgroup__iexact=bloodgroup,
            address__icontains=address
        )

        # Render donor list template with matched donors and recipient info
        return render(request, 'toto/list.html', {
            'donors': matched_donors,
            'selected_receipent': new_receipent
        })

    # For GET requests just render the recipient form
    return render(request, 'toto/order.html')

def matched_donors(request):
    email = request.GET.get('email')
    donors = []
    selected_receipent = None

    if email:
        selected_receipent = get_object_or_404(receipent, email=email)

        donors = donor.objects.filter(
            bloodgroup__iexact=selected_receipent.bloodgroup,
            address__icontains=selected_receipent.address
        )

    return render(request, 'toto/list.html', {
        'selected_receipent': selected_receipent,
        'donors': donors
    })


# def receipent_req(request):

#     if request.method == 'POST':
#         firstname = request.POST.get('firstname', '')
#         middlename = request.POST.get('middlename', '')
#         lastname = request.POST.get('lastname', '')
#         gender = request.POST.get('gender', '')
#         address = request.POST.get('address', '')
#         image = request.FILES.get('image')
#         bloodgroup = request.POST.get('bloodgroup', '')
#         phone = request.POST.get('phone', '')
#         email = request.POST.get('email', '')

#         new_receipent = receipent(
#             firstname=firstname,
#             middlename=middlename,
#             lastname=lastname,
#             gender=gender,
#             address=address,
#             image=image,
#             bloodgroup=bloodgroup,
#             phone=phone,
#             email=email,

#         )
#         new_receipent.save()
#     return render(request, 'toto/order.html') 
#         # return render(request, 'toto/order.html')


# def matched_recipients(request):
#     recipients = []
#     selected_donor = None

#     if request.method == 'POST':
#         donor_email = request.POST.get('donor_email')
#         selected_donor = get_object_or_404(donor, email=donor_email)

#         # Match recipients with same blood group and similar address
#         recipients = receipent.objects.filter(
#             bloodgroup__iexact=selected_donor.bloodgroup,
#             address__icontains=selected_donor.address
#         )

#     donors = donor.objects.all()

#     return render(request, 'toto/list.html', {
#         'donors': donors,
#         'selected_donor': selected_donor,
#         'recipients': recipients
#     })



def main(request):
    return render(request,'toto/main.html')

def service(request):
    return render(request, "toto/service.html")

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        message = request.POST.get('message', '')

        new_entry = det(name=name, email=email, message=message)
        new_entry.save()

        return render(request, 'toto/contact.html')  
    return render(request, 'toto/contact.html')

# def register(request):
#     return render(request, "toto/register.html")

def about(request):
    return render(request, "toto/about.html")

# def order(request):
#     return render(request, "toto/order.html")

from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import views as auth_views

def reset_password(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User.objects.get(pk=uid)
    except (User.DoesNotExist, ValueError, TypeError, OverflowError):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        if request.method == 'POST':
            password1 = request.POST.get('new_password1')
            password2 = request.POST.get('new_password2')
            if password1 == password2:
                user.set_password(password1)
                user.save()
                return render(request, 'toto/password_reset_complete.html')
            else:
                messages.error(request, "Passwords do not match.")
        return render(request, 'toto/password_reset_confirm.html')
    else:
        messages.error(request, "Invalid or expired link.")
        return redirect('forgot_password')
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.models import User
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings

def forgot_password(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        user = User.objects.filter(email=email).first()
        if user:
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            token = default_token_generator.make_token(user)
            reset_link = f"http://127.0.0.1:8000/password_reset_form/{uid}/{token}/"
            send_mail(
                'Password Reset Request - Blood Base',
                f'Hello {user.username},\n\nClick to reset your password:\n{reset_link}\n\nThanks,\nBlood Base Team',
                settings.EMAIL_HOST_USER,
                [user.email]
            )
            return render(request, 'toto/password_reset_done.html')
        else:
            messages.error(request, "No user found with that email.")
    return render(request, 'toto/password_reset.html')