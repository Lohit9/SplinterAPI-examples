# Quick Screenshot - Just mention the URL and take a screenshot

from splinter import Browser

browser = Browser('chrome')

url = "http://lohittalasila.com"
browser.visit(url)

browser.driver.save_screenshot('screenshot.png')

browser.quit()
