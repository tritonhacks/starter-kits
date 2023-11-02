# Entrypoint to your webscraping starter kit
import requests
from bs4 import BeautifulSoup
import urllib # Used for URL encoding (e.g. La Jolla San Diego CA --> La+Jolla%2C+San+Diego%2C+CA)
import webbrowser # Used to open html page after scraping
import os

# HTTP header we'll use for getting the page
headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET',
    'Access-Control-Allow-Headers': 'Content-Type',
    # 'Access-Control-Max-Age': '3600',
    # 'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
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


    
scrape_for("burger", "los angeles")

"""
[list of string prices (e.g. [$, $$])] => float
"""
def avg_price(prices):
    sum = 0
    for i in range(len(prices)):
        sum += len(prices[i])
    
    return sum / len(prices)

"""
[list of numbers] => float
"""
def avg_rating(ratings):
    return sum(ratings) / len(ratings)
    

if __name__ == "__main__":
    # Parse user input for queryngs
    print("Welcome to the location comparator app! Please enter your item to compare (e.g. hot dog):\n")
    item = input()
    print("Ah, {}! An excellent choice! Please enter the first of two locations to compare:\n".format(item))
    place1 = input()
    print("Second of two locations:\n")
    place2 = input()
    print("Thank you! Generating report...\n\n")

    # Make the scrapping requests (this may take a few seconds)
    (prices1, stars1) = scrape_for(item, place1)
    (prices2, stars2) = scrape_for(item, place2)

    # calculate the averaged prices and stars of the separate locations
    place1_avg_price = avg_price(prices1)
    place1_avg_rating = avg_rating(stars1)
    place2_avg_price = avg_price(prices2)
    place2_avg_rating = avg_rating(stars2)

    print("In {p1}, the average rating for {it} is {ra} and the average price is {price}"
    .format(p1=place1, it=item, ra=avg_rating(stars1), price=avg_price(prices1)))

    print("In {p2}, the average rating for {it} is {ra} and the average price is {price}\n"
    .format(p2=place2, it=item, ra=avg_rating(stars2), price=avg_price(prices2)))

    # Determine the cheaper and higher rated places
    cheaper = place2 if place1_avg_price > place2_avg_price else place1
    higher_rating = place2 if place2_avg_rating > place1_avg_rating else place1

    print("Based on this we can conclude that {} is cheaper...".format(cheaper))
    print("and {} is higher rated!".format(higher_rating))

    #webbrowser.open('file://' + os.path.realpath("out.html"))