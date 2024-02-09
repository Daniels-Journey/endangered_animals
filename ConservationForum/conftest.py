import pytest
from django.contrib.auth.models import User
from django.test import Client

from ConservationForum.models import Badge, Species, Post, Topic, ExtinctionLevel





@pytest.fixture
def post_create():
    topic = Topic.objects.create(title="Topic title 1")
    extinct = ExtinctionLevel.objects.create(name="extinction level 1")
    species = Species.objects.create(name="Species name 1", population=1000, description="Your species description 1", extinction_level=extinct)
    user = User.objects.create(username="your_username")
    post = Post.objects.create(text="Your post text goes here", user=user, topic=topic)
    post.species.add(species)
    return post



@pytest.fixture
def post_length():
    posts = []
    topic = Topic.objects.create(title="Topic title ")
    extinct = ExtinctionLevel.objects.create(name="extinction level ")
    species = Species.objects.create(name="Species name ", population=1000, description="Your species description ", extinction_level=extinct)
    user = User.objects.create(username="your_username")
    for i in range(2):
        post = Post.objects.create(text=f"Your post text goes here", user=user, topic=topic)
        post.species.add(species)
        posts.append(post)
    return posts



@pytest.fixture
def species_list():
    extinct = ExtinctionLevel.objects.create(name="extinction level 1")
    species = Species.objects.create(name="Species name 1", population=1000, description="Your species description 1", extinction_level=extinct)
    return species

@pytest.fixture
def species_length():
    extinct = ExtinctionLevel.objects.create(name="extinction level 1")
    lista =[
        Species.objects.create(name="Species name 1", population=1000, description="Your species description 1", extinction_level=extinct),
        Species.objects.create(name="Species name 2", population=500, description="Your species description 2", extinction_level=extinct)
        ]
    return lista


@pytest.fixture
def logged_in_client():
    client = Client()
    user = User.objects.create_user(username='test', password='<PASSWORD>')
    client.login(username='test', password='<PASSWORD>')
    return client


@pytest.fixture
def logged_in_superuser():
    client = Client()
    superuser = User.objects.create_superuser(username='admin', password='adminpassword')
    client.login(username='admin', password='adminpassword')
    return client