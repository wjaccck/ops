#coding=utf-8
from __future__ import unicode_literals

from django.db import models
from abstract.models import CommonModel,UniqueNameDescModel

class Ipv4Address(UniqueNameDescModel):

    class Meta:
        ordering = ['name', ]

class Ipv4Network(UniqueNameDescModel):
    gateway = models.CharField(max_length=18, null=True)

    class Meta:
        ordering = ['name', ]

class Machine_status(CommonModel):
    name=models.CharField(max_length=10)
    alias=models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Resource_status(CommonModel):
    name = models.CharField(max_length=10)
    alias = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Cluster_status(CommonModel):
    name = models.CharField(max_length=10)
    alias = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Machine_tag(CommonModel):
    name = models.CharField(max_length=10)
    alias = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Resource_tag(CommonModel):
    name = models.CharField(max_length=10)
    alias = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Cluster_tag(CommonModel):
    name = models.CharField(max_length=10)
    alias = models.CharField(max_length=10)

    def __str__(self):
        return self.name
