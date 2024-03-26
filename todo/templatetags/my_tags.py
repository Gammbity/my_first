from django import template

register = template.Library()

from ..models import CategoryModel

@register.simple_tag
def get_categories(id=None):
    if id:
        return CategoryModel.objects.filter(id=id)
    else:    
        return CategoryModel.objects.all()

@register.inclusion_tag('layouts/cat_navbar.html')
def category():
    obj = CategoryModel.objects.all()
    return {
        'cats':obj
    }