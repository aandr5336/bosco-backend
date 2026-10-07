from django import template
from catalog.models import Product

register = template.Library()

# 1. Власний фільтр для форматування ціни
@register.filter(name='uah')
def uah(value):
    """Форматує число до вигляду: 1 200.00 грн"""
    try:
        val = float(value)
        return f"{val:,.2f} грн".replace(',', ' ')
    except (ValueError, TypeError):
        return value

# 2. Власний simple_tag для підрахунку товарів
@register.simple_tag
def product_count():
    """Повертає загальну кількість товарів у базі даних"""
    return Product.objects.count()