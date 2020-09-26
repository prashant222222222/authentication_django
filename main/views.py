from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.


def index(request):
    context = {}
    return(render(request, 'main/index.html'))


@login_required(login_url='/auth/login')
def sshh(request):
    return HttpResponse("this is a authenticated view")
