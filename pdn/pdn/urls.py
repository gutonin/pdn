from django.conf.urls import url, include 
from django.contrib import admin
from filebrowser.sites import site
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'admin/filebrowser/', site.urls),
    url(r'^summernote/', include('django_summernote.urls')),
    url(r'grappelli/', include('grappelli.urls')),
    url(r'^admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
