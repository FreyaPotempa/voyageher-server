from django.db import models


class Rating(models.Model):
    guide = models.ForeignKey(
        "Guide", on_delete=models.CASCADE, related_name='ratings')
    traveler = models.ForeignKey("Traveler", on_delete=models.CASCADE)
    score = models.IntegerField()
    review = models.TextField(null=True, blank=True)
