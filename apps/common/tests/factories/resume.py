import factory

from apps.resume.models import (
    Resume,
    Skill,
    SkillCategory,
    Project,
    SocialLink
    
)

from .accounts import UserFactory


class ResumeFactory(factory.django.DjangoModelFactory):

    class Meta:

        model = Resume

    user = factory.SubFactory(
        UserFactory,
    )

    full_name = factory.Faker(
        "name",
    )

    slug = factory.Sequence(
        lambda n: f"resume-{n}"
    )

    title = factory.Faker(
        "job",
    )

    bio = factory.Faker(
        "paragraph",
    )

    email = factory.LazyAttribute(
        lambda obj: obj.user.email,
    )

    phone = "09120000000"

    location = factory.Faker(
        "city",
    )
    

class SkillCategoryFactory(
    factory.django.DjangoModelFactory,
):

    class Meta:

        model = SkillCategory

    name = factory.Sequence(
        lambda n: f"Backend {n}"
    )


class SkillFactory(
    factory.django.DjangoModelFactory,
):

    class Meta:

        model = Skill

    name = factory.Sequence(
        lambda n: f"Django {n}"
    )

    category = factory.SubFactory(
        SkillCategoryFactory,
    )
    
    


class ProjectFactory(
    factory.django.DjangoModelFactory,
):

    class Meta:

        model = Project

    resume = factory.SubFactory(
        ResumeFactory,
    )

    title = factory.Sequence(
        lambda n: f"Project {n}"
    )

    slug = factory.Sequence(
        lambda n: f"project-{n}"
    )

    description = factory.Faker(
        "paragraph",
    )    
    


class SocialLinkFactory(
    factory.django.DjangoModelFactory,
):

    class Meta:

        model = SocialLink

    resume = factory.SubFactory(
        ResumeFactory,
    )

    platform = "github"

    url = factory.Sequence(
        lambda n: f"https://github.com/user{n}"
    )