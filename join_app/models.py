from django.db import models
from join_auth_app.models import CustomUser
# Create your models here.

class Contact(models.Model):
  user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='contacts')
  name = models.CharField(max_length=225)
  email = models.EmailField(unique=True)
  phone = models.CharField(max_length=225)
  initials = models.CharField(max_length=5, blank=True)
  color = models.CharField(max_length=225)

  def __str__(self):
    return f'{self.name}'

class Task(models.Model):

  PRIORITY_CHOICES = [
    ('urgent', 'Urgent'),
    ('medium', 'Medium'), 
    ('low', 'Low')
  ]

  CATEGORY_CHOICES = [
    ('technical task', 'Technical Task'),
    ('user story', 'User Story')
  ]

  COLUMN_CHOICES = [
    ('to-do', 'To do'),
    ('in-progress', 'In Progress'),
    ('await-feedback', 'Await feedback'),
    ('done', 'Done')
  ]


  title = models.CharField(max_length=225)
  board_category = models.CharField(max_length=225, choices=COLUMN_CHOICES)
  description = models.CharField(max_length=225)
  assignees = models.ManyToManyField(Contact, related_name='tasks')
  date = models.CharField(max_length=225)
  priority = models.CharField(max_length=225, choices=PRIORITY_CHOICES)
  category = models.CharField(max_length=225, choices=CATEGORY_CHOICES)

  def __str__(self):
    return f'{self.title}'
  

class SubTask(models.Model):
  title = models.CharField(max_length=225)
  completed = models.BooleanField(default=False)
  task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='subtasks')

  def __str__(self):
    return self.title