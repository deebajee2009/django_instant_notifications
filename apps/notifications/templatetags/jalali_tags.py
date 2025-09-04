from django import template
import jdatetime
import pytz

register = template.Library()

@register.filter
def to_farsi_nums(value):
    """Converts English digits to Farsi digits."""
    value = str(value)
    farsi_digits = "۰۱۲۳۴۵۶۷۸۹"
    english_digits = "0123456789"
    translation_table = str.maketrans(english_digits, farsi_digits)
    return value.translate(translation_table)

@register.filter
def to_jalali(gregorian_date):
    """Converts a Gregorian datetime object to a formatted Jalali string with Farsi numbers."""
    if not gregorian_date:
        return ""
    # 1. Define the target timezone
    tehran_tz = pytz.timezone('Asia/Tehran')

    # 2. Convert the UTC datetime object to Tehran's local time
    local_time = gregorian_date.astimezone(tehran_tz)

    jd = jdatetime.datetime.fromgregorian(datetime=local_time)
    formatted_date = jd.strftime(%H:%M" "%Y/%m/%d)
    return to_farsi_nums(formatted_date)
