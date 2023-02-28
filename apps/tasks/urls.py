from rest_framework.routers import DefaultRouter

from apps.tasks.views import TaskViewSet, TaskSubmissionViewSet


router = DefaultRouter()
router.register(
    prefix="task",
    viewset=TaskViewSet
)
router.register(
    prefix="sumbittask",
    viewset=TaskSubmissionViewSet
)
urlpatterns = router.urls