from django.conf.urls import url
from . import views

# urls/rotas "locais" dos modulos criados
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^details/(?P<id>\d+)/$', views.details, name='details'),
    url(r'^add', views.add, name='add')
]