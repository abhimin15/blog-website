from django.conf.urls import url
from blog import views
from blog import models
urlpatterns = [

    url(r'^$',views.index, name='index'),
    url(r'^register/$',views.UserFormView.as_view(), name='register'),
    url(r'^addpost/$',views.postCreate.as_view(), name='add_post'),
    url(r'^(?P<album_id>[0-9]+)/$',views.detail, name='detail'),
]