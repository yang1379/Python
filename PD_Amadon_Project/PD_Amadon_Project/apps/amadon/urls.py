from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^buy/(?P<item_id>\d+)$', views.buy),
    url(r'^amadon/checkout$', views.checkout),
    url(r'^checkout$', views.checkout),
    url(r'^$', views.index)
]