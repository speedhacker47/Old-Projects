from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get('https://web.whatsapp.com/')

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

