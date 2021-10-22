from django.db import models
from .user import User
from .pet import Pet


class RequestPet(models.Model):

    class RequestKind(models.TextChoices):
        ADOPTION = 'AD', ('Adoption')
        HANDING = 'HD', ('Handing')

    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    request_kind = models.CharField(
        max_length=2,
        choices=RequestKind.choices)
    finalized_at = models.DateTimeField(null=True, blank=True)
