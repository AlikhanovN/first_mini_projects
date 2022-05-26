'''
Task 1 - Aidana
Task 2 - Aidana
Task 5 - Aidana
'''

print("Task 3")
a = 4729461084
counter = 0
while a:
    counter += a % 10
    a //= 10
print(counter)

print("Task 4")
data = input("Data format (2020-10-24 18:30): ")
time = data.split(" ")[1]
new_data = data.split(" ")[0].split("-")
print(new_data.extend(time))
data_dict = {}
data_dict["year"] = new_data[0]
data_dict["month"] = new_data[1]
data_dict["day"] = new_data[2]
data_dict["time"] = time
print(data_dict)

print("Task6")
print("mkdir -p new/new2")

print("Task7")
print("cd ~alikhanov/Desktop/")

print("Task8")
