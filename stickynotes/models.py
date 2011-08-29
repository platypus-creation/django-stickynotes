from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.contrib.auth.models import User

class Stickynote(models.Model):
    user = models.ForeignKey(User, related_name=u"stickynotes", verbose_name=_(u'User'))
    type = models.CharField(_(u'Type'), blank=True, max_length=64)
    message = models.TextField(_(u'Message'))
    read = models.BooleanField(_(u'Read'), default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.message[:50]

    @models.permalink 
    def get_mark_as_read_url(self):
        return ('stickynotes.views.mark_as_read', [str(self.id)])

    @classmethod
    def add(cls, user, message):
        cls.objects.get_or_create(user=user, message=message, read=False)