from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pandas as pd
import time
driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')


driver.get('https://www.coronatracker.com/')
time.sleep(3)

brazil = driver.find_element_by_xpath('//*[@id="__layout"]/div/main/div/div[2]/div[1]/div[1]/table/tbody/tr[3]/td[1]/a').click()
time.sleep(4)

sobre = driver.find_element_by_xpath('//*[@id="__layout"]/div/nav/div/div/div[2]/a[7]').click()
time.sleep(5)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(3)
covid_video = driver.find_element_by_xpath('//*[@id="__layout"]/div/nav/div/div/div[2]/a[3]').click()
time.sleep(3)
play = driver.find_element_by_xpath('//*[@id="movie_player"]/div[4]/div').click()


driver.exit()



recovered = driver.find_element_by_xpath('//*[@id="__layout"]/div/main/div/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/span')
death = driver.find_element_by_xpath('//*[@id="__layout"]/div/main/div/div[1]/div[1]/div[1]/div[2]/div[3]/div[1]/span')
confirmed = driver.find_element_by_xpath('//*[@id="__layout"]/div/main/div/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]')

confirmedtext = confirmed.text
deathttext = death.text
recoveredtext = recovered.text
print(f'Casos confirmados: {confirmedtext}')
print(f'Recuperados: {recoveredtext}')
print(f'Mortes: {deathttext}')


confirmedbrazil = driver.find_element_by_xpath('//*[@id="__layout"]/div/main/div/div/div[1]/div[2]/div/div[2]/div[1]/p[1]')
confirmedbr_text = confirmedbrazil.text
print(f'Casos confirmados no Brasil hoje: {confirmedbr_text}')

