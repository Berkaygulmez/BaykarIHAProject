
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from sample.views import index

urlpatterns = [
    path('admin/', admin.site.urls),     # Bu URL, Django admin arayüzüne yönlendirir. 
    path('', index, name='index'),       #  Ana dizine yapılan istekler, index view fonksiyonunu çalıştırır. 
]

# Django'nun MEDIA_URL'yi ve MEDIA_ROOT'u kullanarak medya dosyalarına erişim sağlamasını sağlar.
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# Django'nun STATIC_URL'yi ve STATIC_ROOT'u kullanarak statik dosyalara erişim sağlamasını sağlar. 
urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)