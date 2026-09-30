# Program Name: Assignment2.py
# Course: IT3883/Section W01
# Student Name: Jared Abbott
# Assignment Number: Lab 2
# Due Date: 10/02/2026
# Purpose: To list who has the highest grades in descending order
# List: https://www.geeksforgeeks.org/python/python-list-sort-method/
# https://www.geeksforgeeks.org/python/find-average-list-python/#google_vignette
# Mom Helped me 
#Bob 100 34 25 22 76 87
#Jack 43 54 99 63 101 44
#Jane 78 98 45 74 65 23
#Pete 99 65 101 56 33 47
#Ann 78 21 22 101 44 100
#Alice 100 102 89 99 92 85
#John 45 66 99 99 89 78
#Ben 45 85 99 99 89 88
#Henry 45 12 78 98 65 32
names = ["Bob ", "Jack ", "Jane ", "Pete ", "Ann ", "Alice ", "John ", "Ben ", "Henry "]
num0 = [100,34,25,22,76,87]
num1 = [43,54,99,63,101,44]
num2 = [78,98,45,74,65,23]
num3 = [99,65,101,56,33,47]
num4 = [78,21,22,101,44,100]
num5 = [100,102,89,99,92,85]
num6 = [45,66,99,99,89,78]
num7 = [45,85,99,99,89,88]
num8 = [45,12,78,98,65,32]
average = sum(num0)/len(num0)
average1 = sum(num1)/len(num1)
average2 = sum(num2)/len(num2)
average3 = sum(num3)/len(num3)
average4 = sum(num4)/len(num4)
average5 = sum(num5)/len(num5)
average6 = sum(num6)/len(num6)
average7 = sum(num7)/len(num7)
average8 = sum(num8)/len(num8)
bobavg = str(round(average,2)) + " Bob"
jackavg = str(round(average1)) + " Jack"
janeavg = str(round(average2,2)) + " Jane"
peteavg = str(round(average3,2)) +" Pete"
annavg =  str(round(average4,2)) + " Ann"
aliavg = str(round(average5,2)) + " Alice"
johnavg = str(round(average6,2)) + " John"
benavg = str(round(average7,2)) + " Ben"
henavg =  str(round(average8,2)) + " Henry"
namesaverge = [bobavg,jackavg,janeavg,peteavg,annavg,aliavg,johnavg,benavg,henavg]
namesaverge.sort(reverse=True)
print(namesaverge)


