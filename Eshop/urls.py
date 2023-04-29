
from django.contrib import admin
from django.urls import path,include

# For Static Files 
from django.conf.urls.static import static
from . import settings

urlpatterns = [
    path("admin/", admin.site.urls),
	path("",include('store.urls'))
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
