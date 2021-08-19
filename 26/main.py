numbers = [1, 1, 2, 3, 5, 8, 13, 21]
squared_numbers = [n**2 for n in numbers]
even_numbers = [n for n in numbers if n%2 == 0]

file1_list = []
file2_list = []

with open("file1.txt") as file1:
    data = file1.read()
    for i in data:
        file1_list.append(i)
new_file1_list = [int(n) for n in file1_list if n != "\n"]

with open("file2.txt") as file2:
    data = file2.read()
    for i in data:
        file2_list.append(i)
new_file2_list = [int(n) for n in file2_list if n != "\n"]

result = [int(n) for n in file1_list if n in file2_list and n != "\n"]
print(result)





