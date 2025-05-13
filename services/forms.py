from django import forms
from .models import Booking, WorkerProfile

class BookingForm(forms.ModelForm):
    worker = forms.ModelChoiceField(
        queryset=WorkerProfile.objects.all(),
        widget=forms.Select(attrs={"class": "worker-dropdown"})
    )

    class Meta:
        model = Booking
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Modify worker dropdown to show hourly rate in the frontend
        self.fields["worker"].queryset = WorkerProfile.objects.all()
        self.fields["worker"].widget.attrs.update({
            "class": "worker-dropdown"
        })
        # self.fields["worker"].widget.choices = [
        #         (worker.id, f"{worker.user.username} - {worker.hourly_rate} RS/hour")
        #         for worker in WorkerProfile.objects.all()
        #     ]



# from django import forms
# from .models import Booking, WorkerProfile

# class BookingForm(forms.ModelForm):
#     class Meta:
#         model = Booking
#         fields = '__all__'

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         if "worker" in self.fields:
#             # Dynamically add worker hourly rate in dropdown
#             self.fields["worker"].queryset = WorkerProfile.objects.all()
#             self.fields["worker"].widget.attrs.update({"class": "worker-dropdown"})
#             self.fields["worker"].widget.choices = [
#                 (worker.id, f"{worker.user.username} - {worker.hourly_rate} RS/hour")
#                 for worker in WorkerProfile.objects.all()
#             ]
