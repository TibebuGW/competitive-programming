def countingValleys(steps, path):
    Dnum = Unum = valley = 0
    checker = ''
    for c in path:
        if Unum == 0 and Dnum == 0:
            checker = c
        
        if c== 'U':
            Unum += 1
        else: 
            Dnum += 1
            
        if Unum == Dnum:
            Unum = Dnum = 0
            if checker == 'D':
                valley += 1
            else: 
                continue
    
    return valley
