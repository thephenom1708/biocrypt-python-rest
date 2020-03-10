from django.db import models
import secrets


class Share(models.Model):
    share_id = models.CharField(max_length=10, primary_key=True)
    share_number = models.CharField(max_length=10, default="1")
    share_data = models.TextField()

    def create_new_share(self, share_number, share_data):
        self.share_id = secrets.token_hex(15)
        self.share_number = share_number
        self.share_data = share_data

    def __str__(self):
        return str(self.share_number + " -- " + self.share_id)


class UserShareMapping(models.Model):
    user_id = models.CharField(max_length=100, primary_key=True)
    shares = models.ManyToManyField(Share)

    def __str__(self):
        return str(self.user_id)

