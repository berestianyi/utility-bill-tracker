from django import template


register = template.Library()


@register.filter
def get_previous_date(bills, index):
    if index == 0:
        return None
    return bills[index - 1].str_time
