# #coding=utf8
from django import forms
# from django.utils.translation import ugettext_lazy as _
from .models import *
from .wiget import *

class MachineForm(forms.ModelForm):
    cpu = forms.CharField(label='CPU', max_length=100,required=False, widget=forms.TextInput({'class': 'form-control'}))
    kernel = forms.CharField(label='kernel', max_length=100,required=False, widget=forms.TextInput({'class': 'form-control'}))
    cpu_number = forms.IntegerField(label='cpu_number',required=False)
    vcpu_number=forms.IntegerField(label='cpu_number',required=False)
    cpu_core=forms.IntegerField(label='cpu_number',required=False)
    hostname=forms.CharField(label='主机名', max_length=100,required=False, widget=forms.TextInput({'class': 'form-control'}))
    memory=forms.IntegerField(label='cpu_number',required=False)
    disk=forms.CharField(label='容量', max_length=100,required=False, widget=forms.TextInput({'class': 'form-control'}))
    swap=forms.CharField(label='swap', max_length=100,required=False, widget=forms.TextInput({'class': 'form-control'}))
    product = forms.CharField(label='服务器型号', max_length=100,required=False, widget=forms.TextInput({'class': 'form-control'}))
    selinux = forms.CharField(label='selinux', max_length=100,required=False, widget=forms.TextInput({'class': 'form-control'}))
    distribution=forms.CharField(label='distribution', max_length=25,required=False, widget=forms.TextInput({'class': 'form-control'}))
    distribution_version=forms.CharField(label='distribution_version', max_length=25,required=False, widget=forms.TextInput({'class': 'form-control'}))
    manufacturer=forms.CharField(label='manufacturer', max_length=25,required=False, widget=forms.TextInput({'class': 'form-control'}))
    serial = forms.CharField(label='序列号', max_length=10,required=False, widget=forms.TextInput({'class': 'form-control'}))

    class Meta:
        model = Machine
        fields = (
            'console_ip',
            'status',
            'ipv4',
            'tag',
            'cpu',
            'kernel',
            'cpu_number',
            'vcpu_number',
            'cpu_core',
            'hostname',
            'memory',
            'disk',
            'swap',
            'product',
            'selinux',
            'distribution',
            'distribution_version',
            'manufacturer',
            'serial',
        )
        widgets = {
            'console_ip': IpModelSelect2Widget,
            'status':MachinestatusModelSelect2Widget,
            'ipv4':IpsModelSelect2MultipleWidget,
            'tag':MachinetagMultipleWidget,
        }
