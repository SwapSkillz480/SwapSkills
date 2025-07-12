from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Profile(models.Model):
    AVAILABILITY_CHOICES = [
        ('Weekends', 'Weekends'),
        ('Evenings', 'Evenings'),
        ('Anytime', 'Anytime'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=255)
    profile_photo = models.ImageField(upload_to='profile_photos/', blank=True, null=True)
    skills_offered = models.TextField()
    skills_wanted = models.TextField()
    availability = models.CharField(max_length=20, choices=AVAILABILITY_CHOICES)
    is_public = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
