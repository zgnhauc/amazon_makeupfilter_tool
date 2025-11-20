
# libraries + set up
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# intializes and allows for a new google chrome browser to be opened
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# product we are checking
productURL = ("https://www.amazon.com/Face-Shop-Cleansing-Hydrating-Moisturizing/dp/B0DB6D3L9N/ref=sr_1_5_sspa?crid=17TE4QHZ0Q9DB&dib=eyJ2IjoiMSJ9.JnQIERFbDYWxZ1Jrg1eGdMQwCOHePJ6WAL_OZ9tll6n4Qap-r_rxP5j6kH8gXbLjBi3ApDBH3t8D6TYjhMgcFtrZhlty7ydHI8P0wElZHsd1PbJPlHbByt9hw5CGag9nFen8zFCSFPTbWDgwIaNG6J3AZEj859HG_pllSBrtgQN34DybSnZ98ImPRoepmOkax_-hBGkKyNpRBBYWjbcpjd9-Pc_I8gDh2RtvKm6zGVm2S_E8nCb1o5GwE9eebodDDbcRqi85wjocdhoZzxvDaimVHaM55GMNIoc9zg56u3M.zx9ocwwpAn9cOTJQHjwaZlyRhPtM_wlGwHIdo_YkDxE&dib_tag=se&keywords=makeup+and+skincare&qid=1763616645&sprefix=makeup+and+skincare%2Caps%2C163&sr=8-5-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1")

driver.get(productURL) # opens webpage to product URL
driver.quit() # exits the webpage of the URL to close

# extracting product details
productName = driver.find_element(By.ID, "productTitle").text # product name is found using the ID
productDescriptionList = driver.find_element(By.CSS_SELECTOR, "a-unordered-list a-vertical a-spacing-mini") # product descriptions is found using the CSS Selector
# still need to get product price and reviews, store in variables productPrice and productReviews

# get skin type
oilyKeywords = ["oily", "greasy", "shiny", "sticky", "glossy"]
normalKeywords = ["normal", "combination", "even", "smooth"]
dryKeywords = ["dry", "rough", "dehydrated", "flaky"]


def skinType(reviews): # tests skin type compatability, takes list of reviews as parameter
  productSkinType = "None"
  sentiments = 0
  mentions = 0
  for review in reviews: # iterates through every review in reviews
    if oilyKeywords in review: # checks for oily keywords
      sentiments -= 1
      mentions += 1
    elif normalKeywords in review: # checks for normal keywords
      mentions += 1
    elif dryKeywords in review: # checks for dry keywords
      sentiments += 1
      mentions += 1
    else: # if no skin type mentions, continues
      continue
  if mentions == 0:
    return "No mentions of skin type"
  
  sentimentScore = sentiments / mentions
  if (sentimentScore >= -1) and (sentimentScore =< -0.4):
    productSkinType = "Oily"
    return productSkinType
  elif (sentimentScore > -0.4) and (sentimentScore < 0.4):
    productSkinType = "Normal"
    return productSkinType
  else:
    productSkinType = "Dry"
    return productSkinType

# check if product meets user specifications

def meetsRequirements(userSkinType, userBudget):
  priceGood = False
  skinTypeGood = False
  allSpecifications = False
  
  if userSkinType == productSkinType:
    skinTypeGood = True
  if userBudget >= productPrice:
    priceGood = True

  if skinTypeGood == True and priceGood == True:
    print("Meets skin type and budget specifications!")
    allSpecifications = True
    return allSpecifications
  elif skinTypeGood == False and priceGood == False:
    print("Does not meet skin type specification.")
    return allSpecifications
  elif skinTypeGood == True and priceGood == False:
    print("Does not meet price specification.")
    return allSpecifications
  else:
    print("Does not meet skin type and price specifications.")
    return allSpecifications

# make a summary of all reviews using AI ... store summary paragraph in variable productReviewSummary

# print results
if allSpecifications == True:
  print(productName)
  print(productDescription)
  print(productPrice)
  print(productReviewSummary)
  print(productSkinType)
else:
  print("Try another product")

