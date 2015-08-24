from django.conf.urls import url

from . import views  # Import the views for this app


urlpatterns = [
    url(r'^$', views.index, name='index'),  # Url for index view
]
