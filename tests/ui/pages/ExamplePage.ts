import { Page, Locator } from '@playwright/test';
import { BasePage } from './BasePage';

/**
 * Example Page Object
 * Demonstrates how to create a page object using the Page Object Model pattern
 */
export class ExamplePage extends BasePage {
  // Locators
  private readonly heading: Locator;
  private readonly moreInfoLink: Locator;

  constructor(page: Page) {
    super(page);
    this.heading = page.locator('h1');
    this.moreInfoLink = page.locator('a[href*="iana"]');
  }

  /**
   * Navigate to example.com
   */
  async goto(): Promise<void> {
    await this.navigate('https://example.com');
  }

  /**
   * Get the main heading text
   */
  async getHeadingText(): Promise<string> {
    return await this.getElementText(this.heading);
  }

  /**
   * Click on More Information link
   */
  async clickMoreInfo(): Promise<void> {
    await this.clickElement(this.moreInfoLink);
  }

  /**
   * Verify page is loaded
   */
  async isPageLoaded(): Promise<boolean> {
    return await this.isElementVisible(this.heading);
  }
}
