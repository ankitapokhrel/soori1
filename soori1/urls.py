
from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('src.user.urls')),
    path('solution/', include('src.solution.urls')),
    path('blog/', include('src.blog.urls')),
    path('contact/', include('src.contact.urls')),
    path('aboutus/', include('src.aboutus.urls')),
    path('gallery/', include('src.gallery.urls')),
    path('brandname/', include('src.brandname.urls')),
    path('technology/', include('src.technology.urls')),

    path('api-auth/', include('rest_framework.urls')),

    path('api/', SpectacularAPIView.as_view(), name='schema'),
    path('api/doc/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    
]
