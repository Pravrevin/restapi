from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from MLMAPP import views

urlpatterns = [
    path('registration/', views.SnippetList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)