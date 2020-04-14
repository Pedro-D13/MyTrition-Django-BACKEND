from .models import TodoList, Items, Habit

from rest_framework import serializers


class TodoListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TodoList
        fields = ['id','title']

class ItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model =Items
        fields = ['id','todolist', 'item','notes']

class HabitSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Habit
        fields = ['id','title','todolist_link']