from django.db import models


class FaveGuide(models.Model):
    guide_id = models.ForeignKey(
        "Guide", on_delete=models.CASCADE, related_name="subscribers")
    traveler_id = models.ForeignKey(
        "Traveler", on_delete=models.CASCADE, related_name="subscribed")
