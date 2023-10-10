print("Hello teacher give me the grades of your students, I ")

for i in range(int(input("How many students are there? "))):
    print("grades ", i + 1, ": ")
    grades = []
    for j in range(int(input("How many grades are there? "))):
      grades.append(float(input("Grade: ")))
    print("The average of the grades is: ", sum(grades) / len(grades))
  
print("Thank you for using this program")
    
