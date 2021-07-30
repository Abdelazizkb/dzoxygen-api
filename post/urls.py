from django.urls import path, include
from . import views


urlpatterns = [
    path("postlist/", views.PostListView.as_view(), name="postlist"),
    path("post-detail/<int:pk>/", views.PostRetrieveUpdateDestroyAPIView.as_view(), name="postdetail"),
    path("post-create/", views.PostCreateView.as_view(), name="postcreate"),
    path("post-author/<int:pk>/", views.postAuthor, name="postauthor"),
]