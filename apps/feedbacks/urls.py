from rest_framework import routers

from apps.feedbacks.views import FeedbackViewSet


router = routers.DefaultRouter()
router.register(
    prefix='', 
    viewset=FeedbackViewSet
    )
urlpatterns=router.urls