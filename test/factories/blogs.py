import factory
from oscar.core.loading import get_model

from django.utils import timezone

from blogs import models


class CategoryFactory(factory.django.DjangoModelFactory):
    name = factory.Sequence(lambda n: 'Category %d' % n)

    class Meta:
        model = models.Category


class PostFactory(factory.django.DjangoModelFactory):
    title = factory.Sequence(lambda n: 'Post %d' % n)
    content = factory.Sequence(lambda n: 'Content Post %d' % n)
    post_date = timezone.now()
    author = factory.SubFactory("test.factories.SuperUserFactory")

    class Meta:
        model = models.Post


class CategoryMappingFactory(factory.DjangoModelFactory):
    post = factory.SubFactory(PostFactory)
    category = factory.SubFactory(CategoryFactory)

    class Meta:
        model = get_model('blogs', 'CategoryMapping')


class PostWithCategoryFactory(PostFactory):
    post_category1 = factory.RelatedFactory(
        CategoryMappingFactory, 'post')
    post_category2 = factory.RelatedFactory(
        CategoryMappingFactory, 'post')
