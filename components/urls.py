from django.conf.urls import include, url
# from django.contrib import admin
from components import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    ### machine_status
    url(r'^machine-status/$',login_required(views.Machinestatus_listViewSet.as_view()),name='machine-status-list'),
    url(r'^machine-status/update/(?P<pk>\d+)/$',login_required(views.Machinestatus_updateViewSet.as_view()),name='machine-status-update'),
    url(r'^machine-status/create/$',login_required(views.Machinestatus_createViewSet.as_view()),name='machine-status-create'),

    ### machine_tag
    url(r'^machine-tag/$', login_required(views.Machinetag_listViewSet.as_view()), name='machine-tag-list'),
    url(r'^machine-tag/update/(?P<pk>\d+)/$', login_required(views.Machinetag_updateViewSet.as_view()),
        name='machine-tag-update'),
    url(r'^machine-tag/create/$', login_required(views.Machinetag_createViewSet.as_view()),
        name='machine-tag-create'),

    ### resource_status
    url(r'^resource-status/$', login_required(views.Resourcestatus_listViewSet.as_view()), name='resource-status-list'),
    url(r'^resource-status/update/(?P<pk>\d+)/$', login_required(views.Resourcestatus_updateViewSet.as_view()),
        name='resource-status-update'),
    url(r'^resource-status/create/$', login_required(views.Resourcestatus_createViewSet.as_view()),
        name='resource-status-create'),

    ### resource_tag
    url(r'^resource-tag/$', login_required(views.Resourcetag_listViewSet.as_view()), name='resource-tag-list'),
    url(r'^resource-tag/update/(?P<pk>\d+)/$', login_required(views.Resourcetag_updateViewSet.as_view()),
        name='resource-tag-update'),
    url(r'^resource-tag/create/$', login_required(views.Resourcetag_createViewSet.as_view()),
        name='resource-tag-create'),

    ### cluster_status
    url(r'^cluster-status/$', login_required(views.Clusterstatus_listViewSet.as_view()), name='cluster-status-list'),
    url(r'^cluster-status/update/(?P<pk>\d+)/$', login_required(views.Clusterstatus_updateViewSet.as_view()),
        name='cluster-status-update'),
    url(r'^cluster-status/create/$', login_required(views.Clusterstatus_createViewSet.as_view()),
        name='cluster-status-create'),

    ### resource_tag
    url(r'^cluster-tag/$', login_required(views.Clustertag_listViewSet.as_view()), name='cluster-tag-list'),
    url(r'^cluster-tag/update/(?P<pk>\d+)/$', login_required(views.Clustertag_updateViewSet.as_view()),
        name='cluster-tag-update'),
    url(r'^cluster-tag/create/$', login_required(views.Clustertag_createViewSet.as_view()),
        name='cluster-tag-create'),

]
