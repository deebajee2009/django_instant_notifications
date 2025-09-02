from django import template
import jdatetime

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

    jd = jdatetime.datetime.fromgregorian(datetime=gregorian_date)
    formatted_date = jd.strftime("%Y/%m/%d ساعت %H:%M")
    return to_farsi_nums(formatted_date)
