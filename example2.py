import sys
# Quick Screenshot - Just mention the URL and take a screenshot

from splinter import Browser

browser = Browser('chrome')

#url = "http://lohittalasila.com"
url = str(sys.argv[1])
print "screenshot of the page found at "+url+" has been taken you can access it by using the command - open screenshot.png"

print "Thanks for using quick screenshot"

browser.visit(url)

browser.driver.save_screenshot('screenshot.png')

browser.quit() 
