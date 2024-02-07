from datetime import datetime

import pytest
from django.test import Client
from django.urls import reverse

from ConservationForum.models import Species, Badge


@pytest.mark.django_db
def test_species(forum1):
    client = Client()
    url = reverse('forum')
    response = client.get(url)
    assert response.status_code == 200
    assert response.context['forum_list'].count() ==1
    assert response.context['forum_list'][0] == forum1

# @pytest.mark.django_db
# def test_species(post_list):
#     client = Client()
#     url = reverse('forum')
#     response = client.get(url)
#     assert response.status_code == 200
#     assert response.context['forum_list'].count() == len(post_list)
#     for post in post_list:
#         assert post in response.context['forum_list']