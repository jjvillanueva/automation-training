"""
Pytest fixtures for API tests
"""
import pytest
import os
from dotenv import load_dotenv
from tests.api.helpers.api_client import APIClient

# Load environment variables
load_dotenv()


@pytest.fixture(scope="session")
def api_base_url():
    """Get API base URL from environment"""
    return os.getenv("API_BASE_URL", "https://jsonplaceholder.typicode.com")


@pytest.fixture(scope="session")
def api_headers():
    """Common API headers"""
    return {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }


@pytest.fixture(scope="function")
def api_client(api_base_url, api_headers):
    """Create API client instance"""
    return APIClient(base_url=api_base_url, headers=api_headers)


@pytest.fixture(scope="session")
def test_data():
    """Sample test data"""
    return {
        "user": {
            "name": "Test User",
            "email": "test@example.com",
            "username": "testuser"
        },
        "post": {
            "title": "Test Post",
            "body": "This is a test post body",
            "userId": 1
        }
    }
