from playwright.sync_api import Page

class PLPPage:
    def __init__(self, page: Page) -> None:
        self.page = page

    # Method to click on the first product in the product listing
    def click_first_product(self) -> None:
        # Locate the first product inside the list (ul.grid > li) on the page
        first_product = self.page.locator("ul.grid li").first
        
        # Wait for the Web Component <shop-list-item> to be visible (max 10 seconds)
        first_product.locator("shop-list-item").wait_for(state="visible", timeout=10000)
        
        # Scroll the first product into view if it's not visible on the screen
        first_product.scroll_into_view_if_needed()
        
        # Click the anchor (<a>) inside the first product to navigate to the PDP
        first_product.locator("a").click()
