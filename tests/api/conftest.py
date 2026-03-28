from framework.api.services.user_service import UserService
import pytest
from faker import Faker

faker = Faker()
name  = f"jhon{faker.first_name()}"  
email = f"jhon{faker.email()}"     

@pytest.fixture
def user_name_email():
    return name, email

@pytest.fixture
def new_user_payload():


    payload = {
        "name": name,
        "email": email,
        "password": faker.password(length=10),
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
def user_service():
    return UserService()