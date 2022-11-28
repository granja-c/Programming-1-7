text = input("Enter text:")
numwords = 0
for index in range(len(text)):
  print(text[index], end=" ")
print()
for letter in text:
  if letter == " ":
    numwords += 1
  print(letter)
print("The number of words is: ", numwords + 1)