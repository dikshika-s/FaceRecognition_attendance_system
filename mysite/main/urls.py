from django.urls import path
from . import views
from django.conf.urls.static import static
from mysite import settings

urlpatterns = [
path("", views.home, name="home"),
path("view/", views.view, name="index"),
path("home/", views.home, name="home"),
path("r_form/", views.register_form, name="upload"),
path('run_graph', views.run_graph),
path('upload', views.upload),
]+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)