def say_hi(name, age):
  return 'Hello, ' + "i'm, " + str(name),  str(age)

print(say_hi("Abel",29))


for i in "Bella is Chis":
  print(i)

nums = [2,6,5,9]
for i in nums:
  print(i)

for i in range(2,5):
  print(i)

friends = ["ABD", "Aman", "Ashe", "Faya"]
for i in range(len(friends)):
  print(friends[i])


two_d_nums = [[1,2],["a","b"]]
print(two_d_nums[1][1])
for first in two_d_nums:
  for second in first:
    print(second)


user_in = input("Insert a word: ")

def translate(phrase):
  translation = ""
  for letters in phrase:
    if letters in "Aa":
      translation = translation + "za"
    elif letters in "Ee":
      translation = translation + "ze"
    elif letters in "Ii":
      translation = translation + "zi"
    elif letters in "Oo":
      translation = translation + "zo"
    elif letters in "Uu":
      translation = translation + "zu"
    else:
      translation = translation + letters
  return translation

print(translate(user_in))


