import pytest

@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.api
def test_get_all_products_list(product_service):
    response_json = product_service.get_all_products()

    assert response_json.get("responseCode") == 200 , f"Expected response code 200, got {response_json.get('responseCode')}"
    products = response_json.get("products")

    product = products[0]
    expected_keys =  {"id", "name", "price", "brand", "category"}

    assert expected_keys.issubset(product.keys()), f"Expected keys {expected_keys} in product details, but got {product.keys()}"


@pytest.mark.regression
@pytest.mark.api
def test_post_to_all_product_list(product_service):
    response_json = product_service.post_to_all_product_list()

    assert response_json.get("responseCode") == 405, f"Expected response code 405 for POST on products list, got {response_json.get('responseCode')}"
    assert response_json.get("message") == "This request method is not supported.", f"Expected message 'This request method is not supported.' for POST on products list, got {response_json.get('message')}"

@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.api
def test_get_all_brands(product_service):
    response_json = product_service.get_all_brands()

    assert response_json.get("responseCode") == 200, f"Expected response code 200, got {response_json.get('responseCode')}"
    brands = response_json.get("brands")

    brand = brands[0]
    expected_keys = {"id", "brand"}
    assert expected_keys.issubset(brand.keys()), f"Expected keys {expected_keys} in brand details, but got {brand.keys()}"

@pytest.mark.regression
@pytest.mark.api
def test_put_to_all_brands(product_service):
    response_json = product_service.put_to_all_brands()

    assert response_json.get("responseCode") == 405, f"Expected response code 405 for PUT on brands list, got {response_json.get('responseCode')}"
    assert response_json.get("message") == "This request method is not supported."
    "", f"Expected message 'This request method is not supported.' for PUT on brands list, got {response_json.get('message')}"

@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.api
@pytest.mark.parametrize("payload", [{"search_product": "jean"}, {"search_product": "top"}, {"search_product": "tshirt"}])
def test_search_a_product(product_service, payload):
    response_json = product_service.search_a_product(payload)
    assert response_json.get("responseCode") == 200, f"Expected response code 200, got {response_json.get('responseCode')}"

    products = response_json.get("products")
    
    product = products[0]
    expected_keys = {"id", "name", "price", "brand", "category"}
    assert expected_keys.issubset(product.keys()), f"Expected keys {expected_keys} in product details, but got {product.keys()}"


@pytest.mark.regression
@pytest.mark.api
def test_search_a_product_without_payload(product_service):
    response_json = product_service.search_a_product_without_payload()

    assert response_json.get("responseCode") == 400, f"Expected response code 400 for searching product without payload, got {response_json.get('responseCode')}"
    assert response_json.get("message") == "Bad request, search_product parameter is missing in POST request.", f"Expected message 'Bad Request: Missing search_product parameter.' for searching product without payload, got {response_json.get('message')}"