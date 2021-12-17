from django.db import models
from user.models import UserModel

STATUS_CHOICES = (
    ("connected", ("connected")),
    ("blocked", ("blocked")),
    ("accepted", ("accepted")),
    ("request", ("request")),
    ("declined", ("declined"))
)

class Connection_request(models.Model):
    requested = models.CharField(max_length=30, choices=STATUS_CHOICES, default="request", null=True)
    sender = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='sender', null=True)
    receiver = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='receiver', null=True)


