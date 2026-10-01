from pages.base_page import BasePage


class CheckoutPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.first_name_input = page.locator("#first-name")
        self.last_name_input = page.locator("#last-name")
        self.postal_code_input = page.locator("#postal-code")
        self.continue_button = page.locator("#continue")
        self.finish_button = page.locator("#finish")
        self.complete_header = page.locator(".complete-header")

    def fill_checkout_info(self, first_name, last_name, postal_code):
        self.fill(self.first_name_input, first_name)
        self.fill(self.last_name_input, last_name)
        self.fill(self.postal_code_input, postal_code)
        self.continue_button.click()

    def finish_order(self):
        self.finish_button.click()

    def get_confirmation_text(self):
        return self.complete_header.text_content()
