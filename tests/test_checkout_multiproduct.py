from pages.homepage import HomePage
from pages.plp_page import PLPPage
from pages.pdp_page import PDPPage
from pages.cart_page import CartPage
from playwright.sync_api import Page
import pytest


def test_add_two_different_products_to_cart(page: Page) -> None:
    """
    Test adding two different products to the cart and verifying the cart displays both.
    """
    # Initialize page objects
    home = HomePage(page)
    plp = PLPPage(page)
    pdp = PDPPage(page)
    cart = CartPage(page)

    # Step 1: Go to homepage
    home.go_to_home()

    # Step 2: Navigate to Men's Outerwear PLP
    home.shop_now_mens_outerwear()

    # Step 3: Click on the first product and add to cart
    plp.click_first_product()
    pdp.add_to_cart()
    pdp.click_view_cart_from_banner()

    # Step 4: Go back to PLP to select second product
    home.go_to_home()
    home.shop_now_mens_outerwear()
    
    # Step 5: Click on the second product in the PLP
    second_product = plp.page.locator("ul.grid li").nth(1)  # 0-indexed: nth(1) = second product
    second_product.locator("shop-list-item").wait_for(state="visible", timeout=10000)
    second_product.scroll_into_view_if_needed()
    second_product.locator("a").click()

    # Step 6: Add the second product to the cart
    pdp.add_to_cart()
    pdp.click_view_cart_from_banner()

    # Step 7: Verify cart page shows 2 items
    cart.verify_cart_page()
    
    # Verify total number of items in the cart
    cart_items_count = cart.get_cart_items_count()
    assert cart_items_count == 2, f"Expected 2 products in cart, but found {cart_items_count}"
    
  
