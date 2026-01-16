
def first_occurence_of_string(main_string, sub_string):
    index = main_string.find(sub_string)
    return index

main_string = input("Enter the main string: ")
sub_string = input("Enter the substring to find: ")
result = first_occurence_of_string(main_string, sub_string)
print("The index of the first occurrence is:", result)