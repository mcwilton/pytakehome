from django.conf.urls import url
from . import views

app_name = 'mymodule' # So we can use it like: {% url 'mymodule:user_register' %} on our template.

urlpatterns = [

    url(r'^register/$', views.user_register, name='user_register')
    url(r'^login/$', views.user_login, name='user_login')
]