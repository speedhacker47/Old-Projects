from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
import

driver = webdriver.Firefox()
driver.get('https://web.whatsapp.com/')

firefox_options = Options()
firefox_options.binary_location = os.environ.get("FIREFOX_BIN")
firefox_options.add_argument("--headless")
firefox_options.add_argument("--disable-dev-shm-usage")
firefox_options.add_argument("--no-sandbox")
#chrome_options.add_argument("--disable-extensions")
firefox_options.add_argument("--example-flag")


print('pls')
firefox_driver = webdriver.Firefox(executable_path=os.getenv('GECKODRIVER_PATH'), firefox_options=firefox_options)


input('Scan QR CODE and type go')

name = input('Enter the name of user or group : ')
msg = input('Enter your message : ')
count = int(input('Enter the count : '))


while True:
    try:
        user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
        user.click()
        break
    except:
        continue

msg_box = driver.find_elements_by_class_name('_3FRCZ')
num = 0
for i in range(count):
    msg_box[1].send_keys(msg+str(num))
    msg_box[1].send_keys(Keys.ENTER)
    num+=1
    #button = driver.find_element_by_class_name('_3M-N-')
    #button.click()

