import pytest

@pytest.mark.smoke
@pytest.mark.api
def test_create_new_user(user_service, new_user_payload):
    
    response_json = user_service.create_new_user(new_user_payload)

    assert response_json["responseCode"] == 201
    assert response_json["message"] == "User created!"


#test api endpoint to get user details by email
@pytest.mark.smoke 
@pytest.mark.api
def test_get_user_details(user_service, user_email):
    response_json = user_service.get_user_details(user_email)

    assert response_json["responseCode"] == 200, f"Expected response code 200, got {response_json['responseCode']}"
    assert response_json["user"]["email"] == user_email ,  f"Expected email to be {user_email}, got {response_json['user']['email']}"
    assert "name" in response_json["user"], "Expected 'name' field in user details, but it is missing"
    assert "id" in response_json["user"], "Expected 'id' field in user details, but it is missing"
    assert response_json["user"]["title"] == "Mr", f"Expected title to be 'Mr', got {response_json['user']['title']}"
    assert response_json["user"]["company"] == "btk", f"Expected company to be 'btk', got {response_json['user']['company']}"
    assert response_json["user"]["country"] == "pakistan", f"Expected country to be 'pakistan', got {response_json['user']['country']}" 


#test api endpoint to update user details
@pytest.mark.smoke
@pytest.mark.api
def test_update_user_details(user_service, update_user_detail):

    response = user_service.update_user_details(update_user_detail)
    assert response["responseCode"] == 200, f"Expected response code 200, got {response['responseCode']}"
    assert response["message"] == "User updated!", f"Expected message 'User updated!',  got {response['message']}"
