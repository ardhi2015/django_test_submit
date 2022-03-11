from django.urls import path

from .views import WallView, WallLikeView

post_list = WallView.as_view({"get": "list", "post": "create"})
post_detail = WallView.as_view(
    {
        "get": "retrieve",
        "put": "update",
        "delete": "destroy",
    }
)

like_list = WallLikeView.as_view({"post": "create"})
like_detail = WallLikeView.as_view(
    {
        "get": "retrieve",
        "put": "update",
        "delete": "destroy",
    }
)

urlpatterns = [
    path("posts", post_list, name="post-list"),
    path("posts/<int:id>", post_detail, name="post-detail"),
    path("posts/<int:id>/likes", like_list, name="like-list"),
    path("posts/<int:id>/likes/<int:like_id>", like_detail, name="like-detail"),
]
