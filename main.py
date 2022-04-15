'''function that takes an array of numbers (integers for the tests) and a target number.
It should find two different items in the array that, when added together, give the target value.'''

def two_sum(lista,target):
    for indexI,i in enumerate(lista):
        for indexX,x in enumerate(lista):
            if x + i == target:
                if indexX == indexI:
                    continue
                return print(indexI,indexX)

two_sum([1234,5678,9012], 14690)