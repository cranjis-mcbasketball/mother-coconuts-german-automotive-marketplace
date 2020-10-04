from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.models import auth
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth import get_user_model
from shop.models import *
User = get_user_model()

# Create views


def register(request):

    if request.method == 'POST':
        if 'customerCreate' in request.POST:
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            email = request.POST['email']
            password1 = request.POST['password1']
            password2 = request.POST['password2']

            if password1 == password2:
                '''if User.objects.filter(username=username).exists():
                    messages.info(request, 'Username Taken')
                    return HttpResponseRedirect(reverse('accounts:register'))
                if User.objects.filter(email=email).exists():
                    messages.info(request, 'Email Taken')
                    return HttpResponseRedirect(reverse('accounts:signup'))
                else:'''
                user = User.objects.create_user(
                    username=email, email=email, password=password1, first_name=first_name, last_name=last_name, is_customer=True)
                user.save()
                return HttpResponseRedirect(reverse('shop:home'))
            else:
                messages.info(request, 'Password not matching')
                return HttpResponseRedirect(reverse('accounts:signup'))
            return HttpResponseRedirect(reverse('accounts:login'))
        elif 'companyCreate' in request.POST:
            first_name = request.POST['company_name']
            email = request.POST['email']
            password1 = request.POST['password1']
            password2 = request.POST['password2']

            if password1 == password2:
                if User.objects.filter(first_name=first_name).exists():
                    messages.info(request, 'Name Taken')
                    return HttpResponseRedirect(reverse('accounts:signup'))
                elif User.objects.filter(email=email).exists():
                    messages.info(request, 'Email Taken')
                    return HttpResponseRedirect(reverse('accounts:signup'))
                else:
                    user = User.objects.create_user(
                        username=email, email=email, password=password1, first_name=first_name, is_company=True)
                    user.save()
                    return HttpResponseRedirect(reverse('accounts:user_login'))
            else:
                messages.info(request, 'Password not matching')
                return HttpResponseRedirect(reverse('accounts:signup'))
            return HttpResponseRedirect(reverse('accounts:user_login'))

    else:
        return render(request, 'signup.html')


def user_login(request):
    if request.method == 'POST':
        username = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect(reverse('shop:home'))
        else:
            messages.info(request, 'Username or password incorrect')
            return redirect('accounts:user_login')
    else:
        return render(request, 'login.html')


def user_logout(request):
    auth.logout(request)
    return redirect(reverse('accounts:user_login'))


''' under-construction'''


def Profile(request, user_id):
    this_user = User.objects.get(id=user_id)
    if this_user.is_company:
        items = Product.objects.filter(company=this_user.company)
        context = {
            'items': items,
            'company': Company.objects.filter(user=this_user).first(),
        }
        return render(request, "companypage.html", context)
    elif this_user.is_customer:
        context = {

        }
        return render(request, "customerProfile.html", context)
    return render(request, "404.html")
