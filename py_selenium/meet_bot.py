from selenium import webdriver
import os
import time

#user = 'electro.wizard24k'
#password = '$bandit$'

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
#chrome_options.add_argument("--headless")
#chrome_options.add_argument("--disable-dev-shm-usage")
#chrome_options.add_argument("--no-sandbox")

chrome_driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)

class meet:
    def __init__(self,link,user,password):
        global chrome_driver
        self.username = user
        self.password = password
        self.driver = chrome_driver
        self.link = link
        self.signer()
        
    def signer(self):
        self.driver.get('https://stackoverflow.com/users/signup?ssrc=head&returnurl=%2fusers%2fstory%2fcurrent%27')
        print('stackOverflow Opened')
        print(self.driver.title)
        print(self.driver.current_url)
        self.driver.save_screenshot('ss.png')
        while True:
            try:
                self.driver.find_element_by_xpath('//*[@id="openid-buttons"]/button[1]').click()
                print('Ready to Log In')
                print(self.driver.current_url)
                print(self.driver.title)
                self.driver.save_screenshot('ss_start.png')
                break
            except:
                print('Trying to log you in...')
                continue

        while True:
            try:
                self.driver.find_element_by_xpath('//input[@type="email"]').send_keys(self.username)
                self.driver.find_element_by_xpath('//*[@id="identifierNext"]').click()
                print('Email Added')
                print(self.driver.current_url)
                break
            except:
                time.sleep(5)
                source = self.driver.page_source
                print(self.driver.title)
                if 'Thats an error':
                    print('bad req 1')
                if 'Error' in source:
                    print('bad req 2')
                if 'error' in source:
                    print('bad req 3')
                if 'The server cannot process the request because it is malformed. It should not be retried' in source:
                    print('really bad req')
                if 'To continue, Google will share your name, email address,' in source and 'Forgot email?' in source:
                    print('google')
                print(self.driver.title)
                print('Trying to put email')
                print(self.driver.current_url)
                self.driver.save_screenshot('ss_e.png')
                continue
        
        while True:
            try:
                self.driver.find_element_by_xpath('//input[@type="password"]').send_keys(self.password)
                self.driver.find_element_by_xpath('//*[@id="passwordNext"]').click()
                print('password added')
                break
            except:
                time.sleep(5)
                print('Trying to put password')
                self.driver.save_screenshot('ss_p.png')
                continue
    def open_meeting(self):
        self.driver.get(self.link)
        while True:
            try:
                button = self.driver.find_element_by_xpath('/html/body/div[1]/c-wiz/div/div/div[4]/div[3]/div/div[2]/div/div/div[2]/div/div[2]/div/div/div[1]')
                button.click()
                print('Asking to join')
                break
            except:
                print('opening google meet')
                continue

link = 'https://meet.google.com/ysm-nkzg-txm'
bot = meet(link,'electro.wizard24k','$bandit$')
bot.open_meeting()
time.sleep(500)
chrome_driver.quit()
