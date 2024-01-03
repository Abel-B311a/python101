try:
  10/0
  num = int(input("Insert a number: "))
  print(num)

except ZeroDivisionError: # good to sepcify it
  print("Div by 0")
except: # to brord 
  print("Invalid input")


pyfile = open("python101.py","r") # to open a file as r = read, w write, r+ read and write, a append
#print(pyfile.readable()) # to check the file s reable 
#print(pyfile.read()) # to actually read all info
#print(pyfile.readline()) # to read the 1st line
#print(pyfile.readline()) # to read the 2nd line, 
#print(pyfile.readlines()) # to put every line in alist array
#print(pyfile.readlines()[2]) # to access the line in the list
for item in pyfile.readlines():
  print(item) # we can loop over the lines
