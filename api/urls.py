from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import PostViewSet, CommentViewSet, GroupViewSet, FollowList
#from rest_framework.authtoken import views as token_views


router = DefaultRouter()

router.register('posts', PostViewSet, basename='posts')
router.register(r'posts/(?P<post_id>\d+)/comments', CommentViewSet, basename='comments')
router.register('group', GroupViewSet, basename ='group')


urlpatterns = [
    path('', include(router.urls)),
    path('follow/', FollowList.as_view()),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
