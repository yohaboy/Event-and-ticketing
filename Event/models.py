from django.db import models
from User.models import UserProfile

# Create your models here.
class Location(models.Model):
    City = models.CharField(max_length=50)

    def __str__(self):
        return self.City

class Category(models.Model):
    category_name = models.CharField(max_length=100)

    def __str__(self):
        return self.category_name

class EventModel(models.Model):
    Title = models.CharField(max_length=256)
    Description = models.TextField()
    """
    try to use Location api form maps
    """
    Location = models.ForeignKey(Location , on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(null=True,blank=True)
    Category = models.ForeignKey(Category , on_delete=models.CASCADE)
    image = models.ImageField(upload_to='event_images/', null=True, blank=True)
    organizer = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.Title
