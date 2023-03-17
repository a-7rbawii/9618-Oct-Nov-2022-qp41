def SearchValue(RootPointer, item):
    global ArrayNodes
    if RootPointer == -1:
        return -1
    else:
        if ArrayNodes[RootPointer][1] == item:
            return RootPointer
        else:
            if ArrayNodes[RootPointer][1] == -1:
                return -1
    if ArrayNodes[RootPointer][1] > item:
        return SearchValue(ArrayNodes[RootPointer][0], item)
    if ArrayNodes[RootPointer][1] < item:
        return SearchValue(ArrayNodes[RootPointer][2], item)

def PostOrder(RootPointer):
    if RootPointer[0] != -1:
        PostOrder(ArrayNodes[RootPointer][0])
    if RootPointer[2] != -1:
        PostOrder(ArrayNodes[RootPointer[2]])
    print(str(RootPointer[1]))

global ArrayNodes
ArrayNodes = [[-1]*3 for i in range(20)]

ArrayNodes[0] = [1, 20, 5]
ArrayNodes[1] = [2, 15, -1]
ArrayNodes[2] = [-1, 3, 3]
ArrayNodes[3] = [-1, 9, 4]
ArrayNodes[4] = [-1, 10, -1]
ArrayNodes[5] = [-1, 58, -1]
ArrayNodes[6] = [-1, -1, -1]

FreeNode = 6
RootPointer = 0

position = SearchValue(RootPointer, 15)
if position == -1:
    print("Not Found")
else:
    print("Found at {}".format(position))
PostOrder(ArrayNodes[RootPointer])