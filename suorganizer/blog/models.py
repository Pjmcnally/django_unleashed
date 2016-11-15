from django.db import models
from organizer.models import Startup, Tag

# Create your models here.
class Post(models.Model):
    title = model.CharField(max_length=63)
    slug = models.SlugField(
        max_length=63,
        unique_for_month='pub_date',
        help_text="A lable for URL config",
    )
    text = models.TestField()
    pub_date = models.DateField(
        'date published',
        auto_now_add=True,
    )
    tags = models.ManyToManyField(Tag, related_name='blog_posts',)
    startups = models.ManyToManyField(Startup, related_name='blog_posts',)

