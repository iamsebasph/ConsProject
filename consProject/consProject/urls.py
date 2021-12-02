
from django.contrib import admin
from django.urls import path
from inventario import views
from django.conf.urls.static import static
from django.conf import settings

app_name = "inventario"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cathalogue', views.list, name= 'catalogoProductos'),
    path('save', views.save, name= 'saveProd'),
    path('contact', views.contact, name= 'contacto'),
    path('admin', views.admin, name= 'administador'),
    path('', views.index, name= 'inicio')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
