from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^persona_listar$', views.persona_list, name='persona_listar'),
    url(r'^persona_album$', views.persona_album, name='persona_album'),
    url(r'^persona_nuevo$', views.persona_add, name='persona_nuevo'),
    url(r'^persona_editar/(?P<id_persona>\d+)/$', views.persona_edit, name='persona_editar'),
    url(r'^empresa_listar$', views.empresa_list, name='empresa_listar'),
    url(r'^locacion_listar$', views.locacion_list, name='locacion_listar'),
]
