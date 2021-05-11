from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pandas as pd
import time
driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')

driver.get('https://www.cec.com.br/')
time.sleep(3)

elem = driver.find_element_by_id("txtSearch")
time.sleep(2)
elem.send_keys("piso")
elem = driver.find_element_by_class_name("bt_pag")
print(elem.get_attribute("href"))
elem.click()

with open("pagina_piso.html", "w") as file:
    file.write(driver.page_source)