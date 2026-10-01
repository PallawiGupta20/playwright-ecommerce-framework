import pytest


@pytest.mark.parametrize("username,password,should_succeed", [
    ("standard_user", "secret_sauce", True),
    ("locked_out_user", "secret_sauce", False),
    ("standard_user", "wrong_password", False),
    ("", "secret_sauce", False),
])
def test_login_variants(login_page, username, password, should_succeed):
    login_page.login(username, password)

    if should_succeed:
        assert "inventory.html" in login_page.page.url
    else:
        assert login_page.error_message.is_visible()
