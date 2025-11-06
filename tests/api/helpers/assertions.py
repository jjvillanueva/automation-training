"""
API Test Assertions
Common assertion helpers for API testing
"""
from typing import Dict, Any, List
import jsonschema
from jsonschema import validate


class APIAssertions:
    """Helper class for API response assertions"""

    @staticmethod
    def assert_status_code(response, expected_status: int):
        """Assert response status code"""
        assert response.status_code == expected_status, \
            f"Expected status {expected_status}, got {response.status_code}"

    @staticmethod
    def assert_response_time(response, max_time_ms: int):
        """Assert response time is within limit"""
        response_time_ms = response.elapsed.total_seconds() * 1000
        assert response_time_ms < max_time_ms, \
            f"Response time {response_time_ms}ms exceeded {max_time_ms}ms"

    @staticmethod
    def assert_json_schema(response_json: Dict, schema: Dict):
        """Validate response against JSON schema"""
        try:
            validate(instance=response_json, schema=schema)
        except jsonschema.exceptions.ValidationError as e:
            raise AssertionError(f"JSON schema validation failed: {e.message}")

    @staticmethod
    def assert_contains_keys(response_json: Dict, keys: List[str]):
        """Assert response contains specific keys"""
        for key in keys:
            assert key in response_json, f"Key '{key}' not found in response"

    @staticmethod
    def assert_not_empty(response_json: Any):
        """Assert response is not empty"""
        assert response_json, "Response is empty"

    @staticmethod
    def assert_header_present(response, header_name: str):
        """Assert header is present in response"""
        assert header_name in response.headers, \
            f"Header '{header_name}' not found in response"

    @staticmethod
    def assert_header_value(response, header_name: str, expected_value: str):
        """Assert header has expected value"""
        actual_value = response.headers.get(header_name)
        assert actual_value == expected_value, \
            f"Header '{header_name}' expected '{expected_value}', got '{actual_value}'"
