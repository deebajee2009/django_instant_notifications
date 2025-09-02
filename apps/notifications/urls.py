from django.urls import path
from apps.notifications.views import *

app_name = 'apps.notifications'

urlpatterns = [
    path('', index_view, name='index'), # Root URL shows the page with the login modal
    path('dashboard/<str:username>/', dashboard_view, name='dashboard'),
    path('message/<int:message_id>/', message_detail_view, name='message_detail'),
    path('send/', send_message_view, name='send_message'),
]
