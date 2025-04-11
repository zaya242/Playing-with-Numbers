# Program to find the HCF/GCD

# Enter 2 numbers
numberLargest = int(input("Enter Largest number : "))
numberSmallest = int(input("Enter Smallest number : "))

#using Eculiden Algorithms
while(numberSmallest):
    numberstore = numberSmallest
    numberSmallest = numberLargest % numberSmallest
    numberLargest = numberstore

print("HCF is : ",numberLargest)    
