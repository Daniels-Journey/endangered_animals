from django.contrib.auth.models import User
from django.test import TestCase
import pytest
from django.test import Client
from django.urls import reverse

@pytest.mark.django_db
def test_login_success(user):
    client = Client()
    url_login = reverse('login_view')
    response = client.post(url_login,{'username': 'test', 'password': 'pas123'})
    assert response.status_code == 302
    assert response.url == reverse('home')


@pytest.mark.django_db
def test_login_failure(user):
    client = Client()
    url_login = reverse('login_view')
    response = client.post(url_login,{'username': 'invalid', 'password': '<PASSWORD>'})
    assert response.status_code == 200






@pytest.mark.django_db
def test_logout_succcessful():
    user = User.objects.create_user(username='test', password='whatever')
    client = Client()
    client.force_login(user)
    response = client.get(reverse("logout_view"))
    assert response.status_code == 302
    assert '_auth_user_id' not in client.session
    assert response.url == reverse('home')


@pytest.mark.django_db
def test_already_logout():
    client = Client()
    response = client.get(reverse('logout_view'))
    assert response.status_code == 302
    assert response.url == reverse('home')





@pytest.mark.django_db
def test_successful_registration():
    client = Client()
    register_url = reverse('register_view')
    response = client.post(register_url,{
        'username': 'testuser',
        'email': 'testuser@example.com',
        'password': 'password123',
        'repeat_password': 'password123'
                                         })
    assert response.status_code == 302
    assert User.objects.filter(username ='testuser').exists()
    assert response.url == reverse('home')


@pytest.mark.django_db
def test_unsuccessful_registration():
    client = Client()
    register_url = reverse('register_view')
    response = client.post(register_url, {
        'username': 'test',
        'email': 'testuser@gmail.com',
        'password': 'password123',
        'repeat_password': 'password123'
                                                })
    assert response.status_code == 302
    assert '' in response.content.decode()