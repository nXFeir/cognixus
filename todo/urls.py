from django.urls import path, include

from .views import TodoList, TodoDetail

apiURL = [
    path('todo', TodoList.as_view(), name='todolist'),
    path('todo/<uuid:pk>', TodoDetail.as_view(), name='tododetail'),
]

urlpatterns = [
    path('api/',  include(apiURL)),
]