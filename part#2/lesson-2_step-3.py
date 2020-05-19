from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math

def calc(a,b):
  c = int(a)+int(b)
  return str(c)

try: 
    #http://suninjuly.github.io/selects1.html
    #http://suninjuly.github.io/selects2.html
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    a_element = browser.find_element_by_id("num1")
    a = a_element.text
    b_element = browser.find_element_by_id("num2")
    b = b_element.text
    c = calc(a,b)

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(c)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 10 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
