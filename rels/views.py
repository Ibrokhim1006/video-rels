from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404

from rels.models import Video


def video_rels(request):
    context = {}
    context['objects'] = Video.objects.all().order_by('?')
    return render(request, 'index.html', context)

@csrf_exempt
def like_video(request, video_id):
    if request.method == 'POST':
        video = get_object_or_404(Video, id=video_id)  # Video ni topish
        video.add_like()  # Like qo'shish
        return JsonResponse({'likes': video.like_count}, status=200)
    return JsonResponse({'error': 'Invalid request method'}, status=400)