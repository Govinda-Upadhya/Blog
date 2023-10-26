from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from datetime import date
from .models import *
from django.views.generic import ListView,DetailView
from django.http import HttpResponse
from .forms import *
from django.views import View
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.

# def starting_page(request):
#     sorted_posts=Post.objects.all()
#     total_post=len(sorted_posts)
#     required_post=total_post-3
#     latest_post=Post.objects.all()[required_post:]
#     return render(request,'blog/index.html',{
#         "posts":latest_post,
#     })
class startPage(ListView):
    model=Post
    template_name="blog/index.html"
    context_object_name="posts"
    fields="__all__"
    ordering=["-date"]
    def get_queryset(self):
        base_query= super().get_queryset()
        data=base_query[:3]
        return data
    
# def posts(request):
#     all_posts=Post.objects.all()
#     return render(request,"blog/all-posts.html",{
#         "all_posts":all_posts
#     })
class Posts(ListView):
    model=Post
    template_name="blog/all-posts.html"
    fields="__all__"
    context_object_name="all_posts"

# def post_detail(request,slug):
#     identified_posts=Post.objects.get(slug=slug)
#     return render(request,"blog/post-detail.html",{
#         "post":identified_posts,
#         "post_tags":identified_posts.caption.all()

#     })

class PostDetails(View):
    
    def get(self,request,slug):
        post=Post.objects.get(slug=slug)
        
        context={
                "post":post,
                "post_tags":post.caption.all(),
                "comment_form":CommentForm(),
                "comments":post.comments.all().order_by("-id")
        }
        
        return render(request,"blog/post-detail.html",context)

    def post(self,request,slug):
        comment_form=CommentForm(request.POST)
        post=Post.objects.get(slug=slug)
        if comment_form.is_valid():
            comment=comment_form.save(commit=False)
            comment.post=post
            comment.save()
            return HttpResponseRedirect(reverse("post-detail-page",args=[slug]))
        
        context={
                "post":post,
                "post_tags":post.caption.all(),
                "comment_form":CommentForm(),
                "comments":post.comments.all().order_by("-id")
        }
        return render(request,"blog/post-detail.html",context)
class ReadLaterView(View):
    def get(self,request):
        stored_posts=request.session.get("stored_posts")
        context={}
        if stored_posts is None or len(stored_posts)==0:
            context["posts"]=[]
            context["has_posts"]=False
        else:
            posts=Post.objects.filter(id__in=stored_posts)
            context["posts"]=posts
            context["has_posts"]=True
        return render(request,"blog/stored-posts.html",context)

    def post(selff,request):
        stored_posts=request.session.get("stored_posts")
        if stored_posts is None:
            stored_posts=[]
        post_id=int(request.POST["post_id"])
        if post_id not in stored_posts:
            stored_posts.append(post_id)
            request.session["stored_posts"]=stored_posts
        return HttpResponseRedirect("/")
       

