from django import template
from stickynotes.models import Stickynote
register = template.Library()

@register.inclusion_tag('stickynotes/stickynotes.html', takes_context=True)
def user_stickynotes(context):
    request = context['request']
    stickynotes = Stickynote.objects.none()
    if request.user.is_authenticated():
        stickynotes = Stickynote.objects.filter(read=False, user=request.user)
    return {
        'request': request,
        'stickynotes': stickynotes,
    }
