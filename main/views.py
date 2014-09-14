from django.http import HttpResponseRedirect
from django.template.response import TemplateResponse

from jscad.models import Item, Configuration

def home(request):
  values = {
    'items': Item.objects.all(),
    'configurations': Configuration.objects.all(),
  }
  return TemplateResponse(request,"index.html",values)

redirect = lambda request,url: HttpResponseRedirect(url)
