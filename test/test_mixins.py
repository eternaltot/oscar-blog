from test import factories
from django.test import TestCase


class WebTestCase(TestCase):
    def create_super_user(self):
        self.super_user = factories.SuperUserFactory()

    def create_user(self):
        self.user = factories.UserFactory()

    def login(self):
        if not hasattr(self, 'user'):
            self.create_user()

        self.client.login(
            username=self.user.email,
            password='skelebrain'
        )

    def login_as_super_user(self):
        if not hasattr(self, 'super_user'):
            self.create_super_user()

        self.client.login(
            username=self.super_user.email,
            password='skelebrain'
        )

    def change_country_store(self, country_code):
        self.client.get("/{}".format(country_code.lower()))
