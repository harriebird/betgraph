from django.urls import path
from . import views as api_views

urlpatterns = [
    path('', api_views.IndexAPIView.as_view(), name='api_index'),
    path('persons/<str:username>', api_views.PersonDetailView.as_view(), name='person_detail'),
    path('new-entry', api_views.NewEntryView.as_view(), name='new_entry')
]
