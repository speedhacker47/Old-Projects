from selenium import webdriver
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.common.keys import Keys
import time

user = 'electro.wizard24k'
password = '$bandit$'


chrome_options = Options()

chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
chrome_driver = os.getcwd() +"\\chromedriver.exe"

#chrome_options.add_argument("--use-fake-ui-for-media-stream")
#chrome_options.add_argument("--disable-user-media-security=true")
#chrome_options.add_argument("--disable-notifications")


#chrome_options.add_argument("--window-size=1920x1080")
#driver = webdriver.Chrome(options=chrome_options, executable_path=chrome_driver)
chrome_driver = webdriver.Chrome(options = chrome_options)


class meet:
    def __init__(self,link):
        global driver
        self.mail = "gmail@gmail.com"
        self.password = 'pass'
        self.driver = chrome_driver
        self.link = link
        self.signer()
        
    def signer(self):
        print(self.driver.title)
        self.driver.get('https://accounts.google.com/signin/oauth/identifier?client_id=717762328687-iludtf96g1hinl76e4lc1b9a82g457nn.apps.googleusercontent.com&scope=profile%20email&redirect_uri=https%3A%2F%2Fstackauth.com%2Fauth%2Foauth2%2Fgoogle&state=%7B%22sid%22%3A1%2C%22st%22%3A%2259%3A3%3ABBC%2C16%3A338c6d9c63e5e42c%2C10%3A1594384669%2C16%3A3aa68e5dd3104bfd%2Cde607ae47e6ce70b2552da09af30c250eeb36c4c09be682928cb7212aaec2060%22%2C%22cdl%22%3Anull%2C%22cid%22%3A%22717762328687-iludtf96g1hinl76e4lc1b9a82g457nn.apps.googleusercontent.com%22%2C%22k%22%3A%22Google%22%2C%22ses%22%3A%22bf6f4799da6744aa960c960e3da1dd32%22%7D&response_type=code&o2v=1&as=CN_NfhD-VMU3AgXUxu6nXg&flowName=GeneralOAuthFlow')
        print('stackOverflow Opened')
        print(self.driver.title)
        self.driver.save_screenshot('ss.png')
        source = self.driver.page_source
        '''while True:
            try:
                self.driver.find_element_by_xpath('//*[@id="openid-buttons"]/button[1]').click()
                print('Ready to Log In')
                print(self.driver.title)
                print(self.driver.current_url)
                break
            except:
                print('Trying to log you in...')
                continue
'''
        while True:
            try:
                self.driver.find_element_by_xpath('//input[@type="email"]').send_keys(user)
                #self.driver.find_element_by_xpath('//*[@id="identifierNext"]').click()
                self.driver.find_element_by_xpath('//input[@id="next"]').click()
                #print(self.driver.current_url)
                print('Email Added')
                break
            except:
                time.sleep(3)
                print('Trying to put email')
                #print(self.driver.current_url)
                continue
        
        while True:
            try:
                self.driver.find_element_by_xpath('//input[@type="password"]').send_keys(password)
                #self.driver.find_element_by_xpath('//*[@id="passwordNext"]').click()
                self.driver.find_element_by_xpath('//input[@id="submit"]').click()
                print('password added')
                break
            except:
                time.sleep(3)
                print('Trying to put password')
                continue
    def open_meeting(self):
        time.sleep(2)
        self.driver.get(self.link)
        while True:
            try:
                button = self.driver.find_element_by_xpath('/html/body/div[1]/c-wiz/div/div/div[4]/div[3]/div/div[2]/div/div/div[2]/div/div[2]/div/div/div[1]')
                button.click()
                print('Asking to join')
                break
            except:
                time.sleep(5)
                source = self.driver.page_source
                print('opening google meet')
                self.driver.save_screenshot('x.png')
                continue
        while True:
            bot.new_tab()
        #bot.present()
        
    def new_tab(self):
        self.driver.execute_script("window.open('');")
        self.driver.switch_to.window(self.driver.window_handles[len(self.driver.window_handles)-1])
        print(len(self.driver.window_handles))
        self.driver.get(self.link)
        self.driver.save_screenshot('last2.png')
        #al = self.driver.switch_to_alert
        #al.dismiss
        while True:
            try:
                bt = self.driver.find_element_by_xpath('//*[@id="yDmH0d"]/div[3]/div/div[2]/div[3]/div')
                bt.click()
                print('dismissed')
                break
            except:
                print('dismissing...')
                continue
        #self.driver.close()
        #self.driver.switch_to.window(self.driver.window_handles[1])
        while True:
            try:
                button = self.driver.find_element_by_xpath('/html/body/div[1]/c-wiz/div/div/div[4]/div[3]/div/div[2]/div/div/div[2]/div/div[2]/div/div/div[1]')
                button.click()
                print('joined')
                break
            except:
                print('joining')
                continue
        source = self.driver.page_source
        #print(source)
        try:            
            chat_b = self.driver.find_element_by_xpath('/html/body/div[1]/c-wiz/div[1]/div/div[4]/div[3]/div[6]/div[3]/div/div[2]/div[3]')
            chat_b.click()
            chat_area = self.driver.find_element_by_xpath('/html/body/div[1]/c-wiz/div[1]/div/div[4]/div[3]/div[3]/div/div[2]/div[2]/div[2]/span[2]/div/div[3]/div[1]/div[1]/div[2]/textarea')
            chat_area.send_keys('I am Bot no.'+str(len(self.driver.window_handles)))
            chat_area.send_keys(Keys.ENTER)
        except:
            print(len(self.driver.window_handles))
            self.driver.save_screenshot('error.png')
            
if __name__ == '__main__':
    link = str(input('Enter URL '))
    bot = meet(link)
    bot.open_meeting()
