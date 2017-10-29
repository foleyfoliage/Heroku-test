from django.conf.urls import url
from . import views

app_name = 'product'


urlpatterns = [
    # /juice/
    url(r'^$', views.IndexView.as_view(), name='index'),

    url(r'^register$', views.UserFormView.as_view(), name='register'),

    # /juice/<product id/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name="detail"),

    # Create new
    url(r'flavour/add/$', views.FlavourCreate.as_view(), name='flavour-add'),

    # edit
    url(r'flavour/(?P<pk>[0-9]+)/$', views.FlavourUpdate.as_view(), name='flavour-update'),

    # delete pk
    url(r'flavour/(?P<pk>[0-9]+)/FlavourDelete/$', views.FlavourDelete.as_view(), name='FlavourDelete'),



]



