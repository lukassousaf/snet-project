from django.conf.urls import url
from django.urls.conf import path
from . import views
from .views import *

app_name = "client"

urlpatterns = [
    path("", views.ClientFormView.as_view(), name="client"),
    url(r'^client_list/', client_list, name="client_list"),
    url(r'^client_new/', client_new, name="client_new"),
    url(r'^client_edit/(?P<pk>[0-9]+)', client_edit, name="client_edit"),
    url(r'^client_remove/(?P<pk>[0-9]+)', client_remove, name="client_remove"),

]
