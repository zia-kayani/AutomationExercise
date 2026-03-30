from framework.api.services.product_service import ProductService
from framework.api.services.user_service import UserService
import pytest
from faker import Faker

faker = Faker()
name  = f"jhon{faker.first_name()}"  
email = f"jhon{faker.email()}"
password = faker.password(length=10)     

@pytest.fixture
def user_name_email():
    return name, email

@pytest.fixture
def user_email():
    return email

@pytest.fixture
def user_name_email_password():

     return {
        "name": name,
        "email": email,
        "password": password
     }

@pytest.fixture
def new_user_payload():

    payload = {
        "name": name,
        "email": email,
        "password": password,
        "title": "Mr",
        "birth_date": "11",
        "birth_month": "06",
        "birth_year": "2002",
        "firstname": "Test",
        "lastname": "User",
        "company": "btk",
        "address1": "askari",
        "address2": "lahore",
        "country": "pakistan",
        "zipcode": "9999",
        "state": "punjab",
        "city": "lahore",
        "mobile_number": "999"
    }
    return payload

@pytest.fixture
def update_user_detail(user_name_email_password):
        payload = {
        "name": user_name_email_password["name"],
        "email": user_name_email_password["email"],
        "password": user_name_email_password["password"],
        "title": "Mr",
        "birth_date": "11",
        "birth_month": "06",
        "birth_year": "2002",
        "firstname": "Test",
        "lastname": "User",
        "company": "btk",
        "address1": "askari",
        "address2": "lahore",
        "country": "pakistan",
        "zipcode": "9999",
        "state": "punjab",
        "city": "lahore",
        "mobile_number": "999"
        }
        return payload
    
# factory fixture for the different login API scenarios
@pytest.fixture
def user_factory():
        def _user_login(*fields,**overrides):
            data =  {
                "name": name,
                "email": email,
                "password": password,
                "title": "Mr",
                "birth_date": "11",
                "birth_month": "06",
                "birth_year": "2002",
                "firstname": "Test",
                "lastname": "User",
                "company": "btk",
                "address1": "askari",
                "address2": "lahore",
                "country": "pakistan",
                "zipcode": "9999",
                "state": "punjab",
                "city": "lahore",
                "mobile_number": "999"
                # **overrides
            }
            #keep only required fields in the payload if specified
            if fields:
                data = {k: data[k] for k in fields }
            data.update(overrides)
            return data
        
        return _user_login
     


@pytest.fixture
def user_service():
    return UserService()

# ---------- product related fixtures -----------
@pytest.fixture
def product_service():
    return ProductService()