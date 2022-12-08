import os
from time import sleep
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def send_letter_test():
    driver = webdriver.Chrome()
    driver.get("https://temp-mail.org/")
    driver.set_page_load_timeout(30)
    driver.find_element(By.XPATH, '(//button[@type="button"])[3]').click()

    driver.execute_script('window.open("https://dedmorozmos.ru/pismo/","santa-letter-service");')
    driver.set_page_load_timeout(30)
    driver.switch_to.window('santa-letter-service')

    driver.execute_script("window.scrollTo(0, 1300)")
    WebDriverWait(driver, 20) \
        .until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#email'))).send_keys(Keys.COMMAND + 'v')
    sleep(2)

    driver.find_element(By.XPATH, "//input[@name='p_file']").send_keys(os.getcwd() + "/image.jpeg")
    driver.find_element(By.CSS_SELECTOR, '#message').send_keys('Happy New Year!')

    driver.execute_script("window.scrollTo(0, 1328)")
    element = driver.find_element(By.XPATH, '(//button[text()="Отправить"])[1]')
    sleep(5)
    driver.execute_script("arguments[0].click();", element)

    driver.switch_to.window(driver.window_handles[0])
    driver.find_element(By.CSS_SELECTOR, '#click-to-refresh')
    driver.execute_script("window.scrollTo(0, 500)")
    WebDriverWait(driver, 20) \
        .until(EC.element_to_be_clickable((By.XPATH, '//a[text()="Письмо от Московского Дедушки Мороза"]')))
    sleep(2)


def order_christmas_tree():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://ananas.rs/")
    WebDriverWait(driver, 20) \
        .until(EC.element_to_be_clickable((By.XPATH, '//*[text()="Slažem se"]'))).click()
    driver.find_element(By.XPATH, "(//input)[1]").click()
    driver.find_element(By.XPATH, "(//input)[1]").send_keys('jelka')
    driver.find_element(By.XPATH, "(//input)[1]").send_keys(Keys.ENTER)
    sleep(8)
    el = driver.find_elements(By.XPATH, "//*[text()='Spark']")[0]
    el.click()
    WebDriverWait(driver, 20) \
        .until(EC.element_to_be_clickable((By.XPATH, '//*[text()="Dodaj u korpu"]'))).click()
    WebDriverWait(driver, 20) \
        .until(EC.element_to_be_clickable((By.XPATH, '//*[text()="Pregledaj korpu"]'))).click()
    sleep(3)


if __name__ == '__main__':
    send_letter_test()
    order_christmas_tree()