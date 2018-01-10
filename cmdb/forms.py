# #coding=utf8
from django import forms
# from django.utils.translation import ugettext_lazy as _
from .models import *
from .wiget import *

class MachineForm(forms.ModelForm):

    class Meta:
        model = Machine
        fields = (
            'console_ip',
            'status',
            'tag',
        )
        widgets = {
            'console_ip': IpModelSelect2Widget,
            'status':MachinestatusModelSelect2Widget,
            'tag':MachinetagMultipleWidget,
        }
