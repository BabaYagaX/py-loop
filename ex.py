string = input("Enter a Word: ")
count = 0
if 'a' in string or 'A' in string:
  count = count + 1
if 'e' in string or 'E' in string:
  count = count + 1
if 'i' in string or 'I' in string:
  count = count + 1
if 'o' in string or 'O' in string:
  count = count + 1
if 'u' in string or 'U' in string:
  count = count + 1

if count == 0:
  print("There are no vowels in the string")
elif count == 1:
  print("There is {} vowel in the string".format(count))
else:
  print("There are {} vowels in the string".format(count))
