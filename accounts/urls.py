from django.urls.conf import path
from . import views


urlpatterns = [
    path('registration', views.registration.as_view(), name='registration'),
]
