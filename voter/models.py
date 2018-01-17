"""
"""
from django.db import models

# Create your models here.
class Show(models.Model):

    name = models.CharField(max_length = 100)

    def __str__(self):
        return self.name

    @property
    def current_season(self):
        return self.seasons.order_by("number").last()


class Season(models.Model):

    number = models.IntegerField()
    airdate = models.DateTimeField()
    show = models.ForeignKey(Show, on_delete = models.CASCADE, related_name = "seasons")

    def __str__(self):
        return f"season {self.number} of {self.show.name}"


class Contestant(models.Model):

    name = models.CharField(max_length = 100)
    date_of_birth = models.DateTimeField()
    origin = models.CharField(max_length = 100)
    seasons = models.ManyToManyField(Season)

    def __str__(self):
        return self.name


class Episode(models.Model):

    length = models.DurationField()
    name = models.CharField(max_length = 100)
    season = models.ForeignKey(Season, on_delete = models.CASCADE)
    winning_contestant = models.ForeignKey(Contestant,
                                           blank = True,
                                           null = True,
                                           related_name = "winning_episodes",
                                           on_delete = models.CASCADE)
    loosing_contestant = models.ForeignKey(Contestant,
                                           blank = True,
                                           null = True,
                                           related_name = "loosing_episodes",
                                           on_delete = models.CASCADE)

    def __str__(self):
        return self.name























if __name__ == "__main__":
    pass
