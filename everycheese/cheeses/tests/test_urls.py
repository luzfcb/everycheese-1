import pytest
from django.urls import reverse, resolve
from .factories import CheeseFactory


pytestmark = pytest.mark.django_db

@pytest.fixture
def cheese():
    return CheeseFactory()
