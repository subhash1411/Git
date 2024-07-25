#funtion to print the numbers from 1 to n
def count_to_n(n):
    for i in range(1,n+1):
        print(i, end=" ")
    print()

#User input Section
x=int(input("Enter a value of n b/w 10 to 20 :"))

for i in range(1,x):
    count_to_n(i)


#--------------------------------------------------------
print("Added this file and code, for 3d commit")

