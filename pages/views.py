from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = "home.html"


class AboutPageView(TemplateView):
    template_name = "about.html"
# Create your views here.

class ProcuctsPageView(TemplateView):
    template_name = "products.html"
