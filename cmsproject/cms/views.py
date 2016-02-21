# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404
from django.db.models import Q
from cmsproject.cms.models import Story, Category


def category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    story_list = Story.objects.filter(category=category)
    heading = "Category: %s" % category.label
    return render_to_response ("cms/story_list.html", locals())


def search(request):
    if 'q' in request.GET:
        term = request.GET['q']
        story_list = Story.objects.filter(Q(title__contains=term) |
                                          Q(markdown_content__contains=term))
        heading = "Search results"
    return render_to_response("cms/story_list.html", locals())
