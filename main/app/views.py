from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import *
from .models import Text
from django.urls import reverse


def index(request):
    return render(request, 'app/index.html', {'pages': Text.objects.all()})


def form(request):
    if request.method == 'POST':
        form = One(request.POST)
        if form.is_valid():
            dict_page = {}
            dict_page['title'] = form.cleaned_data['Title']
            dict_page['href'] = form.cleaned_data['Url']
            dict_page['Text'] = form.cleaned_data['TextArea']
            dict_page['CheckBox'] = form.cleaned_data['CheckBox']
            dict_page['Selection'] = form.cleaned_data['Selection']
            Text.objects.create(title=form.cleaned_data['Title'], content=form.cleaned_data['TextArea'], img_href=form.cleaned_data['Url'], CheckBox=form.cleaned_data['CheckBox'], Selection=form.cleaned_data['Selection'])
            return HttpResponseRedirect(reverse('home'))
    else:
        form = One()
    return render(request, 'app/form.html', {'form': form})