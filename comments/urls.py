from django.urls import path
from .import views

urlpatterns = [
    path('', views.showComments, name="home"),
    path('write', views.WriteReview, name="write-reviews"),
]
