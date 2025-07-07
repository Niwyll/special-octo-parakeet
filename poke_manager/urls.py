from django.urls import path
from poke_manager.views import AddUserToGroupView, RemoveUserFromGroupView, UserDetailView

urlpatterns = [
    path('group/<type>/add/', AddUserToGroupView.as_view(), name='add-user-to-group'),
    path('group/<type>/remove/', RemoveUserFromGroupView.as_view(), name='remove-user-from-group'),
    path('user/me/', UserDetailView.as_view(), name='about-me')
]