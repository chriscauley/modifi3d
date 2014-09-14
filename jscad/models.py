from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import models

from main.utils import cached_property

import requests

class FileModel(models.Model):
  user = models.ForeignKey(User)
  parent = models.ForeignKey("self",null=True,blank=True)
  name = models.CharField(max_length=64)
  description = models.TextField(null=True,blank=True)
  source = models.TextField(null=True,blank=True)
  uri = models.URLField(null=True,blank=True)
  get_url = lambda self: self.uri or self.source_url
  source_url = lambda self: reverse("jscad_source",args=[slugify(self.name),self.pk])
  @cached_property
  def text(self):
    if self.source:
      return self.source
    return requests.get(self.uri).text()
  __unicode__ = lambda self: self.name
  class Meta:
    abstract = True

class Configuration(FileModel):
  class Meta:
    ordering = ('name',)

class Item(FileModel):
  class Meta:
    ordering = ('name',)
