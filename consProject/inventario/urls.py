from django.contrib import admin
from django.urls import path, include

app_name = "inventario"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inventario/', include('inventario.urls', namespace="inventario"))
]
