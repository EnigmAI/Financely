from django import template

register = template.Library()

@register.filter(name='has_group')
def has_group(user, group_name):
    return user.groups.filter(name=group_name).exists()

# @register.filter(name ='get_item')
# def get_item(dictionary, key):
#     return d[str(key)]
