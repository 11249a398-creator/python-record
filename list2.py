# List slicing operations
my_list = ['p', 'r', 'o', 'g', 'r', 'a', 'm', 'm', 'e']
print(my_list[2:5])      # Elements from index 2 to 4
print(my_list[5:])       # Elements from index 5 to end
print(my_list[:])        # Entire list

# List methods
list1 = [10, 15, 11, 65, 30]
list1.insert(1, 80)
print('INSERTED ELEMENT IN THE LIST :', list1)

list1.sort()
print('SORTED ELEMENT IN THE LIST IS :', list1)

list1.reverse()
print('REVERSED ELEMENT IN THE LIST IS :', list1)

removed_element = list1.pop(3)
print('REMOVED ELEMENT FROM THE LIST IS :', removed_element)
print('LIST AFTER REMOVAL :', list1)

print('LARGEST ELEMENT IN THE LIST IS :', max(list1))
print('SMALLEST ELEMENT IN THE LIST IS :', min(list1))
