from django.shortcuts import (
    render, get_object_or_404, render_to_response
)

from .models import Tag, Startup, NewsLink
from .forms import TagForm, StartupForm, NewsLinkForm

def tag_create(request):
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            new_tag = form.save()
            return redirect(new_tag)
        else: # empty or invalid data
            form = TagForm()
    else: # request.method != 'POST'
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

