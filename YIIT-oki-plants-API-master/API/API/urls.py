from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('APIapp.urls')),
    path('tinymce/', include('tinymce.urls')),
    path('', include('djoser.urls')),
    path('', include('djoser.urls.authtoken')),
]
