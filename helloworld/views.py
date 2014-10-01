from django.db.models import Count
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
import datetime
import models


def HelloWorld(request, name):
    now = datetime.datetime.now()
    user = models.MyUsers.objects.all()
    userform = models.UserForm()
    if name:
        print name
        user = models.MyUsers.objects.values('name').filter(
            name=name).annotate(name_count=Count('name'))
        userform = models.UserForm(
            instance=models.MyUsers.objects.filter(name=name)[0])
    return render_to_response('form.html', {
        'now': now, 'users': user, 'userform': userform})


def addUser(request):
    name = request.GET.get('name')
    models.UserForm(request.REQUEST).save()
    return HttpResponseRedirect('/hello/' + name)
