from django.urls import path
from . import views
app_name='qrcode'

urlpatterns = [
    path('<int:qrid>',views.qr_plain,name='qrplain'),
    path('',views.home,name='scan'),
]
