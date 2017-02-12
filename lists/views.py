from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home_page(request):
    return render(request, 'home.html')
    '''
    It takes the request as its first parameter and the name of the template to render.
    Django will automatically search folders called templates inside any of your apps' directories.
    Then it builds an HttpResponse for you, based on the content of the template.
    '''
