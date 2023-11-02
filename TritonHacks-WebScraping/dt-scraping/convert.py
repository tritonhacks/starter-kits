import math

"""
[list of string prices (e.g. [$, $$])] => float
"""
def avg_price(prices):
    sum = 0
    for i in range(len(prices)):
        sum += len(prices[i])
    
    print(sum / len(prices))
    return sum / len(prices)

"""
[list of numbers] => float
"""
def avg_rating(ratings):
    return sum(ratings) / len(ratings)
   

#  Calculate the type of emoji to display for current rating.
def calculate_moons(score, multiplier):
  # 🌑🌘🌓🌖🌕
  MOON_EMOJIS = ["&#x1F311","&#x1F318", "&#x1F317", "&#x1F316", "&#x1F315"]
  score = math.floor(float(score) * multiplier + 0.25) / multiplier
  score_copy = score
  
  display_string = ""
  for i in range (5):
    if(score> 1):
      display_string += MOON_EMOJIS[4]
      score -= 1
    else:
      display_string += MOON_EMOJIS[int(score*4)]
      score = 0

  return (display_string, score_copy)