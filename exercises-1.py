'''
Basics
•1. Write a Python function to find the Max of three numbers - max(a, b, c).	 

•2. Write a Python function to compute the factorial of a number factorial(n). Factorial of 5 is 5 *
4 * 3 * 2 * 1 = 120, etc. If the number given is negative, the function should return None.
• 3. Bob the teenager
• Bob is a lackadaisical teenager. In conversation, his responses are very limited.
Bob answers 'Sure.' if you ask him a question, such as "How are you?".
He answers 'Whoa, chill out!' if you YELL AT HIM (in all capitals).
He answers 'Calm down, I know what I'm doing!' if you yell a question at him.
He says 'Fine. Be that way!' if you address him without actually saying anything.
He answers 'Whatever.' to anything else.
Implement the response function:
def response(hey_bob):
 	 	 pass
4. Students
We have a dictionary with the results of various students:
students = { "Bob": 12, "Sue": 10, "Joe": 14, "Sally": 8, "Sarah": 18}
We'll create several function that can work on such a dict. Remember the values are just an
example - your functions should be able to work with any dict following that structure.
Define the following functions:
• best_student(students) that output the name of the student with the best result
• grade_students(students) that output a list of students, from the best result to the worse one
• success_students(students) that output a dict with only the students that have 12 or more
'''

#declare three numbers to values a b and c 

# a = 10
# b = 14
# c = 12
# def maximum(a, b, c):
  
#     if (a >= b) and (a >= c):
#         max = a
#     elif (b >= a) and (b >= c):
#         max = b
#     else:
#         max = c    
#     return max
  
# print(maximum(a, b, c))

# Exercise 2 
# 1. Solution use the in built factorial 

# def factorial(n):
#     if n < 0:
#         return(f'n is none')
#     if n < 2:
#         return 1
#     return n * factorial(n - 1)

# print(factorial(n=-8))

#There is also an inbuilt Math factorial 

# import math  
# def factorial_func(n): 
#     if num < 0:
#         return(f'none') 
#     return(math.factorial(n))  
  
# num = int(input("Enter a number:")) 
# f = factorial_func(num)  
# print("Factorial of", num, "is", f)  

#Exercise 3 

# def response(hey_bob):
#     if len(hey_bob) == 0:
#         print('Fine. Be that way!')
#     elif (hey_bob ==  hey_bob.upper()) and hey_bob[-1] == '?':
#         print('Calm down, I know what I\'m doing!' )
#     elif hey_bob ==  hey_bob.upper():
#         print('Whoa, chill out!')
#     elif hey_bob == "How are you?":
#         print('Sure.')
#     else: 
#         print('Whatever.')
    
# response('How are you?')
# response("AH")


# Exercise 4 
# Exercise 4.1 output the name of the student with the best result


students = { "Bob": 12, "Sue": 10, "Joe": 14, "Sally": 8, "Sarah": 18}

# def best_student(students):
# 	max_scores = max(students.values())
# 	print(max_scores)

# best_student(students)

# def best_student_name(students):
# 	max_value = max(students, key=students.get)
# 	print(max_value)

# best_student_name(students)

# Exercise 4.2

# def grade_students(students):
# 	for key, value in sorted(students.items(), 
#                             key=lambda item: item[1],
#                             reverse=True):
# 		print(key, '::', value)

# grade_students(students)

# for lowest to highest 
# sorted_values = sorted(students.values()) 
# sorted_dict = {}

# for i in sorted_values:
#     for k in students.keys():
#         if students[k] == i:
#             sorted_dict[k] = students[k]
#             break
# print(sorted_dict)


# Exercise 4.3

# def success_students(students):
# 	new_students = {}
# 	for(key, value) in students.items():
# 		if value > 12:
# 			new_students[key] = value 
# 	print(new_students)

# success_students(students)


