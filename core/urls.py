from django.contrib import admin
from django.urls import path, include  # <-- Agrega 'include' aquí para gestionar el ckeditor_uploader
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # Ruta para el administrador
    path('admin/', admin.site.urls),

    # Ruta para el ckeditor_uploader
    # Agrega esta línea para que no haya ningún problema con la ruta del ckeditor_uploader
    path('ckeditor/', include('ckeditor_uploader.urls')),  

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
