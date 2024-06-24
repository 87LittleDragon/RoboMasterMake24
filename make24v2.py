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
                toShoot.append(ii)
                numbers.pop(numbers.index(ii))
                remain = int(str(i) + str(ii)) - 24
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

    if numberList[4] == multiplication:
        for i in range(10):
            if i == 0:
                i = ""
                toShoot = []
            elif not i in numbers:
                continue
            else:
                numbers.pop(numbers.index(i))
                toShoot = [i]
            for ii in range(10):
                if not ii in numbers:
                    continue
                toShoot.append(ii)
                remain = 24 / int(str(i) + str(ii))
                numbers.pop(numbers.index(ii))
                if remain in numbers:
                    toShoot.append(multiplication)
                    toShoot.append(int(remain))
                    return(toShoot)
                elif len(numbers) < 2:
                    continue
                if remain / numbers[0] / numbers[1] == 1 :
                    toShoot.append(multiplication)
                    toShoot.append(numbers[0])
                    toShoot.append(multiplication)
                    toShoot.append(numbers[1])
                    return toShoot
                if len(numbers) == 3:
                    if remain / numbers[0] / numbers[1] / numbers[2] == 1:
                        toShoot.append(multiplication)
                        toShoot.append(numbers[0])
                        toShoot.append(multiplication)
                        toShoot.append(numbers[1])
                        toShoot.append(multiplication)
                        toShoot.append(numbers[2])
                        return toShoot
                toShoot.pop(-1)
                numbers = numberList[:4]
                numbers.pop(numbers.index(i))
            toShoot.clear()
            numbers = numberList[:4]
    
    if numberList[4] == division:
        toShoot = []
        for i in range(10):
            if i == 0:
                i = ""
                toShoot = []
            elif not i in numbers:
                continue
            else:
                numbers.pop(numbers.index(i))
                toShoot.append(i)
            for ii in range(11):
                if not ii in numbers:
                    continue
                if ii == 10:
                    continue
                toShoot.append(ii)
                numbers.pop(numbers.index(ii))
                for iii in range(10):
                    if not iii in numbers:
                        continue
                    if iii == 10:
                        continue
                    toShoot.append(iii)
                    numbers.pop(numbers.index(iii))
                    remain = int(str(i) + str(ii) + str(iii)) / 24
                    print(int(str(i) + str(ii) + str(iii)))
                    print(remain)
                    if remain in numbers:
                        toShoot.append(division)
                        toShoot.append(int(remain))
                        return toShoot
                    temp = 1
                    temp2 = ""
                    toShoot_t1 = []
                    toShoot_t2 = [division]
                    for iiii in numbers:
                        temp = temp * iiii
                        toShoot_t1.append(division)
                        toShoot_t1.append(iiii)
                        if float(temp) == float(remain):
                            toShoot.extend(toShoot_t1)
                            return toShoot
                        temp2 = int(str(temp2) + str(iiii))
                        toShoot_t2.append(iiii)
                        if float(temp2) == float(remain):
                            toShoot.extend(toShoot_t2)
                            return toShoot
                    numbers = numberList[:4]
                    toShoot.pop(-1)
                toShoot.pop(-1)
            toShoot.clear()
 
                    




print(make24([4,8,3,6, multiplication]))