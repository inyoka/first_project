from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic, Webpage, AccessRecord, User

# Create your views here.
def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records':webpages_list}
    # my_dict = {'insert_content':'HELLO I AM FROM FIRST APP!!!!'}
    return render(request, 'first_app/index.html', context = date_dict)

def users(request):
    user_list = User.objects.order_by('secondname', 'firstname')
    name_dict = {'user_records':user_list}
    return render(request, 'first_app/users.html', context = name_dict)
