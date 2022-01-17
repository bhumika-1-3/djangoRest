from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes),
    path('rooms/', views.getRooms),
    path('rooms/<int:pk>/', views.getSingleRoom),
    path('rooms/newRoom/', views.newRoom),
    path('topics/', views.topics),

    # CRUD
    path('todo/', views.todo_all),
    path('todo/create/', views.todo_create),
    path('todo/update/<int:pk>/', views.todo_update),
    path('todo/delete/<int:pk>/', views.todo_delete),

    # login signup
    path('login/',views.loginUser),
    path('register/',views.registration_view),
]
