from pages.homepage import HomePage
from pages.plp_page import PLPPage
from pages.pdp_page import PDPPage
from pages.cart_page import CartPage
from playwright.sync_api import Page
import pytest

@pytest.mark.exploratory
# Parametrize the test to try multiple quantities
@pytest.mark.parametrize("quantity", [1, 2, 3, 5])
def test_add_multi_quantity_to_cart(page: Page, quantity: int) -> None:
    """
    Exploratory test: Add product to cart with multiple quantities
    and verify that the cart displays the correct quantity.
    """

    # Initialize page objects
    home = HomePage(page)
    plp = PLPPage(page)
    pdp = PDPPage(page)
    cart = CartPage(page)

    # Step 1: Go to the homepage
    home.go_to_home()  

    # Step 2: Click "Men's Outerwear Shop Now" to navigate to PLP
    home.shop_now_mens_outerwear()  

    # Step 3: On the Product Listing Page, click the first product
    plp.click_first_product()  

    # Step 4: On the Product Detail Page, set the desired quantity
    pdp.set_quantity(quantity)  

    # Step 5: Click "Add to Cart" button
    pdp.add_to_cart()  

    # Step 6: Wait for the banner and click "View Cart" to navigate to cart page
    pdp.click_view_cart_from_banner()  

    # Step 7: Verify the user is on the cart page
    cart.verify_cart_page()  

    # Step 8: Verify that the correct quantity is displayed in the cart
    cart.verify_cart_quantity(quantity) 
    pass 

