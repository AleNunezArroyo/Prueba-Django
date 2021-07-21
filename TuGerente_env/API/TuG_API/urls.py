from django.urls import path
from .views import PersonListView, PersonDetailView, StateListView
urlpatterns = [
    path('person/', PersonListView.as_view(), name ='person_list'),
    path('estado/', StateListView.as_view(), name ='person_list'),
    path('person/<int:pk>/', PersonDetailView.as_view(), name ='person'),
]