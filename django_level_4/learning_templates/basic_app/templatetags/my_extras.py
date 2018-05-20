from django import template

register = template.Library()
#need to register this

@register.filter(name='cut')  #passing a name which will act as our filter name
def cut(value,args):
    """
    This cuts out all the args from value
    """
    return value.replace(args,'')
