from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import Keys
from time import sleep


driver = webdriver.Chrome()

# driver.get("https://www.imdb.com")
# driver.maximize_window()
# driver.find_element(By.ID,"imdbHeader-navDrawerOpen").click()
# sleep(5)
# driver.find_element(By.XPATH, "//span[text()='Top 250 Movies']").click()
# film_list = driver.find_elements(By.XPATH, "//div//div//a//h3")

# for i in range(20):
#     print(film_list[i].text)

driver.get("https://www.imdb.com")
driver.maximize_window()
driver.find_element(By.ID,"imdbHeader-navDrawerOpen").click()
sleep(5)
driver.find_element(By.XPATH, "//span[text()='Top 250 Movies']").click()
film_list = driver.find_elements(By.XPATH, "//div//div//a//h3")
film_list_details = driver.find_elements(By.XPATH, "//div//div[@class='sc-b189961a-7 feoqjK cli-title-metadata']")
clean_list_details = []

for i in film_list_details:
    parts= i.text.split("\n",1)
    clean_list_details.append(parts[0])


combined = []
for x, y in zip(film_list, clean_list_details):
    combined.append(x.text +" "+ y)
print(combined)


for i in combined:
    if "2000" in i:
        print(i)

    

driver.quit()