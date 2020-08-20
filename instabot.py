from selenium import webdriver
from time import sleep
from credentials import username, password

'''
Ignore this for now; testing the instagram bot processes below first so that I can determine it works and brings me to the right page before
I move everything to the class
'''
class Instabot:
    def __init_(self, username, password):
        self.driver = webdriver.Firefox()
        sleep(2)
        self.driver.get("https://www.instagram.com/?hl=en")


driver = webdriver.Firefox()
driver.set_window_size(1000, 900)
sleep(2)
driver.get("https://www.instagram.com/?hl=en")
sleep(2)
username_input = driver.find_element_by_name("username")
username_input.send_keys(username)
sleep(2)
password_input = driver.find_element_by_name("password")
password_input.send_keys(password)
sleep(2)
# Login
driver.find_element_by_xpath("//button[@type='submit']").click()
sleep(3)
# Ignore the request to save information
driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/div/button").click()
sleep(2)
# Clicks not now for notifications
driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]").click()
sleep(3)
# Clicks the Explore Page Link
driver.find_element_by_xpath("//a[@href='/explore/']").click()
sleep(4)
