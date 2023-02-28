from rest_framework.routers import DefaultRouter

from apps.themes.views import ThemeViewSet


router = DefaultRouter()
router.register(
    prefix="",
    viewset=ThemeViewSet
)

urlpatterns = router.urls