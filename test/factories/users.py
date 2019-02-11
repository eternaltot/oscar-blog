import factory

from oscar.core.compat import get_user_model

User = get_user_model()


class UserFactory(factory.DjangoModelFactory):
    username = factory.Sequence(lambda n: 'user nummer %d' % n)
    email = factory.Sequence(lambda n: 'example_user_%s@example.com' % n)
    first_name = 'wade'
    last_name = 'wilson'
    password = factory.PostGenerationMethodCall('set_password', 'skelebrain')
    # is_staff = True

    class Meta:
        model = get_user_model()


class SuperUserFactory(factory.DjangoModelFactory):
    is_superuser = True
    username = factory.Sequence(lambda n: 'user admin nummer %d' % n)
    email = factory.Sequence(lambda n: 'example_superuser_%s@example.com' % n)
    first_name = 'wade'
    last_name = 'wilson'
    password = factory.PostGenerationMethodCall('set_password', 'skelebrain')
    is_staff = True

    class Meta:
        model = get_user_model()
