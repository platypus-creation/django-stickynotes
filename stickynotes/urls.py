from django.conf.urls.defaults import *
from articles.models import Article

urlpatterns = patterns('',
    (r'^(?P<stickynote_id>\d+)/$', 'stickynotes.views.mark_as_read'),
)
