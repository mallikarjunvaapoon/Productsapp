from django.db import models
from user.models import UserModel


class Connection_request(models.Model):
    status_of = models.CharField(max_length=30, choices=[('Request', 'Request'), ('Accepted', 'Accepted'), ('Declined', 'Declined')], default="", null=True)
    sender = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='sender', null=True)
    receiver = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='receiver', null=True)


