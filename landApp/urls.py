from django.urls import path
from . import views
urlpatterns = [
    path('',views.dashboard),
    path('login/',views.loginTheBorder),

    
    path('info/',views.borderInfo),
    path('message/',views.borderMessage)
    # path('border-reg/',views.borderReg),
]