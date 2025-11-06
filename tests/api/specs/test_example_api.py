"""
Example API Tests
Demonstrates API testing patterns using JSONPlaceholder API
"""
import pytest
import allure
from tests.api.helpers.assertions import APIAssertions


@allure.feature('Posts API')
@allure.story('Get Posts')
class TestPostsAPI:
    """Test cases for Posts API endpoints"""

    @pytest.mark.smoke
    @allure.title("Get all posts")
    @allure.description("Verify GET /posts returns list of posts")
    def test_get_all_posts(self, api_client):
        with allure.step("Send GET request to /posts"):
            response = api_client.get("/posts")

        with allure.step("Verify response status is 200"):
            APIAssertions.assert_status_code(response, 200)

        with allure.step("Verify response is not empty"):
            posts = response.json()
            APIAssertions.assert_not_empty(posts)

        with allure.step("Verify response time is acceptable"):
            APIAssertions.assert_response_time(response, 2000)

    @pytest.mark.smoke
    @allure.title("Get single post by ID")
    @allure.description("Verify GET /posts/{id} returns specific post")
    def test_get_post_by_id(self, api_client):
        post_id = 1

        with allure.step(f"Send GET request to /posts/{post_id}"):
            response = api_client.get(f"/posts/{post_id}")

        with allure.step("Verify response status is 200"):
            APIAssertions.assert_status_code(response, 200)

        with allure.step("Verify response contains required keys"):
            post = response.json()
            APIAssertions.assert_contains_keys(post, ["id", "title", "body", "userId"])

        with allure.step("Verify post ID matches requested ID"):
            assert post["id"] == post_id

    @pytest.mark.regression
    @allure.title("Create new post")
    @allure.description("Verify POST /posts creates a new post")
    def test_create_post(self, api_client, test_data):
        with allure.step("Prepare post data"):
            post_data = test_data["post"]

        with allure.step("Send POST request to /posts"):
            response = api_client.post("/posts", json=post_data)

        with allure.step("Verify response status is 201"):
            APIAssertions.assert_status_code(response, 201)

        with allure.step("Verify created post contains submitted data"):
            created_post = response.json()
            assert created_post["title"] == post_data["title"]
            assert created_post["body"] == post_data["body"]

    @pytest.mark.regression
    @allure.title("Update existing post")
    @allure.description("Verify PUT /posts/{id} updates a post")
    def test_update_post(self, api_client):
        post_id = 1
        update_data = {
            "title": "Updated Title",
            "body": "Updated body content",
            "userId": 1
        }

        with allure.step(f"Send PUT request to /posts/{post_id}"):
            response = api_client.put(f"/posts/{post_id}", json=update_data)

        with allure.step("Verify response status is 200"):
            APIAssertions.assert_status_code(response, 200)

        with allure.step("Verify post was updated"):
            updated_post = response.json()
            assert updated_post["title"] == update_data["title"]

    @pytest.mark.regression
    @allure.title("Delete post")
    @allure.description("Verify DELETE /posts/{id} removes a post")
    def test_delete_post(self, api_client):
        post_id = 1

        with allure.step(f"Send DELETE request to /posts/{post_id}"):
            response = api_client.delete(f"/posts/{post_id}")

        with allure.step("Verify response status is 200"):
            APIAssertions.assert_status_code(response, 200)


@allure.feature('Users API')
@allure.story('Get Users')
class TestUsersAPI:
    """Test cases for Users API endpoints"""

    @pytest.mark.smoke
    @allure.title("Get all users")
    @allure.description("Verify GET /users returns list of users")
    def test_get_all_users(self, api_client):
        with allure.step("Send GET request to /users"):
            response = api_client.get("/users")

        with allure.step("Verify response status is 200"):
            APIAssertions.assert_status_code(response, 200)

        with allure.step("Verify response contains users"):
            users = response.json()
            APIAssertions.assert_not_empty(users)
            assert len(users) > 0

    @pytest.mark.critical
    @allure.title("Verify user data structure")
    @allure.description("Verify user object contains all required fields")
    def test_user_data_structure(self, api_client):
        with allure.step("Get first user"):
            response = api_client.get("/users/1")
            user = response.json()

        with allure.step("Verify user contains required fields"):
            required_fields = ["id", "name", "username", "email", "address", "phone", "website", "company"]
            APIAssertions.assert_contains_keys(user, required_fields)
