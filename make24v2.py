addition = 40
subtraction = 41
multiplication = 33
division = 42

def make24(numberList):
    numberList.insert(-1,"")
    numbers = numberList[:-1]
    if numberList[-1] == addition:
        for i in range(9, -1, -1):
            if i == 0:
                i = ""
                toShoot = []
            elif not i in numbers:
                continue
            else:
                toShoot = [i]
            numbers.pop(numbers.index(i))
            for ii in range(9, -1, -1):
                if not ii in numbers:
                    numbers = numberList[:-1]
                    numbers.pop(numbers.index(i))
                    continue
                toShoot.append(ii)
                numbers.pop(numbers.index(ii))
                remain = 24 - int(str(i) + str(ii))
                if remain in numbers:
                    toShoot.append(addition)
                    toShoot.append(remain)
                    return toShoot
                for iii in range(10):
                    if not iii in numbers:
                        continue
                    remain -= iii
                    numbers.pop(numbers.index(iii))
                    toShoot.append(addition)
                    toShoot.append(iii)
                    if remain in numbers:
                        toShoot.append(addition)
                        toShoot.append(remain)
                        return toShoot
                toShoot = toShoot[:1]
                numbers = numberList[:-1]
                numbers.pop(numbers.index(i))
            toShoot.clear()
    
    if numberList[-1] == subtraction:
        for i in range(2,10):
            if not i in numbers:
                continue
            else:
                toShoot = [i]
                numbers.pop(numbers.index(i))
            for ii in range(10):
                if not ii in numbers:
                    numbers = numberList[:-1]
                    numbers.pop(numbers.index(i))
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
                numbers = numberList[:-1]
                numbers.pop(numbers.index(i))
                toShoot.pop(-1)
            numbers = numberList[:-1]
            toShoot.clear()

    if numberList[-1] == multiplication:
        for i in range(10):
            if i == 0:
                i = ""
                toShoot = []
            elif not i in numbers:
                continue
            else:
                toShoot = [i]
            numbers.pop(numbers.index(i))
            for ii in range(10):
                if not ii in numbers:
                    numbers = numberList[:-1]
                    numbers.pop(numbers.index(i))
                    if i != "":
                        toShoot = [i]
                    else:
                        toShoot = []
                    continue
                toShoot.append(ii)
                numbers.pop(numbers.index(ii))
                if int(str(i) + str(ii)) == 0:
                    numbers = numberList[:-1]
                    numbers.pop(numbers.index(i))
                    if i != "":
                        toShoot = [i]
                    else:
                        toShoot = []
                    continue
                remain = 24 / int(str(i) + str(ii))
                if remain in numbers:
                    toShoot.append(multiplication)
                    toShoot.append(int(remain))
                    return toShoot
                temp1 = 1
                for iii in range(2, 10):
                    if not iii in numbers:
                        continue
                    temp1 = temp1 / int(iii)
                    if not temp1.is_integer():
                        temp1 = temp1 * int(iii)
                        continue
                    temp1 = int(temp1)
                    toShoot.append(multiplication)
                    toShoot.append(iii)
                    numbers.pop(numbers.index(iii))
                    if temp1 in numbers:
                        toShoot.append(multiplication)
                        toShoot.append(iii)
                        return toShoot
                    for iiii in range(2, 10):
                        if not iiii in numbers:
                            continue
                        temp1 = temp1 / iiii
                        if temp1.is_integer():
                            temp1 = int(temp1)
                        toShoot.append(multiplication)
                        toShoot.append(iiii)
                        numbers.pop(numbers.index(iiii))
                        if temp1 in numbers:
                            toShoot.append(multiplication)
                            toShoot.append(temp1)
                            return toShoot
                        numbers = numberList[:-1]
                        numbers.pop(numbers.index(i))
                        numbers.pop(numbers.index(ii))
                        numbers.pop(numbers.index(iii))
                        toShoot.pop(-1)
                        toShoot.pop(-1)
                    numbers = numberList[:-1]
                    numbers.pop(numbers.index(i))
                    numbers.pop(numbers.index(ii))
                    toShoot.clear()
                    if i != "":
                        toShoot.append(i)
                    toShoot.append(ii)
                numbers = numberList[:-1]
                numbers.pop(numbers.index(i))
                toShoot.clear()
                if i != "":
                    toShoot.append(i)
            numbers = numberList[:-1]
            toShoot.clear()
    
    if numberList[-1] == division:
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
            for ii in range(10):
                if not ii in numbers:
                    numbers = numberList[:-1]
                    numbers.pop(numbers.index(i))
                    continue
                toShoot.append(ii)
                numbers.pop(numbers.index(ii))
                for iii in range(2, 10):
                    if not iii in numbers:
                        numbers = numberList[:-1]
                        numbers.pop(numbers.index(ii))
                        numbers.pop(numbers.index(i))
                        continue
                    toShoot.append(iii)
                    numbers.pop(numbers.index(iii))
                    remain = int(str(i) + str(ii) + str(iii)) / 24
                    # print(remain)
                    # print(numbers)
                    if remain == 0:
                        numbers = numberList[:-1]
                        numbers.pop(numbers.index(iii))
                        numbers.pop(numbers.index(ii))
                        numbers.pop(numbers.index(i))
                        continue
                    if remain in numbers:
                        toShoot.append(division)
                        toShoot.append(int(remain))
                        return toShoot
                    temp = 1
                    temp2 = ""
                    toShoot_t1 = []
                    toShoot_t2 = [division]
                    for iiii in range(10):
                        if not iiii in numbers:
                            continue
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
                    numbers = numberList[:-1]
                    numbers.pop(numbers.index(iii))
                    numbers.pop(numbers.index(ii))
                    numbers.pop(numbers.index(i))
                    toShoot.pop(-1)
                toShoot.pop(-1)
            toShoot.clear()
 
                    


f = open("output.txt", "w")
for i in range(10000):
    l = [int(x) for x in str(i)]
    while(len(l) < 4):
        l.insert(0,0)
    f.write(str(l))
    l.append(multiplication)
    f.write(str(make24(l)))
    f.write("\n")

# print(make24([9, 4, 2, 9, addition]))