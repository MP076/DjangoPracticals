from django.shortcuts import render
from django_level_2_app.models import Topic, Webpage, AccessRecord


# Create your views here.
def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records': webpages_list}
    return render(request, 'django_level_2_app/index.html', context=date_dict)
    # my_dict = {'insert_content': "Hello! This is from Views"}
    # return render(request, 'django_level_2_app/index.html', context=my_dict)
