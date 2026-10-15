'''
Q1. Sum of digits
Input: 5832
Output: 18
'''
num=int(input("Enter you input: "))
sum=0
while num > 0:
    digit = num % 10
    sum = sum + digit
    num = num // 10
print(sum)