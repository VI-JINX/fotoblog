from django import template
from django.utils import timezone

register = template.Library()

@register.filter
def model_type(value):
    return type(value).__name__

@register.simple_tag(takes_context=True)
def get_user_name(context, user):
    context_user = context['user']
    print(f'The user is {user}')
    print(f'the context user is: {context_user}')
    if user == context['user']:
        return 'Vous'
    return user

@register.simple_tag
def get_posted_at_display(post_date):
    if not post_date:
        return 'Date Introuvable'
    
    now = timezone.now()
    delta = now - post_date
    minutes = delta.total_seconds()/60

    if minutes < 1:
        return 'Publié il y quelques secondes'
    elif minutes < 60:
        return f'Publié il y a {int(round(minutes))} minutes'
    elif minutes < 1440:
        return f'Publié il y a {int(round(minutes/60))} heures'
    else:
        return f'Publié il y a {int(round(minutes)/1440)} jours'
