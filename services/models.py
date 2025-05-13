from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.exceptions import ValidationError
from decimal import Decimal

# Custom User Model
class User(AbstractUser):
    is_customer = models.BooleanField(default=False)
    is_worker = models.BooleanField(default=False)

    # Add related_name to prevent conflicts
    groups = models.ManyToManyField(
        "auth.Group",
        related_name="custom_user_groups",  # Custom related_name
        blank=True
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="custom_user_permissions",  # Custom related_name
        blank=True
    )


# Worker Profile Model
class WorkerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="worker_profile",limit_choices_to={"is_worker": True} )
    job_type = models.CharField(max_length=50, choices=[
        ('maid', 'Maid'),
        ('electrician', 'Electrician'),
        ('plumber', 'Plumber'),
        ('gardener', 'Gardener'),
        ('painter', 'Painter'),
        ('carpenter', 'Carpenter'),
        ('mechanic', 'Mechanic'),
        ('chef', 'Chef'),
        ('babysitter', 'Babysitter'),
        ('tutor', 'Tutor'),
        ('trainer', 'Trainer'),
        ('driver', 'Driver'),
        ('cleaner', 'Cleaner'),
    ])
    experience = models.PositiveIntegerField()
    hourly_rate = models.DecimalField(max_digits=6, decimal_places=2, default=0.0)
    location = models.CharField(max_length=255)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username

# Booking Model
class Booking(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bookings",limit_choices_to={"is_customer": True})
    worker = models.ForeignKey(WorkerProfile, on_delete=models.CASCADE,)
    date_time = models.DateTimeField( auto_now_add=True)
    duration= models.PositiveIntegerField(help_text="Duration in hours", default=1)
    rate=models.FloatField(blank=True, default=0.0,)
    total_cost = models.DecimalField(max_digits=8, decimal_places=2, editable=False)
    status = models.CharField(max_length=20, choices=[
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ], default='pending')

    def save(self, *args, **kwargs):
        if self.duration <= 0:
            raise ValidationError("Duration must be greater than zero.")

        if self.worker:
            self.rate=self.worker.hourly_rate
            self.total_cost = Decimal(self.rate) * Decimal(self.duration)
        else:
            self.total_cost =Decimal(0)

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.customer.username} booked {self.worker.user.username}"

# Reviews Model
class Review(models.Model):
    booking = models.OneToOneField(Booking, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
