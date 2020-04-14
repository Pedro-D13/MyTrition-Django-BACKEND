from django.db import models



# Create your models here.
class TodoList(models.Model):
    title = models.CharField(max_length = 50)

    def __str__(self):
        return f"{self.title}"

class Items(models.Model):
    todolist = models.ForeignKey(TodoList, on_delete=models.CASCADE)
    item = models.CharField(max_length = 50)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f'{self.item}'


class Habit(models.Model):
    # a habit has a title, and can be linked to a todolist
    title = models.CharField(max_length=50)
    todolist_link = models.ForeignKey(TodoList,models.SET_NULL,blank=True,null=True)

    def __str__(self):
        return f'{self.title}'




''' 
Get Habit, Which may have a todlist_link, with that we can get the obj by 

tdl = Habit_obj.todolist_link 

TodoList_obj = TodoList.objects.get(id=tdl.id)

TodoList_obj.items_set.all() --- gives us the list of items associated with that todolist

'''

