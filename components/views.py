#coding=utf8
from .models import *
from django.core.urlresolvers import reverse_lazy
from .forms import Machine_statusForm,Machine_tagForm,Resource_tagForm,Resource_statusForm,Cluster_statusForm,Cluster_tagForm
from abstract.views import Base_ListViewSet,Base_CreateViewSet,Base_UpdateViewSet,Base_DeleteViewSet

class Machinestatus_listViewSet(Base_ListViewSet):
    Machine_status.objects.all().count()
    model = Machine_status
    template_name = 'components/machine_status.html'
    paginate_by = 10

    def get_queryset(self):
        try:
            name=self.request.GET['keyword']
        except:
            name=None
        if name:
            return self.model.objects.filter(name__icontains=name)
        else:
            return self.model.objects.all()

class Machinestatus_createViewSet(Base_CreateViewSet):
    model = Machine_status
    form_class = Machine_statusForm
    template_name = 'components/machine_status_form.html'
    success_url = reverse_lazy('machine-status-list')

class Machinestatus_updateViewSet(Base_UpdateViewSet):
    model = Machine_status
    form_class = Machine_statusForm
    template_name = 'components/machine_status_form.html'
    success_url = reverse_lazy('machine-status-list')

class Machinetag_listViewSet(Base_ListViewSet):
    Machine_tag.objects.all().count()
    model = Machine_tag
    template_name = 'components/machine_tag.html'
    paginate_by = 10

    def get_queryset(self):
        try:
            name=self.request.GET['keyword']
        except:
            name=None
        if name:
            return self.model.objects.filter(name__icontains=name)
        else:
            return self.model.objects.all()

class Machinetag_createViewSet(Base_CreateViewSet):
    model = Machine_tag
    form_class = Machine_tagForm
    template_name = 'components/machine_tag_form.html'
    success_url = reverse_lazy('machine-tag-list')

class Machinetag_updateViewSet(Base_UpdateViewSet):
    model = Machine_tag
    form_class = Machine_tagForm
    template_name = 'components/machine_tag_form.html'
    success_url = reverse_lazy('machine-tag-list')


class Resourcestatus_listViewSet(Base_ListViewSet):
    Resource_status.objects.all().count()
    model = Resource_status
    template_name = 'components/resource_status.html'
    paginate_by = 10

    def get_queryset(self):
        try:
            name=self.request.GET['keyword']
        except:
            name=None
        if name:
            return self.model.objects.filter(name__icontains=name)
        else:
            return self.model.objects.all()

class Resourcestatus_createViewSet(Base_CreateViewSet):
    model = Resource_status
    form_class = Resource_statusForm
    template_name = 'components/resource_status_form.html'
    success_url = reverse_lazy('resource-status-list')

class Resourcestatus_updateViewSet(Base_UpdateViewSet):
    model = Resource_status
    form_class = Resource_statusForm
    template_name = 'components/resource_status_form.html'
    success_url = reverse_lazy('resource-status-list')

class Resourcetag_listViewSet(Base_ListViewSet):
    Resource_tag.objects.all().count()
    model = Resource_tag
    template_name = 'components/resource_tag.html'
    paginate_by = 10

    def get_queryset(self):
        try:
            name=self.request.GET['keyword']
        except:
            name=None
        if name:
            return self.model.objects.filter(name__icontains=name)
        else:
            return self.model.objects.all()

class Resourcetag_createViewSet(Base_CreateViewSet):
    model = Resource_tag
    form_class = Resource_tagForm
    template_name = 'components/resource_tag_form.html'
    success_url = reverse_lazy('resource-tag-list')

class Resourcetag_updateViewSet(Base_UpdateViewSet):
    model = Resource_tag
    form_class = Resource_tagForm
    template_name = 'components/resource_tag_form.html'
    success_url = reverse_lazy('resource-tag-list')


class Clusterstatus_listViewSet(Base_ListViewSet):
    Cluster_status.objects.all().count()
    model = Cluster_status
    template_name = 'components/cluster_status.html'
    paginate_by = 10

    def get_queryset(self):
        try:
            name=self.request.GET['keyword']
        except:
            name=None
        if name:
            return self.model.objects.filter(name__icontains=name)
        else:
            return self.model.objects.all()

class Clusterstatus_createViewSet(Base_CreateViewSet):
    model = Cluster_status
    form_class = Cluster_statusForm
    template_name = 'components/cluster_status_form.html'
    success_url = reverse_lazy('cluster-status-list')

class Clusterstatus_updateViewSet(Base_UpdateViewSet):
    model = Cluster_status
    form_class = Cluster_statusForm
    template_name = 'components/cluster_status_form.html'
    success_url = reverse_lazy('cluster-status-list')

class Clustertag_listViewSet(Base_ListViewSet):
    Cluster_tag.objects.all().count()
    model = Cluster_tag
    template_name = 'components/cluster_tag.html'
    paginate_by = 10

    def get_queryset(self):
        try:
            name=self.request.GET['keyword']
        except:
            name=None
        if name:
            return self.model.objects.filter(name__icontains=name)
        else:
            return self.model.objects.all()

class Clustertag_createViewSet(Base_CreateViewSet):
    model = Cluster_tag
    form_class = Cluster_tagForm
    template_name = 'components/cluster_tag_form.html'
    success_url = reverse_lazy('cluster-tag-list')

class Clustertag_updateViewSet(Base_UpdateViewSet):
    model = Cluster_tag
    form_class = Cluster_tagForm
    template_name = 'components/cluster_tag_form.html'
    success_url = reverse_lazy('cluster-tag-list')
