import pytest

from tests.factories import (
    UserFactory,
    ResumeFactory,
    SkillFactory,
    ProjectFactory,
    SocialLinkFactory,
    ResumeAnalyticsFactory,
    AnalyticsEventFactory,
)


@pytest.fixture
def user():

    return UserFactory()


@pytest.fixture
def resume():

    return ResumeFactory()


@pytest.fixture
def skill():

    return SkillFactory()


@pytest.fixture
def project():

    return ProjectFactory()


@pytest.fixture
def social():

    return SocialLinkFactory()


@pytest.fixture
def analytics():

    return ResumeAnalyticsFactory()

@pytest.fixture
def analytics_event():

    return AnalyticsEventFactory()