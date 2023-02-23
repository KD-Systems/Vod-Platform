from django.shortcuts import render
from django.http import HttpResponse
from core.models import Video


def index(request):
    video = Video.objects.filter(visibility="public").order_by("-date")
    # video = Video.objects.all()
    context = {
        "video":video
    }
    return render(request, "index.html", context)