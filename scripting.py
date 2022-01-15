# Take Input from User

# name = input("Enter your name: ")
# print("Hello there, {}!".format(name.title()))

# num = int(input("Enter an integer "))
# print("hello" * num)



# Generate Mesages
# Ask for user input 3 times. Once for a list of names, once for a list of missing assignment counts, and once for a list of grades. Use this input to create lists for names, assignments, and grades.
# Use a loop to print the message for each student with the correct values. The potential grade is simply the current grade added to two times the number of missing assignments.

# names = input("Enter names: ").title().split()
# assignments = input("Enter assignments: ").split()
# grades = input("Enter grades: ").split()

# message = "Hi {},\n\nThis is a reminder that you have {} assignments left to \
# submit before you can graduate. Your current grade is {} and can increase \
# to {} if you submit all assignments before the due date.\n\n"

# for n, a, g in zip(names, assignments, grades):
#     print(message.format(n, a, g, int(g) + int(a)*2))



# Handling Input Errors
# The party_planner function below takes as input a number of party people and cookies
# Edit the party_planner function to handle this invalid input

# def party_planner(cookies, people):
#     leftovers = None
#     num_each = None

#     try:
#         num_each = cookies // people
#         leftovers = cookies % people
#     except ZeroDivisionError:
#         print("Oops, you entered 0 people will be attending.")
#         print("Please enter a good number of people for a party.")

#     return(num_each, leftovers)



# Write a function called create_cast_list that takes a filename as input and returns a list of actors' names.

# def create_cast_list(filename):
#     cast_list = []

#     with open(filename) as f:
#         for line in f:
#             name = line.split(",")[0]
#             cast_list.append(name)

#     return cast_list

# cast_list = create_cast_list('/Users/atam/Code/programming_for_ds/flying_circus.txt')

# for actor in cast_list:
#     print(actor)



# Create a function that opens the flowers.txt, reads every line in it, and saves it as a dictionary

# create function with a flower dictionary

def create_flower_dict(filename):
    flower_dict = {}
    with open(filename) as f:
        for l in f:
            letter = l.split(",")[0].lower()
            flower = l.split(",")[1].strip()
            flower_dict[letter] = flower
    
    return flower_dict

# create function that asks for user input

def main():
    flower_d = create_flower_dict('flowers.txt')
    full_name = input("Enter your First name only: ")
    first_name = full_name[0].lower()
    first_letter = first_name[0]

    print("Unique flower name with first letter: {}".format(flower_d[first_letter]))

main()