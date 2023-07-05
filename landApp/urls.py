from django.urls import path
from . import views
urlpatterns = [
    path('',views.dashboard),
    path('login/',views.loginTheBorder),
    path('logout/', views.logout_view, name='logout'),


    
    path('info/',views.borderInfo),
    path('message/',views.borderMessage),
    path('report/',views.report)
]