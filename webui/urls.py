from django.conf.urls import include, url
# from django.contrib import admin
from webui import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    ### machine_status
    url(r'^$',login_required(views.IndexViews.as_view()),name='index'),
    ]
