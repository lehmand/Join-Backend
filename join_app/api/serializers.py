from rest_framework import serializers
from join_app.models import Task, Contact, SubTask

class SubtaskSerializer(serializers.ModelSerializer):
  
  class Meta:
    model = SubTask
    fields = ['id', 'title', 'completed']

class ContactSerializer(serializers.ModelSerializer):
  class Meta:
    model = Contact
    fields = ['id', 'user', 'name', 'email', 'phone']

class TaskSerializer(serializers.ModelSerializer):
  subtasks = SubtaskSerializer(many=True)
  assignees = ContactSerializer(many=True, read_only=True)
  assignees_ids = serializers.PrimaryKeyRelatedField(queryset=Contact.objects.all(), many=True, write_only=True)

  class Meta:
    model = Task
    fields = '__all__'


  def create(self, validated_data):
    subtasks_data = validated_data.pop('subtasks', [])
    assignees_data = validated_data.pop('assignees_ids', [])

    task = Task.objects.create(**validated_data)

    for subtask_data in subtasks_data:
      SubTask.objects.create(task=task, **subtask_data)

    task.assignees.set(assignees_data)

    return task
  
  def update(self, instance, validated_data):
    subtasks_data = validated_data.pop('subtasks', [])
    assignees_data = validated_data.pop('assignees_ids', [])

    instance = super().update(instance, validated_data)

    instance.subtasks.all().delete()

    for subtask_data in subtasks_data:
        SubTask.objects.create(task=instance, **subtask_data)

    instance.assignees.set(assignees_data)
    return instance
