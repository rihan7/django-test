from django.shortcuts import render
from django.views import View

# Create your views here.


class registration(View):
    def get(self, request):

        return render(request, 'account/registration.html')


class login(View):
    def get(self, request):

        return render(request, 'account/login.html')


class logout(View):
    def get(self, request):

        return render(request, 'logout.html')
