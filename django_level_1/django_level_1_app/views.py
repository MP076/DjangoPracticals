from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    my_dict = {'insert_me': "Hello World! This is from Views"}
    return render(request, 'django_level_1_app/index.html', context=my_dict)
    # 1. return HttpResponse("Hello World!")