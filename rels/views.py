from django.shortcuts import render
from rels.models import Video


def video_rels(request):
    context = {}
    context['objects'] = Video.objects.all().order_by('?')
    return render(request, 'index.html', context)
