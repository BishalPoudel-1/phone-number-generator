print("*************************************")
print('\tPhone Number Generator')
print("*************************************\n")
min = int(input("Enter the minimum Digits: "))
max = int(input("Enter the maximum Digits: "))
firstdigit = int(input('Enter the First Digit of Phone Number: '))



for i in range(min ,max + 1):
    start = int(str(firstdigit) + '0' * (i - 1))
    for startdigit in range(start ,start + 1):
        startdigit = startdigit


for j in range(1, startdigit):
    startdigit = startdigit + 1
    with open("phonenumber.txt", "a") as f:
        if len(str(startdigit)) > max:
            break
        f.write(str(startdigit)+"\n")
        print(startdigit)





    





