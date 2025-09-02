from .models import Message

# Helper function to update and get unread count
def get_updated_unread_count(user):
    count = Message.objects.filter(receiver=user, is_read=False).count()
    cache.set(f"unread_count:{user.username}", count, timeout=None) # Cache forever
    return count
