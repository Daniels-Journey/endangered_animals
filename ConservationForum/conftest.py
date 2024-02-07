import pytest
from django.contrib.auth.models import User

from ConservationForum.models import Badge, Species, Post, Topic, ExtinctionLevel

topic = Topic.objects.create(title="Topic title 1")
extinct = ExtinctionLevel.objects.create(name="extinction level 1")
species = Species.objects.create(name="Species name 1", population=1000, description="Your species description 1", extinction_level=extinct)
user = User.objects.create(username="your_username")

topic2 = Topic.objects.create(title="Topic title 2")
extinct2 = ExtinctionLevel.objects.create(name="extinction level 2")
species2 = Species.objects.create(name="Species name 2", population=1000, description="Your species description 2", extinction_level=extinct2)
user2 = User.objects.create(username="your_username")

@pytest.fixture
def forum1():
    post = Post.objects.create(topic=topic,text="Your post text goes here", user=user)
    post.species.add(species)
    return post



# @pytest.fixture
# def post_list():
#     posts=[]
#     for i in range():
#         post = Post.objects.create(topic=topic2, text=f"Your post text goes herem {i}", user=user)
#         post.species2.add(species2)
#         posts.append(post)
#
#     return post
