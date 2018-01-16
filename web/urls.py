from django.conf.urls import url
from web import views
from web.views import volar
"""
urlpatterns = [
    url(r'^$', volar),

]

"""

urlpatterns = [

    url(r'^$', views.inicio, name='inicio'),
    url(r'^$', views.acerca, name='acerca'),
    url(r'^volar/$', views.volar, name='volar'),
    url(r'^$', views.comentario, name='comentario'),
    url(r'^$', views.destino, name='destino'),
    url(r'^$', views.contacto, name='contacto'),
    url(r'^$', views.conocoto, name='conocoto'),
    url(r'^$', views.historia, name='historia'),
    url(r'^$', views.galeria, name='galeria'),
    url(r'^$', views.comentarioC, name='comentarioC'),
]
