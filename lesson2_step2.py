from selenium import webdriver
import time
import math





def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))


try:
	link = 'http://suninjuly.github.io/redirect_accept.html'
	browser = webdriver.Chrome()
	browser.get(link)
	browser.find_element_by_xpath('//*/button').click()
	browser.switch_to.window(browser.window_handles[1])
	
	browser.find_element_by_css_selector('.form-control').send_keys(calc(browser.find_element_by_css_selector('#input_value').text))
	browser.find_element_by_xpath('//*[text()="Submit"]').click()
	
finally:
	time.sleep(10)
	browser.quit()