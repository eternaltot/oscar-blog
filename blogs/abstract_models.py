from oscar.core.compat import AUTH_USER_MODEL

from django.db import models
from django.core.urlresolvers import reverse
from django.conf import settings
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


class Timestamp(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class AbstractPost(Timestamp):
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    featured_image = models.ImageField(
        _('Featured Image'), upload_to=settings.OSCAR_IMAGE_FOLDER,
        blank=True, null=True, max_length=255
    )
    post_date = models.DateField('Post Date', default=timezone.now())
    categories = models.ManyToManyField(
        'blogs.Category',
        through='CategoryMapping',
        verbose_name=_("Categories")
    )
    excerpt = models.CharField(max_length=200)
    author = models.ForeignKey(
        AUTH_USER_MODEL,
        blank=True, null=True,
        on_delete=models.CASCADE
    )

    def get_absolute_url(self):
        url = reverse('blog-post-detail', kwargs={"id": self.id})
        return url

    class Meta:
        ordering = ['-post_date', 'title']
        abstract = True

    def __str__(self):
        return self.title


class AbstractCategory(Timestamp):
    name = models.CharField(max_length=64)

    class Meta:
        ordering = ['name']
        abstract = True

    def __str__(self):
        return self.name


class AbstractCategoryMapping(Timestamp):
    post = models.ForeignKey('blogs.Post', on_delete=models.CASCADE)
    category = models.ForeignKey('blogs.Category', on_delete=models.CASCADE)

    def __str__(self):
        return "{}-{}".format(self.post, self.category)
    
    class Meta:
        abstract = True
