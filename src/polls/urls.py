from django.urls import path
from .views import (
    PollDetailView,
    PollListView,
    # MyListView,
    PollCreateView,
    PollUpdateView,
    PollDeleteView
    # my_fbv
)

app_name = 'polls'
urlpatterns = [
    path('', PollListView.as_view(), name='polls-list'),
    # path('', my_fbv, name='Polls-list'),

    path('create/', PollCreateView.as_view(), name='polls-create'),
    path('<int:id>/', PollDetailView.as_view(), name='polls-detail'),
    path('<int:id>/update/', PollUpdateView.as_view(), name='polls-update'),
    path('<int:id>/delete/', PollDeleteView.as_view(), name='polls-delete')

]
