from django.db import models


class Rating(models.Model):
    guide_id = models.ForeignKey("Guide", on_delete=models.CASCADE)
    traveler_id = models.ForeignKey("Traveler", on_delete=models.CASCADE)
    rating = models.IntegerField()
