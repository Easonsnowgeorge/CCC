month = int(input())
day = int(input())
thirtyone_day_months = [1, 3, 5, 7, 8, 10, 12]
thirty_day_months = [2, 4, 6, 9, 11]

if (1 <= month <= 12) and (1 <= day <= 31):
    if (month > 2):
        print("After")

    elif (month < 2):
        print("Before")

    else:
        if (day > 18):
            print("After")

        elif (day < 18):
            print("Before")

        else:
            print("Special")