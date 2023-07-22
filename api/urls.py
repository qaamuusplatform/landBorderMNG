from django.urls import path
from .views import *

urlpatterns = [
    path('user-profile/', UserProfileListCreate.as_view(), name='user-profiles'),
    path('user-profile/<int:pk>/', UserProfileDetailDelete.as_view(), name='user-profile-detail'),

    
    path('border/', BorderRegistrationListCreate.as_view(), name='border-registration'),
    path('border/<int:pk>/', BorderRegistrationDetailDelete.as_view(), name='border-registration-detail'),


    
    path('message/', MessagesForListCreate.as_view(), name='message'),
    path('message/<int:pk>/', MessagesForDetailDelete.as_view(), name='message-detail'),
]