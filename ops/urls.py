"""ops URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from rest_framework.authtoken import views
from django.conf import settings
if settings.DEBUG:
    import debug_toolbar

from rest_framework_swagger.views import get_swagger_view
from django.contrib.auth.views import login,logout
from webui.forms import LoginForm
schema_view = get_swagger_view(title='Pastebin API')

admin.autodiscover()


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^__debug__/', include(debug_toolbar.urls)),
    url(r'^api/token/', views.obtain_auth_token),
    url(r'^api/api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^components/', include('components.urls')),
    url(r'^cmdb/', include('cmdb.urls')),
    url(r'^api/', include('api.urls')),
    url(r'^ui/', include('webui.urls')),
    url(r'^swagger/', schema_view),
    # Django Select2
    url(r'^select2/', include('django_select2.urls')),
    url(r'^login/$',
        login,
        {
            'template_name': 'webui/login.html',
            'authentication_form': LoginForm,

        },
        name='login', ),

    url(r'^logout/$',
        logout,
        {
            'next_page': '/ui/',
        },
        name='logout'),
]