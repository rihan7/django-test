from django.http import request
from django.views.generic.base import View
from store.models import Product
from django.views.generic import TemplateView
from django.shortcuts import render


class index(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["products"] = Product.objects.all()
        return context
