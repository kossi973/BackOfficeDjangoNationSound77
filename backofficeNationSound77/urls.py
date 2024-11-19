
from rest_framework.routers import DefaultRouter
from .views import StyleViewSet, ArtisteViewSet, CalendrierViewSet, SceneViewSet, ProgrammeViewSet, EventViewSet, CategoriePoiViewSet, PoiViewSet, MessageUrgentViewSet

router = DefaultRouter()
router.register(r'styles', StyleViewSet)
router.register(r'artistes', ArtisteViewSet)
router.register(r'calendriers', CalendrierViewSet)
router.register(r'scenes', SceneViewSet)
router.register(r'programmes', ProgrammeViewSet)
router.register(r'events', EventViewSet)
router.register(r'categories', CategoriePoiViewSet)
router.register(r'pois', PoiViewSet)
router.register(r'messagesUrgents', MessageUrgentViewSet)

urlpatterns=router.urls