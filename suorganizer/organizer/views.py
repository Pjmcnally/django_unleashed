from django.shortcuts import (
    render, get_object_or_404, redirect
)
from django.views.generic import View

from .models import Tag, Startup, NewsLink
from .forms import TagForm, StartupForm, NewsLinkForm

class TagCreate(View):
    form_class = TagForm
    template_name = 'organizer_tag_create'

    def get(self,request):
        return render(
            request, 
            self.template_name, 
            {'form': self.form_class()}
        )

def tag_create(request):
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            new_tag = form.save()
            return redirect(new_tag)
    else: # request.method != 'POST'
        form = TagForm()
    return render(
        request, 
        'organizer/tag_form.html', 
        {'form': form}
    )

def tag_detail(request, slug):
    tag = get_object_or_404(Tag, slug__iexact=slug)
    return render(
        request,
        'organizer/tag_detail.html',
        {'tag': tag}
    )

def tag_list(request):
    return render(
        request,
        'organizer/tag_list.html', 
        {'tag_list': Tag.objects.all()}
    ) 

def startup_detail(request, slug):
    startup = get_object_or_404(Startup, slug__iexact=slug)
    return render(
        request,
        'organizer/startup_detail.html',
        {'startup': startup}
    )

def startup_list(request):
    return render(
        request,
        'organizer/startup_list.html',
        {'startup_list': Startup.objects.all()}
    )

