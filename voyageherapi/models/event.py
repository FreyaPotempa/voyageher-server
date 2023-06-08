from django.db import models


class Event(models.Model):
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=500)
    img_url = models.URLField()
    date_time = models.DateTimeField(auto_now=False, auto_now_add=False)
    duration = models.IntegerField()
    host = models.ForeignKey(
        "Guide", on_delete=models.CASCADE, related_name="events")
    location = models.ForeignKey(
        "Location", on_delete=models.CASCADE, related_name="events")
    available_spots = models.IntegerField()
    attendees = models.ManyToManyField("Traveler", related_name="attending")

    @property
    def joined(self):
        '''event joined def'''
        return self.__joined

    @joined.setter
    def joined(self, value):
        '''sets the event joined'''
        self.__joined = value


# TODO: add the spots remaining with @property like zis from Bangazon?
    # @property
    # def number_purchased(self):
    #     """Returns the number of times product shows up on completed orders
    #     """
    #     return self.orders.filter(Q(completed_on__isnull=False)).count()
