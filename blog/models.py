from django.db import models
from django.utils import timezone

# Create your models here.

class Post (models.Model): #model.Models means that the Post is a django model, so django can save to db
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE) #foreignkey is a link to another model
    title = models.CharField(max_length=200)
    text = models.TextField() #like charfiled but no word limit
    createdDate = models.DateTimeField(default=timezone.now)
    publishedDate = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.publishedDate = timezone.now()
        self.save()

    def __str__(self):
        return self.title   #we will get a text (string) with a Post title
