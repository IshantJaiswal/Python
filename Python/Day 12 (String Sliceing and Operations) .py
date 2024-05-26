fruit = "Mango"
mangoLen = len(fruit)
print(mangoLen)
# print(fruit[0:4])
# including 0 but not 4
# print(fruit[1:4]) 
# including 1 but not 4
# print(fruit[:5])
# print(fruit[0:-3])
print(fruit[:len(fruit)-3])
# when there is a colon (:) then it will automatically take it 0
# but when there is no semicolon (:) then it will print that particular character 
print(fruit[-1:len(fruit) - 3])
print(fruit[-3:-1])