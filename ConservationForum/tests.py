from datetime import datetime
import pytest
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.urls import reverse, resolve
from django.test import Client
from ConservationForum.models import Species, Badge, ExtinctionLevel, Post


# Testing Forum view
@pytest.mark.django_db
def test_forum_list(post_create):
    client = Client()
    url = reverse('forum')
    response = client.get(url)
    assert response.status_code == 200
    assert response.context['forum_list'].count() ==1
    assert response.context['forum_list'][0] == post_create


@pytest.mark.django_db
def test_forum_length(post_length):
    client = Client()
    url = reverse('forum')
    url = f'{url}?text=Your post text goes here'
    response = client.get(url)
    assert response.status_code == 200
    assert response.context['forum_list'].count() == 2
    assert response.context['forum_list'][0] == post_length[0]





# Testing Species list view
@pytest.mark.django_db
def test_species(species_list):
    client1 = Client()
    url1 = reverse('specList')
    response1 = client1.get(url1)
    assert response1.status_code == 200
    assert response1.context['object_list'].count() == 1
    assert response1.context['object_list'][0] == species_list


@pytest.mark.django_db
def test_species_length(species_length):
    client = Client()
    url = reverse('specList')
    url = f'{url}?name=Species name 1'
    response = client.get(url)
    assert response.status_code == 200
    assert response.context['species_list'].count() == 1
    assert response.context['species_list'][0] == species_length[0]






# Testing Home view
def test_home_view():
    client = Client()
    response = client.get(reverse('home'))
    assert response.status_code == 200
    assert 'Welcome' in response.content.decode()


def test_home_content():
    client = Client()
    response = client.get(reverse('home'))
    assert response.context.get('Title') == 'Home Page'






# Testing Add post view
def test_add_post_requires_login():
    client = Client()
    response = client.get(reverse('addPost'))
    assert response.status_code == 302


@pytest.mark.django_db
def test_add_post_loggedin(logged_in_client):
    client = logged_in_client
    response = client.get(reverse('addPost'))
    assert response.status_code == 200





# Testing alter species view
def test_alter_species():
    client = Client()
    response = client.get(reverse('alter_species', kwargs={'pk':1}))
    assert response.status_code == 302


@pytest.mark.django_db
def test_alter_species_loggedin(logged_in_client):
    client = logged_in_client
    extinct = ExtinctionLevel.objects.create(name="extinction level ")
    species = Species.objects.create(name='Test Species', population=200, description='Test Description', extinction_level=extinct)
    response = client.get(reverse('alter_species', kwargs={'pk': species.pk}))
    assert response.status_code == 200






# Testing faq view
def test_faq_view_status_code():
    response = Client().get(reverse('faq'))
    assert response.status_code == 200


def test_faq_view_template_used():
    response = Client().get(reverse('faq'))
    assert 'faq.html' == response.templates[0].name





# Testing gallery view
def test_gallery_view_status_code():
    client = Client()
    response = client.get(reverse('gallery'))
    assert response.status_code == 200

def test_gallery_view_contains_images():
    client = Client()
    response = client.get(reverse('gallery'))
    assert '<img' in str(response.content)






# Testing add badge view
def test_badge_view_get():
    client = Client()
    response = client.get(reverse('add_badge', kwargs={'pk': 1}))
    assert response.status_code == 302

def test_badge_view_post():
    client = Client()
    response = client.post(reverse('add_badge', kwargs={'pk': 1}), data={'title': 'New Title'})
    assert response.status_code == 302







# Testing delete post view
@pytest.mark.django_db
def test_get_object_owner(post_create, client):
    post = post_create
    user=User.objects.get(username='your_username')
    client.force_login(user)

    response = client.post(reverse('delete_post', kwargs={'pk': post.pk}))

    assert response.status_code == 302
    assert Post.objects.filter(pk=post.pk).count() == 0

@pytest.mark.django_db
def test_get_object_superuser(post_create, logged_in_superuser):
    post = post_create
    client = logged_in_superuser
    response = client.post(reverse('delete_post', kwargs={'pk': post.pk}))

    assert response.status_code == 302
    assert not Post.objects.filter(pk=post.pk).count()
