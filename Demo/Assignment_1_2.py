#Wap to input 3 digit number , reverse it and also find the sum of a digit of a number ?
#Hint :-
#num=123
#rev=321
#sum=6

num=input("Enter number to reverse and sum : ")
print(num[2],num[1],num[0])
print("Sum of digit : ", int(num[0]) + int(num[1]) + int(num[2]))