from django.urls import path
from .views import (
    PollDetailView,
    # my_fbv
)

app_name = 'polls'
urlpatterns = [
    path('', PollDetailView.as_view(template_name='contact.html'), name='Polls-list'),
    # path('', my_fbv, name='Polls-list'),

    # path('create/', <>, name='polls-create'),
    path('<int:id>/', PollDetailView.as_view(), name='polls-detail'),
    # path('<int:id>/update/', <>, name='polls-delete'),
    # path('<int:id>/delete/', <>, name='polls-delete')

]
