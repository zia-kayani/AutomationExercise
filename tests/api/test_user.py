import pytest

@pytest.mark.smoke
@pytest.mark.api
def test_create_new_user(user_service, new_user_payload):
    
    response_json = user_service.create_new_user(new_user_payload)

    # Assert API-level response
    assert response_json["responseCode"] == 201
    assert response_json["message"] == "User created!"
