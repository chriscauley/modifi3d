from django.shortcuts import get_object_or_404
from django.http import HttpResponse

from .models import Item

def item_source(request,pk,name):
  item = get_object_or_404(Item,pk=pk)
  return HttpResponse(str(item.text))
