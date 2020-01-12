from django.urls import path
from . import views

urlpatterns = [
    path('group/', views.GroupList.as_view()),
    path('groupviewid/', views.GroupViewData.as_view()),
    #path('groupview/<int:pk>/', views.GroupViewForUsers.as_view()),

]
