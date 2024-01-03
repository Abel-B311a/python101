try:
  10/0
  num = int(input("Insert a number: "))
  print(num)

except ZeroDivisionError: # good to sepcify it
  print("Div by 0")
except: # to brord 
  print("Invalid input")
