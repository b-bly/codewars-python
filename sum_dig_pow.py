def sum_dig_pow(a, b): # range(a, b + 1) will be studied by the function
    # your code here

    numbers = []
    for x in range(a,b + 1):
        numbers.append(x)


    specialNumbers = []
    for x in range(1, len(numbers) + 1):
        sumPowers = 0
        n = numbers[x - 1]
        numberDigits = [int(d) for d in str(n)]
        for y in range(0, len(numberDigits)):
            sumPowers += numberDigits[y]**(y+1)
            print(sumPowers)
        if sumPowers == n:
            specialNumbers.append(n)
    print(specialNumbers)

sum_dig_pow(1,15)


