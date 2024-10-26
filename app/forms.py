from django import forms
from app.models import *

class TopicForm(forms.Form):
    tn=forms.CharField()

class WebpageForm(forms.Form):
    tn=forms.ModelChoiceField(queryset=Topic.objects.all())
    #We have to do remaining Part
    