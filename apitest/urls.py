from django.conf.urls import url
from . import views

app_name = 'apitest'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^testing/$', views.testing, name='testing'),
    url(r'^returnShares/$', views.returnShares, name='returnShares'),
    url(r'^delete-shares/$', views.delete_shares, name='delete_shares'),
    url(r'^delete-user-mappings/$', views.delete_user_mappings, name='delete_user_mappings'),
    url(r'^delete-users/$', views.delete_users, name='delete_users'),
]