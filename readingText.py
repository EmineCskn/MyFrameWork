from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import Keys
from time import sleep


driver = webdriver.Chrome()

driver.get("https://tr.wikipedia.org/wiki/Anasayfa")
driver.maximize_window()
seckinMaddeAlani= driver.find_element(By.XPATH,"//*[@id='mp-tfa']")
seckinMaddeYazisi = seckinMaddeAlani.text
seckinMaddeYazisi= seckinMaddeYazisi.split(",")[0]
print("seckin madde: " +seckinMaddeYazisi)
kaliteliMaddeAlani = driver.find_element(By.ID, "mf-tfp")
kaliteMaddeYazisi = kaliteliMaddeAlani.text
kaliteMaddeYazisi = kaliteMaddeYazisi.split(",")[0]
print("kaliteli madde: " +kaliteMaddeYazisi)
driver.quit()