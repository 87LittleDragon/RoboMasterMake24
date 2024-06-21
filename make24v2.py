def make24(a,b,c,d,sign):
    numbers = [a,b,c,d]
    if sign == "+":
        for i in range(2,-1,-1):
            for ii in range(9, -1, -1):
                if i == 0:
                    i = ""
                    toShoot = []
                elif i in numbers:
                    toShoot = [numbers.index(i) + 1]
                    numbers[numbers.index(i)] = None
                else:
                    continue
                if not ii in numbers:
                    continue
                temp = str(i) + str(ii)
                remain = 24 - int(temp)
                if remain < 0:
                    continue
                toShoot.append(numbers.index(ii) + 1)
                numbers[numbers.index(ii)] = None
                if remain in numbers:
                    toShoot.append(0)
                    toShoot.append(numbers.index(remain) + 1)
                    return toShoot
                for iii in range(remain, -1, -1):
                    if iii not in numbers:
                        continue
                    toShoot.append(0)
                    toShoot.append(numbers.index(iii) + 1)
                    numbers[numbers.index(iii)] = None
                    if remain - iii in numbers:
                        toShoot.append(0)
                        toShoot.append(numbers.index(remain - iii) + 1)
                        return toShoot
                
                numbers = [a,b,c,d]

    
    

print(make24(3,9,7,8,"-"))