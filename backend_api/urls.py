from django.conf.urls import url
from backend_api import views

urlpatterns = [
    url(r'^api/product$', views.product),
    url(r'^api/product/(?P<pk>[0-9]+)$', views.product_detail),
]