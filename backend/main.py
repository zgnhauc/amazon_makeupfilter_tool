# scrapping data from amazon

# cleaning + organizing data from amazon. put into csv file in following format: product name, description, price, and reviews

# import data + libraries
import pandas as pd
import numpy as np

# get product name

# get price

# get list of reviews

# get skin type
oilyKeywords = ["oily", "greasy", "shiny", "sticky", "glossy"]
normalKeywords = ["normal", "combination", "even", "smooth"]
dryKeywords = ["dry", "rough", "dehydrated", "flaky"]

def skinType(reviews): # tests skin type compatability, takes list of reviews as parameter
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
    return "Oily"
  elif (sentimentScore > -0.4) and (sentimentScore < 0.4):
    return "Normal"
  else:
    return "Dry"

# check if product meets user specifications

# make a summary of all reviews

# print results
  
