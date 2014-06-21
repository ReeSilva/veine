from django.shortcuts import render_to_response
from django.conf import settings
from posts.models import Posts


def index(request):
    return render_to_response('posts/index.html', {
        'posts': Posts.objects.all().order_by('-publication_date')
    })