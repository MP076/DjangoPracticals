from django.shortcuts import render
from . import forms


# Create your views here.
def index(request):
    return render(request, 'django_level_3_app/index.html')


def formNameView(request):
    form = forms.FormName()

    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            # Validation code
            print("Validation Successful")
            print("Name: "+form.cleaned_data['name'])
            print("Email: "+form.cleaned_data['email'])
            print("Text: "+form.cleaned_data['text'])

    return render(request, 'django_level_3_app/form.html', {'form': form})
