def fahr_to_celsius(temp_fahrenheit):
 """
 purpose : the input Fahrenheit temperature converted to Celsius
 parameters : temp_fahrenheit
 returned values : converted_temp
 """
 converted_temp = (temp_fahrenheit-32)/1.8
 return converted_temp

def temp_classifier(temp_celsius):
  """
  purpose of the function : reclassify the entered temperature
  parameters : temp_celsius
  returned values : from 0 to 3
  """
  if temp_celsius <-2:
    return 0
  elif (temp_celsius >= -2)and(temp_celsius < 2):
    return 1
  elif (temp_celsius >= 2)and(temp_celsius < 15):
    return 2
  elif temp_celsius >= 15:
    return 3

"""
purpose of the function : classifying Fahrenheit temperature datasets into four different classes
parameter : "temp_fahrenheit" and "temp_celsius"
returned values : "converted_temp" and "from 0 to 3"
"""