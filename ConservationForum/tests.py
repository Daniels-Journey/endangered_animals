from datetime import datetime

import pytest
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.test import Client, TestCase, RequestFactory
from django.urls import reverse, resolve
from django.test import Client
from ConservationForum.models import Species, Badge, ExtinctionLevel, Post
from ConservationForum.views import DeletePostView


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






@pytest.mark.django_db
def test_spec(species_list):
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







def test_home_view():
    client = Client()
    response = client.get(reverse('home'))
    assert response.status_code == 200
    assert 'Welcome to Wildlife Biodiversity Project' in response.content.decode()



def test_home_content():
    client = Client()
    response = client.get(reverse('home'))
    assert response.context.get('Title') == 'Home Page'







def test_add_post_requires_login():
    client = Client()
    response = client.get(reverse('addPost'))
    assert response.status_code == 302


@pytest.mark.django_db
def test_add_post_loggedin():
    client = Client()
    user = User.objects.create_user(username='test', password='<PASSWORD>')
    client.login(username='test', password='<PASSWORD>')
    response = client.get(reverse('addPost'))
    assert response.status_code == 200






def test_alter_species():
    client = Client()
    response = client.get(reverse('alter_species', kwargs={'pk':1}))
    assert response.status_code == 302


@pytest.mark.django_db
def test_alter_species_loggedin():
    client = Client()
    user = User.objects.create_user(username='test', password='pswd')
    client.login(username='test', password='pswd')
    extinct = ExtinctionLevel.objects.create(name="extinction level ")
    species = Species.objects.create(name='Test Species', population=200, description='Test Description', extinction_level=extinct)
    response = client.get(reverse('alter_species', kwargs={'pk': species.pk}))
    assert response.status_code == 200




@pytest.mark.django_db
def test_get_object_owner(post_create, client):
    post = post_create
    user=User.objects.get(username='your_username')
    client.force_login(user)

    response = client.post(reverse('delete_post', kwargs={'pk': post.pk}))

    assert response.status_code == 302
    assert Post.objects.filter(pk=post.pk).count() == 0

@pytest.mark.django_db
def test_get_object_superuser(post_create, client):
    post = post_create
    superuser = User.objects.create_superuser(username='admin', password='adminpassword')
    client.login(username='admin', password='adminpassword')
    response = client.post(reverse('delete_post', kwargs={'pk': post.pk}))

    assert response.status_code == 302
    assert not Post.objects.filter(pk=post.pk).count()
