from django.urls import path
from .views import home, create, delete, update, login_view, logout_view, register_view


urlpatterns = [
    path('', home, name='home'),
    path('create/', create, name='create'),
    path('delete/<int:id>/', delete, name='delete'),
    path('update/<int:id>/', update, name='update'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
]