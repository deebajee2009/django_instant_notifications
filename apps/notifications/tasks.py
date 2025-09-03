from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.core.cache import cache
from apps.notifications.models import Message
from apps.notifications.services import get_updated_unread_count

from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from celery import shared_task


@shared_task
def send_notification_task(receiver, sender, title, text):
    """
    Celery task to create a message, cache the new unread count,
    and push a notification to the user via WebSocket.
    """

    # 1. Save the new message to the database
    new_message = Message.objects.create(
        receiver=receiver,
        sender=sender,
        title=title,
        text=text,
        is_read=False
    )

    # 2. Update and get the new unread count from cache/db
    unread_count = get_updated_unread_count(receiver)

    # 3. Render HTML snippets for the real-time update
    # New message row to be prepended to the list
    new_message_html = render_to_string(
        'partials/message_row.html',
        {'message': new_message, 'username': receiver}
    )

    # Updated badge count for the navbar
    badge_html = f'<span id="notification-badge" hx-swap-oob="innerHTML" class="badge bg-danger rounded-pill">{unread_count}</span>'

    # Prepend the new message to the list container
    message_list_html = f'<div id="messages-box" hx-swap-oob="afterbegin">{new_message_html}</div>'

    # 4. Get the channel layer and send the combined HTML
    channel_layer = get_channel_layer()
    group_name = f"notifications_{receiver}"

    async_to_sync(channel_layer.group_send)(
        group_name,
        {
            'type': 'send_notification',
            'message': message_list_html + badge_html
        }
    )
    return f"Message sent to {receiver_username}"
