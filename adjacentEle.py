def adjacentElementsProduct(inputArray):

    arraylength = len(inputArray)
    productlist =[]
    for i in range(0,arraylength-1):
        product = inputArray[i]*inputArray[i+1]
        productlist.append(product)
    return max(productlist)
import sys
sys.setrecursionlimit(10004)
def shapeArea(n):
    if n == 1:
        return 1
    else:
        return shapeArea(n-1)+(n-1)*4
def almostIncreasingSequence(sequence):
    arraylen = len(sequence)
    diflist = []
    for i in range(1,arraylen):
        if i < 3:
            dif = sequence[i]-sequence[i-1]
            if dif <1:
                diflist.append(dif)
        else:
            dif = sequence[i]-sequence[i-1]
            if dif < 1 or (sequence[i] <= sequence[i-2] and sequence[i] != max(sequence)):
                diflist.append(dif)
    if len(diflist) > 1:
        return False
    else:
        if max(sequence) ==2:
            return  False
        return True
def almostIncreasingSequence(sequence):
    def pop(sequence):
        for m in range(len(sequence)-1):
            if sequence[m + 1] - sequence[m] < 1:
                if (m + 2) < len(sequence):
                    if sequence[m + 2] - sequence[m] < 1:
                        sequence.pop(m)
                    else:
                        sequence.pop(m + 1)
                else:
                    sequence.pop(m + 1)
                return pop(sequence)
        return sequence
        
    if len(sequence) - len(pop(sequence)) > 1:
        return False
    else:
        return True
