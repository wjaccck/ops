#coding=utf-8
from __future__ import unicode_literals

from django.db import models
from abstract.models import CommonModel,UniqueNameDescModel,NameModel,COMPONENTS_BASE

class Ipv4Address(UniqueNameDescModel):

    class Meta:
        ordering = ['name', ]

class Ipv4Network(UniqueNameDescModel):
    gateway = models.CharField(max_length=18, null=True)

    class Meta:
        ordering = ['name', ]

class Machine_status(NameModel,COMPONENTS_BASE):
    class Meta:
        verbose_name='物理机状态'

class Resource_status(NameModel,COMPONENTS_BASE):
    class Meta:
        verbose_name='资源状态'

class Cluster_status(NameModel,COMPONENTS_BASE):
    class Meta:
        verbose_name='集群状态'

class Machine_tag(NameModel,COMPONENTS_BASE):
    class Meta:
        verbose_name='物理机标签'

class Resource_tag(NameModel,COMPONENTS_BASE):
    class Meta:
        verbose_name='资源标签'

class Cluster_tag(NameModel,COMPONENTS_BASE):
    class Meta:
        verbose_name='集群标签'
