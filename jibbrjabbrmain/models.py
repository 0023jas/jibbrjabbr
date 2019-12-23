from django.db import models

# Create your models here.
class JJStory(models.Model):
    storyTitle = models.TextField()
    storyImg = models.TextField()
    storyURL = models.TextField()

class storyReloadConditional(models.Model):
    conditional = models.TextField()

class JJItem(models.Model):
    content = models.TextField()