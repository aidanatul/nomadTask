from django.conf.urls import url
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static

from reg import views
from reg.views import PostViewSet, CommentViewSet, UserViewSet

router = routers.SimpleRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
                  url(r'register', UserViewSet.as_view()),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += router.urls
