from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^regcar/$', views.regcar, name='regcar')
]


