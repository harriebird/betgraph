from django.urls import path, include
from . import views

app_name = 'webapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('api/', include('betgraph.webapp.api.urls'), name='rest_api')
]
