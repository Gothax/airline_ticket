from django.urls import path
from . import api

urlpatterns = [
    path('signup/', api.signup, name='signup'),
    path('login/', api.login, name='login'),
    path('delete/<int:pk>/', api.delete_user, name='delete_user'),
    path('change-password/', api.edit_password, name='edit_password'),
]
