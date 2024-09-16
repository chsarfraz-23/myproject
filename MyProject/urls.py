from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path

from MyProject import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('myapp/', include('myapp.urls')),
    re_path(r'^auth/', include('drf_social_oauth2.urls', namespace='drf'))
]


urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
