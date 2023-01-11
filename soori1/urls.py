
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('src.user.urls')),
    path('api-auth/', include('rest_framework.urls')),
    
]
