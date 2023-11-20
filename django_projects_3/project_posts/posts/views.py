from django.shortcuts import render
from posts.models import Post
from .services import PostNotFound, FakePostService as service
from django.http import Http404

# Create your views here.
# Create your views here.

def list(request):
    
    if request.method == "GET":
        #p = Post.objects.all()
        p = service.list()
   

    if request.method == "POST":
        service.create(title=request.POST.get("pos_title"),
                       content=request.POST.get("pos_content"),
                       created_at=request.POST.get("pos_created_at"),
                       updated_at=request.POST.get("pos_updated_at")
                       )
        #p = Post.objects.create(
        #    title=request.POST.get("pos_title"),
        #    content=request.POST.get("pos_content"),
        #    created_at=request.POST.get("pos_created_at"),
        #    updated_at=request.POST.get("pos_updated_at")
        # )  # date="2022...", systolic=120
        #
        #p = Post.objects.all()
        p = service.list()
    
    return render(
        request, 
        "posts/list.html",
        {"posts": p}
    )
  

def details(request, id):
    
    #p = Post.objects.get(id=id)

    try:
        p = service.get(id)
    except:
        raise Http404

    return render(
        request, 
        "posts/post_details.html",
        {"posts": p}
    )