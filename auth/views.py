from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login

from django.contrib.auth.views import LoginView, LogoutView
# Create your views here.
from auth import forms


# def auth_login(request):
#     loginForm = forms.LoginForm()
#     error = None
#     if(request.method == "POST"):
#         loginForm = forms.LoginForm(request.POST)
#         if loginForm.is_valid():
#             username = loginForm.cleaned_data['username']
#             password = loginForm.cleaned_data['password']
#             user = authenticate(username=username, password=password)
#             if user:
#                 login(request, user)
#                 return HttpResponseRedirect('/')
#             else:
#                 error = "invalid username or password"
#
#     context = {
#         'form': loginForm,
#         'error': error,
#     }
#     return render(request, 'auth/login.html', context)

# using generic views


class Login(LoginView):
    template_name = 'auth/login.html'
    redirect_authenticated_user = True


class Logout(LogoutView):
    pass
