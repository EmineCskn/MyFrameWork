from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service

# service = Service("C:/Users/Lenovo/OneDrive/Desktop/MyFrameWork/chromedriver-win64/chromedriver.exe")
# driver = webdriver.Chrome(service=service)
driver = webdriver.Chrome()

driver.get("https://www.apple.com")

link = driver.current_url
baslik = driver.title
print("sayfa basligi: " + baslik)

if "apple.com" in link:
    print("Dogru Apple sayfasindayiz: " +link)
driver.maximize_window()
driver.get("https://www.etsy.com")
link = driver.current_url
baslik = driver.title
print("baslik: " + baslik)
if "etsy.com" in link:
    print("Etsy sayfasindayiz: "+link)
driver.back()                             #eski sayfaya geri donme methodu
baslik = driver.title
driver.save_screenshot("./ekrangoruntusu.png") #ekran goruntusu alma methodu
if "Apple" in baslik:
    print("Tebrikler Apple sayfasina dondun")
# else:
#     driver.save_screenshot("./ekrangoruntusu.png")

driver.quit()





