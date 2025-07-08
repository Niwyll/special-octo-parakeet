from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView
from poke_manager.views import AddUserToGroupView, RemoveUserFromGroupView, UserDetailView

urlpatterns = [
    path('group/<type>/add/', AddUserToGroupView.as_view(), name='add-user-to-group'),
    path('group/<type>/remove/', RemoveUserFromGroupView.as_view(), name='remove-user-from-group'),
    path('user/me/', UserDetailView.as_view(), name='about-me'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
]