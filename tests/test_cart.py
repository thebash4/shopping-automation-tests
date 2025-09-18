import pytest
from pages.homepage import HomePage
from pages.plp_page import PLPPage
from pages.pdp_page import PDPPage
from pages.cart_page import CartPage
from playwright.sync_api import Page

@pytest.mark.smoke
def test_add_to_cart(page: Page) -> None:
    home = HomePage(page)
    plp = PLPPage(page)
    pdp = PDPPage(page)
    cart = CartPage(page)

    # Go to homepage
    home.go_to_home()
    home.shop_now_mens_outerwear()

    # Select first product
    plp.click_first_product()
    pdp.add_to_cart()
    pdp.click_view_cart_from_banner()

    # Verify cart
    cart.verify_cart_page()
    
    pass

