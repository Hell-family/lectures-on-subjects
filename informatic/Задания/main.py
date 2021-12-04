def HomeJob:
    def getMaxSumAndCount(array):
        count = 0
        maxSum = 0
        for i in range(len(array)):
            for j in range(i + 1, len(array)):
                if ((array[i] + array[j]) % 7) == 0:
                    count += 1

                    if array[i] + array[j] > maxSum:
                        maxSum = array[i] + array[j]

        return count, maxSum

    def appendNumbersArray(numberLines):
        array = []
        for i in numberLines:
            array.append(int(i))

        return array

    def main():
        file = open('task1.txt', 'r')
        numberLines = file.readlines()
        array = appendNumbersArray(numberLines)
        count, maxSum = getMaxSumAndCount(array)

        print(count, maxSum)

    main()

