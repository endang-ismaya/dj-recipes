from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserProfile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="profile", null=True
    )
    bio = models.TextField(blank=True, null=True)
    photo = models.ImageField(
        upload_to="profile_photos/", null=True, blank=True
    )
    # date time creation
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    else:
        # save profile instance when updated
        try:
            instance.profile.save()
        except ObjectDoesNotExist:
            UserProfile.objects.create(user=instance)
