# --------------
# Code starts here
import string 
# Create the lists 
class1 = ['Geoffrey, Hinton, Andrew Ng, Sebastian Raschka', 'Yoshua Bengio']
class2 = ['Hilary Mason','Carla Gentry', 'Corinna Cortes']

# Concatenate both the strings
new_class = class1 + class2
print(new_class)

# Append the list
new_class.append('Peter Warden')

# Print updated list
print(new_class)

# Remove the element from the list
new_class.remove('Carla Gentry')

# Print the list

print(new_class)



# Create the Dictionary

courses = {'Math' : 65, 'English' : 70, 'History' : 80, 'French' : 70, 'Science' : 60}
print(courses)

# Slice the dict and stores  the all subjects marks in variable
# marks = courses.values()
# print(marks)

marks = []

for p in courses.values():
    marks.append(p)

print(marks)

# Store the all the subject in one variable `Total`
total = 0

for p in courses.values():
    total = total + p 

# Print the total
print(total)

# Insert percentage formula
percentage = (total * 100) /500

# Print the percentage
print(percentage)



# Create the Dictionary
 
mathematics = {'Geoffrey Hinton' : 78, 'Andrew Ng' : 95, 'Sebastian Raschka' : 65, 
'Yoshua Bengio': 50, 'Hilary Mason' : 70, 'Corinna Cortes' : 66, 'Peter Warden' : 75 }

print(mathematics)

# Given string
max_marks_scored = max(courses, key = courses.get)
print(max_marks_scored)

topper = max(mathematics, key = mathematics.get)
print(topper)

# Create variable first_name 
first_name = (topper.split()[0])

# Create variable Last_name and store last two element in the list
last_name = (topper.split()[1])

# Concatenate the string
full_name = last_name + ' ' + first_name

# print the full_name
print(full_name)

# print the name in upper case

print(full_name.upper())

certificate_name = full_name.upper()
print(f'certificate_name is ' + "'" + certificate_name + "'." )
# print(certificate_name)


# Code ends here


