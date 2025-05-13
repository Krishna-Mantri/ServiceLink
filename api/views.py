from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from services.models import WorkerProfile, Booking, Review
from .serializers import WorkerSerializer, BookingSerializer, ReviewSerializer
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required



class WorkerViewSet(viewsets.ModelViewSet):
    queryset = WorkerProfile.objects.all()
    serializer_class = WorkerSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]


    def get_worker_rate(request):
        worker_id = request.GET.get('worker_id')
        if worker_id:
            try:
                worker = WorkerProfile.objects.get(id=worker_id)
                return JsonResponse({'hourly_rate': worker.hourly_rate})
            except WorkerProfile.DoesNotExist:
                return JsonResponse({'error': 'Worker not found'}, status=404)
        return JsonResponse({'error': 'Invalid request'}, status=400)
    

    

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]



def get_worker_rate(request):
    worker_id = request.GET.get('worker_id')
    if worker_id:
        try:
            worker = WorkerProfile.objects.get(id=worker_id)
            return JsonResponse({'hourly_rate': worker.hourly_rate})
        except WorkerProfile.DoesNotExist:
            return JsonResponse({'error': 'Worker not found'}, status=404)
    return JsonResponse({'error': 'Invalid request'}, status=400)
