 Program Name: Assignment1.py (use the name the program is saved as)
# Course: IT3883/Section WO1
# Student Name: Jared Abbott
# Assignment Number: Lab 1
# Due Date: 09/22/ 2026
# Purpose: The purpose of this assignment is to have the user append as many words that they want into python. Morever, end the inputting whenever they so choose
# List: My mother is good at python, so help me quite a bit
# Professor module powerpoints
# Code_Academy Learn Python 2 course https://www.codecademy.com/enrolled/courses/learn-python
# free_Code_Camp_Python https://www.freecodecamp.org/learn/learn-python-for-beginners/#object-oriented-programming-with-python
# W3 Python While Loops https://www.w3schools.com/PYTHON/python_while_loops.asp
# W3 Python if-elif-else statements https://www.w3schools.com/Python/python_conditions.asp
# W3 Python None Keyword https://www.w3schools.com/python/ref_keyword_none.asp
# W3 Python Break Keyword https://www.w3schools.com/python/ref_keyword_break.asp
print("Please pick one of four options:\n Option 1: will ask you for a string\n Option 2: will clear any input that was submitted\n Option 3: will display the string that was inputted by the user\n Option 4: will exit this program")
user_input = []
while True:
    num = int(input("Enter a number between 1 and 4: "))
    if 1 == num:
     print("What string would you like to enter ")
     user_input.append(input("Enter a string: "))
    elif 2 == num:
       user_input = None
    elif 3 == num:
       print(user_input)
    else:
       print("Program Exited")
       break
       <img width="1920" height="1080" alt="PycharmAssignmnt1Screenshot" src="https://github.com/user-attachments/assets/ad0e04e4-83c0-4802-ac14-06009f8d2f29" />

