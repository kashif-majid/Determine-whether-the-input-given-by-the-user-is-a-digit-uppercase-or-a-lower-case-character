i=1
while i==1:
    a=input("ENTER SINGLE CHARACTER INPUT: ")
    if a.isdigit():
        print("INPUT IS DIGIT")
    elif a.isupper():
        print("INPUT IS IN UPPERCASE")
    elif a.islower():
        print("INPUT IS LOWERCASE")
    else:
        print("UNRECOGNIZED INPUT")
    i=int(input("IF U WANT TO CONTINUE PRESS 1 ELSE PRESS ANY KEY: "))
