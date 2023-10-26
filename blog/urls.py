from django.urls import path
from . import views
urlpatterns = [
    path("",views.startPage.as_view(),name="starting_page"),
    path("posts",views.Posts.as_view(),name="posts"),
    path("posts/<slug:slug>",views.PostDetails.as_view(),name="post-detail-page"),
    path("read-later",views.ReadLaterView.as_view(),name="read-later")
    
]
