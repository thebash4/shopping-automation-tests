from playwright.sync_api import Page

# Define a class representing the homepage of the website
class HomePage:
    # Constructor: runs when a HomePage object is created
    def __init__(self, page: Page) -> None:
        self.page: Page = page # Store the Playwright Page object for use in other methods

    # Method to navigate to the homepage
    def go_to_home(self, url: str = "https://shop.polymer-project.org/") -> None:
        self.page.goto(url)

    # Method to click on the "Men's Outerwear Shop Now" link
    def shop_now_mens_outerwear(self) -> None:
        # Find a link by its accessible role and name, then click it
        self.page.get_by_role("link", name="Men's Outerwear Shop Now").click()

