from django.conf.urls import url
from . import views          
urlpatterns = [
    url(r'^$', views.index),
    url(r'semi_users/new$', views.new),
    url(r'semi_users/create$', views.create),
    url(r'semi_users$', views.users), 
    url(r'semi_users/edit/(?P<user_id>\d+)$', views.edit),
    url(r'semi_users/show/(?P<user_id>\d+)$', views.show),
    url(r'semi_users/delete/(?P<user_id>\d+)$', views.delete),
    url(r'semi_users/update/(?P<user_id>\d+)$', views.update)

]


