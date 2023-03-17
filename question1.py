def ReadFile():
    global DataArray
    try:
        filename = r"C:\Users\Abood\Desktop\School\Final Revision Files\Computer Science\Past paper python\P4 Papers\Oct Nov 2022 - 41\IntegerData.txt"
        file = open(filename, "r")
        for i in range(100):
            num = int(file.readline().strip())
            DataArray[i] = num
    except IOError:
        print("File not found !")

def FindValues():
    global DataArray
    count = 0
    searchItem = int(input("Enter number to search: "))
    if searchItem > 0 and searchItem < 101:
        for i in range(100):
            if searchItem == DataArray[i]:
                count = count + 1
        return count
    else:
        print("Number must be between 1 and 100")

def BubbleSort():
    global DataArray
    for i in range(100):
        for j in range(99):
            if DataArray[j] > DataArray[j+1]:
                temp = DataArray[j]
                DataArray[j] = DataArray[j+1]
                DataArray[j+1] = temp

global DataArray
DataArray = [0 for i in range(100)]

ReadFile()
returnValue = FindValues()
print("Value is found at {} instances".format(returnValue))
BubbleSort()
print(DataArray)
