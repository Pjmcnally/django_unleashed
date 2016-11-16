from django.shortcuts import render
from django.http.response import HttpResponse

from .models import Tag, Startup, NewsLink

from django.template import Context, loader

# Create your views here.
def homepage(request):
    tag_list = Tag.objects.all()
    template = loader.get_template('organizer/tag_list.html')
    context = Context({'tag_list': tag_list})
    print(context)
    output = template.render(context)
    return HttpResponse(output)

