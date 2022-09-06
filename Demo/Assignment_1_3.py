#Assignment 1 Part 3
#Wap to input 5 subject marks and find there total,percentage and grade ?
#per>=80 A 
#per>=60 B 
#per>=45 C 
#Fail 

print("Please enter marks for below 5 subjects")
sub1=int(input("English : "))
sub2=int(input("Hindi : "))
sub3=int(input("Maths : "))
sub4=int(input("Science : "))
sub5=int(input("Geography : "))

total = sub1+sub2+sub3+sub4+sub5
percent = (sub1+sub2+sub3+sub4+sub5)/5
grade = ""

if percent >= 80:
    grade = "A"
elif percent >= 60:    
    grade = "B"
elif percent >= 45:    
    grade = "C"
else:
    grade = "Fail"

print("Total : ", total)
print("Percent : ", percent)
print("Grade : ", grade)