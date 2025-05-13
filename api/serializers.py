from rest_framework import serializers
from services.models import WorkerProfile, Booking, Review

class WorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkerProfile
        fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
    worker_hourly_rate = serializers.SerializerMethodField()

    class Meta:
        model = Booking
        fields = '__all__'  # Include all fields along with worker_hourly_rate

    def create(self, validated_data):
        """Auto-calculate total_cost before creating a new booking"""
        # worker = validated_data.get('worker')
        rate = WorkerProfile.hourly_rate if WorkerProfile else 0
        duration = validated_data.get('duration', 1)
        # total_cost = worker.hourly_rate * duration if worker else 0
        total_cost=rate*duration

        validated_data['total_cost'] = total_cost  # Auto-update before saving
        return super().create(validated_data)


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
