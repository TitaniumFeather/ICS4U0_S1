# PART 1
inch = 1000000000000
(foot, inches) = divmod(inch, 12)
(yard, foot_) = divmod(foot, 3)
(mile, yard_) = divmod(yard, 1760)
(earth_to_moon, mile_) = divmod(mile, 238855)

print("One trillion inches is the same as going to the moon and back %d times, plus an extra %d miles,  %d yards,  %d feet,  and  %d  inches." % (earth_to_moon, mile_, yard_, foot_, inches))

# EXERCISE
toLower(letter)
  if 96 < ord(letter) < 123:
    return "Error "
  elif 64 < ord(letter) < 91:
    lowercase = 97 + (ord(letter) - 65)
    return chr(lowercase)
  

