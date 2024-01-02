nums_id = [2,3,6,7]
friends = ["ABD", "Faya","Faya", "Aman","Aman", "Ashe"] # list of any info, strings, nums, boolean and they each can be accessed through index
print(friends[0:2]) # to access the 1st 2 values (index 2 is not included)
friends[3] = 'Adam' # we can replace values 
print(friends) # and it is updated
friends.extend(nums_id) # extends the values from other list to the end of a list
print(friends) # merged values 
friends.append("Boka") # to add individual elements to the end of the list
friends.insert(0,"Nahom") # to add elements at specified place 
print(friends)
friends.remove("Nahom") # to remove a value from the list 
#friends.clear() #will remove all values
friends.pop() # removes the last element from the list
print(friends)
print(friends.index("Aman")) # tells the index of the value in the list
print(friends.count("Faya")) # counts how many times a value apear in a list
nums_id.sort() # in ascending order
nums_id.reverse() # it just the reverse the order of the values in a list
print(nums_id)
nums_id2 = nums_id.copy # it copys a value to other
print(nums_id2)


friends_for_life = ("ABD", "Aman", "Ashe", "Faya", "Boka", "Adam",) #tuples - can not be alterd(imutable) also common for coordinates 