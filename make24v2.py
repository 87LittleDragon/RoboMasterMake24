addition = 40
subtraction = 41
multiplication = 33
division = 42

def make24(numberList):
    numbers = numberList[:4]
    if numberList[4] == addition:
        for i in range(2,-1,-1):
            if i == 0:
                i = ""
                toShoot = []
            elif i in numbers:
                toShoot = [i]
                numbers[numbers.index(i)] = None
            else:
                continue
            for ii in range(9, -1, -1):
                if not ii in numbers:
                    continue
                temp = str(i) + str(ii)
                remain = 24 - int(temp)
                if remain < 0:
                    continue
                toShoot.append(ii)
                numbers[numbers.index(ii)] = None
                if remain in numbers:
                    toShoot.append(numberList[4])
                    toShoot.append(remain)
                    return toShoot
                for iii in range(remain, -1, -1):
                    if iii not in numbers:
                        continue
                    toShoot.append(numberList[4])
                    toShoot.append(iii)
                    numbers[numbers.index(iii)] = None
                    if remain - iii in numbers:
                        toShoot.append(numberList[4])
                        toShoot.append(remain - iii)
                        return toShoot
                toShoot.pop(-1)
                numbers = numberList[:4]
    
    if numberList[4] == subtraction:
        for i in range(2,10):
            if not i in numbers:
                continue
            else:
                toShoot = [i]
                numbers.pop(numbers.index(i))
            for ii in range(10):
                if not ii in numbers:
                    continue
                temp1 = str(i) + str(ii)
                toShoot.append(ii)
                numbers.pop(numbers.index(ii))
                remain = int(temp1) - 24
                if remain in numbers:
                    toShoot.append(subtraction)
                    toShoot.append(remain)
                    return toShoot
                if remain - numbers[0] - numbers[1] == 0:
                    toShoot.append(subtraction)
                    toShoot.append(numbers[0])
                    toShoot.append(subtraction)
                    toShoot.append(numbers[1])
                    return toShoot
                if remain - int(str(numbers[0]) + str(numbers[1])) == 0:
                    toShoot.append(subtraction)
                    toShoot.append(numbers[0])
                    toShoot.append(numbers[1])
                    return toShoot
                if remain - int(str(numbers[1]) + str(numbers[0])) == 0:
                    toShoot.append(subtraction)
                    toShoot.append(numbers[1])
                    toShoot.append(numbers[0])
                    return toShoot
                numbers = numberList[:4]
                numbers.pop(numbers.index(i))
                toShoot.pop(-1)
            numbers = numberList[:4]
            toShoot.clear()


print(make24([5,1,3,0,41]))