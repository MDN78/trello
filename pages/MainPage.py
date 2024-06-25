import allure
from selenium.webdriver.common.by import By
from testdata.DataProvider import DataProvider
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC


class MainPage:

    def __init__(self, driver: WebDriver) -> None:
        self.__driver = driver
        self.data = DataProvider()

    @allure.step("Get current url")
    def get_current_url(self) -> str:
        return self.__driver.current_url

    @allure.step("UI. Open right side menu")
    def open_menu(self):
        self.__driver.find_element(By.CSS_SELECTOR, "button[data-testid='header-member-menu-button']").click()

    @allure.step("UI. Get information about user")
    def get_account_info(self) -> list[str]:
        container = self.__driver.find_element(By.CSS_SELECTOR, "div[class=mJBO4dHZbrIG_0]")
        fields = container.find_elements(By.CSS_SELECTOR, "div")
        name = fields[0].text
        email = fields[1].text
        return [name, email]

    @allure.step("UI. Open create form")
    def open_create_form(self):
        self.__driver.find_element(By.CSS_SELECTOR, "button[data-testid=header-create-menu-button]").click()

    @allure.step("UI. Choose {number} element in list")
    def press_button_create_board(self, number=1):
        pop = self.__driver.find_element(By.CSS_SELECTOR, "section[data-testid=header-create-menu-popover]")
        menu_list = pop.find_elements(By.CSS_SELECTOR, "li")
        menu_list[number-1].click()

    @allure.step("UI. Set board name {board_name}")
    def fill_board_name(self, board_name: str):
        self.__driver.find_element(By.CSS_SELECTOR, "input[data-testid=create-board-title-input]").send_keys(board_name)

    @allure.step("UI. Press button 'Create' via")
    def click_create_button(self):
        button = WebDriverWait(self.__driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid=create-board-submit-button]")))
        button.click()
        WebDriverWait(self.__driver, 20).until(EC.url_contains("https://trello.com/b/"))

