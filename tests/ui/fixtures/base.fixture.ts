import { test as base } from '@playwright/test';
import { ExamplePage } from '../pages/ExamplePage';

/**
 * Custom fixtures for Playwright tests
 * Extends base test with page objects and custom utilities
 */
type CustomFixtures = {
  examplePage: ExamplePage;
};

export const test = base.extend<CustomFixtures>({
  examplePage: async ({ page }, use) => {
    const examplePage = new ExamplePage(page);
    await use(examplePage);
  },
});

export { expect } from '@playwright/test';
