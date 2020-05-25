from selenium import webdriver
import unittest
import time

class TestAbsUI(unittest.TestCase):
	def test_registration1(self):
	    result = self.check_registration("http://suninjuly.github.io/registration1.html")
	    self.assertEqual(result, "Congratulations! You have successfully registered!", "Should be successfully registered!")

	def test_registration2(self):
	    resutl = self.check_registration("http://suninjuly.github.io/registration2.html")
	    self.assertEqual(result, "Congratulations! You have successfully registered!", "Should be successfully registered!")

	def check_registration(self, link):
		try: 
		    # link = "http://suninjuly.github.io/registration1.html"
		    browser = webdriver.Chrome()
		    browser.get(link)

		    # Ваш код, который заполняет обязательные поля
		    firstName = browser.find_element_by_xpath("//div[@class=\"first_block\"]//input[contains(@class, \"first\")]")
		    lastName = browser.find_element_by_xpath("//div[@class=\"first_block\"]//input[contains(@class, \"second\")]")
		    email = browser.find_element_by_xpath("//div[@class=\"first_block\"]//input[contains(@class, \"third\")]")
		    firstName.send_keys("Мой ответ")
		    lastName.send_keys("Мой ответ")
		    email.send_keys("Мой ответ")

		    # Отправляем заполненную форму
		    button = browser.find_element_by_css_selector("button.btn")
		    button.click()

		    # Проверяем, что смогли зарегистрироваться
		    # ждем загрузки страницы
		    time.sleep(1)

		    # находим элемент, содержащий текст
		    welcome_text_elt = browser.find_element_by_tag_name("h1")
		    # записываем в переменную welcome_text текст из элемента welcome_text_elt
		    welcome_text = welcome_text_elt.text

		    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
		    # assert "Congratulations! You have successfully registered!" == welcome_text
		    return welcome_text

		finally:
		    # ожидание чтобы визуально оценить результаты прохождения скрипта
		    time.sleep(10)
		    # закрываем браузер после всех манипуляций
		    browser.quit()
