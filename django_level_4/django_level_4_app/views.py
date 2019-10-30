from django.shortcuts import render


# Create your views here.
def index(request):
    context_dict = {'text': 'Hello World!', 'number': 100}
    return render(request, 'django_level_4_app/index.html', context_dict)


def other(request):
    return render(request, 'django_level_4_app/other.html')


def relative(request):
    return render(request, 'django_level_4_app/relative_url_template.html')
