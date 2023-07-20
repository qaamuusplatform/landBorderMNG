from django.urls import path
from . import views
urlpatterns = [
    path('',views.dashboard),
    path('login/',views.loginTheBorder),
    
    path('face/',views.face),
    
    
    path('info/',views.borderInfo),
    path('message/',views.borderMessage),
    path('report/',views.report)
]