from django.urls import path
from . import views
app_name = 'task'

urlpatterns = [
    path('', views.list_task, name = 'list_tasks'),
    path('add_Tasks', views.add_task, name = 'add_tasks'),
    path('delete_task/<int:id>/', views.delete_task, name = 'delete_tasks'),
    path('edit_task/<int:id>/', views.edit_task, name='edit_tasks'),
    path('mark-complete/<int:id>/', views.mark_complete, name='mark_complete'),
]
