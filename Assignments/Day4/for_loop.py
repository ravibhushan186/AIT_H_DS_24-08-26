# 1.Print the digit in a number
# num = int(input("Enter a number: "))
# for digit in str(num):
#     print(digit)
#2.How to count no. of digit

# num = int(input("Enter a number: "))
# count = 0
# for digit in str(num):
#     count = count + 1
# print("Number of digits:", count)

# 3.print("*") insted of vowels in a string

# s = input("Enter a string: ")
# for ch in s:
#     if ch in "aeiouAEIOU":
#         print("*", end="")
#     else:
#         print(ch, end="")

#  4.How to find a number of factors for num

# num = int(input("Enter a number: "))

# print("Factors of", num, "are:", end=" ")

# for i in range(1, num + 1):
#     if num % i == 0:
#         print(i, end=" ")

# 5.print the sum of digit in a number

# num = int(input("Enter a number: "))

# sum = 0

# for digit in str(num):
#     sum = sum + int(digit)

# print("Sum of digits:", sum)

# 6.print the first 10 fibbonacci(0,1,1,2,3,5,8,13,21,34.....) number

# a = 0
# b = 1

# for i in range(10):
#     print(a, end=" ")
    
#     c = a + b
#     a = b
#     b = c

#  7.prime number 

# num = int(input("Enter a number: "))

# count = 0

# for i in range(1, num + 1):
#     if num % i == 0:
#         count = count + 1

# if count == 2:
#     print("Prime Number")
# else:
#     print("Not a Prime Number")

#  8.print whether a number is even or odd

# num = int(input("Enter a number: "))

# if num % 2 == 0:
#     print("Even Number")
# else:
#     print("Odd Number")

# 9.print the prime number from 1 to 100

# for num in range(2, 101):

#     count = 0

#     for i in range(1, num + 1):
#         if num % i == 0:
#             count = count + 1

#     if count == 2:
#         print(num, end=" ")