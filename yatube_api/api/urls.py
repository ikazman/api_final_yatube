from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from api.views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

router_v1 = DefaultRouter()
router_v1.register('posts', PostViewSet)
router_v1.register('groups', GroupViewSet)
router_v1.register(r'posts/(?P<post_id>\d+)/comments',
                   CommentViewSet,
                   basename='comments')
router_v1.register('follow', FollowViewSet, basename='follow')


urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('v1/api/token/', TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('v1/api/token/refresh/', TokenRefreshView.as_view(),
         name='token_refresh'),
]
