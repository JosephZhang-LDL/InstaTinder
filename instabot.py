from selenium import webdriver
from time import sleep
from credentials import username, password

class Instabot:
    def __init_(self, username, password):
        self.driver = webdriver.Firefox()
        sleep(2)
        self.driver.get("https://www.instagram.com/?hl=en")


driver = webdriver.Firefox()
sleep(2)
driver.get("https://www.instagram.com/?hl=en")
sleep(2)
username_input = driver.find_element_by_name("username")
username_input.send_keys(username)
sleep(2)
password_input = driver.find_element_by_name("password")
password_input.send_keys(password)
sleep(2)
driver.find_element_by_xpath("//button[@type='submit']").click()
sleep(3)
driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/div/button").click()
sleep(2)
driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]").click()