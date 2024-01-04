"""
.       - Any Character Except New Line
\d      - Digit (0-9)
\D      - Not a Digit (0-9)
\w      - Word Character (a-z, A-Z, 0-9, _)
\W      - Not a Word Character
\s      - Whitespace (space, tab, newline)
\S      - Not Whitespace (space, tab, newline)

\b      - Word Boundary
\B      - Not a Word Boundary
^       - Beginning of a String
$       - End of a String

[]      - Matches Characters in brackets
[^ ]    - Matches Characters NOT in brackets
|       - Either Or
( )     - Group

Quantifiers:
*       - 0 or More
+       - 1 or More
?       - 0 or One
{3}     - Exact Number
{3,4}   - Range of Numbers (Minimum, Maximum)


#### Sample Regexs ####

[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+
"""
import re
#pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')# all phone nums with any character in the middle
#pattern = re.compile(r'\d\d\d[-]\d\d\d[-]\d\d\d\d') # phone nums with only - in the middle (we dont need to escape\ the charaters one they are in [])
#pattern = re.compile(r'\d\d\d[-.]\d\d\d[-.]\d\d\d\d') #phone nums with - OR . characters in the middle(Note onece it find one character it ignores the other, it only match one character in the set[])
#pattern = re.compile(r'[89]00[-]\d\d\d[-]\d\d\d\d') # phone nums that start with 800 or 900
pattern = re.compile(r'\d{3}[-]\d{3}[-]\d{4}') # instead of writing every digit, we can use quntifiers to specify howmany times a character exist
#pattern = re.compile(r'[1-5]') # when the - is in middle of characters it tells the range in this case 1 to 5, or [a-zA-Z] (the range of all lower or uper case letters). if its in the beginning or ending it find the character - litrally
#pattern = re.compile(r'[^a-zA-Z]') #if we use the carat^ before the set ^[], all characters that start in the charcters in the set. if it is inside the set[^ ] it negates, i.e. all character that NOT start in the character set
with open('data.txt', 'r') as f:
  contents = f.read()
  matches = pattern.finditer(contents)
  for match in matches:
    print(match)
