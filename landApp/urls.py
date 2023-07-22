from django.urls import path
from . import views
urlpatterns = [
    path('',views.dashboard),
    path('logout/',views.logoutUser),
    path('login/',views.loginUser),


    path('image-tes/',views.validateImages),


    # user-profie
    path('user-profile-register/',views.userProfileRegister),
    path('all-user-profiles/',views.allUserProfiles),

    path('crop-image-face/',views.cropFaceImageToBase64),
    
    # border-iuf
    path('border-register/',views.borderRegister),
    path('all-border/',views.allBorder),


    # information
    path('scan-user-face/',views.scanUserFace),
    path('scaned-user-info/<str:pk>/',views.scanedUserInfo),
    path('face_detect/',views.faceDetect),
    
    path('message-info/',views.messageInfo),

    # report
    path('report-list/',views.reportList),







    # border
    path('border/',views.borderInfoDashboard),
    path('border/messages/',views.borderInfoMessages)

]