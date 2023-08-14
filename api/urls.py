from django.urls import path
from .views import *

urlpatterns = [
    path('user-profile/', UserProfileListCreate.as_view(), name='user-profiles'),
    path('user-profile/<int:pk>/', UserProfileDetailDelete.as_view(), name='user-profile-detail'),

    
    path('border/', BorderRegistrationListCreate.as_view(), name='border-registration'),
    path('border/<int:pk>/', BorderRegistrationDetailDelete.as_view(), name='border-registration-detail'),


    
    path('message/', MessagesForListCreate.as_view(), name='message'),
    path('message/<int:pk>/', MessagesForDetailDelete.as_view(), name='message-detail'),


    
    path('fines/', FinesListCreate.as_view(), name='fines-register'),
    path('fines/<int:pk>/', FinesDetailDelete.as_view(), name='fines-detail'),
    
    path('extras/', ExtrasListCreate.as_view(), name='extra-time'),
    path('extras/<int:pk>/', ExtrasDetailDelete.as_view(), name='extra-time-detail'),


    
    path('scanned-face/', ScannedFaceListCreate.as_view(), name='scanned-face'),
    path('scanned-face/<int:pk>/', ScannedFaceDetailDelete.as_view(), name='scanned-face'),


    path('scan-finger/', ScanFingerListCreate.as_view(), name='scan-finger'),
    path('get-scanned-finger/<int:pk>/', ScanFingerDetailDelete.as_view(), name='get-scanned-finger'),



    
    # fingerprint
    path('get-finger-print-scaned/',GetScannedFingerPrint.as_view())

    
]