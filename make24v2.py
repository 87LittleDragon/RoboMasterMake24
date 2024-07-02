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
                toShoot.clear()
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
        toShoot = []
        for i in range(10):
            numbers = numberList[:-1]
            if toShoot != []:
                toShoot.clear()

            if i == 0:
                i = ""
                toShoot = []
            elif not i in numbers:
                continue
            else:
                numbers.pop(numbers.index(i))
                toShoot = [i]    
            for ii in range(9,-1,-1):
                numbers = numberList[:-1]
                numbers.pop(numbers.index(i))
                toShoot = toShoot[:0]
                if not ii in numbers:
                    continue
                toShoot.append(ii)
                numbers.pop(numbers.index(ii))
                if int(str(i) + str(ii)) == 0:
                    continue
                remain = 24 / int(str(i) + str(ii))
                if remain in numbers:
                    toShoot.append(multiplication)
                    toShoot.append(remain)
                    return toShoot
                for iii in range(2, 10):
                    toShoot.append(multiplication)
                    numbers = numberList[:-1]
                    numbers.pop(numbers.index(i))
                    numbers.pop(numbers.index(ii))
                    toShoot = toShoot[:(toShoot.index(multiplication))]
                    if not iii in numbers:
                        continue
                    temp1 = remain / iii
                    toShoot.append(multiplication)
                    toShoot.append(iii)
                    numbers.pop(numbers.index(iii))
                    if temp1 in numbers:
                        toShoot.append(multiplication)
                        toShoot.append(temp1)
                        return toShoot
                    if not temp1.is_integer():
                        continue
                    for iiii in range(2, 10):
                        numbers = numberList[:-1]
                        numbers.pop(numbers.index(i))
                        numbers.pop(numbers.index(ii))
                        numbers.pop(numbers.index(iii))
                        toShoot = toShoot[:(toShoot.index(multiplication) + 2)]
                        if not iiii in numbers:
                            continue
                        temp2 = temp1 / iiii
                        toShoot.append(multiplication)
                        toShoot.append(iiii)
                        numbers.pop(numbers.index(iiii))
                        if temp2 in numbers:
                            toShoot.append(multiplication)
                            toShoot.append(temp2)
                            return toShoot
                        if not temp2.is_integer():
                            continue
                        if i != "":
                            continue
                        for iiiii in range(2, 10):
                            numbers = numberList[:-1]
                            numbers.pop(numbers.index(i))
                            numbers.pop(numbers.index(ii))
                            numbers.pop(numbers.index(iii))
                            numbers.pop(numbers.index(iiii))
                            toShoot = toShoot[:(toShoot.index(multiplication) + 4)]
                            if not iiiii in numbers:
                                continue
                            temp3 = temp2 / iiiii
                            toShoot.append(multiplication)
                            toShoot.append(iiiii)
                            numbers.pop(numbers.index(iiiii))
                            if temp3 in numbers:
                                toShoot.append(multiplication)
                                toShoot.append(temp3)
                                return toShoot
                            

                            
                        

                        
                                       
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
    l.append(addition)
    f.write(str(make24(l)))
    f.write("\n")
# print([2,4,3,7,addition])
# print(make24([2, 4, 3, 7, addition]))