from django.conf.urls import url
from . import views


urlpatterns = [
# personas
    url(r'^$', views.persona_album, name='index'),
    url(r'^persona_listar$', views.persona_list, name='persona_listar'),
    url(r'^persona_album$', views.persona_album, name='persona_album'),
    url(r'^persona_nuevo$', views.persona_add, name='persona_nuevo'),
    url(r'^persona_editar/(?P<id_persona>\d+)/$', views.persona_edit, name='persona_editar'),
    url(r'^persona_eliminar/(?P<id_persona>\d+)/$', views.persona_delete, name='persona_eliminar'),

    url(r'^persona_album2$', views.persona_album2, name='persona_album2'),
# empresa
    url(r'^empresa_listar$', views.empresa_list, name='empresa_listar'),
    url(r'^empresa_nuevo$', views.empresa_add, name='empresa_nuevo'),
    url(r'^empresa_editar/(?P<id_empresa>\d+)/$', views.empresa_edit, name='empresa_editar'),
    url(r'^empresa_eliminar/(?P<id_empresa>\d+)/$', views.empresa_delete, name='empresa_eliminar'),
# locacion
    url(r'^locacion_listar$', views.locacion_list, name='locacion_listar'),
    url(r'^locacion_nuevo$', views.locacion_add, name='locacion_nuevo'),
    url(r'^locacion_editar/(?P<id_locacion>\d+)/$', views.locacion_edit, name='locacion_editar'),
    url(r'^locacion_eliminar/(?P<id_locacion>\d+)/$', views.locacion_delete, name='locacion_eliminar'),
]
