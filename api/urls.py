from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import WorkerViewSet, BookingViewSet, ReviewViewSet, get_worker_rate

router = DefaultRouter()
router.register(r'workers', WorkerViewSet)
router.register(r'bookings', BookingViewSet)
router.register(r'reviews', ReviewViewSet)

urlpatterns = [
    # API endpoints
    path("", include(router.urls)),
    path("get_worker_rate/", get_worker_rate, name="get_worker_rate"),
]