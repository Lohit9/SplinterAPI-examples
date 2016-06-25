#import the Browser class
from splinter import Browser

#instantiate
browser = Browser('chrome') # note that if you do not provide any browser name then it defaults to Firefox

#visit any website using browser.visit
browser.visit('http://google.com')

#fill in the text field (inspect the page to find the tag corresponding text field)
browser.fill('q', 'lohit talasila')

#press the search button
button = browser.find_by_name('btnG').click()

#Check if Splinter website is in the search results
if browser.is_text_present('https://github.com/Lohit9'):
   print "Yes, Your Github is visible! :)"
else:
   print "No, Your Github is not visible :("

browser.quit()
