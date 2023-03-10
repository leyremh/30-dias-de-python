list = () 

fruits = ['naranja', 'banana', 'fresa', 'melon', 'manzana']
print(fruits)
print(len(fruits))

first_fruits = [0]
third_fruits = [2]
last_fruits = [4]
print(first_fruits)
print(third_fruits)
print(last_fruits)
 
mixed_data_types = ['Leyre',16, 1.53, 'con novio', 'Jerez']

it_compaines = [ 'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print(it_compaines)

print(len(it_compaines))

first_fruits = [0]
middle_company = [3]
last_company = [6]

it_compaines[0] = 'Instagram'
print(it_compaines)

it_compaines.append('Nokia')

it_compaines.insert(4, 'LG')

it_compaines[0] = it_compaines[0].upper()

it_compaines = '#it_compaines'

does_exit = 'Google' in it_compaines
print(does_exit)

it_compaines.sort()
print(it_compaines)

it_compaines.sort(reverse=True)
print(it_compaines)

INSTAGRAM, Google, Microsoft = it_compaines[0:2]
Oracle, Amazon, Nokia = it_compaines[6:8]
Apple, IBM, LG = it_compaines[3:5]

it_compaines.remove(INSTAGRAM)
it_compaines.pop(3)
it_compaines.pop(4)
it_compaines.pop(5)
del it_compaines
it_compaines.clear()

front_end = ['HTML','CSS','JS' 'Redux']
back_end = ['Node', 'Express', 'MongoDB']

full_stack = front_end
print(full_stack)
full_stack.insert(5,"Python")

full_stack[5] = "Python"





