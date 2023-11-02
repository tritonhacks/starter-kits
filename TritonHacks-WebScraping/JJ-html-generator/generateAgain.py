import sys
import math

# we have list of strings
# --> HTML file

HTML_FORMAT = """
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <title>Price Comparison App</title>
    
    <!-- import the webpage's stylesheet -->
    <link rel="stylesheet" href="./css_template.css">
   
  </head>  
  <body>
     <!--Title-->
    <h1 id="title">Statistics Comparison of Burger</h1>
    
    <!--Board-->
    <div id="board">
      {}
    </div>
  </body>
</html>
"""
STAR_EMOJI = "&#x2B50;"
PRICE_EMOJI = "&#x1F4B8;"

ITEM_FORMAT = """
      <div class="slide">
        <!--location-->
        <h2>{location}</h2>
        <!--average rating-->
        <div><strong>Average rating:</strong>{rating}</div>
        <!--average price-->
        <div><strong>Average price:</strong>{price}</div>
        <!--Image-->
        <div class="imageCollage">
          {images}
        </div>
      </div>
"""


# TODO: USE THE MOON EMOJIS TO REPRESENT THE STARS,
# EMPTY MOON CAN REPRESENT THE NON-FILLED STARS
# WHAT ABOUT DOLLARS...?

# void generate(ArrayList<Integer> dataList)
def generate(dataList):
    middle = ""
    for data in dataList:

        # rating_int = int(data['rating'])
        # rating_string = STAR_EMOJI * rating_int 

        # Add a 0.5 star if needed
        # if float(data['rating']) - rating_int > 0:
        #     rating_string += ".5"
        
        # 🌑🌘🌓🌖🌕
        MOON_EMOJIS = ["&#x1F311","&#x1F318", "&#x1F313", "&#x1F316", "&#x1F315"]

        rating= math.floor(float(data['rating']) * 4 + 0.25)/4
        rating_stringInt = rating
        rating_string = ""
        for i in range (5):
          if(rating > 1):
            rating_string += MOON_EMOJIS[4]
            rating -= 1
          else:
            rating_string += MOON_EMOJIS[int(rating*4)]
            rating = 0

        # price_string = PRICE_EMOJI * int(data['price'])

        price = math.floor(float(data['price']) * 5 + 0.25)/4
        price_stringInt = price
        price_string = ""
        for i in range (5):
          if(price > 1):
            price_string += MOON_EMOJIS[4]
            price -= 1
          else:
            price_string += MOON_EMOJIS[int(price*4)]
            price = 0

        # Load i
        images_string = ""
        for url in data['images']:
            images_string += """<img src="{}">""".format(url) + "\n"

        middle += ITEM_FORMAT.format(location=data['location'], 
                  rating = rating_string + "(" + str(rating_stringInt) + ")",
                  price = price_string + "(" + str(price_stringInt) + ")",
                  images=images_string)


    with open("out6.html", "w+") as new_file:
        new_file.write(HTML_FORMAT.format(middle))


generate([{"location":"paris", "rating":4.7, "price":3, "images":["https://sickr.files.wordpress.com/2014/07/pikachu_sit.png?w=1200"]*5}]*2)