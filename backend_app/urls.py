"""backend_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from todolist import views

router = routers.DefaultRouter()
router.register(r'todolist', views.TodoListViewSet)
router.register(r'items', views.ItemsListViewSet)
router.register(r'habit', views.HabitListViewSet)


urlpatterns = [
    path('api/', include(router.urls)),
    path('api/todolist/<int:todolist_id>', views.TodoListDetailView.as_view(), name='todolist-detail'),
    path('api/habits/<int:habit_id>',views.HabitDetailViewSet.as_view(), name='habit-detail'),
    path('api/item/<int:item_id>',views.ItemCRUDViewset.as_view(), name='habit-detail'),
    path('admin/', admin.site.urls),
]
