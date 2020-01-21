from django.urls import path
from . import views

urlpatterns = [
    path('helpdesk/<int:pk>/', views.TicketList.as_view()),

]
