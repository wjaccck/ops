from django.db import models


# Base models that have some common fields.

class CommonModel(models.Model):
    # Meta data for one object.
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class NameModel(models.Model):
    name = models.CharField(max_length=50)
    alias = models.CharField(max_length=50)
    # Meta data for one object.
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name

class UniqueNameDescModel(models.Model):
    name = models.CharField(max_length=80, unique=True)
    description = models.CharField(max_length=255, null=True)
    # Meta data for one object.
    creator = models.ForeignKey('auth.user', related_name='%(app_label)s_%(class)s_creator', verbose_name='creator',on_delete=models.CASCADE)
    last_modified_by = models.ForeignKey('auth.user', related_name='%(app_label)s_%(class)s_last_modified_by', verbose_name='last modified by',on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name

class API_BASE(models.Model):
    pass
    @staticmethod
    def father():
        return u'api'

    class Meta:
        abstract=True


class COMPONENTS_BASE(models.Model):
    pass
    @staticmethod
    def father():
        return u'components'

    class Meta:
        abstract=True

class IDC_BASE(models.Model):
    pass
    @staticmethod
    def father():
        return u'idc'

    class Meta:
        abstract=True

class ITEM_BASE(models.Model):
    pass
    @staticmethod
    def father():
        return u'item'

    class Meta:
        abstract=True

class APPLY_BASE(models.Model):
    pass
    @staticmethod
    def father():
        return u'apply'

    class Meta:
        abstract=True


class HISTORY_BASE(models.Model):
    pass
    @staticmethod
    def father():
        return u'history'

    class Meta:
        abstract=True


class PUBLISH_BASE(models.Model):
    pass
    @staticmethod
    def father():
        return u'publish'

    class Meta:
        abstract=True