from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from rest_framework import status
from rest_framework.test import APIClient

from todo.models import TodoItem
from users.models import User


class TodoListAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.force_authenticate(user=self.user)
    
    def test_unauthenticated_user_access(self):
        # create a dummy todo
        todo = TodoItem.objects.create(user=self.user, title='Test Task', start_time=timezone.now())

        # create a new client without authenticating the user
        unauthenticated_client = APIClient()

        # get request
        response = unauthenticated_client.get(reverse('todolist'))

        # check output
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_todo_list_get(self):
        # create some dummy todo
        todo1 = TodoItem.objects.create(user=self.user, title='Todo 1', start_time=timezone.now())
        todo2 = TodoItem.objects.create(user=self.user, title='Todo 2', start_time=timezone.now())

        # get request
        response = self.client.get(reverse('todolist'))

        # check output
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_todo_list_post(self):
        # post request
        data = {'title': 'New Task', 'start_time': timezone.now()}
        response = self.client.post(reverse('todolist'), data=data)

        # check output
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Check that the todo item was created in the database
        self.assertTrue(TodoItem.objects.filter(user=self.user, title='New Task').exists())

class TodoDetailAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.force_authenticate(user=self.user)
        self.todo = TodoItem.objects.create(user=self.user, title='Task', start_time=timezone.now())
    
    def test_unauthenticated_user_access(self):
        # create a dummy todo
        todo = TodoItem.objects.create(user=self.user, title='Test Task', start_time=timezone.now())

        # create a new client without authenticating the user
        unauthenticated_client = APIClient()

        # get request
        response = unauthenticated_client.get(reverse('tododetail', args=[self.todo.uuid]))

        # check output
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_todo_detail_get(self):
        # get request
        response = self.client.get(reverse('tododetail', args=[self.todo.uuid]))

        # check output
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Task')

    def test_todo_detail_put(self):
        # put request
        data = {'title': 'Updated Task'}
        response = self.client.put(reverse('tododetail', args=[self.todo.uuid]), data=data)

        # check output
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Refresh db
        self.todo.refresh_from_db()

        # Check that the todo item was updated in the database
        self.assertEqual(self.todo.title, 'Updated Task')

    def test_todo_detail_delete(self):
        # delete request
        response = self.client.delete(reverse('tododetail', args=[self.todo.uuid]))

        # check output
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Check that the todo item was deleted from the database
        self.assertFalse(TodoItem.objects.filter(user=self.user, uuid=self.todo.uuid).exists())


class MarkTodoItemCompletedTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.force_authenticate(user=self.user)
        self.todo = TodoItem.objects.create(user=self.user, title='Task', start_time=timezone.now())

    def test_mark_todo_item_completed(self):
        # put request
        response = self.client.put(reverse('mark_todo_item_completed', args=[self.todo.uuid]))

        # Refresh db
        self.todo.refresh_from_db()

        # check output
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(self.todo.is_completed)
    
