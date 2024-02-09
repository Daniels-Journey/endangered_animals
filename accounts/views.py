from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from accounts.forms import LoginForm, SignUpForm

# Create your views here.

class LoginView(View):
    def get(self,request):
        form = LoginForm()
        return render(request, 'login.html', {'form':form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                next= request.GET.get('next','home')
                return redirect(next)
        return render(request, 'Login.html', {'form': form})


class LogoutView(View):

    def get(self,request):
        logout(request)
        return redirect('home')



class RegisterView(View):

    def get(self,request):
        signupform = SignUpForm()
        return render(request, 'CreateUser.html', {'signupform':signupform})

    def post(self,request):
        signupform = SignUpForm(request.POST)
        if signupform.is_valid():
            username = signupform.cleaned_data.get('username')
            email = signupform.cleaned_data.get('email')
            if User.objects.filter(username=username).exists():
                messages.error(request, 'This username is already in use.')
                return redirect('register_view')

            if User.objects.filter(email=email).exists():
                error_message = 'This email is already in use.'
                return redirect(reverse('register_view') + '?error=' + error_message)

            user = signupform.save(commit=False)
            user.set_password(signupform.cleaned_data.get('password'))
            user.save()
            login(request, user)
            return redirect('home')
        return render(request, 'CreateUser.html', {'signupform': signupform})