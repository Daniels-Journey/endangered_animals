from django.contrib.auth import logout, login, authenticate
from django.shortcuts import render, redirect
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
                return redirect('home')
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
            user = signupform.save(commit=False)
            user.set_password(signupform.cleaned_data.get('password'))
            user.save()
            login(request, user)
            return redirect('home')
        return render(request, 'CreateUser.html', {'signupform': signupform})