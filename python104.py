try:
  10/0
  num = int(input("Insert a number: "))
  print(num)

except ZeroDivisionError: # good to sepcify it
  print("Div by 0")
except: # to brord 
  print("Invalid input")


pyfile = open("python101.py","a") # to open a file as r = read, w write, r+ read and write, a append
#print(pyfile.readable()) # to check the file s reable 
#print(pyfile.read()) # to actually read all info
#print(pyfile.readline()) # to read the 1st line
#print(pyfile.readline()) # to read the 2nd line, 
#print(pyfile.readlines()) # to put every line in alist array
#print(pyfile.readlines()[2]) # to access the line in the list
for item in pyfile.readlines():
  print(item) # we can loop over the lines
pyfile.close() # good practice to close it


python101.py.write("\nBella is lela tarik")   # note: using a(append)each time we run the program it will add it to the file and \n to make it on new line
# using "w", it will replace all the content of the file with the new value we write and if we choose to open new file name, it will create a file for it with the value added, u can use diffrent file types like .html
