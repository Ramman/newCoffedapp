from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.

class LandingView(TemplateView):
    template_name = "base/index.html"
   # template_name = "index.html"