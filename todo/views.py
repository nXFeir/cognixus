from django.http import QueryDict
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

from todo.models import TodoItem

from .serializers import TodoSerializer


class TodoList(generics.ListCreateAPIView):
    """
    GET: get list of todo by user
    POST: create a new todo
    """
    permission_classes = [IsAuthenticated]
    serializer_class = TodoSerializer

    def get_queryset(self):
        qs = TodoItem.objects.filter(user=self.request.user)
        return qs
    
    def post(self, request, *args, **kwargs):
        if isinstance(request.data, QueryDict):
            request.data._mutable = True
        request.data.update({'user': request.user.uuid})
        return self.create(request, *args, **kwargs)
    
class TodoDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    GET: get a todo
    PUT: update a todo
    DELETE: delete a todo
    """
    permission_classes = [IsAuthenticated]
    serializer_class = TodoSerializer

    def get_queryset(self):
        qs = TodoItem.objects.filter(user=self.request.user)
        return qs
    
    def put(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
    
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def mark_todo_item_completed(request, pk):
    todo = get_object_or_404(TodoItem, uuid=pk, user=request.user)
    todo.is_completed = True
    todo.save()
    return Response(TodoSerializer(todo).data, 200)
