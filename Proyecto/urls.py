from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin

from web import views
from web.views import volar

urlpatterns = [
                  url(r'^', include('web.urls')),
                  url(r'^admin/', admin.site.urls),
                  url(r'^inicio/$', views.inicio, name='inicio'),
                  url(r'^acerca/$', views.acerca, name='acerca'),
                  url(r'^volar/$', views.volar, name='volar'),
                  url(r'^comentario/$', views.comentario, name='comentario'),
                  url(r'^destino/$', views.destino, name='destino'),
                  url(r'^contacto/$', views.contacto, name='contacto'),
                  url(r'^conocoto/$', views.conocoto, name='conocoto'),
                  url(r'^h/$', views.historia, name='historia'),
                  url(r'^g/$', views.galeria, name='galeria'),
                  url(r'^c/$', views.comentarioC, name='comentarioC'),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
