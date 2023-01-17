from django.urls import path
from page.views import nout,about
urlpatterns=[
    path('nout', nout, name='nout'),
    path('about', about, name='about')
    
]