import time
PROMISED_DOWN=150
PROMISED_UP=10
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
class InternetSpeedTwitterBot:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)
        self.up=0
        self.down=0
    def getinternetspeed(self):
        self.driver.get("https://www.speedtest.net/")
        go=self.driver.find_element(By.XPATH,value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a')
        go.click()
        time.sleep(60)
        up=self.driver.find_element(By.XPATH,value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span')
        self.up=up.text
        down=self.driver.find_element(By.XPATH,value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
        self.down=down.text
    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/home")
        time.sleep(4)
        email=self.driver.find_element(By.NAME,value="text")
        email.send_keys("your gmail",Keys.ENTER)
        time.sleep(4)
        password=self.driver.find_element(By.NAME,value='password')
        password.send_keys("your password",Keys.ENTER)
        time.sleep(4)
        tweet=self.driver.find_element(By.XPATH,value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div')
        tweet.send_keys(f"Hey internet provider why my internet is{self.down} down,{self.up} up when i pay for {PROMISED_UP}/{PROMISED_DOWN}?",Keys.ENTER)
        time.sleep(3)
        post=self.driver.find_element(By.XPATH,value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/div[3]/div')
        post.click()

