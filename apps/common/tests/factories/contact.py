import factory

from apps.contact.models import ContactMessage

from .accounts import UserFactory


class ContactFactory(
    factory.django.DjangoModelFactory,
):

    class Meta:

        model = ContactMessage

    user = factory.SubFactory(
        UserFactory,
    )

    name = factory.Faker(
        "name",
    )

    email = factory.Faker(
        "email",
    )

    subject = factory.Sequence(
        lambda n: f"Subject {n}"
    )

    message = factory.Faker(
        "paragraph",
    )

    ip_address = "127.0.0.1"

    user_agent = "pytest"