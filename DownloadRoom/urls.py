from django.urls import path
from django.conf.urls import include
from . import views

urlpatterns = [
    path("DownloadFresh/", views.download_trigger, name="DownloadRoom"),
   
]