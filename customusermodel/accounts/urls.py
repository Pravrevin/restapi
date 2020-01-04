from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('registration/', views.Registration.as_view()),
    path('login/',obtain_auth_token,name='login')
]

#urlpatterns = format_suffix_patterns(urlpatterns)