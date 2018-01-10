# #coding=utf8
from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.utils.translation import ugettext_lazy as _
from .models import *

class Name_abstractForm(forms.ModelForm):
    name=forms.CharField(label='名字',max_length=50,widget=forms.TextInput({'class': 'form-control'}))
    alias=forms.CharField(label='别名',max_length=50,widget=forms.TextInput({'class': 'form-control'}))


class Machine_statusForm(Name_abstractForm):
    class Meta:
        model = Machine_status
        fields = (
            'name',
            'alias',
        )

class Machine_tagForm(Name_abstractForm):
    class Meta:
        model = Machine_tag
        fields = (
            'name',
            'alias',
        )

class Resource_statusForm(Name_abstractForm):
    class Meta:
        model = Resource_status
        fields = (
            'name',
            'alias',
        )

class Resource_tagForm(Name_abstractForm):
    class Meta:
        model = Resource_tag
        fields = (
            'name',
            'alias',
        )


class Cluster_statusForm(Name_abstractForm):
    class Meta:
        model = Cluster_status
        fields = (
            'name',
            'alias',
        )


class Cluster_tagForm(Name_abstractForm):
    class Meta:
        model = Cluster_tag
        fields = (
            'name',
            'alias',
        )