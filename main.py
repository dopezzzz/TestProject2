# taking input year from user
year = int(input("Enter the year you want to check"))

#logic
if year % 4 == 0:
    if year%100!=0:
        print("leap year")
    else:
        if year%400 == 0:
            print("leap year") 
        else:
            print("not a leap year")

else:
    print("not a leap year")

# looking for git pull
