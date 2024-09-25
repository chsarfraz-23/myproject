import pytest

from tests.fixtures import fx_product_type
from tests.fixtures import api_client

@pytest.mark.django_db
def test_product_type(api_client,
                      fx_product_type):
    url = "/myapp/ProductType/"
    response =  api_client.get(url)
    assert response.status_code == 200



