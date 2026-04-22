

text = input()
charList = []

for char in text:
    charList.append(ord(char))
charList.sort()

newString = ""
for char in charList:
    newString += chr(char)

print(newString)