from rest_framework import generics
from join_app.models import Task, Contact, SubTask
from .serializers import TaskSerializer, ContactSerializer, SubtaskSerializer
from rest_framework.permissions import AllowAny

class TaskList(generics.ListCreateAPIView):
  queryset = Task.objects.all()
  serializer_class = TaskSerializer

class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Task.objects.all()
  serializer_class = TaskSerializer

class ContactList(generics.ListCreateAPIView):
  queryset = Contact.objects.all()
  serializer_class = ContactSerializer
  permission_classes = [AllowAny]

class ContactDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Contact.objects.all()
  serializer_class = ContactSerializer

class SubtaskList(generics.ListCreateAPIView):
  queryset = SubTask.objects.all()
  serializer_class = SubtaskSerializer

class SubtaskDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = SubTask.objects.all()
  serializer_class = SubtaskSerializer