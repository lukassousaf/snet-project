from django.conf.urls import url
from django.urls import path
from allauth.account.views import LoginView, SignupView


from . import views

app_name = "pages"

urlpatterns = [
    path("", views.HomePageView.as_view(), name="home"),

]
