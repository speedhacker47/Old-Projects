from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import time
#from signer import *

chrome_options = Options()
#chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--example-flag")


chrome_driver = webdriver.Chrome(options=chrome_options)
chrome_options.add_argument("--example-flag")
#chrome_driver.delete_all_cookies()
print('cookie cleared')
print('new task opened')
class meet:
    def __init__(self):
        global chrome_driver
        self.driver = chrome_driver
            
    def open_meeting(self,link):
        time.sleep(1)
        self.driver.get(link)
        while True:
            print(self.driver.title)
            try:
                time.sleep(1)
                button = self.driver.find_element_by_xpath('/html/body/div[1]/c-wiz/div/div/div[4]/div[3]/div/div[2]/div/div/div[2]/div/div[2]/div/div/div[1]')
                button.click()
                print(self.driver.title)
                print('Asking to join')
                break
            except:
                try:
                    button = self.driver.find_element_by_xpath('/html/body/div[1]/c-wiz/div/div[2]/div/div')
                    button.click()
                    print('Cant join meeting going back..')
                    time.sleep(4)
                    print(self.driver.title)
                    break
                except:
                    print('other problem')
                time.sleep(1)
                print('opening google meet')
                continue

    def signer(self,user,password,recovery):
        self.driver.get('https://accounts.google.com/signin/oauth/identifier?client_id=717762328687-iludtf96g1hinl76e4lc1b9a82g457nn.apps.googleusercontent.com&scope=profile%20email&redirect_uri=https%3A%2F%2Fstackauth.com%2Fauth%2Foauth2%2Fgoogle&state=%7B%22sid%22%3A1%2C%22st%22%3A%2259%3A3%3ABBC%2C16%3A338c6d9c63e5e42c%2C10%3A1594384669%2C16%3A3aa68e5dd3104bfd%2Cde607ae47e6ce70b2552da09af30c250eeb36c4c09be682928cb7212aaec2060%22%2C%22cdl%22%3Anull%2C%22cid%22%3A%22717762328687-iludtf96g1hinl76e4lc1b9a82g457nn.apps.googleusercontent.com%22%2C%22k%22%3A%22Google%22%2C%22ses%22%3A%22bf6f4799da6744aa960c960e3da1dd32%22%7D&response_type=code&o2v=1&as=CN_NfhD-VMU3AgXUxu6nXg&flowName=GeneralOAuthFlow')
        print('Opened Stack')

        time.sleep(4)
        #print(driver.page_source)
        self.driver.find_element_by_xpath('//input[@type="email"]').send_keys(user)
        self.driver.find_element_by_xpath('//input[@id="next"]').click()
        print('Email added')

        time.sleep(1)
        self.driver.find_element_by_xpath('//input[@type="password"]').send_keys(password)
        self.driver.find_element_by_xpath('//input[@id="submit"]').click()
        print('Password Added')
        print(self.driver.title)
        time.sleep(1)
        '''
        print('Asking for recovery email')
        bt = self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/ol/li[1]/form/button')
        bt.click()
        print('Recovery mail added')
        time.sleep(1)
        
        time.sleep(1)
        get = self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/form/span/div/div[2]/input')
        get.send_keys(recovery)
        print('recovery email '+str(recovery)+' added')

        time.sleep(1)
        put = self.driver.find_element_by_xpath('//input[@id="submit"]')
        put.click()
        print('Logged in with id '+str(user))

        time.sleep(1)
        print(self.driver.page_source)
        self.driver.find_element_by_xpath('//*[@id="submit_approve_access"]').click()
        time.sleep(1)
'''
        print(self.driver.title)
        print('Login Complete')

    def i_joiner(self):
        global link
        self.driver.execute_script("window.open('');")
        self.driver.switch_to.window(self.driver.window_handles[len(self.driver.window_handles)-1])
        print('opening tab no.',len(self.driver.window_handles))
        self.driver.get(link)
        while True:
            try:
                button = self.driver.find_element_by_xpath('/html/body/div[1]/c-wiz/div/div/div[4]/div[3]/div/div[2]/div/div/div[2]/div/div[2]/div/div/div[1]')
                button.click()
                print('joined')
                break
            except:
                print('joining')
                continue
        

link = str(input("Enter URL"))
bot = meet()
bot.signer('majumthebot','$bandit$','electro.wizard24k@gmail.com')
bot.open_meeting(link)
tab = 0
while True:
    bot.i_joiner()
    tab += 1
#time.sleep(500)
#chrome_driver.quit()
while True:
    print('In process')
