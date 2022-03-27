introduction = input("Enter introduction.. ")
count = 0
wordCount = 1
print(introduction)
for intro in introduction:     
    count = count + 1
    if(intro == " "):
        wordCount = wordCount + 1
print(count)
print(wordCount)