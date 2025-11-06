import { test, expect } from '../fixtures/base.fixture';
import { Logger } from '../helpers/Logger';

test.describe('Example Test Suite', () => {
  test.beforeEach(async ({ examplePage }) => {
    Logger.step('Navigate to example.com');
    await examplePage.goto();
  });

  test('should display correct heading', async ({ examplePage }) => {
    Logger.step('Verify page is loaded');
    const isLoaded = await examplePage.isPageLoaded();
    expect(isLoaded).toBeTruthy();

    Logger.step('Get heading text');
    const headingText = await examplePage.getHeadingText();

    Logger.step('Verify heading contains "Example Domain"');
    expect(headingText).toContain('Example Domain');
  });

  test('should have correct page title', async ({ examplePage }) => {
    Logger.step('Get page title');
    const title = await examplePage.getTitle();

    Logger.step('Verify title is "Example Domain"');
    expect(title).toBe('Example Domain');
  });

  test('should navigate to more info page', async ({ examplePage, page }) => {
    Logger.step('Click on More Information link');
    await examplePage.clickMoreInfo();

    Logger.step('Wait for navigation');
    await page.waitForLoadState('networkidle');

    Logger.step('Verify URL changed');
    expect(page.url()).toContain('iana.org');
  });
});
