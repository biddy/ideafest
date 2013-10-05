from django.db.models import Count
from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.core.urlresolvers import reverse

from model_utils import Choices
from model_utils.fields import StatusField
from model_utils.managers import QueryManager
from model_utils.models import TimeStampedModel


class Title(TimeStampedModel):
    title = models.CharField(max_length=255, unique=True)
    user = models.ForeignKey(User, related_name='titles')
    slug = models.SlugField(max_length=255, blank=True, default='')

    def __unicode__(self):
        return '%s' % (self.title)

    def save(self,*args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Title, self).save(*args,**kwargs)

    def get_absolute_url(self, **kwargs):
        return reverse('ideas:list')


class Node(TimeStampedModel):
    STATUS=Choices(u'new',u'improved')

    user = models.ForeignKey(User, related_name='nodes')
    inherit = models.IntegerField()
    content = models.TextField()
    status = StatusField()
    title = models.ForeignKey(Title)
    slug = models.SlugField(max_length=255, blank=True, default='')
    stage = models.IntegerField(blank=True, default=0)

    objects = models.Manager()
    new = QueryManager(status=u'new').order_by(u'-modified')
    improved = QueryManager(status=u'improved').order_by(u'-modified')

    def __unicode__(self):
        return 'inherited:%s, title: %s' % (self.inherit, self.title)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Node, self).save(*args, **kwargs)

    def get_absolute_url(self, **kwargs):
        return reverse('ideas:title', kwargs={'pk':self.title.id})
