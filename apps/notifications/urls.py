from django.urls import path
from . import views

app_name = 'apps.notifications'

urlpatterns = [
    path('', views.index_view, name='index'), # Root URL shows the page with the login modal
    path('dashboard/<str:username>/', views.dashboard_view, name='dashboard'),
    path('message/<int:message_id>/', views.message_detail_view, name='message_detail'),
    path('send/', views.send_message_view, name='send_message'),
]
