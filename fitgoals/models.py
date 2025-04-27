from django.db import models

class Workouts(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    date = models.DateField()
    activity = models.CharField(max_length=100)
    duration = models.IntegerField()  # in minutes
    set = models.CharField(max_length=100)
    reps = models.IntegerField()
    weight = models.IntegerField()  # in kg
    notes = models.TextField(blank=True, null=True)


    # new code below
    def __str__(self):
        return self.name



