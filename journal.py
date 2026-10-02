entries = ["My name is nuur!\n", "I am 21 years old\n", "I love to bake\n"]

for entry in entries:
    with open("journal.txt", "a") as file:
        file.write(entry)


count = 0
with open("journal.txt", "r") as file:
    data = file.read()
    print(data)
    

for char in data:
    if char == '\n':
        count+=1

print(count)
