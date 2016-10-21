from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$',views.register),
    url(r'^success$',views.success),
    url(r'^login$',views.login),
    url(r'^wish_items/create$', views.wish_items_create),
    url(r'^product_process$', views.product_process),
    url(r'^home$',views.home),
    url(r'^logout$',views.logout),
    url(r'^remove/(?P<id>\d+)$',views.remove),
    url(r'^wish_items/(?P<id>\d+)$',views.show)
    
]