from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get('http://videojs.com')

video = driver.find_element_by_xpath('//*[@id="preview-player_html5_api"]')

url = driver.execute_script('return arguments[0].currentSrc;', video)
print(url)

print('start')
driver.execute_script("return arguments[0].play()", video)
