from django.db import models
import datetime

class Movie(models.Model):
    """Describes a Movie"""
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    year = models.IntegerField()
    pub_date = models.DateTimeField(auto_now=True)
    GENRES = (
        ('A', 'Action'),
        ('D','Drama'),
        ('C', 'Comedy'),
        ('S', 'Sci-Fi'),
    )
    genre = models.CharField(max_length=1, choices=GENRES)
#    creator = models.ForeignKey(models.User)

    def __unicode__(self):
        return self.title
    
    def was_published_today(self):
        return self.pub_date.date() == datetime.date.today()
    
    
    
