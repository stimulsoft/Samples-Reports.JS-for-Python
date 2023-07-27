from django.urls import path
from webapp import views

urlpatterns = [
    path("", views.home, name="home"),
    path("viewer", views.viewer, name="viewer"),
    path("designer", views.designer, name="designer"),
]