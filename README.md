# Automation Testing Framework

A comprehensive test automation framework combining UI testing with Playwright and API testing with Pytest, featuring Allure reporting.

## Project Structure

```
automation-training/
├── tests/
│   ├── ui/                      # UI Tests (Playwright + TypeScript)
│   │   ├── specs/               # Test specifications
│   │   ├── pages/               # Page Object Models
│   │   ├── fixtures/            # Custom fixtures
│   │   ├── helpers/             # Helper utilities
│   │   └── data/                # Test data
│   │
│   └── api/                     # API Tests (Pytest + Python)
│       ├── specs/               # Test specifications
│       ├── fixtures/            # Pytest fixtures
│       ├── helpers/             # Helper utilities
│       └── data/                # Test data
│
├── reports/                     # Test reports
│   ├── allure-results/          # Allure raw results
│   ├── playwright-report/       # Playwright HTML report
│   ├── screenshots/             # Test screenshots
│   └── videos/                  # Test recordings
│
├── config/                      # Configuration files
├── .github/workflows/           # CI/CD pipelines
├── playwright.config.ts         # Playwright configuration
├── pytest.ini                   # Pytest configuration
└── requirements.txt             # Python dependencies
```

## Prerequisites

- **Node.js** (v18 or higher)
- **Python** (v3.9 or higher)
- **npm** or **yarn**
- **pip**

## Installation

### 1. Install Node.js Dependencies

```bash
npm install
```

### 2. Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 3. Install Playwright Browsers

```bash
npx playwright install --with-deps
```

### 4. Install Allure Command Line (Optional)

**macOS:**
```bash
brew install allure
```

**Windows:**
```bash
scoop install allure
```

**Linux:**
```bash
# Download and extract from https://github.com/allure-framework/allure2/releases
```

## Configuration

### Environment Variables

Copy `.env.example` to `.env` and configure:

```bash
cp .env.example .env
```

Edit `.env` with your configuration:
```env
BASE_URL=https://your-app.com
API_BASE_URL=https://api.your-app.com
TEST_USER_EMAIL=test@example.com
TEST_USER_PASSWORD=yourpassword
```

## Running Tests

### UI Tests (Playwright)

```bash
# Run all UI tests
npx playwright test

# Run in headed mode
npx playwright test --headed

# Run specific test file
npx playwright test tests/ui/specs/example.spec.ts

# Run with specific browser
npx playwright test --project=chromium

# Run in UI mode (interactive)
npx playwright test --ui

# Run in debug mode
npx playwright test --debug
```

### API Tests (Pytest)

```bash
# Run all API tests
pytest

# Run with markers
pytest -m smoke
pytest -m regression
pytest -m api

# Run specific test file
pytest tests/api/specs/test_example_api.py

# Run in parallel
pytest -n auto

# Run with verbose output
pytest -v
```

## Reports

### Generate Allure Report

```bash
# Generate and open Allure report
allure serve reports/allure-results

# Generate Allure report to specific folder
allure generate reports/allure-results -o reports/allure-report --clean
```

### Playwright HTML Report

```bash
# Open Playwright report
npx playwright show-report reports/playwright-report
```

### Pytest HTML Report

After running pytest, open:
```
reports/pytest-report.html
```

## Writing Tests

### UI Test Example (Page Object Model)

**1. Create Page Object** (`tests/ui/pages/LoginPage.ts`):
```typescript
import { Page, Locator } from '@playwright/test';
import { BasePage } from './BasePage';

export class LoginPage extends BasePage {
  private readonly emailInput: Locator;
  private readonly passwordInput: Locator;
  private readonly loginButton: Locator;

  constructor(page: Page) {
    super(page);
    this.emailInput = page.locator('#email');
    this.passwordInput = page.locator('#password');
    this.loginButton = page.locator('button[type="submit"]');
  }

  async login(email: string, password: string) {
    await this.fillInput(this.emailInput, email);
    await this.fillInput(this.passwordInput, password);
    await this.clickElement(this.loginButton);
  }
}
```

**2. Create Test** (`tests/ui/specs/login.spec.ts`):
```typescript
import { test, expect } from '../fixtures/base.fixture';
import { Logger } from '../helpers/Logger';

test('user can login successfully', async ({ page }) => {
  const loginPage = new LoginPage(page);

  Logger.step('Navigate to login page');
  await loginPage.goto('/login');

  Logger.step('Login with valid credentials');
  await loginPage.login('user@example.com', 'password123');

  Logger.step('Verify successful login');
  expect(page.url()).toContain('/dashboard');
});
```

### API Test Example

**Create Test** (`tests/api/specs/test_users.py`):
```python
import pytest
import allure
from tests.api.helpers.assertions import APIAssertions

@allure.feature('User Management')
class TestUsers:

    @pytest.mark.smoke
    @allure.title("Create new user")
    def test_create_user(self, api_client):
        user_data = {
            "name": "John Doe",
            "email": "john@example.com"
        }

        with allure.step("Send POST request"):
            response = api_client.post("/users", json=user_data)

        with allure.step("Verify user created"):
            APIAssertions.assert_status_code(response, 201)
            created_user = response.json()
            assert created_user["name"] == user_data["name"]
```

## Best Practices

### UI Testing
- ✅ Use Page Object Model pattern
- ✅ Keep locators in page objects
- ✅ Use meaningful test names
- ✅ Add proper waits and assertions
- ✅ Use custom fixtures for common setups
- ✅ Log important test steps

### API Testing
- ✅ Separate concerns (client, assertions, data)
- ✅ Use fixtures for common setup
- ✅ Validate response schemas
- ✅ Check response times
- ✅ Use markers to categorize tests
- ✅ Add allure steps for better reporting

### General
- ✅ Keep tests independent
- ✅ Use descriptive naming
- ✅ Don't hardcode test data
- ✅ Clean up test data after tests
- ✅ Use environment variables for configuration

## CI/CD Integration

GitHub Actions workflow is configured in `.github/workflows/playwright.yml`. It will:
- Run on push to main/master
- Run on pull requests
- Execute all Playwright tests
- Upload test reports as artifacts

## Troubleshooting

### Playwright Issues

```bash
# Clear Playwright cache
npx playwright cache clear

# Reinstall browsers
npx playwright install --force
```

### Python Issues

```bash
# Recreate virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

## Additional Resources

- [Playwright Documentation](https://playwright.dev)
- [Pytest Documentation](https://docs.pytest.org)
- [Allure Documentation](https://docs.qameta.io/allure/)
- [Page Object Model Pattern](https://playwright.dev/docs/pom)

## License

MIT
