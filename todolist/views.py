from django.shortcuts import render,get_object_or_404
from django.http import Http404


from rest_framework import permissions,  generics, status, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializer import TodoListSerializer, ItemsSerializer, HabitSerializer

from .models import TodoList,Habit,Items


class HabitListViewSet(viewsets.ModelViewSet):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permissions_class = [permissions.AllowAny]
    
class HabitDetailViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    lookup_url_kwarg = 'habit_id'

# Viewset and methods for List
class TodoListViewSet(viewsets.ModelViewSet):
    queryset = TodoList.objects.all().order_by('-id')
    serializer_class = TodoListSerializer
    permissions_classes = [permissions.AllowAny]

class TodoListDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TodoList.objects.all()
    serializer_class = TodoListSerializer
    lookup_url_kwarg = 'todolist_id'

# Viewset and methods for item
class ItemsListViewSet(viewsets.ModelViewSet):
    queryset = Items.objects.all().order_by('-id')
    serializer_class = ItemsSerializer
    permissions_classes = [permissions.AllowAny]




class ItemCRUDViewset(generics.RetrieveUpdateDestroyAPIView):
    queryset = Items.objects.all()
    serialize_class = ItemsSerializer




''' 
Get Habit, Which may have a todlist_link, with that we can get the obj by 

tdl = Habit_obj.todolist_link 

TodoList_obj = TodoList.objects.get(id=tdl.id)

TodoList_obj.items_set.all() --- gives us the list of items associated with that todolist

'''