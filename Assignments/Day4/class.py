
# 1.Print the digit in a number

# num = 1234
# i=0
# while num > 0:
#     res = num % 10
#     print(res)
#     num //=10
    
# 2.How to count no. of digit

# num = 1234
# count=0
# while num >0:
#     num=num //10
#     count=count+1
# print(count)

# 3.print("*") insted of vowels in a string

# vowels = 'aeiouAEIOU'
# n = str(input("Enter the string: "))
# i=0;
# while i < len(n):
#     if n[i] in vowels:
#         print('*', end="")
#     else:
#         print(n[i], end="")
#     i+=1

# 4.How to find a number of factors for num

num = int(input("Enter a number: "))
i = 1
while i <= num:
    if num % i == 0:
        print(i,"is the factor of ",num)
    i += 1

# 5.print the sum of digit in a number

# num = 1234
# sum = 0
# while num > 0:
#     result = num % 10
#     sum += result
#     num=num//10
# print(sum)


# 6.print the first 10 fibbonacci(0,1,1,2,3,5,8,13,21,34.....) number

# a=0
# b=1
# c=0
# while c < 11:
#     print(a, end="\n ")
#     d=a+b
#     a,b=b,d
#     ## a=b
#     ## b=d
#     c+=1
# ## print(d)

# 7.prime number 

# p = 0
# i = 1
# num = int(input("Enter the number: "))
# while i <= num:
#     if num % i == 0:
#         p = p+1
#     i = i+1
# if p == 2:
#     print("Prime Number ")
# else:
#     print("Not a Prime Number")

# 8.print whether a number is even or odd

# num = int(input("Enter the number: "))

# while num >= 0:
#     if num % 2 == 0:
#         print("Even number")
#     else:
#         print("Odd number")
#     break

# 9.print the prime number from 1 to 100

# num = 1
# while num <= 100:
#     p=0
#     i=1

#     while i <= num:
#         if num % i == 0:
#             p=p+1
#         i=i+1
#     if p == 2:
#         print(num)
#     num = num+1