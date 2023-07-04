from django.urls import path, include

from .views import TodoList, TodoDetail, mark_todo_item_completed

apiURL = [
    path('todo', TodoList.as_view(), name='todolist'),
    path('todo/<uuid:pk>', TodoDetail.as_view(), name='tododetail'),
    path('todo/mark_completed/<uuid:pk>', mark_todo_item_completed, name='mark_todo_item_completed'),

]

urlpatterns = [
    path('api/',  include(apiURL)),
]