from django.db import models


class Message(models.Model):
    sender     = models.CharField(
        max_length=150,
        verbose_name="فرستنده"
    )
    receiver   = models.CharField(
        max_length=150,
        verbose_name="گیرنده"
    )
    title      = models.CharField(
        max_length=255,
        verbose_name="عنوان"
    )
    text       = models.TextField(
        verbose_name="متن پیام"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="تاریخ و ساعت ارسال"
    )
    is_read    = models.BooleanField(
        default=False,
        verbose_name="خوانده شده"
    )

    class Meta:
        ordering = ['-created_at']
        verbose_name = "پیام"
        verbose_name_plural = "پیام‌ها"

    def __str__(self):
        return f"پیام از {self.sender} به {self.receiver.username}: {self.title}"
