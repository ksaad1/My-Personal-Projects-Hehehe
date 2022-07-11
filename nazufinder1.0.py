firstSequence = 'gctgnazutatttcgatcgattnazutatgct'
nazuSequence = 'gcatcnazugtacgatcgatcgatcgtagctagggtcnazucatatgcctctacgtacgtctctnazuacgagc'
saadSequence = 'gctacgatgcnazuatcgatcganazunazutcgatcgatgcatgtgnazutnazuagctagctanazugctgttttttt'

# a list of given sequences

mySequence = firstSequence + nazuSequence + saadSequence  # defining the sequence to be analyzed


def locator(strain, startposition):  # defining a locator function
    mySequence.find(strain, startposition)
    return mySequence.find(strain, (int(startposition) + 1))


mystartposition = 0  # a counter for starting position
mystrain = input("Enter strain: ")  # asking user for strain

if locator(mystrain, mystartposition) == -1:
    print("Oops, this isn't here at all!")
else:
    print("Okay, sequence found! Finding positions!")
    while 0 <= int(mystartposition) < int(len(mySequence)):# the loop for giving all positions where strain is found
        locator(mystrain, mystartposition)
        if locator(mystrain, mystartposition) == -1:
            pass  # ending loop to avoid -1 as position for not found
        else:
            print(locator(mystrain, mystartposition))
        mystartposition = locator(mystrain, mystartposition)  # resetting counter for starting position
    print("Those are all the positions!")  # concluding statement yayayaya
print(' ')
