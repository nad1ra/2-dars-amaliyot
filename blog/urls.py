from django.urls import path, include
from rest_framework.routers import DefaultRouter
from blog.views import AuthorViewSet, CategoryViewSet, TagViewSet, PostViewSet, CommentViewSet

router = DefaultRouter()
router.register(r'authors', AuthorViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'tags', TagViewSet)
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
