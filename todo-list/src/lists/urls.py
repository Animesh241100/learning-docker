from django.urls import path
from .views import (
    GetTasksList,
    CreateTask,
    UpdateTask,
    DeleteTask
)

app_name = 'lists'

urlpatterns = [
    path('get-task-list/', GetTasksList.as_view()),
    path('create-task/', CreateTask.as_view()),
    path('update-task/', UpdateTask.as_view()),
    path('delete-task/', DeleteTask.as_view()),
]