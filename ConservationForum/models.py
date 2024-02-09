from django.contrib.auth.models import User, AbstractUser
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
        return f'{self.name}'


class Badge(models.Model):
    title = models.CharField(max_length=64)

    def __str__(self):
        return self.title



class Topic(models.Model):
    title = models.CharField(max_length=64)

    def __str__(self):
        return f'{self.title}'



class Post(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date = models.DateField(auto_now_add=True)
    species = models.ManyToManyField(Species)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'topic: {self.topic.title}, text: {self.text} date: {self.date}, species: {", ".join(species.name for species in self.species.all())}'
