from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)

    #button = browser.find_element_by_css_selector("button.btn")
    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)

    answer = browser.find_element_by_id("answer")
    answer.send_keys(y)

    checkbox_element = browser.find_element_by_id("robotCheckbox")
    checkbox_element.click()
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    radiobutton_element = browser.find_element_by_id("robotsRule")
    radiobutton_element.click()

    button.click()

finally:
    # успеваем скопировать код за 10 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
