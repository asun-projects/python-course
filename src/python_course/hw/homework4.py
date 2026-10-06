# 1. Check if number A is a multiple of 11 
a = int(input("Input your number here:"))
if (a % 11 == 0):
    print("Number", a, "is a multiple of 11")
else:
    print("Number", a, "is not a multiple of 11.")


# 2. Check if number A is a multiple of 3 but not a multiple of  9
A = int(input("Enter your number: "))
if (A%3==0) and (A%9!=0):
    print("It is a multiple of 3 and not a multiple of 9")
else:
    print("It is not a multiple of three, or a multiple of nine.")


# 3. Check if number A is a multiple of 5 between 10 and 100, inclusively
A = int(input("Enter your number here: "))
if (10<=A<=100) and (A%5==0):
    print("It is a multiple of 5 and beetween 10 and 100")
else:
    print("It is not a multiple of 5 beetween 10 and 100.")


# 4. Check if number A is not greater than number B
A = int(input("Enter a number assigned A: "))
B = int(input("Enter a number assigned B: "))
if (A<B):
    print("A is not greater than B")
else:
    print("A is greater or equal to B")


# 5. Check if number A is a multiple of number B or if number B is a multiple of number A
A = int(input("Enter a value for A: "))
B = int(input("Enter a value for B: "))
if (A%B==0) or (B%A==0):
    print("They are multiples or factors of each other")
else:
    print("A and B are not multiples or factors of each other.")


