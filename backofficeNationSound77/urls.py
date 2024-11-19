
from rest_framework.routers import DefaultRouter
from .views import StyleViewSet, ArtisteViewSet, CalendrierViewSet, SceneViewSet, ProgrammeViewSet, EventViewSet, CategoriePoiViewSet, PoiViewSet, MessageUrgentViewSet, InformationViewSet, ImageCarrouselViewSet

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
router.register(r'informations', InformationViewSet)
router.register(r'carrousel', ImageCarrouselViewSet)

urlpatterns=router.urls