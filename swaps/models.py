from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class SwapRequest(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Accepted', 'Accepted'),
        ('Rejected', 'Rejected'),
    ]
    from_user = models.ForeignKey(User, related_name='sent_requests', on_delete=models.CASCADE)
    to_user = models.ForeignKey(User, related_name='received_requests', on_delete=models.CASCADE)
    # Deprecated: skill = models.CharField(max_length=255)
    skill_offered_by_sender = models.CharField(max_length=255, help_text="Skill you will teach in exchange", default="N/A")
    skill_requested_by_sender = models.CharField(max_length=255, help_text="Skill you want to learn", default="N/A")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.from_user} ↔ {self.to_user} (Wants: {self.skill_requested_by_sender}, Offers: {self.skill_offered_by_sender}) [{self.status}]"

class Feedback(models.Model):
    swap_request = models.OneToOneField(SwapRequest, on_delete=models.CASCADE, related_name='feedback')
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    comment = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Feedback for {self.swap_request} - Rating: {self.rating}"
