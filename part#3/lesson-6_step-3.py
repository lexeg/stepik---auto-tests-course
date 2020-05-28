import time
import math
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pytest

def calc():
  return str(math.log(int(time.time())))

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('link', ["https://stepik.org/lesson/236895/step/1","https://stepik.org/lesson/236896/step/1",
"https://stepik.org/lesson/236897/step/1",
"https://stepik.org/lesson/236898/step/1",
"https://stepik.org/lesson/236899/step/1",
"https://stepik.org/lesson/236903/step/1",
"https://stepik.org/lesson/236904/step/1",
"https://stepik.org/lesson/236905/step/1"])
def test_guest_should_see_login_link(browser, link):
    browser.get(link)
    area = WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.TAG_NAME, "textarea")))
    answer = calc()
    area.send_keys(answer)
    button = browser.find_element_by_css_selector("button.submit-submission")
    button.click()
    #hint = browser.find_element_by_css_selector("pre.smart-hints__hint")
    hint = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "pre.smart-hints__hint")))
    hintMessage = hint.text
    assert hintMessage == "Correct!", f"Should be Correct, but was {hintMessage}"
