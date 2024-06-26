from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import Keys
from time import sleep


driver = webdriver.Chrome()

# driver.get("https://the-internet.herokuapp.com/login")
# driver.maximize_window()

'''
test otomasyonu
test : beklentileri karsiliyor mu ?
1- Istenileni yapiyor mu? pozitif test 2. Istenmeyeni yapiyor mu? negatif 

Internet login sayfasina git *https://the-internet.herokuapp.com/login
kullanici adi gir 
sifre gir 
login butonuna tikla
yanlis kullanici adi : Your username is invalid!
yanlis password      : Your password is invalid!
ikiside dogruysa     : You logged into a secure area!Link secure icerecek *https://the-internet.herokuapp.com/secure
'''

# usernameBox = driver.find_element(By.ID , "username")
# passwordBox = driver.find_element(By.ID , "password")
# usernameBox.send_keys("test")
# passwordBox.send_keys("SuperSecretPassword!")
# loginButton = driver.find_element(By.CSS_SELECTOR , "button.radius")
# loginButton.click()
# mesaj = driver.find_element(By.ID, "flash").text
# if "Your username is invalid!" in mesaj:
#     print("OK , invalid username worked curruntly")
# else:
#     print("Eror , incorrect username did not work")


    
#usernameBox.send_keys("tomsmith")

def login(username,password):
    driver.get("https://the-internet.herokuapp.com/login")
    driver.maximize_window()

    usernameBox = driver.find_element(By.ID , "username").send_keys(username)
    passwordBox = driver.find_element(By.ID , "password").send_keys(password)
    sleep(2)
    loginButton = driver.find_element(By.CSS_SELECTOR , "button.radius")
    loginButton.click()
    message = driver.find_element(By.ID, "flash").text
    return message

message = login("test","SuperSecretPassword!")
assert "Your username is invalid!" in message

# if "Your username is invalid!" in message:
#      print("OK , invalid username worked curruntly")
# else:
#      print("Eror , incorrect username did not work")

sleep(3)

message = login("tomsmith","asdf")
assert "Your password is invalid!" in message

# if "Your password is invalid!" in message:
#      print("OK , invalid password worked curruntly")
# else:
#      print("Eror , incorrect password did not work" +message)

sleep(3)
message = login("tomsmith","SuperSecretPassword!")
assert "You logged into a secure area!" in message

# if "You logged into a secure area!" in message:
#      print("OK , Succesfull login with valid password and username")
# else:
#      print("Eror , Unable to login with valid password and username" + message)


link=driver.current_url
assert "secure" in link

driver.quit()