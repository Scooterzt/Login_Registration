from django.conf.urls import url, include
from . import views


urlpatterns = [
    url(r'^$', views.index),
    url(r'^success$', views.success),
    url(r'^registration$', views.registration),
    url(r'^login$', views.login),
    url(r'^log_out$', views.log_out),

]