import pytest
from selenium.webdriver.common.by import By
import time


@pytest.mark.run(order=1)
def test_add_to_cart_button_exists(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(30)  # Для визуальной проверки языка
    button = browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")
    assert button.is_displayed(), "Кнопка добавления в корзину не отображается"
