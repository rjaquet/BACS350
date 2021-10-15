from django.http import HttpResponse
from django.views.generic import TemplateView

def homePageView(request):
    return HttpResponse('<h1>Hello World</h1>')

class MyView(TemplateView):
    template_name = "index.html"
