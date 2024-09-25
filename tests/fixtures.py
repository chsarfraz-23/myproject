import pytest
from rest_framework.test import APIClient

from myapp.models import ProductTypes

@pytest.fixture
def api_client():
    yield APIClient()


@pytest.fixture
def fx_product_type():
    ProductTypes.objects.create(name="test_name")