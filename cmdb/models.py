from django.db import models
from abstract.models import CommonModel,CMDB_BASE
from components.models import *
class Machine(CommonModel,CMDB_BASE):
    console_ip=models.OneToOneField(Ipv4Address,related_name='console_ip')
    ipv4=models.ManyToManyField(Ipv4Address,blank=True)
    cpu=models.CharField(max_length=100,blank=True)
    kernel=models.CharField(max_length=100,blank=True)
    cpu_number=models.IntegerField(blank=True,null=True)
    vcpu_number=models.IntegerField(blank=True,null=True)
    cpu_core=models.IntegerField(blank=True,null=True)
    hostname=models.CharField(max_length=100,blank=True)
    memory=models.IntegerField(blank=True,null=True)
    disk=models.CharField(max_length=100,blank=True)
    swap=models.CharField(max_length=100,blank=True)
    product = models.CharField(max_length=100, verbose_name=u'服务器类型', blank=True)
    selinux = models.CharField(max_length=10, blank=True)
    distribution=models.CharField(max_length=25, blank=True)
    distribution_version=models.CharField(max_length=25,blank=True)
    manufacturer=models.CharField(max_length=25, blank=True)
    serial = models.CharField(max_length=10, blank=True,db_index=True)
    status=models.ForeignKey(Machine_status)
    tag=models.ManyToManyField(Machine_tag,blank=True)
    def __str__(self):
        return self.console_ip.name

    class Meta:
        verbose_name=u'服务器信息'