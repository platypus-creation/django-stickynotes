from django.shortcuts import get_object_or_404
from stickynotes.models import Stickynote
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

@login_required
def mark_as_read(request, stickynote_id):
    stickynote = get_object_or_404(Stickynote, id=stickynote_id, user=request.user)
    stickynote.read = True
    stickynote.save()
    return HttpResponseRedirect(request.GET.get('next', '/'))