from django.urls import path
from app2.views import *
app_name = 'Tom'

urlpatterns = [
    path('third/', third, name='thrid'),
    path('fourth/', fourth, name='fourth'),
]