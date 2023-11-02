import sys

# we have list of strings
# --> HTML file

HTML_FORMAT = """
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Web scrapering!</title>
    
    <!-- import the webpage's stylesheet -->
    <link rel="stylesheet" href="/css_template.css">
   
  </head>  
  <body>
     <!--Title-->
    <h1 id="title">Statistics Comparison of Burger</h1>
    
    <!--Board-->
    <div id="board">
      <!--Left Slide-->
      <div class="slide">
        <!--location-->
        <h2>{location1}</h2>
        <!--average rating-->
        <div><strong>Average rating:</strong>{rating1}/5</div>
        <!--average price-->
        <div><strong>Average price:</strong>{price1}/$$$$</div>
        <!--Image (9)-->
        <div class="imageCollage">
        {image1}
        </div>
      </div>
      <!--Right Slide-->
      <div class="slide">
        <!--location-->
        <h2>{location2}</h2>
        <!--average rating-->
        <div><strong>Average rating:</strong>{rating2}/5</div>
        <!--average price-->
        <div><strong>Average price:</strong>{price2}/$$$$</div>
        <!--Image (9)-->
        <div class="imageCollage">
        {image2}
        </div>
      </div>
    </div>
  </body>
</html>

"""

# TODO: Create CSS file to properly format the columns

# void generate(ArrayList<Integer> dataList)
def generate(dataList):
    middle = ""
    for data in dataList:
        middle += "<div>{}</div>\n".format(data)

    with open("out.html", "w") as new_file:
        new_file.write(HTML_FORMAT.format(middle))


generate(["1", "2", "3"])