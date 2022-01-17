from django.urls import path
from .views import home_view, logout_page_view, room_view, create_room_view, update_room_view, delete_room_view, login_page_view,trial_view

urlpatterns = [
    path('login/', login_page_view, name='login'),
    path('logout/', logout_page_view, name='logout'),
    path('', home_view, name='home'),
    path('trial/',trial_view,name='trial'),
    path('room/<int:pk>/', room_view, name='room'),
    path('createroom/', create_room_view, name='create_room'),
    path('updateRoom/<int:pk>/', update_room_view, name='update_room'),
    path('deleteRoom/<int:pk>/', delete_room_view, name='delete_room'),
]
