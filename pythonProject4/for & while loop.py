# ex : dictionary and format
student = {"name ": "abdul","age": 19, "dep ":"bca"}

for key,value in student.items () :
    print(f"{key.capitalize() }:{value}")

#list of squares
squares = [x**2 for x in range(1,10)]
print(squares)

#count frequency of each letter
text ="banana"
freq ={}

for char in text:
    freq[char] = freq.get(char,0) + 1
print(freq) # ?

#2d list and find the sum
matrix =[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
for row in matrix:
    row_sum = sum(row)
    print("row sum :",row_sum )
    
#use enumerate to get index
colors = ["red","yellow","violet"]

for index ,color in enumerate (colors):
    print(f"{index + 1}  {color}")

#nested loop
for i in range(1,5):
    print()
    for j in range(1,i +1):
        print(end = "*")


print("\nwhile loop\n")

#while loop

#add natural num
i = 1
total = 0

while i <=10 :
    total += i
    i +=1
print(total)

#count down
count = 5

while count >0:
    print("count down :",count)
    count = count -1

# user input unit they type exit

user_input = ""

while user_input != "exit":
    user_input =input ("type anything or enter 'exit' to quit")
    print("you typed ",user_input)

# user input unit they type exit

user_input = ""

while user_input != "exit":
    user_input =input ("type anything or enter 'exit' to quit")
    print("you typed ",user_input)