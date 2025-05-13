from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.contrib.staticfiles.storage import staticfiles_storage
from django.contrib.admin.sites import site
from .models import Booking, WorkerProfile, Review, User
from .forms import BookingForm
from django import forms

# Worker Profile Admin
@admin.register(WorkerProfile)
class WorkerProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'job_type', 'experience', 'hourly_rate', 'location', 'is_available')
    list_filter = ('job_type', 'location', 'is_available')
    search_fields = ('user__username', 'job_type', 'location')
    ordering = ('job_type', 'hourly_rate', 'experience')



@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    form = BookingForm
    list_display = ('customer', 'worker', 'date_time', 'duration', 'total_cost', 'status', 'rate')
    list_filter = ('status', 'date_time')
    search_fields = ('customer__username', 'worker__user__username', 'status')
    ordering = ('date_time', 'status')
    readonly_fields = ('total_cost','rate')

    class Media:
        js = ('admin/js/booking.js',)  # Ensure JS is loaded

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        """Customize worker dropdown to include hourly rate as data attribute."""
        if db_field.name == "worker":
            kwargs["queryset"] = WorkerProfile.objects.all()
            kwargs["widget"] = forms.Select(attrs={"data-rate": "rate"})
        return super().formfield_for_foreignkey(db_field, request, **kwargs)



# Review Admin Panel
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('booking', 'rating', 'comment')
    list_filter = ('rating',)
    search_fields = ('booking__worker__user__username', 'comment')
    ordering = ('rating',)

# User Admin Panel
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_customer', 'is_worker', 'is_superuser')
    list_filter = ('is_customer', 'is_worker', 'is_superuser')
    search_fields = ('username', 'email')
    ordering = ('username', 'email')
