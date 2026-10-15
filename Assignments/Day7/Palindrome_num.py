#121
s=0
n = int(input("Enter a number: "))
m = n
while n > 0:
    r = n % 10
    s=s*10+r
    n=n//10
if m == s:
    print("Number is Palindrome ")
else:
    print("Number is not a palindrome")