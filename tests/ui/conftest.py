import pytest
from faker import Faker

faker = Faker()

#---- Fixture for user registeration data ----
name = faker.name()
email = faker.email()
first_name = faker.first_name()
last_name = faker.last_name()


@pytest.fixture
def user_data():
    return {
        "name": f"{name}",
        "email": f"{email}",
        "password": "Test@123",

        "day": "1",
        "month": "1",
        "year": "2000",

        "first_name": f"{first_name}",
        "last_name": f"{last_name}",
        "company": "TestCorp",
        "address": "Street 1",
        "address2": "Apt 101",
        "country": "India",
        "state": "Sindh",
        "city": "Karachi",
        "zipcode": "74000",
        "mobile": "03001234567"
    }



