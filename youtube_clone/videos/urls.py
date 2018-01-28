from django.conf.urls import url

from .views import get_video_by_keyword

urlpatterns = [
    url(r'^search/$', get_video_by_keyword, name='get_video_by_keyword')
]
