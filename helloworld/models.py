from django.forms import ModelForm
from django.db import models

# Create your models here.


class MyUsers(models.Model):
    name = models.CharField(max_length=20)
    country = models.CharField(max_length=50, default='India')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return u'%s' % (self.name)


class UserForm(ModelForm):

    class Meta:
        model = MyUsers
        fields = ['name']
