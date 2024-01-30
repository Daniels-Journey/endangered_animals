from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class ExtinctionLevel(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Species(models.Model):
    name = models.CharField(max_length=64)
    population = models.IntegerField()
    description = models.TextField()
    extinction_level = models.ForeignKey(ExtinctionLevel, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}, population: {self.population}, threat_level: {self.extinction_level}, description: {self}'


class Badge(models.Model):
    title = models.CharField(max_length=64)

    def __str__(self):
        return self.title


class Post(models.Model):
    text = models.TextField()
    date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # topic = models.ForeignKey(Topic, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.text}, topic: {self.topic.title}, date: {self.date}, user: {self.user.name}'


class Topic(models.Model):
    title = models.CharField(max_length=64)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    species = models.ForeignKey(Species, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}, post: {self.post.text}, species: {self.species}'