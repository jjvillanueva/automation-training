"""
API Client Helper
Provides reusable methods for making API requests
"""
import requests
from typing import Dict, Any, Optional
import logging

logger = logging.getLogger(__name__)


class APIClient:
    """Base API Client for making HTTP requests"""

    def __init__(self, base_url: str, headers: Optional[Dict[str, str]] = None):
        self.base_url = base_url
        self.headers = headers or {}
        self.session = requests.Session()
        self.session.headers.update(self.headers)

    def get(self, endpoint: str, params: Optional[Dict] = None, **kwargs) -> requests.Response:
        """Make GET request"""
        url = f"{self.base_url}{endpoint}"
        logger.info(f"GET {url}")
        response = self.session.get(url, params=params, **kwargs)
        logger.info(f"Response Status: {response.status_code}")
        return response

    def post(self, endpoint: str, data: Optional[Dict] = None, json: Optional[Dict] = None, **kwargs) -> requests.Response:
        """Make POST request"""
        url = f"{self.base_url}{endpoint}"
        logger.info(f"POST {url}")
        response = self.session.post(url, data=data, json=json, **kwargs)
        logger.info(f"Response Status: {response.status_code}")
        return response

    def put(self, endpoint: str, data: Optional[Dict] = None, json: Optional[Dict] = None, **kwargs) -> requests.Response:
        """Make PUT request"""
        url = f"{self.base_url}{endpoint}"
        logger.info(f"PUT {url}")
        response = self.session.put(url, data=data, json=json, **kwargs)
        logger.info(f"Response Status: {response.status_code}")
        return response

    def delete(self, endpoint: str, **kwargs) -> requests.Response:
        """Make DELETE request"""
        url = f"{self.base_url}{endpoint}"
        logger.info(f"DELETE {url}")
        response = self.session.delete(url, **kwargs)
        logger.info(f"Response Status: {response.status_code}")
        return response

    def patch(self, endpoint: str, data: Optional[Dict] = None, json: Optional[Dict] = None, **kwargs) -> requests.Response:
        """Make PATCH request"""
        url = f"{self.base_url}{endpoint}"
        logger.info(f"PATCH {url}")
        response = self.session.patch(url, data=data, json=json, **kwargs)
        logger.info(f"Response Status: {response.status_code}")
        return response

    def set_header(self, key: str, value: str):
        """Add or update a header"""
        self.session.headers[key] = value

    def remove_header(self, key: str):
        """Remove a header"""
        if key in self.session.headers:
            del self.session.headers[key]
