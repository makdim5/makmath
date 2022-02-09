import requests
import pytest
from django.urls import reverse

BASE_LOCATION = "http://127.0.0.1:8000"


@pytest.mark.parametrize("location",
                         ['',
                          '/topics/topc1/',
                          ])
def test_view_url_exists_at_desired_location(location):
    resp = requests.get(BASE_LOCATION + location)
    assert resp.status_code == 200


@pytest.mark.parametrize("name",
                         ['home',
                          'about',
                          'login',
                          'logout',
                          'registration'
                          ])
def test_view_url_accessible_by_name(name):
    resp = requests.get(BASE_LOCATION + reverse(name))
    assert resp.status_code == 200



