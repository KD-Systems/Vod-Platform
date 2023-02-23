from django.shortcuts import render
from django.http import HttpResponse
from core.models import Video


# from userauths.models import Profile


def index(request):
    video = Video.objects.filter(visibility="public").order_by("-date")
    # video = Video.objects.all()
    context = {
        "video":video
    }
    return render(request, "index.html", context)

def videoDetail(request, pk):
    video = Video.objects.get(id=pk)
    # channel = Channel.objects.get(user=video.user)
    
    # channel.total_views = channel.total_views + 1
    # channel.save()

    video.views = video.views + 1
    video.save()

    # Suggesting Video
    # video_tags_id = video.tags.values_list("id", flat=True)
    # similar_videos = Video.objects.filter(tags__in=video_tags_id).exclude(id=video.id)
    # similar_videos = similar_videos.annotate(same_tags=Count("tags")).order_by("-same_tags", "-date")[:25]

    # Getting all comment related to a video
    # comment = Comment.objects.filter(active=True, video=video).order_by("-date")

    context = {
        "video":video,
        # "channel":channel,
        # "comment":comment,
        # "similar_videos":similar_videos,
    }
    return render(request, "video-detail.html", context)