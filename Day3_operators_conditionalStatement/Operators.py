'''
1.Arithmetic Operators

+ addition
- subtraction
* multiplication
/ division
% modulus
** exponentiation
// floor division

## Example

x = 15
y = 4

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)
print(x ** y)
print(x // y)

2.Comparison (Relational) Operators

== equal to
!= not equal to
<  less than
> greater than
<= less than or equal to
>= greater than or equal to

## Example
x = 5
y = 3

print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)

3.Logical Operators

and
or
not

x = 5

print(x > 0 and x < 10) #True
print(x > 0 or x < 10) #True
print(not x > 0) #False

4.Identity Operators

is

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)
print(x is y)
print(x == y)

is not

x = ["apple", "banana"]
y = ["apple", "banana"]

print(x is not y)


5.Membership Operators

in

print('a' in ''aeiou') #True
print('b' in 'aeiou') #False

not in

print('a' not in 'aeiou') #False
print('b' not in 'aeiou') #True

6.Bitwise Operators

&

The & operator compares each bit and set it to 1 if both are 1, otherwise it is set to 0
6 = 0110
3 = 0011
 --------
2 = 0010

print(6 & 3) # 2

|

The | operator compares each bit and set it to 1 if one or both is 1, otherwise it is set to 0
6 = 0110
3 = 0011
--------
7 = 0111

print(6 | 3) # 7

^

The ^ operator compares each bit and set it to 1 if only one is 1, otherwise it is set to 0
6 = 0110
3 = 0011
--------
5 = 0101

print(6 ^ 3) # 5

<<
>>



7.Assignment Operators

=

# Assignment Operator 
a = 3
b = 5

c = a + b 
print(c)

+=

a = 3
b = 5
a += b # a = a + b

print(a)

a = 10
a -= 5 # a = a - 5
print(a)

a = 3
a *= 5 # a = a * 5
print(a)

a = 10
a /= 2 # a = a / 2
print(a)

a = 10
a %= 3 # a = a % 3
print(a)

a = 2
a **= 3 # a = a ** 3
print(a)

a = 10
a //= 3 # a = a // 3
print(a)

'''
