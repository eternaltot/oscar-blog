from oscar.core.loading import is_model_registered

from blogs.abstract_models import AbstractCategory
from blogs.abstract_models import AbstractCategoryMapping, AbstractPost

if not is_model_registered('blogs', 'Category'):
    class Category(AbstractCategory):
        pass

if not is_model_registered('blogs', 'CategoryMapping'):
    class CategoryMapping(AbstractCategoryMapping):
        pass

if not is_model_registered('blogs', 'Post'):
    class Post(AbstractPost):
        pass
