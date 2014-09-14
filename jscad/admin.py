from django.contrib import admin

from models import Configuration, Item
from simplediff import html_diff

class FileModelAdmin(admin.ModelAdmin):
  readonly_fields = ('parent_diff',)
  save_as = True
  def parent_diff(self,obj):
    if not obj.parent:
      return "This object has no parent"
    return html_diff(obj.parent.text,obj.text)
  parent_diff.allow_tags = True

class ConfigurationAdmin(FileModelAdmin):
  pass

class ItemAdmin(FileModelAdmin):
  pass

admin.site.register(Configuration,ConfigurationAdmin)
admin.site.register(Item,ItemAdmin)
