#coding=utf8
from .models import *
from django.core.urlresolvers import reverse_lazy
from django.db.models import Q
from .forms import MachineForm
from abstract.views import Base_ListViewSet,Base_CreateViewSet,Base_UpdateViewSet,Base_DeleteViewSet

import operator
from functools import reduce

class Machine_createViewSet(Base_CreateViewSet):
    model = Machine
    form_class = MachineForm
    template_name = 'cmdb/machine_form.html'
    success_url = reverse_lazy('machine-list')

class Machine_updateViewSet(Base_UpdateViewSet):
    model = Machine
    form_class = MachineForm
    template_name = 'cmdb/machine_form.html'
    success_url = reverse_lazy('machine-list')

class Machine_listViewSet(Base_ListViewSet):
    Machine.objects.all().count()
    model = Machine
    template_name = 'cmdb/machine.html'
    paginate_by = 10

    def get_queryset(self):
        try:
            idc=self.request.GET['idc']
        except:
            idc=''
        query_list=[]
        if idc:
            query_list.append(Q(idc=idc))
        try:
            ip=self.request.GET['ip']
            query_list.append(Q(ipv4__name__istartswith=ip))
        except:
            pass
        try:
            sys_desc=self.request.GET['sys']
            query_list.append(Q(distribution_version__istartswith=sys_desc))
        except:
            pass
        try:
            tag=self.request.GET['tag']
            query_list.append(Q(tag__name=tag))
        except:
            pass
        if query_list:
            return list(set(Machine.objects.select_related().filter(reduce(operator.and_, query_list))))
        else:
            return Machine.objects.all()