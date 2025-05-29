print("*************************************")
print('\tPhone Number Generator')
print("*************************************\n")
min = int(input("Enter the minimum Digits: "))
max = int(input("Enter the maximum Digits: "))
firstdigit = int(input('Enter the First Digit of Phone Number: '))



for i in range(min ,max + 1):
    start = int(str(firstdigit) + '0' * (i - 1))
    for j in range(start ,start + 1):
        j = j
print(j)





