from django.urls import path
from .views import PostList,PostDetail,CreatePost,UpdatePost,DeletePost

urlpatterns = [
    path("", PostList.as_view(), name="home"),
    path("detail/<int:pk>/", PostDetail.as_view(), name="detail"),
    path("create/", CreatePost.as_view(), name="create"),
    path("edit/<int:pk>/", UpdatePost.as_view(), name="edit"),
    path("delete/<int:pk>/", DeletePost.as_view(), name="delete"),
    
]
 