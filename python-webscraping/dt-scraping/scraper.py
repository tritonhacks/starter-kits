from bs4 import BeautifulSoup
import requests # Used to request webpages
import urllib   # Used for URL encoding (e.g. La Jolla San Diego CA -> La+Jolla%2C+San+Diego%2C+CA)

# HTTP header we'll use for getting the page
headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET',
    'Access-Control-Allow-Headers': 'Content-Type',
}

"""
String, String => ([ratings], [costs])
"""
def scrape_for(query, location):
    url = "https://www.yelp.com/search?"
    params = {"find_desc": query, "find_loc": location, "ns": 1}
    url += urllib.parse.urlencode(params)

    # caculate the location url encoded string
    page = requests.get(url, headers)
    scraper = BeautifulSoup(page.content, 'html.parser')

    # Get all search results
    results = scraper.find_all("div", class_="container__09f24__21w3G")

    # Get all star ratings
    stars = scraper.find_all("div", class_="i-stars__09f24__1T6rz")

    # Get all prices
    prices = scraper.find_all("span", class_="priceRange__09f24__2O6le")

    # Get all images, store only source attributes
    images = scraper.find_all(class_="photo-box-img__09f24__3F3c5")[:10]
    image_sources = [img["src"] for img in images]
    
    # turn stars into numbers
    for i in range(len(stars)):
        stars[i] = float(stars[i]["aria-label"][:-12])
    
    # turn prices into numbers as well
    for i in range(len(prices)):
        prices[i] = prices[i].string

    return (prices, stars, image_sources)