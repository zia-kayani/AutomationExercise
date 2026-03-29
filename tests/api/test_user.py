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

#test api endpoint to login user with valid data
@pytest.mark.smoke
@pytest.mark.api
def test_login_user_with_valid_data(user_service, user_factory):
    payload =  user_factory("email", "password")
    response_json =  user_service.login_user_with_valid_data(payload)
    assert response_json["responseCode"] == 200, f"Expected response code 200, got {response_json['responseCode']}"
    assert response_json["message"] == "User exists!", f"Expected message 'User exists!', got {response_json['message']}"

#test api endpoint to login user with invalid data
@pytest.mark.smoke
@pytest.mark.api
def test_login_user_with_invalid_data(user_service, user_factory):
    payload = user_factory(email="test@gmail.com", password="wrongpassword")
    response_json = user_service.login_user_with_invalid_data(payload)
    assert response_json["responseCode"] == 404, f"Expected response code 404   for invalid login, got {response_json['responseCode']}"
    assert response_json["message"] == "User not found!", f"Expected message 'User not found!' for invalid login, got {response_json['message']}"

#test api endpoint to login user without email
@pytest.mark.smoke
@pytest.mark.api
def test_login_user_without_email(user_service, user_factory):
    payload = user_factory("password") # Only include email and password, using defaults for password 
    response_json = user_service.login_user_without_email(payload)
    assert response_json["responseCode"] == 400, f"Expected response code 400 for login without email, got {response_json['responseCode']}"
    assert response_json["message"] == "Bad request, email or password parameter is missing in POST request.", f"Expected message 'Bad request, email or password parameter is missing in POST request.' for login without email, got {response_json['message']}"

#test api endpoint to login user with delete method
@pytest.mark.api   
def test_login_user_with_delete_method(user_service):
    response_json = user_service.login_user_with_delete_method()
    assert response_json["responseCode"] == 405, f"Expected response code 405 for delete method on login, got {response_json['responseCode']}"
    assert response_json["message"] == "This request method is not supported.", f"Expected message 'This request method is not supported.' for delete method on login, got {response_json['message']}"

# in test methods we can utlitlze factory function like this accoring to our needs
# payload = user_factory("email", "password") # only email and password will be included in the payload, rest of the fields will be default
# payload = user_factory() # all fields will be included in the payload with default values
# payload = user_factory("email", "password", name="Custom Name") # email and password will be included with default values, but name will be overridden with "Custom Name"
#payload = user_factory(name="Custom Name", email="custom email", password="custom password") # all fields will be included but name, email and password will be overridden with custom values


