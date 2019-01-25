import datetime
from django.db import models
from django.utils import timezone
# Create your models here.



class Category(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name
        
class Post(models.Model):
    post_title = models.CharField(max_length=200)
    post_content = models.TextField()
    feature_image = models.ImageField()
    post_date = models.DateTimeField('Post Date')
    categories = models.ManyToManyField(
        Category,
        through='CategoryMapping',
        through_fields=('post', 'category'),
    )
    post_excerpt = models.CharField(max_length=200)

    def __str__(self):
        return self.question_text
    
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
        
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

class CategoryMapping(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
