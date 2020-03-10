from django.db import models


class Share(models.Model):
    share_id = models.CharField(max_length=10, primary_key=True)
    share_data = models.TextField()

    def create_new_share(self, share_id, share_data):
        self.share_data = share_data
        self.share_id = share_id

    def __str__(self):
        return str(self.share_id + "-" + self.user_id)


class UserShareMapping(models.Model):
    user_id = models.CharField(max_length=100, primary_key=True)
    shares = models.ManyToManyField(Share, blank=True, null=True)

    def __str__(self):
        return str(self.user_id)

