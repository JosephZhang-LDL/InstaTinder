from selenium import webdriver
from time import sleep
from credentials import username, password

'''
Ignore this for now; testing the instagram bot processes below first so that I can determine it works and brings me to the right page before
I move everything to the class
'''
class Instabot:
    def __init__(self, username=username, password=password):
        self.driver = webdriver.Firefox()
        self.driver.set_window_size(1000, 900)
        sleep(2)

        self.driver.get("https://www.instagram.com/?hl=en")
        sleep(2)
        # Username
        self.username_input = driver.find_element_by_name("username")
        self.username_input.send_keys(self.username)
        sleep(2)

        #Password
        self.password_input = driver.find_element_by_name("password")
        self.password_input.send_keys(self.password)
        sleep(2)

        # Login
        self.driver.find_element_by_xpath("//button[@type='submit']").click()
        sleep(3)

        # Ignore the request to save information
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/div/button").click()
        sleep(2)

        # Clicks not now for notifications
        self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]").click()
        sleep(3)

        # Clicks the Explore Page Link
        self.driver.find_element_by_xpath("//a[@href='/explore/']").click()
        sleep(4)