# file= open("abc.txt")
# print(file.read())
# activity 2
# file= open("abc.txt", "r")
# print(file.read())
# file= open("abc.txt", "a")
# file.write("sky")
# file.write("sky")
# activity 3
file= open("abc.txt", "r")
counter= 0
content= file.read()
list= content.split("\n")
for i in list:
    if i:
        counter+=1
print(counter)