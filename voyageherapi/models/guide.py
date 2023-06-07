from django.db import models
from django.contrib.auth.models import User


class Guide(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=250)
    location = models.ForeignKey(
        "Location", on_delete=models.CASCADE, related_name="guides")

    @property  # decorator
    def full_name(self):
        """Additional field to capture from the client"""
        return f'{self.user.first_name} {self.user.last_name}'

    @property
    def average_rating(self):
        '''average rating calculator per guide'''

        total_rating = 0
        count = self.ratings.count()
        if count > 0:
            for rating in self.ratings.all():
                total_rating += rating.score

            avg = total_rating / self.ratings.count()
            try:
                return avg
            except ZeroDivisionError:
                return 0
