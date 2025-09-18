from playwright.sync_api import Page

class CartPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.quantity_selector = "shop-cart-item select"  # Selector for quantity dropdown in cart
        self.cart_items_locator = "shop-cart-item"  # Locator for cart items

    def proceed_to_checkout(self) -> None:
        # Click Checkout button
        self.page.locator("div.checkout-box a[href='/checkout']").click()

    def verify_cart_page(self) -> None:
        # Verify that we are on the cart page by checking the URL
        assert "/cart" in self.page.url, f"Expected '/cart' in URL, but got {self.page.url}"
        
    def verify_cart_quantity(self, expected_quantity: int) -> None:
        """
        Verify that the quantity of the product in the cart matches expected_quantity.
        """
        # Wait until the quantity select element is visible
        self.page.locator(self.quantity_selector).wait_for(state="visible", timeout=5000)
        # Get the value of the select element
        actual_quantity = int(self.page.locator(self.quantity_selector).input_value())
        # Assert it matches expected
        assert actual_quantity == expected_quantity, f"Expected quantity {expected_quantity}, but got {actual_quantity}"

        
    def get_cart_items_count(self) -> int:
        return self.page.locator(self.cart_items_locator).count()