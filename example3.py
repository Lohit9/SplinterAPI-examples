# By Lohit Talasila

# Please fill in your MWS credentials:

SellerId = 'xxx'

MWSAuthToken = 'xxx'

AWSAccessKeyId = 'xxx'

SecretKey = 'xxx'

FeedType = '_POST_PRODUCT_DATA_'

MarketplaceId = 'xxx'

#---------------------------------- script begins here --->
import time

from splinter import Browser

browser = Browser('chrome')

browser.visit('https://mws.amazonservices.ca/scratchpad/index.html')

browser.select('apicall', 'SubmitFeed')

browser.fill('merchantID', SellerId)

browser.fill('authToken', MWSAuthToken)

browser.fill('awsAccountID', AWSAccessKeyId)

browser.fill('secretKey', SecretKey)

print "I was unable to autofill the Feedtype and Marketplace id, please fill them manually \n"
print "Your Feed Type is: " + FeedType
print "Your MarketPlace Id is: " + MarketplaceId
