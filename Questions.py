
# 5-Write a program to find a sum of all  the even numbers upto 50:
for i in range(0,51,2):
        sum+=i
        print(sum)

#6-write a program to write a first 20 numbers and their squarewd numbers:

for i in range (1,21):
   print(i,i**2)

   #7 - Write a program tomfind a sum of first 10 odd numbers using while loop:

sum=0
for i in range(1,11,2):
    sum+=i
    print(sum)

    #OR

sum=0
for i in range(1,11):
    if(i%2!=0):
        sum+=i
        print(sum)

#8- Write aprogram to chewck if a number is divisible by 8 and 12 upto 100 numbers:

for i in range(1,101):
    if(i%8==0 and i%12==0):
        print(i)


#9 Wite a program to create a billing system at supermnart:
while True:
    Name = input("Enmter your name")
    Address = input("Enter adress")
    total=0

    while True:
        quantity=int(input("How many item?"))
        amount=int(input("Enter the Amount!"))

        total+=quantity*amount

        repeat=input("Is there any item left")
        if repeat=="yes":
            continue
        elif repeat=="No":
            print("Name=",Name)
            print("Address=",Address)
            print("quantity=",quantity)
            print("Total Amount=",total)
            break











       





 

