from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, re_path
from django.views.static import serve
from rels.views import video_rels, like_video

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', video_rels, name='video_rels'),
    path('video/<int:video_id>/like/', like_video, name='like_video'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += [re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT, }), ]