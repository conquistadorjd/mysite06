from django.urls import path
from . import views

app_name = 'todo'
urlpatterns = [
    path('', views.index, name='index'),  
    path('<int:task_id>/', views.detail, name='detail'),
    path('newtask/', views.newtask, name='newtask'),
    path('edit/<int:task_id>', views.edit, name='edit'),
    path('delete/<int:task_id>', views.delete, name='delete'),
]