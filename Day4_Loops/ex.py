'''
conditional Looping:
While loop is known as centianal loop
For is known as foreach loop sequence

while True:
    print("Hello world") # ctrl+C to stop the loop

    i=0
    while i < 11:
        print(i)
        i += 1

    i=10
    while i>0:
        print(i)
        i -= 1

    python is easy to learn
    01234567891011121314 (squential)

    negative index
    -1-2-3-4-5-6...

    subscript
    s='Python is easy to learn'

    print(s[0]) #it will print p

    lenth Method

    print(len(s)) ##23

    i=0
    while i<len(s): ##
    print(s[i])
    i+=1

    Range method

    print(list(range(11))) ## single var is considerd as stop value Default starting value is 0
     print(list(range(1,11))) ## starting value , stop value default step=1
      print(list(range(1,11,2))) ## stepvalue

    for i  in s:
    print(i)

    for item in range(1,11):
        print(item)
    
    for item in range(10,0-1): ##Reverse (10987654321)
    print(item)

    for i in range(len(s))
    print(i)



'''
for item in range(1,11):
    print(item)