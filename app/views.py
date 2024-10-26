from django.shortcuts import render

# Create your views here.
from app.forms import *
from app.models import *
from django.http import HttpResponse
def insert_topic(request):
    ETFO=TopicForm()
    d={'ETFO':ETFO}

    if request.method=='POST':
        TFDO=TopicForm(request.POST)
        if TFDO.is_valid():
            tn=request.POST['tn']

            TO=Topic.objects.get_or_create(topic_name=tn)
            return HttpResponse('Topic is Created')
        else:
            return HttpResponse('Invalid data')


    return render(request,'insert_topic.html',d)




def insert_webpage(request):
    d={'EWFO':WebpageForm()}
    return render(request,'insert_webpage.html',d)


