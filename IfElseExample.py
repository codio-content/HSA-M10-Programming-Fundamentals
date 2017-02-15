__author__ = 'mcclure'

number1 = int(input("Enter a number between 0 and 9:"))
number2 = int(input("Enter another number between 0 and 9:"))

if number1 > number2 :
    if number2 > 5: 
      print ("You chose a number greater than 5")
      if number2 > 8: 
        print("One of your numbers was 9")
      else: 
        print("One of your numbers was less than 5")