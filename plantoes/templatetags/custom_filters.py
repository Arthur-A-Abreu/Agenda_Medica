from django import template

register = template.Library()

@register.filter
def get_item(dictionary, key):
    if not dictionary: return None
    val = dictionary.get(key)
    if val is None:
        val = dictionary.get(str(key))
    if val is None:
        try:
            val = dictionary.get(int(key))
        except:
            pass
    return val

@register.filter
def strip(value):
    if isinstance(value, str):
        return value.strip()
    return value
