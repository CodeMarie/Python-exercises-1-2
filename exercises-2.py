'''
List Comprehension exercises
1. - Write a Python program to check if the elements in list are unique or not:
	 

- Original list: [1, 2, 3, 1 , 5, 80, 80, 90, 4, 5, 8, 9, 10]
2. Write a Python program to calculat the average of two lists:
	 	 Original list: [1, 10, 7, 3, 8]
	 	 	 [0, 9, 80, 4, 1]
3. Square the even numbers in mylist and store the result in a evenlist:
 mylist = [2, 10, 5, 8, 7]
'''

#Exercise 1. 

# original_list = [1, 2, 3, 1 , 5, 80, 80, 90, 4, 5, 8, 9, 10]

#check true or falsy that if unique items are present only or not
# def all_unique(list):
#   return len(list) == len(set(list))

# print(all_unique(original_list))

#List comprehension 

# def only_unique(original_list):
#     unique = []
#     [unique.append(number) for number in original_list if number not in unique]
#     print(unique)

# only_unique(original_list)

#Exercise 2

# Original_list: [1, 10, 7, 3, 8]
	 	 	 

# Example to find average of list
# number_list = [0, 9, 80, 4, 1]
# avg = sum(number_list)/len(number_list)
# print("The average is ", round(avg,2))

#To find average of two lists 

lst_a= [1, 10, 7, 3, 8]
lst_b= [0, 9, 80, 4, 1]

#abs returns absolute value from argument, zip(iterables) yields tuples until an input is exhausted


diff = [abs(x-y) for x, y in zip(lst_a, lst_b)]  # find index-wise differences
print(sum(diff)/len(diff))    # divide sum of differences by total

# list concatenation could be used also lsts = lst_a + lst_b

# Exercise 3

mylist = [2, 10, 5, 8, 7]
squared_even_list = [ num ** 2 for num in mylist if num % 2 == 0 ]
print(squared_even_list)