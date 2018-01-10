from django.conf.urls import include, url
# from django.contrib import admin
from cmdb import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    ### machine_status
    url(r'^machine/$',login_required(views.Machine_listViewSet.as_view()),name='machine-list'),
    url(r'^machine/update/(?P<pk>\d+)/$',login_required(views.Machine_updateViewSet.as_view()),name='machine-update'),
    url(r'^machine/create/$',login_required(views.Machine_createViewSet.as_view()),name='machine-create'),

]
