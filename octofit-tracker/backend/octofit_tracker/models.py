# models.py
from djongo import models

class User(models.Model):
    _id = models.ObjectIdField(primary_key=True)
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        abstract = False

class Team(models.Model):
    _id = models.ObjectIdField(primary_key=True)
    name = models.CharField(max_length=100)
    members = models.ManyToManyField(User)

    def __str__(self):
        return self.name

    class Meta:
        abstract = False

class Activity(models.Model):
    _id = models.ObjectIdField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=50)
    duration = models.IntegerField()

    def __str__(self):
        return f"{self.type} - {self.duration} mins"

    class Meta:
        abstract = False

class Leaderboard(models.Model):
    _id = models.ObjectIdField(primary_key=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    points = models.IntegerField()

    def __str__(self):
        return f"{self.team.name} - {self.points} points"

    class Meta:
        abstract = False

class Workout(models.Model):
    _id = models.ObjectIdField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        abstract = False
