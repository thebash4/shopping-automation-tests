from playwright.sync_api import Page

class PDPPage:
    def __init__(self, page: Page) -> None:
        self.page = page  
        # Selectors for elements on the PDP
        self.add_to_cart_button = "shop-button >> text=Add to Cart"
        self.view_cart_anchor = "#viewCartAnchor"  # Using the element's ID for precise targeting
        self.quantity_select = "#quantitySelect"   # Dropdown for quantity

    # Method to click the "Add to Cart" button
    def add_to_cart(self) -> None:
        self.page.locator(self.add_to_cart_button).click()
        
    # Method to click the "View Cart" link from the banner after adding a product
    def click_view_cart_from_banner(self) -> None:
        # Wait until the "View Cart" link is visible (max 10 seconds)
        self.page.locator(self.view_cart_anchor).wait_for(state="visible", timeout=10000)
        self.page.locator(self.view_cart_anchor).click()
        
    # Method to set the quantity of the product before adding to cart
    def set_quantity(self, quantity: int) -> None:
        """
        Select the product quantity from the dropdown.
        """
        # Wait for the dropdown to be visible
        self.page.locator(self.quantity_select).wait_for(state="visible", timeout=5000)
        # Select the quantity
        self.page.locator(self.quantity_select).select_option(str(quantity))