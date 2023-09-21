# test_stellar_burgers.py
import unittest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options  # Импорт настроек для Firefox
from locators import LoginPageLocators, RegistrationPageLocators, PersonalCabinetLocators

class StellarBurgersTests(unittest.TestCase):

    def setUp(self):
        # Инициализация браузера
        self.driver = webdriver.Chrome()
        self.driver.get("https://stellarburgers.nomoreparties.site/")

        # Используем Firefox вместо Chrome
        options = Options()
        options.headless = True  # Запуск в "headless" режиме (без графического интерфейса)
        self.driver = webdriver.Firefox(options=options)
        self.driver = webdriver.Firefox(options=options)
        self.driver.get("https://stellarburgers.nomoreparties.site/")

    def test_successful_registration(self):
        # Тест успешной регистрации
        driver = self.driver
        driver.find_element_by_id(RegistrationPageLocators.NAME_INPUT).send_keys("Имя")
        driver.find_element_by_id(RegistrationPageLocators.EMAIL_INPUT).send_keys("example@example.com")
        driver.find_element_by_id(RegistrationPageLocators.PASSWORD_INPUT).send_keys("password123")
        driver.find_element_by_id(RegistrationPageLocators.REGISTER_BUTTON).click()
        # Добавьте проверки на успешную регистрацию

    def test_invalid_password_error(self):
        # Тест ошибки для некорректного пароля
        driver = self.driver
        driver.find_element_by_id(RegistrationPageLocators.NAME_INPUT).send_keys("Имя")
        driver.find_element_by_id(RegistrationPageLocators.EMAIL_INPUT).send_keys("example@example.com")
        driver.find_element_by_id(RegistrationPageLocators.PASSWORD_INPUT).send_keys("short")
        driver.find_element_by_id(RegistrationPageLocators.REGISTER_BUTTON).click()
        # Добавьте проверку на появление ошибки

    def tearDown(self):
        # Завершение работы браузера после каждого теста
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()