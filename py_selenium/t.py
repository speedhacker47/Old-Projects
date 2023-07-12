from pyvirtualdisplay import Display
from selenium import webdriver

    # we can now start Firefox and it will run inside the virtual display
browser = webdriver.Firefox()

display = Display(visible=0 , size = (1000,600))
display.start()

    # put the rest of our selenium code in a try/finally
    # to make sure we always clean up at the end

browser.get('http://www.google.com')


print(browser.title) #this should print "Google"


