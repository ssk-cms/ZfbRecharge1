from django.conf.urls import url,include
from users.views import *
urlpatterns = [
    url(r'^login/$', Login_views,name='login'),
    url(r'^register/$', Register_views,name='register'),
    url(r'^logout/$',Logout_views,name='logout'),
    url(r'^detail_login/$',Detail_views,name='detail')
]