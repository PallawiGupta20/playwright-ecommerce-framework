from pages.base_page import BasePage


class InventoryPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.cart_badge = page.locator(".shopping_cart_badge")
        self.cart_icon = page.locator(".shopping_cart_link")
        self.inventory_items = page.locator(".inventory_item")

    def add_product_to_cart(self, product_slug):
        """product_slug example: 'sauce-labs-backpack'"""
        self.page.locator(f"#add-to-cart-{product_slug}").click()

    def get_cart_count(self):
        if self.cart_badge.is_visible():
            return self.cart_badge.text_content()
        return "0"

    def go_to_cart(self):
        self.cart_icon.click()

    def get_product_names(self):
        return self.page.locator(".inventory_item_name").all_text_contents()
