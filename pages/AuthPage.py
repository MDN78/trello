import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from configuration.ConfigProvider import ConfigProvider
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC


class AuthPage:

    def __init__(self, driver: WebDriver) -> None:
        url = ConfigProvider().get("ui", "base_url")
        self.__url = f"{url}/login"
        self.__driver = driver

    @allure.step("UI. Go to authorization page")
    def go(self) -> None:
        self.__driver.get(self.__url)

    @allure.step("UI. Authorization with login {email}")
    def login_as(self, email: str, password: str):
        self.__driver.find_element(By.CSS_SELECTOR, "#username").send_keys(email)
        self.__driver.find_element(By.CSS_SELECTOR, "#login-submit").click()
        # waiting downloading field "password"
        WebDriverWait(self.__driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "svg[role='presentation']")))
        self.__driver.find_element(By.CSS_SELECTOR, "#password").send_keys(password)
        self.__driver.find_element(By.CSS_SELECTOR, "#login-submit").click()

    @allure.step("UI. Get current url")
    def get_current_url(self):
        WebDriverWait(self.__driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '.boards-page-section-header-name')))
        return self.__driver.current_url
