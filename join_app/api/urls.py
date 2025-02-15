from django.urls import include, path
from .views import TaskList, TaskDetail, ContactList, ContactDetail, SubtaskList, SubtaskDetail

urlpatterns = [
    path('tasks/', TaskList.as_view(), name='task-list'),
    path('tasks/<int:pk>/', TaskDetail.as_view(), name='task-detail'),
    path('contacts/', ContactList.as_view(), name='user-list'),
    path('contacts/<int:pk>/', ContactDetail.as_view(), name='user-detail'),
    path('subtasks/', SubtaskList.as_view(), name='subtask-list'),
    path('subtasks/<int:pk>', SubtaskDetail.as_view(), name='subtask-detail'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
