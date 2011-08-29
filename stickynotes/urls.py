from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^(?P<stickynote_id>\d+)/$', 'stickynotes.views.mark_as_read'),
)
