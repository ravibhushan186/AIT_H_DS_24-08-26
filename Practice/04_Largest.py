'''
Q4. Find largest of three numbers
Take three numbers and find the largest without using max().

'''
a=int(input("Enter 1st number: "))
b=int(input("Enter 1st number: "))
c=int(input("Enter 1st number: "))

if a>b:
    largest=a
else:
    largest=b
if c > largest:
    largest =c
print(largest)