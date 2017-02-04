from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^persona_listar$', views.persona_list, name='persona_listar'),
    url(r'^persona_album$', views.persona_album, name='persona_album'),
]
