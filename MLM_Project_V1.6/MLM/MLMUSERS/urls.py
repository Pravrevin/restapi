from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.PhotoList.as_view()),

]
