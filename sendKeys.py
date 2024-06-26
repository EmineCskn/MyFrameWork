from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import Keys
from time import sleep

# service = Service("C:/Users/Lenovo/OneDrive/Desktop/MyFrameWork/chromedriver-win64/chromedriver.exe")
# driver = webdriver.Chrome(service=service)
driver = webdriver.Chrome()

driver.get("https://www.duckduckgo.com")
driver.maximize_window()
aramakutusu= driver.find_element(By.ID,"searchbox_input")
aramakutusu.send_keys("Selenium")
aramakutusu.send_keys(Keys.ENTER)

#driver.find_element(By.XPATH , "//*[@id='searchbox_homepage']/div/div[1]/div/button[2]").click
#driver.execute_script("window.scrollTo(0,100)")
#driver.find_element(By.XPATH, "//*[@id='r1-1']").click
sleep(5)
ilksayfa= driver.find_element(By.ID, "r1-1")
ilksayfa.click()


