from .models import Message

def notifications_context(request):
    """
    Makes the unread notification count available to all templates.
    """
    if request.resolver_match:

        username = request.resolver_match.kwargs.get('username')
        count = Message.objects.filter(receiver=username, is_read=False).count()
    else:
        # No count for anonymous users
        count = 0

    return {'unread_notif_counts': count}
