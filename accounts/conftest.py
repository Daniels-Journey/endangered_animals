import pytest
from django.contrib.auth.models import User

from ConservationForum.models import Badge, Species, Post, Topic, ExtinctionLevel


@pytest.fixture
def user():
    return User.objects.create_user(username='test', password='pas123')

