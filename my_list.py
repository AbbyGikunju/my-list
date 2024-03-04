#empty list
my_list = []

#appending these elements to my list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

#inserting a value at the second position 
my_list.insert(1,15)

#extending my list with another list
my_list.extend([50,60,70])

#remove the last element from my list
del my_list[-1]

#sort my list in ascending order
my_list.sort()

#find and print the index of the value 30 in my list
index_of_30 = my_list.index(30)
print("Index of 30 is:", index_of_30 )

print(my_list)