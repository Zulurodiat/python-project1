 
# greeting = "Hello World!"

# for g in range(5):
#     print(greeting)


# count = 0
# while count < 5:
#     print("Hello World!")
#     count = count + 1


# fruit = ["banana", "mango", "orange", "apple"]
# print(len(fruit))

# my_dictionary = {
#     "name": "Rodiat",
#     "age": 12,
#     "hubby": "baking"
# }
# print(my_dictionary)
# print(my_dictionary["name"])


file = open("justice.txt", "w")
file.write("Hello, my name is Nuur!\n")
file.close()

with open("justice.txt", "a") as file:
    file.write("I am 20 years old\n")

