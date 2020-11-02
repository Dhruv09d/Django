from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
'''def Pagehomeview(request):
    return render(request, 'pages/home.html')

def Pageaboutview(request):
    return render(request, 'pages/about.html')'''

class Pagehomeview(TemplateView):
    template_name = 'pages/home.html'


class Pageaboutview(TemplateView):
    template_name = 'pages/about.html'