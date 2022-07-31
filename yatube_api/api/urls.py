from django.urls import include, path
from rest_framework.authtoken import views as token_views
from rest_framework.routers import DefaultRouter
from .views import CommentViewSet, GroupViewSet, PostViewSet


router = DefaultRouter()
router.register(r'posts/(?P<post_id>\d+)/comments', CommentViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'posts', PostViewSet)

urlpatterns = [
    path('v1/api-token-auth/', token_views.obtain_auth_token),
    path('v1/', include(router.urls)),
]
