from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import models
from django.template.defaultfilters import slugify

from main.utils import cached_property

import requests

class FileModel(models.Model):
  user = models.ForeignKey(User)
  parent = models.ForeignKey("self",null=True,blank=True)
  name = models.CharField(max_length=64)
  description = models.TextField(null=True,blank=True)
  source = models.TextField(null=True,blank=True)
  uri = models.URLField(null=True,blank=True)
  get_url = lambda self: self.source_url
  source_url = cached_property(lambda self: reverse("item_source",args=[self.pk,slugify(self.name)]),
                               name="source_url")
  @cached_property
  def text(self):
    if self.source:
      return self.source
    print self.uri
    return requests.get(self.uri).text
  __unicode__ = lambda self: self.name
  class Meta:
    abstract = True

class Configuration(FileModel):
  class Meta:
    ordering = ('name',)

class Item(FileModel):
  class Meta:
    ordering = ('name',)

class ItemSetting(FileModel):
  item = models.ForeignKey(Item)
  class Meta:
    ordering = ('name',)
