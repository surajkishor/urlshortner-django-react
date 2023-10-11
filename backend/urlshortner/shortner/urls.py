from django.urls import path
from .views import *

urlpatterns = [
    path("", shorten_url.as_view(), name='shorten_url'),
    path("<str:short_code>", redirect_url.as_view(), name='redirect_url')
]