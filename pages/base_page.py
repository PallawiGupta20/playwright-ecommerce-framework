class BasePage:
    """Shared functionality for all page objects."""

    def __init__(self, page):
        self.page = page

    def click(self, locator):
        locator.click()

    def fill(self, locator, text):
        locator.fill(text)

    def is_visible(self, locator):
        return locator.is_visible()
