'''
1.Print the digits in a number
2.How to count no of Digits in a number
3.Print '*' insted of vowels in a string
4.How to find out the number of factors for a number
5.Print the sum of the digits in a number
6.print the first 10 fibbanocci series numbers
7.prime number
'''
# num=1234
# while num>0:
#     res=num%10
#     print(res)
#     num//=10

# num=1234
# count=0
# while num>0:
#     res=num%10
#     # print(res)
#     num//=10
#     count+=1
# print(count)    

# vowels='aeiouAEIOU'
# s=input('Enter the string: ')
# i=0
# while i<len(s):
#     if s[i] in vowels:
#         print('*',end='')
#     else:
#         print(s[i],end='')    
#     i+=1    

# num=int(input('Enter a number: '))
# i=1
# while i<=num:
#     if num%i==0:
#         print(i,'is a factor of a number')
#     i+=1

# num=1234
# sum=0
# while num>0:
#     res=num%10
#     # print(res)
#     num//=10
#     sum+=res
# print(sum)

# a=0
# b=1
# i=1
# while i<11:
#     print(a)
#     c=a+b
#     a=b
#     b=c
#     i+=1

# num=int(input('Enter the number: '))
# count=0
# i=1
# while i<=num:
#     if num%i==0:
#         count+=1
#     i+=1
# else:
#     if count==2:
#         print(num,' is a prime number') 
#     else:
#         print(num,'is not a prime number')           