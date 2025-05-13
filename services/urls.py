
# from rest_framework.routers import DefaultRouter
# from .views import (
#     WorkerViewSet, BookingViewSet, ReviewViewSet,
#     get_worker_rate, index, bookings, worker_profile
# )

# router = DefaultRouter()
# router.register(r'workers', WorkerViewSet)
# router.register(r'bookings', BookingViewSet)
# router.register(r'reviews', ReviewViewSet)

from django.urls import path, include
from .views import index, bookings, worker_profile

urlpatterns = [
    # # API endpoints
    # path("api/", include(router.urls)),
    # path("api/get_worker_rate/", get_worker_rate, name="get_worker_rate"),

    # Frontend pages
    path("", index, name="index"),
    path("bookings/", bookings, name="bookings"),
    path("worker/", worker_profile, name="worker_profile"),

]
