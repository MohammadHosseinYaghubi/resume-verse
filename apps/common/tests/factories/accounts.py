import factory

from apps.accounts.models import User


class UserFactory(factory.django.DjangoModelFactory):

    class Meta:

        model = User

    username = factory.Sequence(
        lambda n: f"user{n}"
    )

    email = factory.LazyAttribute(
        lambda obj: f"{obj.username}@example.com"
    )

    first_name = factory.Faker(
        "first_name",
    )

    last_name = factory.Faker(
        "last_name",
    )

    is_active = True

    @factory.post_generation
    def password(
        self,
        create,
        extracted,
        **kwargs,
    ):

        self.set_password(
            extracted or "password123",
        )

        if create:

            self.save()