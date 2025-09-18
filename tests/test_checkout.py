from pages.homepage import HomePage
from pages.plp_page import PLPPage
from pages.pdp_page import PDPPage
from pages.cart_page import CartPage
from playwright.sync_api import Page
import pytest

@pytest.mark.smoke
def test_checkout(page: Page) -> None:
    home = HomePage(page)
    plp = PLPPage(page)
    pdp = PDPPage(page)
    cart = CartPage(page)

    home.go_to_home()
    home.shop_now_mens_outerwear()

    plp.click_first_product()
    pdp.add_to_cart()
    pdp.click_view_cart_from_banner()

    cart.verify_cart_page()
    cart.proceed_to_checkout()
    pass
    

