import json
import jdatetime

from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.core.cache import cache

from apps.notifications.models import Message
from apps.notifications.tasks import send_notification_task
from apps.notifications.services import get_updated_unread_count


def index_view(request):
    """
    Renders the main page shell. JavaScript will handle showing the
    login modal or loading the dashboard.
    """
    return render(request, 'dashboard.html')

def dashboard_view(request, username):
    """
    Handles GET for loading the dashboard content and POST for date filtering.
    This view now returns a partial HTML fragment, not a full page.
    """
    # Invalidate the cache by recalculating on every load for simplicity,
    # or use a more sophisticated caching strategy.
    unread_count = get_updated_unread_count(username)

    if request.method == "POST":
        # Handle HTMX date filtering (this logic remains the same)
        start_date_str = request.POST.get("start_date")
        end_date_str = request.POST.get("end_date")
        try:
            start_date = jdatetime.datetime.strptime(start_date_str, '%Y/%m/%d').togregorian()
            end_date = jdatetime.datetime.strptime(end_date_str, '%Y/%m/%d').togregorian()
            end_date = end_date.replace(hour=23, minute=59, second=59)
            messages = Message.objects.filter(
                receiver=username,
                created_at__range=[start_date, end_date]
            ).order_by('-created_at')
        except (ValueError, TypeError):
            messages = []
        return render(request, 'partials/message_list.html', {'messages': messages, 'username': username})

    # Handle GET request for loading the main dashboard content
    all_messages = Message.objects.filter(receiver=username).order_by('-created_at')
    context = {
        'messages': all_messages,
        'unread_notif_counts': unread_count,
        'username': username,
    }
    # IMPORTANT: Render the partial content, not the full dashboard.html
    return render(request, 'partials/dashboard_content.html', context)


def message_detail_view(request, message_id):
    """
    Displays a single message and marks it as read.
    """
    message = get_object_or_404(Message, id=message_id)

    # Basic security check - a real app would use request.user
    # For this demo, we assume the user is "logged in" via URL
    user = message.receiver

    if not message.is_read:
        message.is_read = True
        message.save()

    unread_notif_counts = get_updated_unread_count(user)

    context = {
        'message': message,
        'username': user,
        'unread_notif_counts': unread_notif_counts
    }
    return render(request, 'message_detail.html', context)


@csrf_exempt
@require_POST
def send_message_view(request):
    """
    API-like endpoint to trigger sending messages.
    """
    try:
        data = json.loads(request.body)
        receivers = data.get('receivers', [])
        sender = data.get('sender', 'سیستم')
        title = data.get('title')
        text = data.get('text')

        if not all([receivers, title, text]):
            return JsonResponse({'status': 'error', 'message': 'Missing required fields'}, status=400)

        for receiver in receivers:
            task_result = send_notification_task.delay(
                receiver=receiver,
                sender=sender,
                title=title,
                text=text
            )
            print(task_result)

        return JsonResponse({'status': 'success', 'message': f'Messages queued for delivery to {len(receivers)} users.'})

    except json.JSONDecodeError:
        return JsonResponse({'status': 'error', 'message': 'Invalid JSON'}, status=400)
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
