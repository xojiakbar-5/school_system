from django import template
import hashlib

register = template.Library()

@register.filter
def subject_color(subject_name):
    """Dars nomidan kelib chiqib, bir xil va yoqimli rang generatsiya qiladi."""
    if not subject_name:
        return '#6c757d' # default grey color
    # Nomdan hash generatsiya qilamiz
    hash_object = hashlib.md5(subject_name.encode())
    hex_dig = hash_object.hexdigest()
    # Hashning bir qismidan RGB rang hosil qilamiz (juda to'q bo'lmasligi uchun)
    r = int(hex_dig[0:2], 16) % 150 + 80
    g = int(hex_dig[2:4], 16) % 150 + 80
    b = int(hex_dig[4:6], 16) % 150 + 80
    return f'#{r:02x}{g:02x}{b:02x}'