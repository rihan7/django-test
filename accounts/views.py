from django.forms import ModelForm
from django.shortcuts import redirect, render
from django.views import View

from accounts.modelForm import register_form
from .models import CustomUserModel
# Create your views here.


class registration(View):
    def get(self, request):
        form = register_form()
        return render(request, 'account/registration.html', {'form': form})

    def post(self, request):
        form = register_form(request.POST)
        if form.is_valid():
            f_name = form.cleaned_data['first_name']
            l_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            username = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            password = form.cleaned_data['password']

            user = CustomUserModel.objects.create_user(first_name=f_name, last_name=l_name,
                                                       email=email, username=username, password=password)
            user.phone = phone
            user.save()
            return redirect('registration')

        else:
            return render(request, 'account/registration.html', {'form': form})


class login(View):
    def get(self, request):

        return render(request, 'account/login.html')


class logout(View):
    def get(self, request):

        return render(request, 'logout.html')
