def make24(numberList):
    numbers = numberList[:4]
    if numberList[4] == 40:
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

    
    

print(make24([1,2,3,4,40]))