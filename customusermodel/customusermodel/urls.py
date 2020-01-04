from django.conf.urls import url
from django.contrib import admin
from django.urls import path,include
from rest_framework.authtoken import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('get-user-auth-token/', views.obtain_auth_token, name='get_user_auth_token'),
    path('', include('accounts.urls')),
]
