Student Grading System

A simple Python grading system that checks a student's mark and prints the corresponding grade classification.

📌 Features
Detects invalid marks
Displays grade categories based on score ranges
Uses Python if, elif, and else statements
Beginner-friendly project
🖥️ Code
mark = 40

if 100 <= mark <= 101:
    print("error")

if 75 <= mark <= 100:
    print("Distinction")

elif 60 <= mark < 75:
    print("pass")

elif 50 <= mark < 69:
    print("credit")

elif 35 <= mark < 49:
    print("almost")

elif 20 <= mark < 35:
    print("fail")

elif 0 <= mark < 20:
    print("ungraded")

else:
    print("error")
📊 Grade Categories
Marks Range	Result
75 - 100	Distinction
60 - 74	Pass
50 - 68	Credit
35 - 48	Almost
20 - 34	Fail
0 - 19	Ungraded
▶️ How to Run
Install Python
Save the file as grading.py
Run the program:
python grading.py
📚 Learning Objectives

This project helps beginners understand:

Conditional statements
Comparison operators
Python syntax
Program flow control
