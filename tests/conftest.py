import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

@pytest.fixture
def login_page(page):
    lp = LoginPage(page)
    lp.goto()
    return lp

@pytest.fixture
def logged_in_page(login_page):
    login_page.login("standard_user", "secret_sauce")
    return login_page.page

@pytest.fixture
def inventory_page(logged_in_page):
    return InventoryPage(logged_in_page)

# FIX: Force cart_page to use the exact same logged_in_page context
@pytest.fixture
def cart_page(logged_in_page):
    return CartPage(logged_in_page)

# FIX: Force checkout_page to use the exact same logged_in_page context
@pytest.fixture
def checkout_page(logged_in_page):
    return CheckoutPage(logged_in_page)
